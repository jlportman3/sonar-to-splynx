# Normalized Field Mappings (Draft)

This document expands the normalized schema outline with Sonar → normalized field mappings. It now covers the **Customer & Account**, **Service & Tariff**, and **Billing & Finance** domains and will be extended to other areas in subsequent iterations.

## 1. Customer & Account Domain

### 1.1 NormalizedCustomer

| Normalized Attribute | Sonar Source (table.field) | Notes / Transformations |
| --- | --- | --- |
| `external_id` | `accounts.id` | Primary Sonar identifier (integer) |
| `sonar_unique_id` | `accounts.sonar_unique_id` | UUID reference used across tables |
| `status_id` | `accounts.account_status_id` → `account_statuses.id` | Join to `account_statuses` to resolve code/name |
| `status_name` | `account_statuses.name` | Normalize to Splynx status enumeration |
| `status_flags` | `account_statuses.activates_account`, `account_statuses.icon`, etc. | Evaluate for mapping to Splynx customer statuses |
| `type_id` | `accounts.account_type_id` → `account_types.id` | Required for customer category mapping |
| `type_name` | `account_types.name` | Align with Splynx customer categories (person/company/business) |
| `company_id` | `accounts.company_id` | Maps to Splynx partner/operator where applicable |
| `name` | `accounts.name` | Customer display name |
| `activation_date` | `accounts.activation_date`, `accounts.activation_time` | Combine to produce precise activation datetime |
| `next_bill_date` | `accounts.next_bill_date` | Used for billing schedule |
| `next_recurring_charge_amount` | `accounts.next_recurring_charge_amount` | Helpful for validation/forecasting |
| `is_delinquent` | `accounts.is_delinquent` | Use to seed customer status/action flags |
| `parent_account_id` | `accounts.parent_account_id` | For business/residential hierarchies |
| `balance_summary` | Derived from `core_transactions.running_balance`, `core_invoices.balance` | Requires aggregation per customer |
| `billing_preferences` | `account_billing_parameters.*` | Terms, auto-pay settings, invoice delivery |
| `created_at` / `updated_at` | `accounts.created_at`, `accounts.updated_at` | Audit metadata |
| `archived_at` | `accounts.archived_at` | Determine inactive/archived state |
| `tags` | `account_tags` (if available) | Map to Splynx customer groups/tags |

**Additional Joins:** `account_billing_parameters` (auto-pay, delivery), `account_events` (timeline), `account_statuses`, `account_types`.

### 1.2 NormalizedContact

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `contacts.id` | Primary key |
| `customer_id` | `contacts.contactable_id` where `contactable_type='Account'` | FK to `NormalizedCustomer.external_id` |
| `role` | `contacts.role` | Map to Splynx contact types (billing/technical/etc.) |
| `is_primary` | `contacts.primary` | Boolean |
| `name` | `contacts.name` | |
| `email` | `contacts.email_address` | |
| `phone` | `contacts.phone_numbers[]` (CSV `phone_numbers.csv`) | Capture phone entries via supplemental table |
| `language` | `contacts.language` | Optional locale mapping |
| `marketing_opt_in` | `contacts.marketing_opt_in` | Communication preference |
| `portal_username` | `contacts.username` | For customer portal access |
| `created_at` / `updated_at` | `contacts.created_at`, `contacts.updated_at` | |

### 1.3 NormalizedAddress

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `addresses.id` | |
| `customer_id` | `addresses.addressable_id` where `addressable_type='Account'` | |
| `kind` | Determine from `addresses` flags (`billing_default_id`, `service_default_id`) | Map to billing/service/shipping |
| `line1`, `line2`, `city`, `state`, `postal_code`, `country` | `addresses.*` | |
| `latitude` / `longitude` | `addresses.latitude`, `addresses.longitude` | Geo positioning |
| `attainable_speed` | `addresses.attainable_download_speed`, `addresses.attainable_upload_speed` | Service qualification |
| `address_status` | `addresses.address_status_id` → `address_statuses.name` | |
| `created_at` / `updated_at` | `addresses.created_at`, `addresses.updated_at` | |

### 1.4 NormalizedAccountGroup / Tags

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `account_groups.id` | |
| `name` | `account_groups.name` | Map to Splynx categories/partner assignments |
| `description` | `account_groups.description` (if present) | |
| `created_at` / `updated_at` | `account_groups.created_at`, `account_groups.updated_at` | |
| `members` | Bridge via CSV `account_group_members.csv` | Link `account_id` ↔ `group_id` |

### 1.5 Supporting Tables / Lookups

- `account_statuses`, `account_types`, `account_billing_parameters`, `account_events`.

## 2. Service & Tariff Domain

### 2.1 NormalizedService

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `account_services.id` | Service instance |
| `customer_id` | `account_services.account_id` | |
| `service_template_id` | `account_services.service_id` | Join to `services` |
| `package_id` | `account_services.package_id` | Sonar bundle reference |
| `status` | Derived (GraphQL `account_services` + status history) | Map to Splynx service states |
| `activation_date` | `account_services.created_at` / `addition_prorate_date` | |
| `next_bill_date` | `account_services.next_bill_date` | |
| `price_override` | `account_services.price_override`, `price_override_reason`, `quantity` | |
| `usage_percent` | `account_services.data_usage_percentage` | For usage-based services |
| `notes` | `account_services.name_override`, `account_services.notes` (CSV) | |
| `created_at` / `updated_at` | `account_services.created_at`, `account_services.updated_at` | |

**Detail data:** `account_voice_service_details`, `data_service_details`, `usage_based_service_details` provide technology-specific attributes (bandwidth, call plans, caps). Inventory/IP relationships derived from `account_equipment_assignments`, `account_ip_assignments`.

### 2.2 NormalizedTariff (Service Template)

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `services.id` | |
| `name` | `services.name` | |
| `type` | `services.type` | Map to Splynx tariff type |
| `enabled` | `services.enabled` | |
| `base_price` | `services.amount` | Default recurring price |
| `application` | `services.application` | Indicates recurring vs one-time |
| `general_ledger_code_id` | `services.general_ledger_code_id` | |
| `tax_definition_id` | `services.tax_definition_id` → `service_tax_definitions` | |
| `reverse_tax_definition_id` | `services.reverse_tax_definition_id` | |
| `created_at` / `updated_at` | `services.created_at`, `services.updated_at` | |

**Supplementary:** `service_metadata` / `service_metadata_values`, `service_taxes`, `service_tax_definitions`, `packages`, `package_service` (CSV) to capture bundled offerings and tax details.

## 3. Billing & Finance Domain

### 3.1 NormalizedInvoice

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `core_invoices.id` | |
| `customer_id` | `core_invoices.account_id` | |
| `number` | `core_invoices.number` (if populated) | Generate deterministic number when absent |
| `status` | Derived from `core_invoices` flags (`frozen`, `delinquent`, `balance`) | Map to Splynx invoice status codes |
| `issue_date` | `core_invoices.date` | |
| `due_date` | `core_invoices.due_date` | |
| `subtotal` | `core_invoices.subtotal` (CSV) or sum of lines | |
| `tax_total` | `core_invoices.tax_total` (CSV) | |
| `total` | `core_invoices.total` | |
| `balance` | `core_invoices.balance` | |
| `auto_pay_date` | `core_invoices.auto_pay_date` | |
| `delinquency_date` | `core_invoices.delinquency_date` | |
| `created_at` / `updated_at` | `core_invoices.created_at`, `core_invoices.updated_at` | |

### 3.2 NormalizedInvoiceLine

- **Primary Source:** Sonar CSV `invoice_items.csv` (GraphQL collection not in backup). Use CSV columns `invoice_id`, `service_id`, `description`, `quantity`, `price`, `tax_amount`, `type`, timestamps.
- **Transformation:** Map Sonar line `type` to Splynx invoice item categories (recurring, setup, discount, tax).

### 3.3 NormalizedPayment

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `payments.id` | |
| `customer_id` | `payments.account_id` | |
| `amount` | `payments.amount` | |
| `status` | Evaluate using `payments.amount_remaining`, status fields (CSV) | |
| `method` | Combine `payments.method`, `credit_card_id`, `bank_account_id` | Map to Splynx payment method IDs |
| `transaction_fee` | `payments.fee`, `payments.fractional_fee` | Optional surcharge |
| `processor_response` | `payments.full_processor_response` | Preserve for audit |
| `created_at` | `payments.created_at` | |
| `description` | `payments.description` | |

### 3.4 NormalizedTransaction

- **Source:** `core_transactions`, `transactions`, `tax_transactions`.
- **Attributes:** `external_id`, `customer_id`, `amount`, `type`, `running_balance`, `related_invoice_id`, `related_payment_id`, `description`, `created_at`.
- **Use:** Provide ledger history for validation/reporting; optional load into Splynx as journal entries.

### 3.5 Payment Applications / Credits / Debits

- Use Sonar CSV tables (`credits.csv`, `debits.csv`, `payments.csv`, `invoice_item_payments.csv` if available) to determine how payments settle invoices.
- Normalized model should represent many-to-many relationship so Splynx payment allocation APIs can be driven correctly.

## 4. Security & Administration Domain

### 4.1 NormalizedUser

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `users.id` | |
| `username` | `users.username` | |
| `name` | `users.name` | |
| `email` | `users.email_address` | |
| `status` | `users.status` | Map to Splynx admin status |
| `auth_provider` | `users.auth_provider_type` | |
| `last_login` | `users.last_sign_in_at` | |

### 4.2 NormalizedRole

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `roles.id` | |
| `name` | `roles.name` | |
| `description` | `roles.description` | |
| `scope` | `roles.scope` | Map to Splynx scope codes (fallback `global`) |
| `is_system` | `roles.system` | Boolean |

### 4.3 NormalizedPermission

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `external_id` | `permissions.id` | |
| `category` | `permission_categories.name` via `permissions.permission_category_id` | |
| `code` | `permissions.name` | Lowercase, replace spaces with `_` |
| `description` | `permissions.description` | |
| `is_active` | `permissions.active` | Default to true when null |

### 4.4 NormalizedRolePermission

| Normalized Attribute | Sonar Source | Notes |
| --- | --- | --- |
| `role_id` | `role_permissions.role_id` | FK to `NormalizedRole.external_id` |
| `permission_id` | `role_permissions.permission_id` | FK to `NormalizedPermission.external_id` |
| `granted_at` | `role_permissions.created_at` | |
| `granted_by` | `role_permissions.created_by_user_id` | Optional; resolve via `NormalizedUser` |
| `inherited_from` | `role_permissions.inherited_role_id` | Track inheritance chain |

## Next Steps
- Extend this document with mappings for Inventory/Devices, Network/IP, Security, Support, etc.
- Cross-reference the Sonar CSV exports (`zips/*.csv`) to validate field names and enumerations where GraphQL samples are sparse.
- Define transformation rules (e.g., boolean to enum, date combination, derived balances) alongside each normalized attribute.
