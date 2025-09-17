# Sonar GraphQL Schema Overview

This document summarizes the structure of the Sonar GraphQL API and the underlying data domains it exposes. It distills the official API guidance at https://docs.sonar.expert/system/consuming-the-sonar-api and our local schema introspection (`docs/sonar/schema_analysis.json`, generated on 2025-09-12).

## Platform Snapshot

- **API Shape:** GraphQL 16-style schema with root `Query` and `Mutation` types (no public subscriptions).
- **Total Types:** 1,393 (scalars, objects, interfaces, unions, enums, and input objects).
- **Object Models:** 591 object types grouped across more than two dozen business domains.
- **Root Queries:** 318 entry points, almost all implemented as connection-style collections with `entities`, `page_info`, and `total_count` fields for pagination.
- **Authentication:** Bearer token (API key) over HTTPS. All requests must include an `Authorization: Bearer <token>` header.
- **Pagination Pattern:** Each collection query accepts combinations of `limit`/`offset` or `first`/`after` arguments. Result sets are wrapped in connection objects that expose `page_info.has_next_page` and `page_info.end_cursor`.
- **Filtering & Sorting:** Most collection queries accept filter input objects (e.g., `accounts(filter: AccountFilterInput)`) and sort enums (e.g., `order_by: [AccountSortInput!]`). Filters combine equality, range, and pattern operators following the documented `*FilterInput` standards.
- **Custom Scalars:** Common primitives (`Date`, `DateTime`, `Numeric`, `EmailAddress`, `Json`, `Seconds`) supplement the base GraphQL scalar set. Unique identifiers are consistently surfaced as `Int64Bit` and `UUID`.

## Domain Map

The table below highlights the major functional areas extracted from schema introspection.

| Domain | Representative Entities | Notes |
| --- | --- | --- |
| Accounts & Contacts | `Account`, `AccountStatus`, `AccountService`, `Contact`, `Address` | Central customer records, account hierarchy, billing parameters, associated services. |
| Services & Packages | `Service`, `ServicePlan`, `Package`, `ServicePlanTerm`, `UsageBasedServiceDetail` | Defines sellable services, bundles, terms, and service-specific provisioning details. |
| Billing & Finance | `Invoice`, `InvoiceItem`, `Payment`, `Transaction`, `Tax`, `Credit`, `Debit`, `Charge` | Full revenue lifecycle: invoicing, payments, adjustments, taxation, dunning. |
| Inventory & Equipment | `InventoryItem`, `InventoryModel`, `Vendor`, `DeploymentType`, `EquipmentTemplate` | Tracks all physical/logical assets, deployment status, vendor metadata, monitoring hooks. |
| Network & IP Management | `IpAssignment`, `Subnet`, `IpPool`, `DhcpServer`, `RadiusAccount`, `Vlan`, `NetworkSite` | IPv4/IPv6 address orchestration, DHCP/RADIUS integration, topology sites and nodes. |
| Monitoring & Events | `Event`, `Notification`, `SnmpTrap`, `MonitoringTemplate`, `MetricSample` | Real-time device status, alarms, threshold tracking, performance sampling. |
| Support & Operations | `Ticket`, `TicketComment`, `WorkOrder`, `Task`, `InboundMailbox`, `TicketGroup` | Helpdesk workflows, work management, email-based ticket ingestion, SLA metrics. |
| Scheduling & Dispatch | `ScheduleEvent`, `ScheduleBlocker`, `TechnicianSchedule`, `CalendarEvent` | Field operations planning, technician availability, blocker overrides. |
| Usage & Analytics | `UsageRecord`, `UsageSummary`, `BandwidthReport` | Aggregated consumption metrics driving usage-based billing and reporting. |
| Administration & Security | `User`, `Role`, `Permission`, `ApiKey`, `Authenticatable`, `AuditLog` | Identity management, RBAC, API credentials, audit trails. |
| Integrations & Automation | `Webhook`, `BackgroundJob`, `QueuedJob`, `IntegrationSetting` | System-to-system notifications and async processing. |
| Documents & Contracts | `Document`, `Contract`, `SignatureRequest`, `Template` | Customer-facing documents, signature tracking, templating. |
| Miscellaneous | `Config`, `LookupValue`, `FeatureToggle`, `TaskTemplate` | Platform configuration, enumerations, feature controls. |

## Core Entity Relationships

- **Account-Centric Hub:** `Account` is the anchor for most domains. It links to services (`account.services`), billing (`account.invoices`, `account.payments`), support (`account.tickets`), inventory (`account.inventory_items`), and network allocations (`account.ip_assignments`). Foreign keys consistently use `*_id` with `Int64Bit` scalar types.
- **Service Composition:** `AccountService` ties an `Account` to a specific `Service` or `Package`. Usage of bundles is modeled through `Package` ↔ `Service` relationships, while upgrade/downgrade history is surfaced via `AccountServiceHistory`.
- **Financial Ledger:** `Invoice` aggregates `InvoiceItem`s and references `Payment`s and `Transaction`s. Taxation is handled via `TaxProvider` and `TaxZone`. Credits/debits post back to the account’s balance and reconcile through `PaymentApplication` records.
- **Inventory Lifecycle:** `InventoryItem` references models, deployment types, parent/child items (for nested hardware), and optionally the associated `AccountService`. Monitoring status (SNMP, ICMP) and warehouse position are stored alongside procurement data (`PurchaseOrder`, `WarehouseLocation`).
- **Network Provisioning:** `IpAssignment` connects `Account`/`InventoryItem` to IP space. Subnet structures (`Subnet`, `SubnetGroup`) and access infrastructure (`NetworkSite`, `Tower`, `AccessPoint`) define topology. Authentication flows rely on `RadiusAccount`, `PppoeAccount`, and configuration templates.
- **Support Workflows:** `Ticket` aggregates comments, watchers, attachments, and related accounts/services. Escalations leverage `TicketGroup`, `TicketTag`, `TicketPriority`, and `WorkflowRule` entities. Field work orders (`WorkOrder`, `WorkOrderItem`) associate with technician schedules.
- **Security & Audit:** `User` ties to `Role`, `Permission`, and `PermissionCategory`. Authentication metadata (MFA, API tokens) surfaces through `UserTwoFactorStatus`, `ApiKey`, and `AuditLog` objects.

## Query Access Patterns

1. **Collections via Connections**
   ```graphql
   query Accounts($limit: Int!, $offset: Int) {
     accounts(limit: $limit, offset: $offset, filter: { status_id: { eq: 5 } }) {
       total_count
       entities {
         id
         name
         account_status { name }
         services { id name }
       }
       page_info { has_next_page end_cursor }
     }
   }
   ```
   - `limit`/`offset` for page stepping; some resources expose `first`/`after` cursor pagination instead.
   - Filter input types mirror documentation, allowing nested logic (`and`, `or`, `not`), comparison operators (`eq`, `in`, `gt`, `ilike`), and date ranges.
   - Sorting is defined via `order_by` arrays referencing `*_Sort` enums.

2. **Single-Entity Fetch**
   - `account(id: Int!)`, `invoice(id: Int!)`, `inventory_item(id: Int!)` return single nodes with the same field structure as the entities inside collections.

3. **Mutations**
   - Mutations follow the documented naming convention: `create_*`, `update_*`, `archive_*`, `restore_*`. Each expects a `*Input!` payload and returns the affected entity plus a standard `errors` array when validation fails.
   - Bulk operations (e.g., `bulk_create_account_services`) accept list inputs and respond with per-record statuses.

4. **Shared Utility Queries**
   - System metadata: `feature_flags`, `configurations`, `time_zones`.
   - Enumerations: `enumerations { name values }` for dynamic pick-list population.
   - Background operations: `jobs`, `queued_jobs`, and `webhooks` surfaces operational status.

## Data Integrity Considerations

- **Company Isolation:** Many entities include a `company_id` foreign key, reflecting Sonar’s multi-company tenancy. Filters should constrain by `company_id` when operating across tenants.
- **Soft Deletes:** Archival is handled via `archived_at`/`archived_by_user_id` fields. Most collections exclude archived records by default unless filters explicitly request them (`include_archived: true`).
- **Versioned Templates:** Billing (`InvoiceTemplateVersion`), documents (`TemplateVersion`), and communication templates use versioned entities. Downstream references typically point to the version active at the time of generation.
- **Telemetry Volume:** Monitoring and log entities can grow quickly; prefer cursor-based pagination and time-window filters to control payload size.

## Working with the Schema

- **Introspection Artifacts:** Keep `docs/sonar/schema_analysis.json` as the source of truth for type counts and machine-readable metadata. Regenerate after Sonar upgrades to capture schema drift.
- **Client Generation:** The consistent naming scheme and pervasive `id`/`sonar_unique_id` fields make it straightforward to auto-generate local data models directly from the GraphQL schema.
- **Field Selection Strategy:** Favor depth-limited selections (1–2 levels) and rely on follow-up queries for deeply nested data to avoid server-side timeouts.
- **Rate Limiting:** While the GraphQL API does not publish hard limits, the documentation recommends batching requests and respecting retry headers. The schema exposes `rate_limit_status` for monitoring usage.

## References

- Sonar API Guide: https://docs.sonar.expert/system/consuming-the-sonar-api
- Local Schema Snapshot: `docs/sonar/schema_analysis.json` (introspection snapshot dated 2025-09-12)
