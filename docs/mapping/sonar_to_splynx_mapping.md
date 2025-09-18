# Sonar → Splynx Entity Mapping

This report captures the high-level alignment between Sonar GraphQL domains and their target entities inside Splynx. It is intended as a living reference for migration work.

## 1. Customer & Account Management

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `Account`, `AccountService`, `AccountStatus`, `AccountType` | `admin/customers/customer`, `admin/customers/statuses`, `admin/customers/categories` | Sonar accounts become Splynx customers. Service assignments translate into Splynx services (internet/voice/bundle). Account status/type map to customer categories/status in Splynx. |
| `Contact`, `Address`, `PhoneNumber` | Customer contact details (REST: `admin/customers/contact` fields or direct DB insert into `customer_contacts`, `customer_info`) | Splynx stores contacts in `customer_contacts` and `customer_info`. Ensure email/phone tagging (primary/billing/technical). |
| `CustomerPortalUser` | Splynx customer portal credentials (`customers`, `customer_logins`) | Password handling may require reset/temporary password due to hashing differences. |
| `Note`, `AccountEvent` | Splynx customer notes (`customer_notes`) | Track author timestamps and visibility flags. |

## 2. Services & Tariffs

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `Service`, `ServicePlan`, `Package` | `admin/tariffs/*` (internet, voice, bundle, recurring) | Plan metadata (speed, price, billing taxonomy) maps to tariff attributes. Usage-based services may require Splynx quotas/caps. |
| `AccountServiceHistory`, `ServiceOverride` | Service assignment history (custom migration tables) | Use for audit or rollback support if needed. |
| `UsageBasedServiceDetail`, `DataServiceDetail`, `VoiceServiceDetail` | Tariff-specific attributes | Map to Splynx tariff fields (download/upload, data cap, voice settings). |

## 3. Billing & Finance

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `Invoice`, `InvoiceItem`, `InvoiceTemplateVersion` | `billing/invoices`, `billing_invoice_items` | Invoices can be inserted via DB (MySQL) or REST API if enabled. Preserve numbering and statuses (draft/final/void). |
| `Payment`, `PaymentApplication`, `Credit`, `Debit` | `billing/payments`, `billing_transactions`, `billing_credits` | Payment methods (credit card/bank) map to payment_type fields. Applications to invoices should be preserved. |
| `Transaction`, `Charge`, `RecurringCharge` | `billing_transactions` | Ensure tax handling (VAT inclusive/exclusive). |
| `Tax`, `TaxZone`, `TaxDefinition` | Splynx tax configuration (`finance_tax_rules`) | Validate existing Splynx tax structure matches Sonar rules or create new ones. |
| `DepositSlip`, `Batch` | Optional: map to Splynx payment journal/batches if needed. |

## 4. Inventory & Equipment

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `InventoryItem`, `InventoryModel`, `Vendor`, `Warehouse`, `DeploymentType` | Splynx inventory tables (`inventory_items`, `inventory_models`, `inventory_vendors`) | Ensure hierarchical parent/child items preserved. Deployment status maps to Splynx item state. |
| `InventoryAssignment`, `EquipmentTemplate`, `MonitoringTemplate` | Splynx equipment monitoring (`network_routers`, `monitoring_templates`) | Additional configuration may require Splynx module enablement. |

## 5. Network & IP Management

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `IpAssignment`, `IpPool`, `Subnet`, `Vlan` | `network/ip_pools`, `network/subnets`, `network/vlans` | Splynx distinguishes static vs dynamic ranges; align Sonar assignments accordingly. |
| `DhcpServer`, `DhcpLease`, `RadiusAccount`, `PppoeAccount` | Splynx network modules (`network/dhcp`, `network/radius`, `network/pppoe`) | Requires module activation; verify credentials and shared secrets. |
| `NetworkSite`, `Tower`, `AccessPoint`, `Device` | Splynx network infrastructure (`network_sites`, `network_devices`) | Topology mapping may need custom transformers. |

## 6. Support & Operations

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `Ticket`, `TicketComment`, `TicketGroup`, `TicketPriority` | Splynx support module (`support/tickets`) | Splynx may need module licensing. Preserve ticket status, owner, SLA timers. |
| `WorkOrder`, `Task`, `MaintenanceEvent` | Splynx scheduling/maintenance modules (`scheduling/work_orders`, `scheduling/technician_routes`) | Mapping requires matching technician identities and calendar slots. |

## 7. Monitoring & Events

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `Event`, `Notification`, `MetricSample` | Splynx monitoring (`monitoring/events`, `monitoring_history`) | Evaluate whether to migrate historical monitoring or start fresh. |
| `AlertingRotation`, `SnmpTrap`, `SnmpSetting` | Splynx monitoring configuration | Align SNMP credentials and trap destinations. |

## 8. Administrative & Security

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `User`, `Role`, `Permission`, `ApiKey` | Splynx admins (`admin/administrators`, `admin/roles`) | Map roles carefully; Splynx permissions differ from Sonar. |
| `AuditLog`, `BackgroundJob`, `Webhook` | Optional | Evaluate necessity; could store externally for compliance. |

## 9. Documents & Contracts

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `Document`, `Template`, `SignatureRequest` | Splynx document templates (`documents/templates`, `documents/files`) | Ensure file storage accessible (S3/local). |
| `Contract`, `Agreement` | Customer contract tables (`customer_contracts`) | Align contract statuses and renewal dates. |

## 10. Usage & Analytics

| Sonar Entities | Splynx Targets | Notes |
| --- | --- | --- |
| `UsageRecord`, `UsageSummary`, `BandwidthReport` | Splynx usage records (`internet_usage_data`, `usage_statistics`) | May require aggregation to match Splynx data model. |

## Migration Notes

1. **Field Level Mapping:** Detailed mappings reside under `src/migration/` modules. This report is intentionally high-level.
2. **Nested Data:** Sonar GraphQL responses contain rich nested objects. The backup tooling defaults to scalar-only selection to keep snapshots manageable. Increase `--max-depth` when richer context is required.
3. **Hybrid Approach:** Core customer/billing/service data should flow through the migration orchestrator (GraphQL → transform → Splynx REST/DB). Monitoring logs or historical metrics may be archived separately.
4. **Validation:** Always validate migrated entities via Splynx REST API or direct DB queries. Use the progress tracker to monitor batch conversions.

_Update this file whenever new entities or mappings are defined._
