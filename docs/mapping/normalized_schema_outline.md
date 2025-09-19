# Normalized Migration Schema Outline

This outline groups the Sonar collections (see `source_inventory.md`) into normalized entities that align with Splynx’s data model. Each section lists the core entity, purpose, key attributes we need to retain, and downstream relationships.

## 1. Customer & Account Domain

### NormalizedCustomer
- **Purpose:** Master customer record (maps Sonar `accounts`, `account_statuses`, `account_types`).
- **Key Attributes:** `external_id` (Sonar ID), `status`, `type`, `company_id`, `name`, `billing_cycle`, `balance_summary`, `tags`, `created_at`, `updated_at`.
- **Relationships:**
  - `NormalizedContact` (1‑to‑many)
  - `NormalizedAddress` (service/billing) (1‑to‑many)
  - `NormalizedService` (1‑to‑many)
  - `NormalizedInvoice` / `NormalizedTransaction`
  - `NormalizedContract`

### NormalizedContact
- **Source Collections:** `contacts`, `contact_types`.
- **Attributes:** `external_id`, `customer_id`, `role`, `name`, `email`, `phone`, `preferences`.

### NormalizedAddress
- **Source Collections:** `addresses`, `address_statuses`, `address_lists`.
- **Attributes:** `external_id`, `customer_id`, `kind` (service, billing, shipping), `line1`, `line2`, `city`, `state`, `postal_code`, `country`, `geolocation`.

### NormalizedAccountGroup
- **Source Collections:** `account_groups`, `account_group_memberships`.
- **Attributes:** `external_id`, `name`, `description`.
- **Relationships:** Many customers can share groups (Splynx customer categories/partners).

## 2. Service & Tariff Domain

### NormalizedService
- **Source Collections:** `account_services`, `service_plans`, `services`, `service_metadata`.
- **Attributes:** `external_id`, `customer_id`, `tariff_id`, `status`, `activation_date`, `suspension_state`, `pricing`, `usage_policy`, `notes`.
- **Relationships:** Links to `NormalizedTariff`, `NormalizedDeviceAssignment`, `NormalizedIPAssignment`.

### NormalizedTariff
- **Source Collections:** `service_plans`, `internet_service_details`, `voice_service_details`, `usage_based_service_details`.
- **Attributes:** `external_id`, `type` (internet/voice/custom), `name`, `download_speed`, `upload_speed`, `price`, `billing_frequency`, `one_time_fees`, `tax_profile`.

### NormalizedServiceHistory
- **Source Collections:** `account_service_histories`, `service_status_histories`.
- **Attributes:** `service_id`, `event_type`, `timestamp`, `notes`.

## 3. Billing & Finance Domain

### NormalizedInvoice
- **Source Collections:** `core_invoices`, `invoice_items`, `invoice_payments`.
- **Attributes:** `external_id`, `customer_id`, `number`, `status`, `issue_date`, `due_date`, `subtotal`, `tax_total`, `total`, `balance`.
- **Relationships:** `NormalizedInvoiceLine`, `NormalizedPaymentApplication`.

### NormalizedInvoiceLine
- **Source Collections:** `invoice_items`, `charges`, `credits`, `debits`.
- **Attributes:** `external_id`, `invoice_id`, `line_type`, `description`, `quantity`, `unit_price`, `tax_amount`, `service_id` (optional).

### NormalizedPayment
- **Source Collections:** `payments`, `core_transactions`, `payment_methods`, `credit_cards`, `bank_accounts`.
- **Attributes:** `external_id`, `customer_id`, `method`, `amount`, `posted_at`, `status`, `reference`, `processor_metadata`.
- **Relationships:** `NormalizedPaymentApplication` (mapping payments to invoices).

### NormalizedTransaction
- **Source Collections:** `core_transactions`, `transactions`, `tax_transactions`.
- **Attributes:** `external_id`, `customer_id`, `type`, `amount`, `running_balance`, `related_invoice`, `related_payment`, `description`, `notes`.

### NormalizedCreditDebit
- **Source Collections:** `credits`, `debits`, `recurring_debits`, `recurring_credit_templates`.
- **Attributes:** `external_id`, `customer_id`, `type`, `amount`, `reason`, `applied_invoice_id`, `period`.

## 4. Inventory & Device Domain

### NormalizedInventoryItem
- **Source Collections:** `inventory_items`, `inventory_models`, `inventory_vendors`, `inventory_locations`.
- **Attributes:** `external_id`, `sku`, `model_id`, `vendor_id`, `serial_number`, `status`, `warehouse_location`, `assigned_customer_id`, `assigned_service_id`.

### NormalizedDeviceAssignment
- **Source Collections:** `account_ip_assignments`, `account_equipment_assignments`, `device_credentials`.
- **Attributes:** `external_id`, `service_id`, `device_id`, `assignment_type`, `start_date`, `end_date`, `notes`.

## 5. Network & IP Management Domain

### NormalizedNetworkSite / Node
- **Source Collections:** `network_sites`, `towers`, `access_points`, `network_nodes`.
- **Attributes:** `external_id`, `name`, `type`, `geolocation`, `parent_site_id`.

### NormalizedSubnet / IPPool
- **Source Collections:** `subnets`, `ip_pools`, `ip_assignments`, `radius_accounts`.
- **Attributes:** `external_id`, `cidr`, `gateway`, `pool_type`, `assignment_strategy`, `vlan`, `radius_profile`.

### NormalizedIPAssignment
- **Source Collections:** `account_ip_assignments`, `ip_assignments`, `serviceable_address_account_assignment_histories`.
- **Attributes:** `external_id`, `service_id`, `ip_address`, `assignment_type`, `status`, `provisioned_at`, `released_at`.

## 6. Security & Administration Domain

### NormalizedUser
- **Source Collections:** `users`, `user_groups`, `user_role_assignments`.
- **Attributes:** `external_id`, `username`, `name`, `email`, `status`, `auth_provider`, `last_login`.
- **Relationships:** `NormalizedRole`, `NormalizedPermission` (through assignments).

### NormalizedRole & NormalizedPermission
- **Source Collections:** `roles`, `permissions`, `permission_categories`, `role_permissions`.
- **Attributes (Role):** `external_id`, `name`, `description`, `scope`, `is_system`.
- **Attributes (Permission):** `external_id`, `category`, `code`, `description`, `is_active`.
- **Relationships:** `NormalizedRolePermission` bridge captures assignment metadata (`granted_at`, `granted_by`, `inherited_from`).

## 7. Support & Operations Domain

### NormalizedTicket
- **Source Collections:** `tickets`, `ticket_comments`, `ticket_attachments`, `ticket_groups`, `ticket_priorities`, `ticket_tags`.
- **Attributes:** `external_id`, `customer_id`, `subject`, `status`, `priority`, `assigned_to`, `created_at`, `updated_at`.
- **Relationships:** `NormalizedTicketComment`, `NormalizedAttachment`.

### NormalizedWorkOrder / Task
- **Source Collections:** `tasks`, `task_templates`, `work_orders`, `schedule_events`.
- **Attributes:** `external_id`, `customer_id`, `type`, `status`, `scheduled_at`, `technician_id`, `notes`.

## 8. Documents & Contracts Domain

### NormalizedContract
- **Source Collections:** `contracts`, `contract_templates`, `signatures`.
- **Attributes:** `external_id`, `customer_id`, `template_id`, `status`, `effective_date`, `expiration_date`, `document_url`.

### NormalizedDocument
- **Source Collections:** `documents`, `document_versions`, `document_folders`.
- **Attributes:** `external_id`, `customer_id`, `type`, `title`, `url`, `created_at`.

## 9. Communications Domain

### NormalizedCommunicationLog
- **Source Collections:** `call_logs`, `emails`, `triggered_emails`, `sms_messages`.
- **Attributes:** `external_id`, `customer_id`, `channel`, `subject`, `body`, `sent_at`, `status`, `related_ticket_id`.

## 10. Scheduling & Calendar Domain

### NormalizedScheduleEvent
- **Source Collections:** `schedule_events`, `calendar_icals`, `technician_schedules`.
- **Attributes:** `external_id`, `customer_id`, `event_type`, `start_at`, `end_at`, `technician_id`, `location_id`, `status`.

## Cross-Cutting Considerations
- Maintain original Sonar IDs for traceability (`external_id`).
- Capture `created_at`, `updated_at`, and archival metadata for audit purposes.
- Record references to Sonar-specific enums or lookup values for later translation (e.g., service statuses, tax codes).
- Ensure normalized entities include hooks for notes/tasks (`NormalizedNote`) if needed.

This outline serves as the basis for Step 3 (field-level mapping). As we examine each domain, we will refine attributes, note required transformations, and decide whether additional normalized junction tables are needed (e.g., a customer ↔ group bridge).
