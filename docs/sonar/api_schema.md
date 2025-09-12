# Sonar GraphQL API Deep Schema Analysis

Generated on: 2025-09-12T04:04:40.078366

## Executive Summary

- **Query Type**: Query
- **Mutation Type**: Mutation
- **Total Types**: 1393
- **Schema Complexity**: high
- **Total Entities Found**: 591
- **Business Objects**: 621
- **Custom Scalars**: 27

## API Capabilities Overview

### Queries (318 total)

This Sonar instance exposes 318 different query endpoints categorized as follows:

- **Accounts**: 19 queries
- **Services**: 29 queries
- **Billing**: 35 queries
- **Network_Equipment**: 9 queries
- **Network_Interfaces**: 9 queries
- **Ip_Management**: 17 queries
- **Network_Protocols**: 10 queries
- **Sites**: 6 queries
- **Towers**: 2 queries
- **Geographic**: 9 queries
- **Physical_Assets**: 4 queries
- **Inventory**: 20 queries
- **Devices**: 4 queries
- **Users**: 4 queries
- **Roles**: 3 queries
- **Authentication**: 7 queries
- **Tickets**: 8 queries
- **Maintenance**: 1 queries
- **Monitoring**: 4 queries
- **Availability**: 1 queries
- **Contacts**: 13 queries
- **Financial**: 1 queries
- **Contracts**: 2 queries
- **Jobs**: 6 queries
- **Logs**: 9 queries
- **Configuration**: 7 queries
- **Backup**: 1 queries
- **Integration**: 2 queries
- **Provisioning**: 2 queries
- **Usage**: 5 queries
- **Documents**: 2 queries
- **Scheduling**: 7 queries
- **Voip**: 2 queries
- **Security**: 2 queries
- **Other**: 56 queries

### Detailed Query Breakdown


#### Accounts Queries (19 total)

- `account_adtran_mosaic_service_details`
- `account_billing_parameters`
- `account_calix_service_details`
- `account_events`
- `account_groups`
- `account_ip_assignments`
- `account_services`
- `account_statuses`
- `account_types`
- `account_voice_service_details`
- `accounts`
- `bank_account_processor_credentials`
- `bank_account_processors`
- `bank_accounts`
- `radius_accounts`
- `scheduled_event_account_calix_service_details`
- `scheduled_event_account_voice_service_details`
- `serviceable_address_account_assignment_futures`
- `serviceable_address_account_assignment_histories`

#### Services Queries (29 total)

- `adjustment_service_details`
- `billing_services`
- `data_service_details`
- `expiring_service_details`
- `fibermap_plans`
- `fibermap_service_locations`
- `find_address_by_fibermap_service_location`
- `instance_service_funds`
- `integration_service_mappings`
- `job_services`
- `network_site_serviceable_address_lists`
- `overage_service_details`
- `package_services`
- `packages`
- `rate_centers`
- `recurring_service_details`
- `service_metadata`
- `service_metadata_values`
- `service_tax_definitions`
- `service_taxes`
- `services`
- `subscriptions`
- `voice_provider_rate_import_recipes`
- `voice_provider_rate_imports`
- `voice_provider_rates`
- `voice_service_details`
- `voice_service_generic_parameter_tax_definitions`
- `voice_service_generic_parameter_taxes`
- `voice_service_generic_parameters`

#### Billing Queries (35 total)

- `avalara_tax_categories`
- `avalara_tax_definitions`
- `billing_defaults`
- `billing_setting`
- `core_credit_cards`
- `core_invoices`
- `core_transactions`
- `credit_card_processor_credentials`
- `credit_card_processors`
- `credit_cards`
- `credits`
- `debits`
- `fractional_debits`
- `fractional_tax_transactions`
- `geo_tax_zones`
- `invoice_attachments`
- `invoice_messages`
- `invoice_template_versions`
- `invoice_templates`
- `invoices`
- `monthly_billing_completions`
- `payments`
- `printed_invoice_batches`
- `refunded_payments`
- `reversed_payments`
- `tax_exemptions`
- `tax_overrides`
- `tax_provider_credentials`
- `tax_providers`
- `tax_transactions`
- `taxes`
- `transactions`
- `usage_based_billing_policies`
- `usage_based_billing_policy_free_periods`
- `voided_payments`

#### Network_Equipment Queries (9 total)

- `application_firewall_rules`
- `cable_modem_provisioner_credentials`
- `cable_modem_provisioners`
- `device_interface_mappings`
- `fibermap_integrations`
- `integration_field_mappings`
- `map_overlays`
- `map_overlays_within_box`
- `network_monitoring_graphs`

#### Network_Interfaces Queries (9 total)

- `available_reports`
- `call_detail_record_import_recipes`
- `call_detail_record_imports`
- `did_import_recipes`
- `fcc_form_477_reports`
- `imports`
- `snmp_interface_numeric_results`
- `splice_report`
- `system_backup_exports`

#### Ip_Management Queries (17 total)

- `deposit_slips`
- `dhcp_server_credentials`
- `dhcp_server_identifiers`
- `dhcp_servers`
- `did_assignment_histories`
- `did_assignments`
- `get_next_ip_address_in_ip_pool`
- `get_next_subnet_in_subnet`
- `get_next_subnet_in_supernet`
- `ip_assignment_histories`
- `ip_assignments`
- `ip_pools`
- `my_ip_address`
- `netflow_allowed_subnets`
- `subnets`
- `ticket_recipients`
- `uninventoried_mac_addresses`

#### Network_Protocols Queries (10 total)

- `radius_group_reply_attributes`
- `radius_groups`
- `radius_server_credentials`
- `radius_servers`
- `radius_session_histories`
- `snmp_oid_threshold_violations`
- `snmp_oid_thresholds`
- `snmp_oids`
- `snmp_overrides`
- `snmp_results`

#### Sites Queries (6 total)

- `email_locations`
- `internal_locations`
- `inventory_locations`
- `netflow_on_premises`
- `network_sites`
- `vehicle_location_histories`

#### Towers Queries (2 total)

- `towercoverage_configuration`
- `towercoverage_submissions`

#### Geographic Queries (9 total)

- `address_lists`
- `address_statuses`
- `addresses`
- `email_address_lookup`
- `get_gps_tracking_provider_vehicles`
- `gps_tracking_provider_credentials`
- `gps_tracking_providers`
- `schedule_addresses`
- `validate_address`

#### Physical_Assets Queries (4 total)

- `order_groups`
- `stored_groups`
- `system_backups`
- `ticket_groups`

#### Inventory Queries (20 total)

- `alerting_rotation_inventory_items`
- `company_departments`
- `departments`
- `generic_inventory_assignees`
- `generic_inventory_item_action_logs`
- `generic_inventory_items`
- `global_inventory_model_min_maxes`
- `inventory_item_events`
- `inventory_items`
- `inventory_model_categories`
- `inventory_model_field_data`
- `inventory_model_fields`
- `inventory_model_min_maxes`
- `inventory_models`
- `non_inventory_items`
- `purchase_order_items`
- `task_template_items`
- `vendor_items`
- `vendors`
- `webhook_model_events`

#### Devices Queries (4 total)

- `inline_device_credentials`
- `inline_devices`
- `webhook_endpoint_event_dispatch_attempts`
- `webhook_endpoint_event_dispatches`

#### Users Queries (4 total)

- `mfa_admin_setting`
- `order_group_users`
- `stored_view_users`
- `users`

#### Roles Queries (3 total)

- `access_logs`
- `personal_access_tokens`
- `roles`

#### Authentication Queries (7 total)

- `auth_providers`
- `external_marketing_provider_credentials`
- `lte_provider_credentials`
- `password_policy`
- `pay_pal_credentials`
- `system_backup_destination_credentials`
- `validate_credential`

#### Tickets Queries (8 total)

- `instance_management_requests`
- `task_templates`
- `tasks`
- `ticket_categories`
- `ticket_comments`
- `ticket_replies`
- `ticketing_setting`
- `tickets`

#### Maintenance Queries (1 total)

- `scheduled_events`

#### Monitoring Queries (4 total)

- `alerting_rotation_days`
- `alerting_rotations`
- `network_monitoring_templates`
- `notifications`

#### Availability Queries (1 total)

- `schedule_availability_day_times`

#### Contacts Queries (13 total)

- `contacts`
- `email_categories`
- `email_clicks`
- `email_domains`
- `email_message_contents`
- `email_messages`
- `email_opens`
- `email_variables`
- `emails`
- `mass_emails`
- `phone_number_types`
- `phone_numbers`
- `triggered_emails`

#### Financial Queries (1 total)

- `general_ledger_codes`

#### Contracts Queries (2 total)

- `contract_templates`
- `contracts`

#### Jobs Queries (6 total)

- `ach_batches`
- `job_available_times`
- `job_check_ins`
- `job_types`
- `jobs`
- `print_to_mail_batches`

#### Logs Queries (9 total)

- `adtran_mosaic_audits`
- `adtran_mosaic_kafka_events`
- `adtran_mosaic_workflow_events`
- `calix_cloud_audits`
- `call_logs`
- `disconnection_logs`
- `logs`
- `smtp_events`
- `webhook_endpoint_events`

#### Configuration Queries (7 total)

- `adtran_mosaic_settings`
- `calix_cloud_settings`
- `poller_setting`
- `print_to_mail_setting`
- `sms_setting`
- `system_backup_setting`
- `system_setting`

#### Backup Queries (1 total)

- `system_backup_destinations`

#### Integration Queries (2 total)

- `external_marketing_providers`
- `webhook_endpoints`

#### Provisioning Queries (2 total)

- `calix_provisioning_list`
- `deployment_types`

#### Usage Queries (5 total)

- `custom_field_data`
- `data_usage`
- `data_usage_histories`
- `data_usage_top_offs`
- `data_usage_totals`

#### Documents Queries (2 total)

- `files`
- `print_to_mail_document_cost_estimate`

#### Scheduling Queries (7 total)

- `calendar_icals`
- `schedule`
- `schedule_availabilities`
- `schedule_blocker_day_times`
- `schedule_blocker_overrides`
- `schedule_blockers`
- `schedule_time_offs`

#### Voip Queries (2 total)

- `call_detail_records`
- `voice_providers`

#### Security Queries (2 total)

- `handwritten_signatures`
- `signatures`

#### Other Queries (56 total)

- `adtran_mosaic_cloud_list`
- `available_explores`
- `calix_integrations`
- `canned_replies`
- `canned_reply_categories`
- `canned_reply_with_variable_replacement`
- `companies`
- `custom_fields`
- `custom_links`
- `custom_links_allowed_variables`
- `custom_links_for_entity`
- `daily_aggregate_values`
- `delinquency_exclusions`
- `dids`
- `disbursement_details`
- `disbursements`
- `discounts`
- `disputes`
- `drive_times`
- `epcs`
- `general_search`
- `geofences`
- `icmp_results`
- `identity_provider_active_directory_details`
- `identity_provider_google_details`
- `identity_provider_microsoft_details`
- `identity_provider_saml_details`
- `identity_providers`
- `inbound_mailboxes`
- `local_prefixes`
- `looker_explore_licenses`
- `looker_view_licenses`
- `lte_providers`
- `manufacturers`
- `me`
- `message_categories`
- `netflow_endpoints`
- `netflow_whitelists`
- `notes`
- `pollers`
- `preseem`
- `print_to_mail_order_errors`
- `print_to_mail_orders`
- `purchase_orders`
- `reverse_geocode`
- `saved_message_categories`
- `search_filters`
- `sms_message_contents`
- `sms_messages`
- `sms_outbound_messages`
- `stored_filters`
- `stored_views`
- `supernets`
- `system_environment`
- `triggered_messages`
- `vehicles`

## Complete Entity Catalog (591 entities)

### Entity Distribution by Category

- **Accounts**: 46 entities
- **Authentication**: 14 entities
- **Availability**: 4 entities
- **Backup**: 4 entities
- **Billing**: 67 entities
- **Configuration**: 8 entities
- **Contacts**: 22 entities
- **Contracts**: 4 entities
- **Devices**: 22 entities
- **Documents**: 3 entities
- **Financial**: 2 entities
- **Geographic**: 17 entities
- **Integration**: 5 entities
- **Inventory**: 44 entities
- **Ip_Management**: 33 entities
- **Jobs**: 11 entities
- **Logs**: 20 entities
- **Maintenance**: 2 entities
- **Monitoring**: 12 entities
- **Network_Equipment**: 18 entities
- **Network_Interfaces**: 18 entities
- **Network_Protocols**: 22 entities
- **Other**: 48 entities
- **Physical_Assets**: 1 entities
- **Provisioning**: 2 entities
- **Roles**: 11 entities
- **Scheduling**: 11 entities
- **Security**: 4 entities
- **Services**: 58 entities
- **Sites**: 13 entities
- **Tickets**: 24 entities
- **Towers**: 3 entities
- **Usage**: 6 entities
- **Users**: 8 entities
- **Voip**: 4 entities

### Detailed Entity Analysis


## Accounts Entities (46 total)


### TriggeredMessage

**Description**: A message that is sent when a specific event occurs.

**Category**: accounts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 26

**Key Fields**: `id`, `sonar_unique_id`, `email_message_id`, `job_type_id`, `name`, `signature_id`, `sms_message_id`, `email_message`, `email_categories`

**Enum Fields**: 1 (`trigger`)

**Relationship Fields**: 17 (`id`, `email_message_id`, `job_type_id`, `signature_id`, `sms_message_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `allow_children`: `Boolean` (required) - Whether or not child accounts are allowed.
- `count`: `Int` - The count associated with this `TriggeredMessage`. This is defined by the trigger, and could be something like a number of days, months, gigabytes, etc.
- `email_message_id`: `Int64Bit` - The ID of an EmailMessage.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `job_type_id`: `Int64Bit` - The ID of a `JobType`.
- `name`: `String` (required) - A descriptive name.
- `protected`: `Boolean` (required) - If an item is protected, it cannot be modified or deleted.
- `signature_id`: `Int64Bit` - The ID of a signature.
- `sms_message_id`: `Int64Bit` - The ID of the SMS message.
- `trigger`: `MessageTrigger` (required) (enum) - The trigger for this message.
- `email_message`: `EmailMessage` - An email message.
- `job_type`: `JobType` - The type of a `Job`.
- `signature`: `Signature` - A signature.
- `sms_message`: `SmsMessage` - An SMS message.
- `message_categories`: `MessageCategoryConnection` (required) (connection) - A categorization of a message by type.
- `email_categories`: `EmailCategoryConnection` (required) (connection) - A categorization of an `Email` by type.
- `invoices`: `InvoiceConnection` (required) (connection) - An invoice.
- `accounts_exceeding_usage_triggers`: `AccountConnection` (required) (connection) - Accounts exceeding a data usage triggered email.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Poller

**Description**: A `Poller`.

**Category**: accounts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `api_key`, `name`

**Relationship Fields**: 5 (`id`, `subnets`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `api_key`: `String` (required) - An API key.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `icmp_time_taken`: `Int` - The amount of time it took to poll ICMP status.
- `name`: `String` (required) - A descriptive name.
- `results_last_received`: `Datetime` - When the results were last received.
- `snmp_time_taken`: `Int` - The amount of time it took to poll SNMP status.
- `time_of_last_account_poll`: `Datetime` - The UTC timestamp for the last time accounts were polled.
- `time_of_last_infrastructure_poll`: `Datetime` - The UTC timestamp for the last time infrastructure was polled.
- `version`: `String` - Version.
- `subnets`: `SubnetConnection` (required) (connection) - An IPv4/IPv6 subnet.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Company

**Description**: A company you do business as.

**Category**: accounts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 39

**Key Fields**: `id`, `sonar_unique_id`, `name`, `phone_number`, `tax_identification`

**Enum Fields**: 2 (`country`, `isp_type`)

**Relationship Fields**: 27 (`id`, `country`, `customer_portal_url`, `isp_type`, `phone_number`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `billing_communication_delay_end_local_time`: `Time` - The daily end time of the period during which billing communication e.g. new invoices, delinquency, etc. will not be sent.
- `billing_communication_delay_start_local_time`: `Time` - The daily start time of the period during which billing communication e.g. new invoices, delinquency, etc. will not be sent.
- `checks_payable_to`: `String` - On an enabled remittance slip, who should checks be made payable to?
- `country`: `Country` (required) (enum) - A two character country code.
- `customer_portal_url`: `URL` - The URL to your customer portal.
- `default`: `Boolean` (required) - Whether or not this entity is a default entry.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `isp_type`: `IspType` (enum) - The ISP type of this `Company`.
- `name`: `String` (required) - A descriptive name.
- `phone_number`: `Numeric` - A telephone number.
- `primary_color`: `HtmlHexColor` (required) - The primary color to use in Sonar.
- `secondary_color`: `HtmlHexColor` (required) - The secondary color to use in Sonar.
- `show_remittance_slip`: `Boolean` (required) - Whether or not to include a detachable remittance slip on the invoice.
- `tax_identification`: `String` - A tax identification number. Should only be entered if you are required to share some type of tax identification information with your customers.
- `website_address`: `URL` - The address of the company website.
- `payments`: `PaymentConnection` (required) (connection) - A payment.
- `accounts`: `AccountConnection` (required) (connection) - A customer account.
- `debits`: `DebitConnection` (required) (connection) - A debit.
- `invoices`: `InvoiceConnection` (required) (connection) - An invoice.
- `services`: `ServiceConnection` (required) (connection) - A service.
- `contract_templates`: `ContractTemplateConnection` (required) (connection) - A contract template.
- `job_types`: `JobTypeConnection` (required) (connection) - The type of a `Job`.
- `discounts`: `DiscountConnection` (required) (connection) - A discount.
- `company_departments`: `CompanyDepartmentConnection` (required) (connection) - A department in a company.
- `network_sites`: `NetworkSiteConnection` (required) (connection) - A network site.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `custom_fields`: `CustomFieldConnection` (required) (connection) - A user defined field.
- `credit_card_processors`: `CreditCardProcessorConnection` (required) (connection) - A company that processes `CreditCard` transactions.
- `bank_account_processors`: `BankAccountProcessorConnection` (required) (connection) - A processor or method of processing bank account payments.
- `invoice_templates`: `InvoiceTemplateConnection` (required) (connection) - A template for generating invoices.

---

### CalixIntegration

**Description**: A configuration for a specific Calix SMx endpoint.

**Category**: accounts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 41

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `org_id`, `residential_delinquency_policy_map`, `residential_delinquency_service_template`, `subscriber_custom_field_id`

**Enum Fields**: 2 (`smx_version`, `status`)

**Relationship Fields**: 13 (`id`, `company_id`, `smx_version`, `status`, `subscriber_custom_field_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `alarms_change_device_status`: `Boolean` (required) - Controls if Sonar updates the ICMP device status from SMx alarms
- `alarms_create_logs`: `Boolean` (required) - Controls if Sonar should add SMx device alarms to inventory item logs
- `alarms_update_ip_assignment`: `Boolean` (required) - Controls if Sonar updates the inventory item's soft IP address from SMx DHCP lease alarms.
- `bounce_ports`: `Boolean` (required) - Disable, pause, then re-enable Calix ONT ports after creating or removing service.  Recommended for deployments using DHCP within SMx.
- `commercial_delinquency_policy_map`: `String` - The Calix policy map name to use when a commercial account becomes delinquent.
- `commercial_delinquency_service_template`: `String` - The Calix service template name to use when a commercial account becomes delinquent.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `create_default_service_detail`: `Boolean` - Whether or not a default Calix service detail record is created when integration service added.
- `enable_ont_synchronization`: `Boolean` (required) - Controls whether to turn on synchronization of Calix ONTs and Subscribers, from Sonar Inventory Items and Accounts.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `government_delinquency_policy_map`: `String` - The Calix policy map name to use when a government account becomes delinquent.
- `government_delinquency_service_template`: `String` - The Calix service template name to use when a government account becomes delinquent.
- `industrial_delinquency_policy_map`: `String` - The Calix policy map name to use when an industrial account becomes delinquent.
- `industrial_delinquency_service_template`: `String` - The Calix service template name to use when an industrial account becomes delinquent.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `org_id`: `String` (required) - Subscriber organization ID to use for integration
- `residential_delinquency_policy_map`: `String` - The Calix policy map name to use when a residential account becomes delinquent.
- `residential_delinquency_service_template`: `String` - The Calix service template name to use when a residential account becomes delinquent.
- `senior_citizen_delinquency_policy_map`: `String` - The Calix policy map name to use when a senior citizen account becomes delinquent.
- `senior_citizen_delinquency_service_template`: `String` - The Calix service template name to use when a senior citizen account becomes delinquent.
- `smx_credentials`: `String` (required) - The basic auth credentials to use with SMx, username:password
- `smx_url`: `String` (required) - The URL of the SMx server including the SMx API port, eg. mysmx.org:18443 (SMx uses 18443 as the default API port)
- `smx_version`: `CalixIntegrationVersion` (required) (enum) - The software version of SMx that will be used in integration
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `subscriber_custom_field_id`: `Int64Bit` - The ID of the account custom field which holds the SMx subscriber ID of the account.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `company`: `Company` - A company you do business as.
- `integration_field_mappings`: `IntegrationFieldMappingConnection` (required) (connection) - An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
- `integration_service_mappings`: `IntegrationServiceMappingConnection` (required) (connection) - An entity which maps a service to a vendor specific service name
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `account_calix_service_details`: `AccountCalixServiceDetailConnection` (required) (connection) - Holds information for provisioning service on Calix devices.
- `scheduled_event_account_calix_service_details`: `ScheduledEventAccountCalixServiceDetailConnection` (required) (connection) - The `AccountCalixServiceDetail` records used to configure the Calix integrations when a `ScheduledEvent` is executed.

---

### AccountType

**Description**: The account type.

**Category**: accounts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `invoice_message_id`, `name`

**Enum Fields**: 2 (`icon`, `type`)

**Relationship Fields**: 14 (`id`, `color`, `icon`, `invoice_message_id`, `type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `color`: `HtmlHexColor` (required) - Color.
- `icon`: `Icon` (required) (enum) - An icon.
- `invoice_message_id`: `Int64Bit` - The ID of an `InvoiceMessage`.
- `name`: `String` (required) - A descriptive name.
- `type`: `AccountTypeEnum` (required) (enum) - The type.
- `accounts`: `AccountConnection` (required) (connection) - A customer account.
- `address_lists`: `AddressListConnection` (required) (connection) - An address list defines some criteria by which to group accounts for network policy enforcement.
- `alerting_rotations`: `AlertingRotationConnection` (required) (connection) - An alerting rotation.
- `invoice_templates`: `InvoiceTemplateConnection` (required) (connection) - A template for generating invoices.
- `radius_groups`: `RadiusGroupConnection` (required) (connection) - A RADIUS group.
- `invoice_message`: `InvoiceMessage` - A message that is appended to specific invoices.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Discount

**Description**: A discount.

**Category**: accounts
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 40

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `company_id`, `debit_id`, `general_ledger_code`, `general_ledger_code_description`, `reversed_by_user_id`, `service_id`, `service_name`, `tax_provider_id`, `user_id`, `tax_provider`

**Enum Fields**: 2 (`service_transaction_type`, `type`)

**Relationship Fields**: 21 (`id`, `account_id`, `company_id`, `debit_id`, `reversed_by_user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `amount`: `Int` (required) - The amount of the `Discount`.
- `amount_remaining`: `Int` (required) - The amount remaining that can be used.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `debit_id`: `Int64Bit` - If this discount was created due to reversal of a `Debit`, this field will link to the reversed `Debit`.
- `description`: `String` - A human readable description.
- `general_ledger_code`: `String` - A general ledger code.
- `general_ledger_code_description`: `String` - A general ledger code description.
- `minutes`: `Float` - The total number of minutes.
- `prorated_from`: `Date` - The date this transaction was prorated from.
- `prorated_to`: `Date` - The date this transaction was prorated to.
- `quantity`: `Int` (required) - The quantity for this service.
- `quantity_prorated_from`: `Int` - The quantity the associated service had before the quantity was changed and prorated.
- `quantity_prorated_to`: `Int` - The quantity the associated service was changed to when the quantity was changed and prorated.
- `reversed`: `Boolean` (required) - Whether or not this has been reversed.
- `reversed_at`: `Datetime` - When this was reversed.
- `reversed_by_user_id`: `Int64Bit` - The user ID that reversed this.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service_name`: `String` (required) - The name of a service.
- `service_transaction_type`: `ServiceTransactionType` (enum) - The type of transaction on this service.
- `tax_committed`: `Boolean` (required) - Whether this entity's taxes have been committed or not.
- `tax_provider_id`: `Int64Bit` - The ID of an `TaxProvider`.
- `type`: `ServiceType` (required) (enum) - The type.
- `user_id`: `Int64Bit` - The ID of the user who created this transaction.
- `account`: `Account` - A customer account.
- `company`: `Company` - A company you do business as.
- `service`: `Service` - A service.
- `user`: `User` - A user that can login to Sonar.
- `debit`: `Debit` - A debit.
- `tax_provider`: `TaxProvider` - A tax provider.
- `reversed_by_user`: `User` - The user that caused a reversal.
- `tax_transactions`: `TaxTransactionConnection` (required) (connection) - A tax transaction.
- `credits`: `CreditConnection` (required) (connection) - The application of a `Discount` or `Payment` against an `Invoice`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Disbursement

**Description**: A disbursement.

**Category**: accounts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 23

**Key Fields**: `id`, `sonar_unique_id`, `bank_account_processor_id`, `credit_card_processor_id`, `external_id`, `merchant_id`

**Enum Fields**: 3 (`schedule`, `schedule_unit`, `status`)

**Relationship Fields**: 12 (`id`, `bank_account_processor_id`, `credit_card_processor_id`, `schedule`, `schedule_unit`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `bank_account`: `String` - The bank account.
- `bank_account_processor_id`: `Int64Bit` - The ID of a BankProcessor.
- `credit_card_processor_id`: `Int64Bit` - The ID of a CreditCardProcessor.
- `external_id`: `String` (required) - The payment processor's external ID.
- `merchant_id`: `String` - The sonarPay Merchant ID
- `processed_at`: `Datetime` - The date and time this entity was processed.
- `schedule`: `DisbursementSchedule` (enum) - The disbursement payout schedule.
- `schedule_amount`: `Int` - The amount scheduled for payout.
- `schedule_factor`: `Int` - The disbursement payout scheduling factor.
- `schedule_unit`: `SonarPayUnit` (enum) - The unit of measurement for this disbursement's payout amount.
- `status`: `DisbursementStatus` (required) (enum) - The status.
- `disbursement_details`: `DisbursementDetailConnection` (required) (connection) - A disbursement detail.
- `bank_account_processor`: `BankAccountProcessor` - A processor or method of processing bank account payments.
- `credit_card_processor`: `CreditCardProcessor` - A company that processes `CreditCard` transactions.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountStatus

**Description**: The status of an account.

**Category**: accounts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 1 (`icon`)

**Relationship Fields**: 9 (`id`, `color`, `icon`, `accounts`, `address_lists`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `activates_account`: `Boolean` (required) - Whether or not this status activates the account.
- `color`: `HtmlHexColor` (required) - Color.
- `icon`: `Icon` (required) (enum) - An icon.
- `name`: `String` (required) - A descriptive name.
- `accounts`: `AccountConnection` (required) (connection) - A customer account.
- `address_lists`: `AddressListConnection` (required) (connection) - An address list defines some criteria by which to group accounts for network policy enforcement.
- `radius_groups`: `RadiusGroupConnection` (required) (connection) - A RADIUS group.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountGroup

**Description**: An account group.

**Category**: accounts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 9 (`id`, `accounts`, `services`, `address_lists`, `radius_groups`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `accounts`: `AccountConnection` (required) (connection) - A customer account.
- `services`: `ServiceConnection` (required) (connection) - A service.
- `address_lists`: `AddressListConnection` (required) (connection) - An address list defines some criteria by which to group accounts for network policy enforcement.
- `radius_groups`: `RadiusGroupConnection` (required) (connection) - A RADIUS group.
- `alerting_rotations`: `AlertingRotationConnection` (required) (connection) - An alerting rotation.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Account

**Description**: A customer account.

**Category**: accounts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 68

**Key Fields**: `id`, `sonar_unique_id`, `account_status_id`, `account_type_id`, `archived_by_user_id`, `company_id`, `name`, `parent_account_id`, `emails`, `tax_overrides`, `did_assignments`, `did_assignment_histories`

**Relationship Fields**: 55 (`id`, `account_status_id`, `account_type_id`, `archived_by_user_id`, `company_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_status_id`: `Int64Bit` (required) - The ID of an AccountStatus.
- `account_type_id`: `Int64Bit` (required) - The ID of an AccountType.
- `activation_date`: `Date` - The date an account was first activated.
- `activation_time`: `Time` - The time an account was first activated.
- `archived_at`: `Datetime` - The date and time this entity was archived.
- `archived_by_user_id`: `Int64Bit` - The ID of the `User` that archived this entity.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `data_usage_percentage`: `Int` - The percentage of the data usage cap that this account has consumed this month, taking into account any data usage top offs.
- `geopoint`: `Geopoint` - A geo-point.
- `is_delinquent`: `Boolean` (required) - Whether or not this account is delinquent.
- `is_eligible_for_archive`: `Boolean` - Whether or not the Account meets the eligibility criteria for archiving.
- `name`: `String` (required) - A descriptive name.
- `next_bill_date`: `Date` - The next date this service will bill. If this is null, it will bill on the next account billing date.
- `next_recurring_charge_amount`: `Int` - The next recurring charge amount for an account. This is the sum of data, expiring, recurring, and voice services of an account for this billing cycle, including tax.
- `parent_account_id`: `Int64Bit` - The ID of the `Account` that is this `Account`s master.
- `account_billing_parameter`: `AccountBillingParameter` - Parameters that define the billing settings for an `Account`.
- `account_status`: `AccountStatus` - The status of an account.
- `account_type`: `AccountType` - The account type.
- `parent_account`: `Account` - The `Account` that is a parent of this `Account`.
- `archived_by_user`: `User` - The `User` that archived an entity.
- `company`: `Company` - A company you do business as.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `ip_assignment_histories`: `IpAssignmentHistoryConnection` (required) (connection) - A historical record of an IP assignment.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `jobs`: `JobConnection` (required) (connection) - A job, typically in the field.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `account_groups`: `AccountGroupConnection` (required) (connection) - An account group.
- `geo_tax_zones`: `GeoTaxZoneConnection` (required) (connection) - A geographical tax zone.
- `usage_triggered_messages`: `TriggeredMessageConnection` (required) (connection) - The data cap `TriggeredMessages` sent to this `Account` for the current billing cycle.
- `credit_cards`: `CreditCardConnection` (required) (connection) - A credit card.
- `payments`: `PaymentConnection` (required) (connection) - A payment.
- `debits`: `DebitConnection` (required) (connection) - A debit.
- `discounts`: `DiscountConnection` (required) (connection) - A discount.
- `invoices`: `InvoiceConnection` (required) (connection) - An invoice.
- `credits`: `CreditConnection` (required) (connection) - The application of a `Discount` or `Payment` against an `Invoice`.
- `account_services`: `AccountServiceConnection` (required) (connection) - The relationship between an `Account` and a `Service`.
- `child_accounts`: `AccountConnection` (required) (connection) - A list of `Account`s that this `Account` is a parent of.
- `bank_accounts`: `BankAccountConnection` (required) (connection) - A bank account.
- `radius_accounts`: `RadiusAccountConnection` (required) (connection) - A RADIUS account.
- `uninventoried_mac_addresses`: `UninventoriedMacAddressConnection` (required) (connection) - A MAC address that is not recorded in the inventory system.
- `scheduled_events`: `ScheduledEventConnection` (required) (connection) - An `Account` event that is run at a specific time.
- `contracts`: `ContractConnection` (required) (connection) - A contract.
- `monthly_billing_completions`: `MonthlyBillingCompletionConnection` (required) (connection) - A record of a monthly billing cycle.
- `tax_overrides`: `TaxOverrideConnection` (required) (connection) - An override to the default taxation rate.
- `tax_exemptions`: `TaxExemptionConnection` (required) (connection) - A tax exemption.
- `call_logs`: `CallLogConnection` (required) (connection) - A call log.
- `disconnection_logs`: `DisconnectionLogConnection` (required) (connection) - The `Account` disconnections log.
- `serviceable_address_account_assignment_histories`: `ServiceableAddressAccountAssignmentHistoryConnection` (required) (connection) - A `ServiceableAddressAccountAssignmentHistory` for accounts and addresses.
- `data_usage_histories`: `DataUsageHistoryConnection` (required) (connection) - A data usage history entry.
- `data_usage_top_offs`: `DataUsageTopOffConnection` (required) (connection) - A data usage top off.
- `did_assignments`: `DidAssignmentConnection` (required) (connection) - A direct inward dial (DID) assignment.
- `did_assignment_histories`: `DidAssignmentHistoryConnection` (required) (connection) - A historical record of a direct inward dial (DID) assignment.
- `call_detail_records`: `CallDetailRecordConnection` (required) (connection) - A call detail record (CDR).
- `account_events`: `AccountEventConnection` (required) (connection) - A tracked event that has occurred for an `Account`.
- `serviceable_address_account_assignment_futures`: `ServiceableAddressAccountAssignmentFutureConnection` (required) (connection) - An expected change of serviceable address account assignment.

---

### BankAccountProcessor

**Description**: A processor or method of processing bank account payments.

**Category**: accounts
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `provider`

**Enum Fields**: 1 (`provider`)

**Relationship Fields**: 8 (`id`, `provider`, `bank_accounts`, `bank_account_processor_credentials`, `disbursements`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `primary`: `Boolean` (required) - Whether or not this is the primary type of entity.
- `provider`: `BankAccountProvider` (required) (enum) - The provider for this processor.
- `bank_accounts`: `BankAccountConnection` (required) (connection) - A bank account.
- `bank_account_processor_credentials`: `BankAccountProcessorCredentialConnection` (required) (connection) - A credential used when processing bank account payments.
- `disbursements`: `DisbursementConnection` (required) (connection) - A disbursement.
- `companies`: `CompanyConnection` (required) (connection) - A company you do business as.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceableAddressAccountAssignmentHistory

**Description**: A `ServiceableAddressAccountAssignmentHistory` for accounts and addresses.

**Category**: accounts
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `address_id`

**Relationship Fields**: 7 (`id`, `account_id`, `address_id`, `account`, `address`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `address_id`: `Int64Bit` (required) - The ID of the address.
- `end_date`: `Date` - The date that this ends.
- `start_date`: `Date` (required) - The start date for this `ScheduleAvailability`.
- `account`: `Account` - A customer account.
- `address`: `Address` - A geographical address.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduledEventAccountVoiceServiceDetail

**Description**: The `AccountVoiceServiceDetail` records used to configure a voice service when a `ScheduledEvent` is executed.

**Category**: accounts
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `price_override`, `price_override_reason`, `scheduled_event_id`, `voice_service_generic_parameter_id`

**Relationship Fields**: 8 (`id`, `scheduled_event_id`, `voice_service_generic_parameter_id`, `scheduled_event`, `voice_service_generic_parameter`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `price_override`: `Int` - The amount that this service price has been overridden to. If this is null, then the service price is used.
- `price_override_reason`: `String` - The reason that the price of a service has been overridden.
- `quantity`: `Int` (required) - The quantity for this service.
- `scheduled_event_id`: `Int64Bit` (required) - The ID of a `ScheduledEvent`
- `voice_service_generic_parameter_id`: `Int64Bit` (required) - The ID of a voice service configuration parameter.
- `scheduled_event`: `ScheduledEvent` - An `Account` event that is run at a specific time.
- `voice_service_generic_parameter`: `VoiceServiceGenericParameter` - A configurable attribute for a voice service.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduledEventAccountCalixServiceDetail

**Description**: The `AccountCalixServiceDetail` records used to configure the Calix integrations when a `ScheduledEvent` is executed.

**Category**: accounts
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `calix_integration_id`, `ont_port_id`, `scheduled_event_id`

**Relationship Fields**: 9 (`id`, `calix_integration_id`, `scheduled_event_id`, `vlan`, `calix_integration`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `calix_integration_id`: `Int64Bit` (required) - Calix Inegartion ID.
- `custom_json`: `String` - Custom JSON.
- `cvlan`: `Int` - C-VLAN.
- `global_vlan`: `String` - Global VLAN.
- `ont_port_id`: `String` - ONT Port ID.
- `policy_map`: `String` - Policy Map.
- `scheduled_event_id`: `Int64Bit` (required) - The ID of a `ScheduledEvent`
- `use_custom_json`: `Boolean` - Use Custom JSON.
- `vlan`: `Int64Bit` - VLAN.
- `calix_integration`: `CalixIntegration` - A configuration for a specific Calix SMx endpoint.
- `scheduled_event`: `ScheduledEvent` - An `Account` event that is run at a specific time.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountEvent

**Description**: A tracked event that has occurred for an `Account`.

**Category**: accounts
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `account_id`

**Enum Fields**: 1 (`event`)

**Relationship Fields**: 7 (`id`, `account_id`, `event`, `account`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `current`: `String` - Current data.
- `event`: `AccountUpdateEvent` (required) (enum) - An event.
- `event_datetime`: `Datetime` (required) - The date and time of an event sent from Mandrill
- `previous`: `String` - Previous data.
- `account`: `Account` - A customer account.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceableAddressAccountAssignmentFuture

**Description**: An expected change of serviceable address account assignment.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `address_id`

**Relationship Fields**: 9 (`id`, `account_id`, `address_id`, `note`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `address_id`: `Int64Bit` (required) - The ID of the address.
- `note`: `Text` - A note about this expected change of serviceable address account assignment.
- `target_date`: `Date` (required) - The date this is targeted to happen.
- `account`: `Account` - A customer account.
- `address`: `Address` - A geographical address.
- `jobs`: `JobConnection` (required) (connection) - A job, typically in the field.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RadiusAccount

**Description**: A RADIUS account.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `account_service_id`, `username`

**Relationship Fields**: 11 (`id`, `account_id`, `account_service_id`, `password`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `password`: `Text` - A password.
- `username`: `String` (required) - A username, used for authentication.
- `account`: `Account` - A customer account.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `radius_session_histories`: `RadiusSessionHistoryConnection` (required) (connection) - The history of a RADIUS session.

---

### IdentityProviderMicrosoftDetail

**Description**: Details regarding a Microsoft `IdentityProvider`.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `client_id`, `identity_provider_id`, `identity_provider`

**Relationship Fields**: 6 (`id`, `identity_provider_id`, `identity_provider`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `client_id`: `String` (required) - The client ID for this identity provider.
- `client_secret`: `String` (required) - The client secret for this identity provider.
- `identity_provider_id`: `Int64Bit` (required) - The ID of an `IdentityProvider`.
- `identity_provider`: `IdentityProvider` - An identity provider.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IdentityProviderGoogleDetail

**Description**: Details regarding a Google `IdentityProvider`.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `client_id`, `identity_provider_id`, `identity_provider`

**Relationship Fields**: 6 (`id`, `identity_provider_id`, `identity_provider`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `client_id`: `String` (required) - The client ID for this identity provider.
- `client_secret`: `String` (required) - The client secret for this identity provider.
- `identity_provider_id`: `Int64Bit` (required) - The ID of an `IdentityProvider`.
- `identity_provider`: `IdentityProvider` - An identity provider.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### BankAccountProcessorCredential

**Description**: A credential used when processing bank account payments.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `bank_account_processor_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 7 (`id`, `bank_account_processor_id`, `credential`, `bank_account_processor`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `bank_account_processor_id`: `Int64Bit` (required) - The ID of a BankProcessor.
- `credential`: `BankAccountProviderCredential` (required) (enum) - The credential name.
- `value`: `String` (required) - The value.
- `bank_account_processor`: `BankAccountProcessor` - A processor or method of processing bank account payments.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### BankAccount

**Description**: A bank account.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 22

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `bank_account_processor_id`, `customer_profile_id`, `masked_account_number`, `name_on_account`, `routing_number`, `token_id`

**Enum Fields**: 1 (`bank_account_type`)

**Relationship Fields**: 11 (`id`, `account_id`, `bank_account_processor_id`, `bank_account_type`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `auto`: `Boolean` (required) - Whether or not this payment method is enabled for automatic payments.
- `bank_account_processor_id`: `Int64Bit` (required) - The ID of a BankProcessor.
- `bank_account_type`: `BankAccountType` (required) (enum) - The type of bank account this is.
- `customer_profile_id`: `String` - The profile ID provided by a credit card processing service.
- `masked_account_number`: `String` (required) - A partial account number that can be used for identification.
- `name_on_account`: `String` - The name on the account.
- `routing_number`: `String` - The bank routing number.
- `token`: `String` - The tokenized value that represents a credit card, provided by a credit card processing service.
- `token_id`: `String` - The tokenized credit card ID
- `account`: `Account` - A customer account.
- `bank_account_processor`: `BankAccountProcessor` - A processor or method of processing bank account payments.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `payments`: `PaymentConnection` (required) (connection) - A payment.

---

### AccountVoiceServiceDetail

**Description**: A voice service configuration that links a service parameter to an account.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `price_override`, `price_override_reason`, `voice_service_generic_parameter_id`

**Relationship Fields**: 8 (`id`, `account_service_id`, `voice_service_generic_parameter_id`, `account_service`, `voice_service_generic_parameter`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` (required) - The ID of an AccountService.
- `price_override`: `Int` - The amount that this service price has been overridden to. If this is null, then the service price is used.
- `price_override_reason`: `String` - The reason that the price of a service has been overridden.
- `quantity`: `Int` (required) - The quantity for this service.
- `voice_service_generic_parameter_id`: `Int64Bit` (required) - The ID of a voice service configuration parameter.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `voice_service_generic_parameter`: `VoiceServiceGenericParameter` - A configurable attribute for a voice service.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountService

**Description**: The relationship between an `Account` and a `Service`.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 35

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `name_override`, `number_of_times_billed`, `package_id`, `price_override`, `price_override_reason`, `service_id`, `unique_package_relationship_id`

**Relationship Fields**: 20 (`id`, `account_id`, `package_id`, `service_id`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `addition_prorate_date`: `Date` - If this service was prorated when added, this is the date it was prorated from.
- `data_usage_last_calculated_date`: `Date` - The date data usage was last calculated.
- `data_usage_percentage`: `Int` - The percentage of the data usage cap that this account has consumed this month, taking into account any data usage top offs.
- `is_additional`: `Boolean` - Whether or not this account service is an additional service.
- `name_override`: `String` - Overriding the service name will alter the service name printed on an invoice.
- `next_bill_date`: `Date` - The next date this service will bill. If this is null, it will bill on the next account billing date.
- `number_of_times_billed`: `Int` - The number of billing cycles that have already been consumed by this particular service. This is only used for expiring services. NOTE: Typically this is the number of times billed but the value may be modified manually to adjust service expiration. See also the the `ExpiringServiceDetail` `times_to_run` field.
- `package_id`: `Int64Bit` - The ID of a `Package`.
- `price_override`: `Int` - The amount that this service price has been overridden to. If this is null, then the service price is used.
- `price_override_reason`: `String` - The reason that the price of a service has been overridden.
- `quantity`: `Int` (required) - The quantity for this service.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `unique_package_relationship_id`: `String` - A unique ID that describes this unique instance of a `Package` assignment.
- `account`: `Account` - A customer account.
- `package`: `Package` - A collection of `Service`s.
- `service`: `Service` - A service.
- `account_adtran_mosaic_service_details`: `AccountAdtranMosaicServiceDetailConnection` (required) (connection) - An account Adtran Mosaic service detail.
- `account_calix_service_details`: `AccountCalixServiceDetailConnection` (required) (connection) - Holds information for provisioning service on Calix devices.
- `account_voice_service_details`: `AccountVoiceServiceDetailConnection` (required) (connection) - A voice service configuration that links a service parameter to an account.
- `adtran_mosaic_audits`: `AdtranMosaicAuditConnection` (required) (connection) - An Adtran Mosaic audit record.
- `data_usage_histories`: `DataUsageHistoryConnection` (required) (connection) - A data usage history entry.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `ip_assignment_histories`: `IpAssignmentHistoryConnection` (required) (connection) - A historical record of an IP assignment.
- `radius_accounts`: `RadiusAccountConnection` (required) (connection) - A RADIUS account.
- `service_metadata_values`: `ServiceMetadataValueConnection` (required) (connection) - The value of a `ServiceMetadata` field, as it relates to a specific `Service` on a specific `Account`.
- `uninventoried_mac_addresses`: `UninventoriedMacAddressConnection` (required) (connection) - A MAC address that is not recorded in the inventory system.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountCalixServiceDetail

**Description**: Holds information for provisioning service on Calix devices.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `calix_integration_id`, `ont_port_id`

**Relationship Fields**: 8 (`id`, `account_service_id`, `calix_integration_id`, `vlan`, `account_service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` (required) - The ID of an AccountService.
- `calix_integration_id`: `Int64Bit` (required) - Calix Inegartion ID.
- `custom_json`: `String` - Custom JSON.
- `cvlan`: `Int` - C-VLAN.
- `global_vlan`: `String` - Global VLAN.
- `ont_port_id`: `String` - ONT Port ID.
- `policy_map`: `String` - Policy Map.
- `use_custom_json`: `Boolean` - Use Custom JSON.
- `vlan`: `Int64Bit` - VLAN.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `calix_integration`: `CalixIntegration` - A configuration for a specific Calix SMx endpoint.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountBillingParameter

**Description**: Parameters that define the billing settings for an `Account`.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 37

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `billing_default_id`, `delinquency_account_status_id`, `delinquency_removal_account_status_id`

**Enum Fields**: 6 (`anchor_delinquency_logic`, `auto_pay_day`, `bill_day_mode`, `bill_mode`, `default_for`, `due_days_day`)

**Relationship Fields**: 17 (`id`, `account_id`, `anchor_delinquency_logic`, `auto_pay_day`, `bill_day_mode`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `aggregate_invoice_taxes`: `Boolean` (required) - Whether or not to aggregate invoice taxes instead of printing with each charge.
- `aggregate_linked_debits`: `Boolean` (required) - Whether or not to aggregate linked debits on Anchor invoices.
- `anchor_delinquency_logic`: `AnchorDelinquencyLogic` (enum) - Determines if delinquency settings on an Anchor default is applied only to the Anchor account or the Linked accounts as well.
- `auto_pay_day`: `BillingParameterDayOption` (required) (enum) - If `invoice_day` is not null, this allows you to select whether `auto_pay_days` is calculated from the billing day, or the invoice day.
- `auto_pay_days`: `Int` (required) - The number of days after `auto_pay_day` that autopay runs for an invoice.
- `bill_day`: `Int` - The day that billing runs.
- `bill_day_mode`: `BillDayModeOption` (required) (enum) - Whether the account bill and invoice day are fixed, the account activation day is used as bill day, or the account activation day is used as the invoice day.
- `bill_mode`: `BillMode` (required) (enum) - The type of bill this account receives.
- `billing_default_id`: `Int64Bit` - The ID of a BillingDefault.
- `days_of_delinquency_for_status_switch`: `Int` - If `switch_status_after_delinquency` is `true`, then this is the number of days of delinquency to allow before the status switch.
- `default_for`: `BillingDefaultFor` (required) (enum) - Determines if the billing parameters apply by account type or for anchor / linked types.
- `delinquency_account_status_id`: `Int64Bit` - If `switch_status_after_delinquency` is true, this is the account status that the account will be moved into after `days_of_delinquency_for_status_switch` days of delinquency.
- `delinquency_removal_account_status_id`: `Int64Bit` - If `switch_status_after_delinquency` is `true`, then this is the status the account will be moved back into if delinquency is cleared while the account is set to the `delinquency_account_status_id` account status.
- `due_days`: `Int` (required) - The number of days after the invoice date that it is due.
- `due_days_day`: `BillingParameterDayOption` (required) (enum) - If `invoice_day` is not null, this allows you to select whether `due_days` is calculated from the billing day, or the invoice day.
- `grace_days`: `Int` (required) - The number of days after the invoice due date that the invoice is marked delinquent.
- `grace_until`: `Date` - A temporary override that stops the account becoming delinquent until this date.
- `invoice_day`: `Int` - The day that automatic billing invoices are generated for. If this is `null`, then `bill_day` is used.
- `lifeline`: `Boolean` (required) - Whether or not this account participates in the federal Lifeline program.
- `months_to_bill`: `Int` (required) - The number of months to bill at a time.
- `print_invoice`: `Boolean` (required) - Whether this account receives a printed invoice.
- `service_period_duration`: `Int` - The length of the service period in days when using a Flexible Bill Day Mode.
- `service_period_offset`: `Int` - The offset between the service period and the billing period in days when using a Flexible Bill Day Mode.
- `switch_status_after_delinquency`: `Boolean` (required) - Whether or not this account should be moved into another status after being delinquent for a preset period.
- `tax_exempt`: `Boolean` (required) - Whether or not this account is tax exempt.
- `delinquency_account_status`: `AccountStatus` - The status that an `Account` is moved into after a certain length of delinquency.
- `delinquency_removal_account_status`: `AccountStatus` - The `AccountStatus` an account is moved back into after no longer being delinquent, if it is currently in the delinquency account status defined on the `AccountBillingParameter`.
- `account`: `Account` - A customer account.
- `billing_default`: `BillingDefault` - Default billing settings that are applied to some accounts on creation.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccountAdtranMosaicServiceDetail

**Description**: An account Adtran Mosaic service detail.

**Category**: accounts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `adtran_mosaic_setting_id`, `downlink_interface_name`, `uplink_content_provider_name`

**Relationship Fields**: 8 (`id`, `account_service_id`, `adtran_mosaic_setting_id`, `account_service`, `adtran_mosaic_setting`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` (required) - The ID of an AccountService.
- `adtran_mosaic_setting_id`: `Int64Bit` (required) - The ID of an Adtran Mosaic setting.
- `downlink_inner_tag_vlan`: `String` - The name of the Adtran Mosaic downlink inner tag vlan.
- `downlink_interface_name`: `String` - The name of the Adtran Mosaic downlink interface.
- `downlink_outer_tag_vlan`: `String` - The name of the Adtran Mosaic downlink outer tag vlan.
- `uplink_content_provider_name`: `String` - The name of the Adtran Mosaic content provider.
- `uplink_inner_tag_vlan`: `String` - The name of the Adtran Mosaic uplink inner tag vlan.
- `uplink_outer_tag_vlan`: `String` - The name of the Adtran Mosaic uplink outer tag vlan.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `adtran_mosaic_setting`: `AdtranMosaicSetting` - An Adtran Mosaic settings record.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceableAddressAccountAssignmentHistoryConnection

**Description**: The connection wrapper around the `ServiceableAddressAccountAssignmentHistoryConnection` type.

**Category**: accounts
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ServiceableAddressAccountAssignmentHistory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ScheduledEventAccountVoiceServiceDetailConnection

**Description**: The connection wrapper around the `ScheduledEventAccountVoiceServiceDetailConnection` type.

**Category**: accounts
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduledEventAccountVoiceServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ScheduledEventAccountCalixServiceDetailConnection

**Description**: The connection wrapper around the `ScheduledEventAccountCalixServiceDetailConnection` type.

**Category**: accounts
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduledEventAccountCalixServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountEventConnection

**Description**: The connection wrapper around the `AccountEventConnection` type.

**Category**: accounts
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ServiceableAddressAccountAssignmentFutureConnection

**Description**: The connection wrapper around the `ServiceableAddressAccountAssignmentFutureConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ServiceableAddressAccountAssignmentFuture` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RadiusAccountConnection

**Description**: The connection wrapper around the `RadiusAccountConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RadiusAccount` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### Query

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 318

**Key Fields**: `auth_providers`, `dhcp_server_identifiers`, `did_assignment_histories`, `did_assignments`, `did_import_recipes`, `dids`, `email_address_lookup`, `email_categories`, `email_clicks`, `email_domains`, `email_locations`, `email_message_contents`, `email_messages`, `email_opens`, `email_variables`, `emails`, `external_marketing_provider_credentials`, `external_marketing_providers`, `general_ledger_codes`, `get_gps_tracking_provider_vehicles`, `gps_tracking_provider_credentials`, `gps_tracking_providers`, `identity_provider_active_directory_details`, `identity_provider_google_details`, `identity_provider_microsoft_details`, `identity_provider_saml_details`, `identity_providers`, `lte_provider_credentials`, `lte_providers`, `mass_emails`, `phone_number_types`, `phone_numbers`, `reverse_geocode`, `schedule_blocker_overrides`, `snmp_oid_threshold_violations`, `snmp_oid_thresholds`, `snmp_oids`, `snmp_overrides`, `tax_overrides`, `tax_provider_credentials`, `tax_providers`, `triggered_emails`, `validate_address`, `validate_credential`, `voice_provider_rate_import_recipes`, `voice_provider_rate_imports`, `voice_provider_rates`, `voice_providers`, `voided_payments`

**Relationship Fields**: 318 (`access_logs`, `account_adtran_mosaic_service_details`, `account_billing_parameters`, `account_calix_service_details`, `account_events`...)

**All Fields**:

- `access_logs`: `AccessLogConnection` (required) (connection) - All access logs for this entity.
- `account_adtran_mosaic_service_details`: `AccountAdtranMosaicServiceDetailConnection` (required) (connection) - Account Adtran Mosaic service details.
- `account_billing_parameters`: `AccountBillingParameterConnection` (required) (connection) - Account billing parameters.
- `account_calix_service_details`: `AccountCalixServiceDetailConnection` (required) (connection) - Account Calix Service Details.
- `account_events`: `AccountEventConnection` (required) (connection) - Account events.
- `account_groups`: `AccountGroupConnection` (required) (connection) - Account groups.
- `account_ip_assignments`: `AccountIpAssignmentsConnection` (required) (connection) - IP assignments associated with account(s).
- `account_services`: `AccountServiceConnection` (required) (connection) - Services that have been attached to accounts.
- `account_statuses`: `AccountStatusConnection` (required) (connection) - Account statuses.
- `account_types`: `AccountTypeConnection` (required) (connection) - Account types.
- `account_voice_service_details`: `AccountVoiceServiceDetailConnection` (required) (connection) - Details of a voice service attached to an account.
- `accounts`: `AccountConnection` (required) (connection) - Customer accounts.
- `ach_batches`: `AchBatchConnection` (required) (connection) - ACH batches.
- `address_lists`: `AddressListConnection` (required) (connection) - Address lists.
- `address_statuses`: `AddressStatusConnection` (required) (connection) - Address statuses.
- `addresses`: `AddressConnection` (required) (connection) - Geographical addresses.
- `adjustment_service_details`: `AdjustmentServiceDetailConnection` (required) (connection) - Details related to an adjustment service.
- `adtran_mosaic_audits`: `AdtranMosaicAuditConnection` (required) (connection) - Adtran Mosaic audits.
- `adtran_mosaic_cloud_list`: `AdtranMosaicCloudListConnection` (required) (connection) - Adtran Mosaic cloud list.
- `adtran_mosaic_kafka_events`: `AdtranMosaicKafkaEventConnection` (required) (connection) - Adtran Mosaic Kafka events.
- `adtran_mosaic_settings`: `AdtranMosaicSettingConnection` (required) (connection) - Adtran Mosaic Settings.
- `adtran_mosaic_workflow_events`: `AdtranMosaicWorkflowEventConnection` (required) (connection) - Adtran Mosaic workflow events.
- `alerting_rotation_days`: `AlertingRotationDayConnection` (required) (connection) - Alerting rotation days and times.
- `alerting_rotation_inventory_items`: `AlertingRotationInventoryItemConnection` (required) (connection) - Inventory items associated with alerting rotations.
- `alerting_rotations`: `AlertingRotationConnection` (required) (connection) - Alerting rotations.
- `application_firewall_rules`: `ApplicationFirewallRuleConnection` (required) (connection) - Application firewall rules.
- `auth_providers`: `AuthProviderConnection` (required) (connection) - Auth providers.
- `available_explores`: `AvailableExploresConnection` (required) (connection) - Available explores.
- `available_reports`: `AvailableReportsConnection` (required) (connection) - Available reports.
- `avalara_tax_categories`: `AvalaraTaxCategoryConnection` (required) (connection) - Avalara tax categories.
- `avalara_tax_definitions`: `AvalaraTaxDefinitionConnection` (required) (connection) - Avalara tax definitions.
- `bank_account_processor_credentials`: `BankAccountProcessorCredentialConnection` (required) (connection) - Bank account processor credentials.
- `bank_account_processors`: `BankAccountProcessorConnection` (required) (connection) - Processors of transactions to and from bank accounts.
- `bank_accounts`: `BankAccountConnection` (required) (connection) - Bank accounts.
- `billing_defaults`: `BillingDefaultConnection` (required) (connection) - Default billing values for new accounts.
- `billing_services`: `BillingServiceConnection` (required) (connection) - Services associated with a linked billing default.
- `billing_setting`: `BillingSetting` (required) - Billing settings.
- `cable_modem_provisioner_credentials`: `CableModemProvisionerCredentialConnection` (required) (connection) - Cable modem provisioner credentials.
- `cable_modem_provisioners`: `CableModemProvisionerConnection` (required) (connection) - Cable modem provisioners.
- `calendar_icals`: `CalendarIcalConnection` (required) (connection) - Calendar - iCalendar
- `calix_cloud_audits`: `CalixCloudAuditConnection` (required) (connection) - Calix Cloud audits.
- `calix_cloud_settings`: `CalixCloudSettingConnection` (required) (connection) - Calix Cloud settings.
- `calix_integrations`: `CalixIntegrationConnection` (required) (connection) - Unique Calix SMx server configuration.
- `calix_provisioning_list`: `CalixProvisioningListConnection` (required) (connection) - Calix provisioning list.
- `call_detail_record_import_recipes`: `CallDetailRecordImportRecipeConnection` (required) (connection) - Call Detail Record Import Recipes
- `call_detail_record_imports`: `CallDetailRecordImportConnection` (required) (connection) - Call Detail Record Imports
- `call_detail_records`: `CallDetailRecordConnection` (required) (connection) - Call Detail Records
- `call_logs`: `CallLogConnection` (required) (connection) - Call Logs for accounts.
- `canned_replies`: `CannedReplyConnection` (required) (connection) - Canned replies.
- `canned_reply_categories`: `CannedReplyCategoryConnection` (required) (connection) - Canned reply categories.
- `canned_reply_with_variable_replacement`: `CannedReply` (required) - Canned reply with variable replacement.
- `companies`: `CompanyConnection` (required) (connection) - Companies that you do business as.
- `company_departments`: `CompanyDepartmentConnection` (required) (connection) - Departments in a company.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `contract_templates`: `ContractTemplateConnection` (required) (connection) - Contract templates.
- `contracts`: `ContractConnection` (required) (connection) - Contracts.
- `core_credit_cards`: `CreditCardConnection` (required) (connection) - Core credit cards.
- `core_invoices`: `InvoiceConnection` (required) (connection) - Core invoices.
- `core_transactions`: `TransactionConnection` (required) (connection) - Core transactions.
- `credit_card_processor_credentials`: `CreditCardProcessorCredentialConnection` (required) (connection) - Credit card processor credentials.
- `credit_card_processors`: `CreditCardProcessorConnection` (required) (connection) - Credit card processors configured in Sonar.
- `credit_cards`: `CreditCardConnection` (required) (connection) - Credit cards.
- `credits`: `CreditConnection` (required) (connection) - Credits applied to invoices.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data in custom fields.
- `custom_fields`: `CustomFieldConnection` (required) (connection) - Custom fields.
- `custom_links`: `CustomLinkConnection` (required) (connection) - Custom links.
- `custom_links_allowed_variables`: `CustomLinksAllowedVariables` (required) (list) - Variables that are available to be used in Custom Links. These variables will be URL encoded in the custom link.
- `custom_links_for_entity`: `CustomLinksForEntityConnection` (required) (connection) - Custom links that are for a given entity.
- `daily_aggregate_values`: `DailyAggregateValueConnection` (required) (connection) - Aggregate values for a given date.
- `data_service_details`: `DataServiceDetailConnection` (required) (connection) - Details related to a data service.
- `data_usage`: `DataUsage` (required) (list) - Data usage.
- `data_usage_histories`: `DataUsageHistoryConnection` (required) (connection) - Data usage history.
- `data_usage_top_offs`: `DataUsageTopOffConnection` (required) (connection) - Data usage top offs.
- `data_usage_totals`: `DataUsageTotalConnection` (required) (connection) - Shows the data usage total for a given time period.
- `debits`: `DebitConnection` (required) (connection) - Debits.
- `delinquency_exclusions`: `DelinquencyExclusionConnection` (required) (connection) - Periods of time in which delinquency is not calculated.
- `departments`: `DepartmentConnection` (required) (connection) - Departments.
- `deployment_types`: `DeploymentTypeConnection` (required) (connection) - Modes in which a piece of inventory can be deployed.
- `deposit_slips`: `DepositSlipConnection` (required) (connection) - Deposit slips.
- `device_interface_mappings`: `DeviceInterfaceMappingConnection` (required) (connection) - Device interface mappings.
- `dhcp_server_credentials`: `DhcpServerCredentialConnection` (required) (connection) - DHCP server credentials.
- `dhcp_server_identifiers`: `DhcpServerIdentifierConnection` (required) (connection) - DHCP sever identifiers.
- `dhcp_servers`: `DhcpServerConnection` (required) (connection) - DHCP servers.
- `did_assignment_histories`: `DidAssignmentHistoryConnection` (required) (connection) - DID assignment histories.
- `did_assignments`: `DidAssignmentConnection` (required) (connection) - DID assignments.
- `did_import_recipes`: `DidImportRecipeConnection` (required) (connection) - DID Import Recipes.
- `dids`: `DidConnection` (required) (connection) - DIDs.
- `disbursement_details`: `DisbursementDetailConnection` (required) (connection) - Disbursement details.
- `disbursements`: `DisbursementConnection` (required) (connection) - Disbursements.
- `disconnection_logs`: `DisconnectionLogConnection` (required) (connection) - Disconnection logs.
- `discounts`: `DiscountConnection` (required) (connection) - Discounts.
- `disputes`: `DisputeConnection` (required) (connection) - Disputes.
- `drive_times`: `DriveTimeResultWrapper` - Drive times.
- `email_address_lookup`: `Contact` (required) - Validate contact email address.
- `email_categories`: `EmailCategoryConnection` (required) (connection) - Email categories are associated with contacts, and define the types of emails those contacts receive. The "default" property determines whether or not the category is added to newly created contacts by default.
- `email_clicks`: `EmailClickConnection` (required) (connection) - All clicks for each sent email.
- `email_domains`: `EmailDomainConnection` (required) (connection) - Email domains.
- `email_locations`: `EmailLocationConnection` (required) (connection) - Get a list of all locations saved for opened and clicked emails.
- `email_message_contents`: `EmailMessageContentConnection` (required) (connection) - Localized email message details for an EmailMessage container.
- `email_messages`: `EmailMessageConnection` (required) (connection) - Email message templates.
- `email_opens`: `EmailOpenConnection` (required) (connection) - All opens for each sent email.
- `email_variables`: `EmailVariable` (list) - Get a list of valid email variables for a specific email trigger.
- `emails`: `EmailConnection` (required) (connection) - Emails that have been sent.
- `epcs`: `EpcConnection` (required) (connection) - LTE EPCs.
- `expiring_service_details`: `ExpiringServiceDetailConnection` (required) (connection) - Details related to an expiring service.
- `external_marketing_provider_credentials`: `ExternalMarketingProviderCredentialConnection` (required) (connection) - External marketing provider credentials.
- `external_marketing_providers`: `ExternalMarketingProviderConnection` (required) (connection) - External marketing providers.
- `fcc_form_477_reports`: `FccForm477ReportConnection` (required) (connection) - The generated FCC Form 477 report.
- `fibermap_integrations`: `FibermapIntegrationConnection` (required) (connection) - FiberMap integrations.
- `fibermap_plans`: `FibermapPlanConnection` (required) (connection) - FiberMap plans.
- `fibermap_service_locations`: `FibermapServiceLocationConnection` (required) (connection) - FiberMap service locations
- `files`: `FileConnection` (required) (connection) - Files.
- `find_address_by_fibermap_service_location`: `Address` (required) - Find address by fibermap service location.
- `fractional_debits`: `FractionalDebitConnection` (required) (connection) - Fractional debits.
- `fractional_tax_transactions`: `FractionalTaxTransactionConnection` (required) (connection) - Fractional tax transactions.
- `general_ledger_codes`: `GeneralLedgerCodeConnection` (required) (connection) - General ledger codes.
- `general_search`: `GeneralSearchConnection` (required) (connection) - This query provides the ability to perform a general, partial matching search across various entities at the same time.
- `generic_inventory_assignees`: `GenericInventoryAssigneeConnection` (required) (connection) - Generic inventory assignees.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - Logs of changes made to generic inventory items.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - Generic inventory items.
- `geo_tax_zones`: `GeoTaxZoneConnection` (required) (connection) - Geographical tax zones.
- `geofences`: `GeofenceConnection` (required) (connection) - Geofences.
- `get_gps_tracking_provider_vehicles`: `GetGpsTrackingProviderVehiclesConnection` (connection) - Get list of vehicles from external GPS tracking provider.
- `get_next_ip_address_in_ip_pool`: `NextIpAddress` (required) - Returns the next IP address in the IP pool.
- `get_next_subnet_in_subnet`: `NextSubnet` (required) - Returns the next subnet in the subnet.
- `get_next_subnet_in_supernet`: `NextSubnet` (required) - Returns the next available subnet of the requested size in the supernet.
- `global_inventory_model_min_maxes`: `GlobalInventoryModelMinMaxConnection` (required) (connection) - Global inventory model minimums/maximums.
- `gps_tracking_provider_credentials`: `GpsTrackingProviderCredentialConnection` (required) (connection) - GPS tracking provider credentials.
- `gps_tracking_providers`: `GpsTrackingProviderConnection` (required) (connection) - GPS tracking providers.
- `handwritten_signatures`: `HandwrittenSignatureConnection` (required) (connection) - Signatures on signed contracts.
- `icmp_results`: `IcmpNetworkMonitoringResultConnection` (required) (connection) - ICMP results.
- `identity_provider_active_directory_details`: `IdentityProviderActiveDirectoryDetailConnection` (required) (connection) - Details related to an ActiveDirectory identity provider.
- `identity_provider_google_details`: `IdentityProviderGoogleDetailConnection` (required) (connection) - Details related to a Google identity provider.
- `identity_provider_microsoft_details`: `IdentityProviderMicrosoftDetailConnection` (required) (connection) - Details related to a Microsoft identity provider.
- `identity_provider_saml_details`: `IdentityProviderSamlDetailConnection` (required) (connection) - Details related to a SAML identity provider.
- `identity_providers`: `IdentityProviderConnection` (required) (connection) - Identity providers.
- `imports`: `ImportConnection` (required) (connection) - Imports of entities in bulk.
- `inbound_mailboxes`: `InboundMailboxConnection` (required) (connection) - Inbound mailboxes.
- `inline_device_credentials`: `InlineDeviceCredentialConnection` (required) (connection) - Inline device credentials.
- `inline_devices`: `InlineDeviceConnection` (required) (connection) - Inline devices.
- `instance_management_requests`: `InstanceManagementRequestConnection` (required) (connection) - Instance management requests.
- `instance_service_funds`: `InstanceServiceFunds` (required) - Instance Service Funds
- `integration_field_mappings`: `IntegrationFieldMappingConnection` (required) (connection) - Integration field mappings.  Mapping of Sonar model field with vendor specific field.
- `integration_service_mappings`: `IntegrationServiceMappingConnection` (required) (connection) - Integration service mappings.  One-to-one mapping of Sonar service with vendor service name.
- `internal_locations`: `InternalLocationConnection` (required) (connection) - Internal locations within an inventory location (e.g. a shelf or room.)
- `inventory_item_events`: `InventoryItemEventConnection` (required) (connection) - Inventory item events.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - Inventory items.
- `inventory_locations`: `InventoryLocationConnection` (required) (connection) - Locations that inventory can be stored.
- `inventory_model_categories`: `InventoryModelCategoryConnection` (required) (connection) - Categories of inventory.
- `inventory_model_field_data`: `InventoryModelFieldDataConnection` (required) (connection) - Data stored on an inventory field (e.g. a MAC address or serial number.)
- `inventory_model_fields`: `InventoryModelFieldConnection` (required) (connection) - Fields that contain data about an inventory item.
- `inventory_model_min_maxes`: `InventoryModelMinMaxConnection` (required) (connection) - Inventory model minimums/maximums.
- `inventory_models`: `InventoryModelConnection` (required) (connection) - Inventory models.
- `invoice_attachments`: `InvoiceAttachmentConnection` (required) (connection) - Invoice attachments.
- `invoice_messages`: `InvoiceMessageConnection` (required) (connection) - Invoice messages.
- `invoice_template_versions`: `InvoiceTemplateVersionConnection` (required) (connection) - Invoice Template Versions.
- `invoice_templates`: `InvoiceTemplateConnection` (required) (connection) - Invoice Templates.
- `invoices`: `InvoiceConnection` (required) (connection) - Invoices.
- `ip_assignment_histories`: `IpAssignmentHistoryConnection` (required) (connection) - IP assignment histories.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - IP assignments.
- `ip_pools`: `IpPoolConnection` (required) (connection) - IP pools.
- `job_available_times`: `JobAvailableTimes` (list) - Job available times.
- `job_check_ins`: `JobCheckInConnection` (required) (connection) - Job check ins.
- `job_services`: `JobServiceConnection` (required) (connection) - Services associated with jobs.
- `job_types`: `JobTypeConnection` (required) (connection) - Job types.
- `jobs`: `JobConnection` (required) (connection) - Jobs.
- `local_prefixes`: `LocalPrefixConnection` (required) (connection) - Local prefixes for voice services.
- `logs`: `LogConnection` (required) (connection) - Log entries for various events throughout Sonar.
- `looker_explore_licenses`: `LookerExploreLicenseConnection` (required) (connection) - Report builder licenses.
- `looker_view_licenses`: `LookerViewLicenseConnection` (required) (connection) - Report viewer licenses.
- `lte_provider_credentials`: `LteProviderCredentialConnection` (required) (connection) - The credentials for an LTE provider.
- `lte_providers`: `LteProviderConnection` (required) (connection) - LTE providers.
- `manufacturers`: `ManufacturerConnection` (required) (connection) - Manufacturers.
- `map_overlays`: `MapOverlayConnection` (required) (connection) - Map Overlays.
- `map_overlays_within_box`: `MapOverlayConnection` (required) (connection) - Returns all map overlays within a camera view represented by the north, south, east and west arguments
- `mass_emails`: `MassEmailConnection` (required) (connection) - Mass email communications.
- `me`: `Me` (required) - Get information about yourself!
- `message_categories`: `MessageCategoryConnection` (required) (connection) - Message categories are associated with contacts, and define the types of messages those contacts receive. The "default" property determines whether or not the category is added to newly created contacts by default.
- `mfa_admin_setting`: `MfaAdminSetting` (required) - Multi-factor authentication admin settings.
- `monthly_billing_completions`: `MonthlyBillingCompletionConnection` (required) (connection) - Logs of when billing ran successfully for an `Account`.
- `my_ip_address`: `MyIpAddress` (required) - Get your IP address
- `netflow_allowed_subnets`: `NetflowAllowedSubnetConnection` (required) (connection) - Netflow allowed subnets.
- `netflow_endpoints`: `NetflowEndpointConnection` (required) (connection) - Netflow endpoints.
- `netflow_on_premises`: `NetflowOnPremiseConnection` (required) (connection) - Netflow on premises.
- `netflow_whitelists`: `NetflowWhitelistConnection` (required) (connection) - Netflow whitelists.
- `network_monitoring_graphs`: `NetworkMonitoringGraphConnection` (required) (connection) - Network monitoring graphs.
- `network_monitoring_templates`: `NetworkMonitoringTemplateConnection` (required) (connection) - Network monitoring templates.
- `network_site_serviceable_address_lists`: `NetworkSiteServiceableAddressListConnection` (required) (connection) - Network site serviceable address lists.
- `network_sites`: `NetworkSiteConnection` (required) (connection) - Network sites.
- `non_inventory_items`: `NonInventoryItemConnection` (required) (connection) - Items sold by vendors that are not convertible to an inventory model (i.e. labor charges).
- `notes`: `NoteConnection` (required) (connection) - Notes.
- `notifications`: `NotificationConnection` (required) (connection) - Notifications.
- `order_group_users`: `OrderGroupUserConnection` (required) (connection) - Order group relationships to users.
- `order_groups`: `OrderGroupConnection` (required) (connection) - Order groups.
- `overage_service_details`: `OverageServiceDetailConnection` (required) (connection) - Details related to an overage service.
- `package_services`: `PackageServiceConnection` (required) (connection) - Services associated with a package.
- `packages`: `PackageConnection` (required) (connection) - Packages.
- `password_policy`: `PasswordPolicy` (required) - The password policy for users.
- `pay_pal_credentials`: `PayPalCredentialConnection` (required) (connection) - PayPal Credentials.
- `payments`: `PaymentConnection` (required) (connection) - Payments.
- `personal_access_tokens`: `PersonalAccessTokenConnection` (required) (connection) - Your personal access tokens.
- `phone_number_types`: `PhoneNumberTypeConnection` (required) (connection) - Types of phone numbers (e.g. mobile, home, fax.)
- `phone_numbers`: `PhoneNumberConnection` (required) (connection) - Phone numbers.
- `poller_setting`: `PollerSetting` (required) - Poller settings.
- `pollers`: `PollerConnection` (required) (connection) - Pollers.
- `preseem`: `Preseem` (required) - Preseem integration.
- `print_to_mail_batches`: `PrintToMailBatchConnection` (required) (connection) - Print to mail batches.
- `print_to_mail_document_cost_estimate`: `PrintToMailDocumentCostEstimate` (required) - Estimated print to mail document/invoice cost.
- `print_to_mail_order_errors`: `PrintToMailOrderErrorConnection` (required) (connection) - Print to mail order errors.
- `print_to_mail_orders`: `PrintToMailOrderConnection` (required) (connection) - Print to mail orders.
- `print_to_mail_setting`: `PrintToMailSetting` (required) - Print to mail settings.
- `printed_invoice_batches`: `PrintedInvoiceBatchConnection` (required) (connection) - Printed invoice batches.
- `purchase_order_items`: `PurchaseOrderItemConnection` (required) (connection) - Purchase order line items.
- `purchase_orders`: `PurchaseOrderConnection` (required) (connection) - Purchase orders.
- `radius_accounts`: `RadiusAccountConnection` (required) (connection) - RADIUS accounts.
- `radius_group_reply_attributes`: `RadiusGroupReplyAttributeConnection` (required) (connection) - RADIUS group reply attributes.
- `radius_groups`: `RadiusGroupConnection` (required) (connection) - RADIUS groups.
- `radius_server_credentials`: `RadiusServerCredentialConnection` (required) (connection) - Radius server credentials.
- `radius_servers`: `RadiusServerConnection` (required) (connection) - RADIUS servers.
- `radius_session_histories`: `RadiusSessionHistoryConnection` (required) (connection) - RADIUS session histories.
- `rate_centers`: `RateCenterConnection` (required) (connection) - Rate Centers.
- `recurring_service_details`: `RecurringServiceDetailConnection` (required) (connection) - Details related to a recurring service.
- `refunded_payments`: `RefundedPaymentConnection` (required) (connection) - Refunded payments.
- `reverse_geocode`: `ValidatedAddress` (required) - Attempt to translate a latitude and longitude into a street address.
- `reversed_payments`: `ReversedPaymentConnection` (required) (connection) - Reversed payments.
- `roles`: `RoleConnection` (required) (connection) - Roles for users. Roles define the permission set that a user can have.
- `saved_message_categories`: `SavedMessageCategoryConnection` (required) (connection) - Saved message categories.
- `schedule`: `ScheduleResult` - Scheduling data.
- `schedule_addresses`: `ScheduleAddressConnection` (required) (connection) - Starting and ending addresses for technician schedules.
- `schedule_availabilities`: `ScheduleAvailabilityConnection` (required) (connection) - Schedule availabilities.
- `schedule_availability_day_times`: `ScheduleAvailabilityDayTimeConnection` (required) (connection) - Schedule availability day/times.
- `schedule_blocker_day_times`: `ScheduleBlockerDayTimeConnection` (required) (connection) - Schedule blocker day/times.
- `schedule_blocker_overrides`: `ScheduleBlockerOverrideConnection` (required) (connection) - Schedule blocker overrides.
- `schedule_blockers`: `ScheduleBlockerConnection` (required) (connection) - Schedule blockers.
- `schedule_time_offs`: `ScheduleTimeOffConnection` (required) (connection) - Schedule time offs.
- `scheduled_event_account_calix_service_details`: `ScheduledEventAccountCalixServiceDetailConnection` (required) (connection) - Scheduled event account Calix service details.
- `scheduled_event_account_voice_service_details`: `ScheduledEventAccountVoiceServiceDetailConnection` (required) (connection) - Scheduled event account voice service details.
- `scheduled_events`: `ScheduledEventConnection` (required) (connection) - Scheduled events.
- `search_filters`: `SearchFilterConnection` (required) (connection) - User-defined search filters.
- `service_metadata`: `ServiceMetadataConnection` (required) (connection) - Metadata fields on a service.
- `service_metadata_values`: `ServiceMetadataValueConnection` (required) (connection) - Values entered into service metadata fields.
- `service_tax_definitions`: `ServiceTaxDefinitionConnection` (required) (connection) - Tax definitions that have been assigned to services.
- `service_taxes`: `ServiceTaxConnection` (required) (connection) - The relationship between a service and a tax.
- `serviceable_address_account_assignment_futures`: `ServiceableAddressAccountAssignmentFutureConnection` (required) (connection) - Serviceable address account assignment futures.
- `serviceable_address_account_assignment_histories`: `ServiceableAddressAccountAssignmentHistoryConnection` (required) (connection) - Serviceable address account assignment histories.
- `services`: `ServiceConnection` (required) (connection) - Services.
- `signatures`: `SignatureConnection` (required) (connection) - Signatures.
- `sms_message_contents`: `SmsMessageContentConnection` (required) (connection) - SMS message contents.
- `sms_messages`: `SmsMessageConnection` (required) (connection) - SMS Messages.
- `sms_outbound_messages`: `SmsOutboundMessageConnection` (required) (connection) - SMS outbound messages.
- `sms_setting`: `SmsSetting` (required) - SMS settings.
- `smtp_events`: `SmtpEventConnection` (required) (connection) - All SMTP events for each sent email.
- `snmp_interface_numeric_results`: `SnmpInterfaceNumericResult` (required) (list) - SNMP interface numeric results
- `snmp_oid_threshold_violations`: `SnmpOidThresholdViolationConnection` (required) (connection) - SNMP OID threshold violations.
- `snmp_oid_thresholds`: `SnmpOidThresholdConnection` (required) (connection) - SNMP OID thresholds.
- `snmp_oids`: `SnmpOidConnection` (required) (connection) - SNMP OIDs.
- `snmp_overrides`: `SnmpOverrideConnection` (required) (connection) - SNMP Overrides.
- `snmp_results`: `SnmpNetworkMonitoringResultConnection` (required) (connection) - SNMP results.
- `splice_report`: `SpliceReport` (required) - Vetro FiberMap Splice Report.
- `stored_filters`: `StoredFilterConnection` (required) (connection) - Stored view filters.
- `stored_groups`: `StoredGroupConnection` (required) (connection) - Stored view groups.
- `stored_view_users`: `StoredViewUserConnection` (required) (connection) - Stored views associated with users.
- `stored_views`: `StoredViewConnection` (required) (connection) - Stored views.
- `subnets`: `SubnetConnection` (required) (connection) - Subnets.
- `subscriptions`: `SubscriptionConnection` (required) (connection) - Subscriptions.
- `supernets`: `SupernetConnection` (required) (connection) - Supernets.
- `system_backup_destination_credentials`: `SystemBackupDestinationCredentialConnection` (required) (connection) - The configured credentials for a system backup export destination.
- `system_backup_destinations`: `SystemBackupDestinationConnection` (required) (connection) - All configured destinations to export system backups to.
- `system_backup_exports`: `SystemBackupExportConnection` (required) (connection) - A history of all system backup export attempts.
- `system_backup_setting`: `SystemBackupSetting` (required) - System backup settings.
- `system_backups`: `SystemBackupConnection` (required) (connection) - Your system backups.
- `system_environment`: `SystemEnvironment` (required) - System environment.
- `system_setting`: `SystemSetting` (required) - System settings.
- `task_template_items`: `TaskTemplateItemConnection` (required) (connection) - Task template items.
- `task_templates`: `TaskTemplateConnection` (required) (connection) - Task templates.
- `tasks`: `TaskConnection` (required) (connection) - Tasks.
- `tax_exemptions`: `TaxExemptionConnection` (required) (connection) - Tax exemptions.
- `tax_overrides`: `TaxOverrideConnection` (required) (connection) - Overrides of specific taxes on a per account basis.
- `tax_provider_credentials`: `TaxProviderCredentialConnection` (required) (connection) - The credentials for a tax provider.
- `tax_providers`: `TaxProviderConnection` (required) (connection) - Tax providers.
- `tax_transactions`: `TaxTransactionConnection` (required) (connection) - Tax transactions.
- `taxes`: `TaxConnection` (required) (connection) - Taxes.
- `ticket_categories`: `TicketCategoryConnection` (required) (connection) - Ticket categories.
- `ticket_comments`: `TicketCommentConnection` (required) (connection) - Ticket comments.
- `ticket_groups`: `TicketGroupConnection` (required) (connection) - Ticket groups.
- `ticket_recipients`: `TicketRecipientConnection` (required) (connection) - Ticket recipients.
- `ticket_replies`: `TicketReplyConnection` (required) (connection) - Ticket replies.
- `ticketing_setting`: `TicketingSetting` (required) - Ticketing settings.
- `tickets`: `TicketConnection` (required) (connection) - Tickets.
- `towercoverage_configuration`: `TowercoverageConfiguration` (required) - TowerCoverage integration.
- `towercoverage_submissions`: `TowercoverageSubmissionConnection` (required) (connection) - TowerCoverage submissions.
- `transactions`: `TransactionConnection` (required) (connection) - A list of transactions for display on an account.
- `triggered_emails`: `TriggeredEmailConnection` (required) (connection) - Emails that are sent when specific conditions are met.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - Messages that are sent when specific conditions are met.
- `uninventoried_mac_addresses`: `UninventoriedMacAddressConnection` (required) (connection) - Uninventoried MAC addresses.
- `usage_based_billing_policies`: `UsageBasedBillingPolicyConnection` (required) (connection) - Usage based billing policies.
- `usage_based_billing_policy_free_periods`: `UsageBasedBillingPolicyFreePeriodConnection` (required) (connection) - Usage based billing policy free periods.
- `users`: `UserConnection` (required) (connection) - Users that can login to Sonar.
- `validate_address`: `ValidatedAddress` (required) - Validate an address. This will attempt to resolve the subdivision, geocode if necessary, etc. The more information you input, the more accurate the output is likely to be.
- `validate_credential`: `Contact` (required) - Validate contact portal credentials.
- `vehicle_location_histories`: `VehicleLocationHistoryConnection` (required) (connection) - Vehicle location histories.
- `vehicles`: `VehicleConnection` (required) (connection) - Vehicles.
- `vendor_items`: `VendorItemConnection` (required) (connection) - Items sold by vendors.
- `vendors`: `VendorConnection` (required) (connection) - Third party vendors.
- `voice_provider_rate_import_recipes`: `VoiceProviderRateImportRecipeConnection` (required) (connection) - Voice Provider Rate Import Recipes
- `voice_provider_rate_imports`: `VoiceProviderRateImportConnection` (required) (connection) - Voice Provider Rate Imports
- `voice_provider_rates`: `VoiceProviderRateConnection` (required) (connection) - Voice Provider Rates.
- `voice_providers`: `VoiceProviderConnection` (required) (connection) - Voice Providers.
- `voice_service_details`: `VoiceServiceDetailConnection` (required) (connection) - Details related to a voice service.
- `voice_service_generic_parameter_tax_definitions`: `VoiceServiceGenericParameterTaxDefinitionConnection` (required) (connection) - Tax definitions that have been assigned to voice service generic parameters.
- `voice_service_generic_parameter_taxes`: `VoiceServiceGenericParameterTaxConnection` (required) (connection) - The relationship between a service and a tax.
- `voice_service_generic_parameters`: `VoiceServiceGenericParameterConnection` (required) (connection) - Parameters attached to a voice service.
- `voided_payments`: `VoidedPaymentConnection` (required) (connection) - Voided payments.
- `webhook_endpoint_event_dispatch_attempts`: `WebhookEndpointEventDispatchAttemptConnection` (required) (connection) - All attempts made to send dispatched webhooks for models and events.
- `webhook_endpoint_event_dispatches`: `WebhookEndpointEventDispatchConnection` (required) (connection) - All dispatched webhooks for models and events.
- `webhook_endpoint_events`: `WebhookEndpointEventConnection` (required) (connection) - Webhooks models and their events.
- `webhook_endpoints`: `WebhookEndpointConnection` (required) (connection) - Webhook endpoints.
- `webhook_model_events`: `WebhookModelEventResultConnection` (connection) - Webhook model events.

---

### Mutation

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 640

**Key Fields**: `createDhcpServerIdentifier`, `createDid`, `createDidAssignment`, `createDidImportFlatfile`, `createEmailCategory`, `createEmailDomain`, `createEmailMessage`, `createEmailMessageContent`, `createExternalMarketingProvider`, `createGeneralLedgerCode`, `createGpsTrackingProvider`, `createIdentityProviderActiveDirectory`, `createIdentityProviderGoogle`, `createIdentityProviderMicrosoft`, `createIdentityProviderSaml`, `createLteProvider`, `createMailingAddress`, `createMassEmail`, `createPhoneNumber`, `createPhoneNumberType`, `createSnmpOid`, `createSnmpOidThreshold`, `createSnmpOverride`, `createTaxOverride`, `createTaxProvider`, `createTriggeredEmail`, `createVoiceProvider`, `createVoiceProviderRate`, `createVoiceProviderRateImportFlatfile`, `deleteDhcpServerIdentifier`, `deleteDid`, `deleteDidAssignment`, `deleteEmailCategory`, `deleteEmailDomain`, `deleteEmailMessage`, `deleteEmailMessageContent`, `deleteExternalMarketingProvider`, `deleteGeneralLedgerCode`, `deleteGpsTrackingProvider`, `deleteIdentityProvider`, `deleteLteProvider`, `deleteMailingAddress`, `deletePhoneNumber`, `deletePhoneNumberType`, `deleteSnmpOid`, `deleteSnmpOidThreshold`, `deleteSnmpOverride`, `deleteTaxOverride`, `deleteTaxProvider`, `deleteTriggeredEmail`, `deleteVoiceProvider`, `deleteVoiceProviderRate`, `emailInvoiceBatch`, `emailInvoiceToContact`, `emailPurchaseOrderToVendor`, `resendUserCreationEmail`, `scheduleManyJobsAndScheduleBlockerOverrides`, `scheduleManyJobsAndScheduleBlockerOverridesSkipsValidation`, `sendEmailDomainVerificationEmail`, `sendTestEmail`, `sendTestTriggeredEmail`, `synchronizeLteProvider`, `updateAuthProvider`, `updateDhcpServerIdentifier`, `updateDid`, `updateDidAssignment`, `updateEmailCategory`, `updateEmailMessage`, `updateEmailMessageContent`, `updateExternalMarketingProvider`, `updateGeneralLedgerCode`, `updateGpsTrackingProvider`, `updateIdentityProviderActiveDirectory`, `updateIdentityProviderGoogle`, `updateIdentityProviderMicrosoft`, `updateIdentityProviderSaml`, `updateJobSkipsValidation`, `updateLteProvider`, `updateMailingAddress`, `updatePhoneNumber`, `updatePhoneNumberType`, `updateSnmpOid`, `updateSnmpOidThreshold`, `updateSnmpOverride`, `updateTaxOverride`, `updateTaxProvider`, `updateTriggeredEmail`, `updateVoiceProvider`, `updateVoiceProviderRate`, `updateVoiceProviderRateChargePercentMutation`, `validateCableModemProvisionerCredentials`, `validateCalixCredentials`, `validateDhcpServerCredentials`, `validateEmailDomain`, `validateFibermapIntegrationCredentials`, `validateGpsTrackingProviderCredentials`, `validateInlineDeviceCredentials`, `validateLteProviderCredentials`, `validateRadiusServerCredentials`, `validateTaxProviderCredentials`, `voidCredit`, `voidInvoice`, `voidPayment`

**Relationship Fields**: 640 (`addInstanceServiceFunds`, `addPackageToAccount`, `addServiceToAccount`, `allocateLookerExploreLicenseToUser`, `allocateLookerViewLicenseToUser`...)

**All Fields**:

- `addInstanceServiceFunds`: `InstanceServiceFunds` (required) - Make additional funds available to the instance service fund.
- `addPackageToAccount`: `AccountService` (list) - Add a package to an account.
- `addServiceToAccount`: `AccountService` - Add a recurring or expiring service to an account.
- `allocateLookerExploreLicenseToUser`: `LookerExploreLicense` - Allocate a report builder license to a user.
- `allocateLookerViewLicenseToUser`: `LookerViewLicense` - Allocate a report viewer license to a user.
- `applyCreditToInvoice`: `Invoice` - Apply a credit to an invoice with a due balance.
- `archiveAccount`: `Account` - Archive an account.
- `assignGenericInventoryItems`: `GenericInventoryItem` - Assign generic inventory items to an assignee.
- `assignInventoryItems`: `InventoryItem` (list) - Assign one or more inventory items to a new assignee.
- `auditAdtranMosaic`: `AdtranMosaicSetting` - Perform manual Adtran Mosaic audit.
- `auditCalixCloud`: `CalixCloudSetting` - Audit Calix Cloud subscribers to Sonar accounts.
- `auditRepairAdtranMosaic`: `SuccessResponse` - Perform manual repair of Adtran Mosaic Cloud audit entries.
- `cancelPrintToMailBatch`: `SuccessResponse` - Cancel a print to mail batch.
- `checkInToJob`: `JobCheckIn` - Check in to a job.
- `checkOutOfJob`: `JobCheckIn` - Check out of a job.
- `claimInventoryItems`: `SuccessResponse` - Claim one or many inventory items.
- `completeFileTask`: `Task` - Complete a task that requires a file for a completion type.
- `completeJob`: `Job` - Complete a job.
- `completeTask`: `Task` - Complete or uncomplete a task.
- `consumeGenericInventoryItems`: `GenericInventoryItem` - Consume generic inventory items.
- `createAccessLog`: `AccessLog` - Create an access log entry on an entity for the current user.
- `createAccount`: `Account` - Create a new account.
- `createAccountAdjustmentTransaction`: `TransactionInterface` - Create a one time transaction from an adjustment service for an account.
- `createAccountAdtranMosaicServiceDetail`: `AccountAdtranMosaicServiceDetail` - Create account Adtran Mosaic service details.
- `createAccountCalixServiceDetail`: `AccountCalixServiceDetail` - Create an account calix service detail.
- `createAccountGroup`: `AccountGroup` - Create a new account group.
- `createAccountOneTimeTransaction`: `TransactionInterface` (list) - Create a one time transaction for an account.
- `createAccountStatus`: `AccountStatus` - Create a new account status.
- `createAccountType`: `AccountType` - Create a new account type.
- `createAchBatch`: `AchBatch` (required) (list) - Create a new ACH batch.
- `createAddressList`: `AddressList` - Create an address list.
- `createAddressStatus`: `AddressStatus` - Create a new address status.
- `createAdjustmentService`: `Service` - Create a new adjustment service.
- `createAdtranMosaicSetting`: `AdtranMosaicSetting` - Create Adtran Mosaic settings.
- `createAlertingRotation`: `AlertingRotation` - Create a new alerting rotation.
- `createAlertingRotationDay`: `AlertingRotationDay` - Create a new alerting rotation day.
- `createApplicationFirewallRule`: `ApplicationFirewallRule` - Create a new application firewall rule.
- `createAuthenticationFactor`: `AuthenticationFactor` - Create an authentication factor.
- `createAvalaraTaxDefinition`: `AvalaraTaxDefinition` - Create an Avalara bundled tax definition.
- `createBankAccount`: `BankAccount` - Create a new bank account.
- `createBankAccountPayment`: `Payment` - Create a payment using a bank account.
- `createBankAccountProcessor`: `BankAccountProcessor` - Create a new bank account processor.
- `createBillingDefault`: `BillingDefault` - Create a new billing default.
- `createCableModemProvisioner`: `CableModemProvisioner` - Create a cable modem provisioner.
- `createCalendarIcal`: `CalendarIcal` - Create a calendar - iCalendar.
- `createCalixCloudSetting`: `CalixCloudSetting` - Create a Calix Cloud setting.
- `createCalixIntegration`: `CalixIntegration` - Create a Calix integration
- `createCallDetailRecord`: `CallDetailRecord` - Create a call detail record (CDR).
- `createCallDetailRecordImportFlatfile`: `CallDetailRecordImportRecipe` - Create a Flatfile import of call detail records (CDRs).
- `createCallLog`: `CallLog` - Create a call log.
- `createCannedReply`: `CannedReply` - Create a new canned reply.
- `createCannedReplyCategory`: `CannedReplyCategory` - Create a new canned reply category.
- `createCompany`: `Company` - Create a new company.
- `createContact`: `Contact` - Create a new contact.
- `createContract`: `Contract` - Create a new contract.
- `createContractTemplate`: `ContractTemplate` - Create a new contract template.
- `createCoreCreditCard`: `CoreCreditCard` - Create a Core credit card.
- `createCorePayment`: `CorePayment` - Create a Core payment.
- `createCreditCard`: `CreditCard` - Create a new credit card.
- `createCreditCardPayment`: `Payment` - Create a credit card.
- `createCreditCardProcessor`: `CreditCardProcessor` - Create a new credit card processor.
- `createCustomField`: `CustomField` - Create a new custom field.
- `createCustomLink`: `CustomLink` - Create a new custom link.
- `createDataService`: `Service` - Create a data service.
- `createDataUsageTopOff`: `DataUsageTopOff` - Create a data usage top off.
- `createDataUsages`: `SuccessResponse` - Create data usage entries.  This will also update each account last aggregation date to the earliest datetime in the submitted recordset. 
- `createDelinquencyExclusion`: `DelinquencyExclusion` - Create a delinquency exclusion.
- `createDepartment`: `Department` - Create a department.
- `createDeploymentType`: `DeploymentType` - Create a new deployment type.
- `createDepositSlip`: `DepositSlip` - Create a new deposit slip.
- `createDhcpServer`: `DhcpServer` - Create a DHCP server.
- `createDhcpServerIdentifier`: `DhcpServerIdentifier` - Create a DHCP server identifier.
- `createDid`: `Did` - Create a DID.
- `createDidAssignment`: `DidAssignment` - Create a DID assignment.
- `createDidImportFlatfile`: `DidImportRecipe` - Create a Flatfile import of DIDs.
- `createEmailCategory`: `EmailCategory` - Create a new messaging category.
- `createEmailDomain`: `EmailDomain` - Create a new email domain.
- `createEmailMessage`: `EmailMessage` - Create a new saved message.
- `createEmailMessageContent`: `EmailMessageContent` - Create new saved message contents.
- `createEpc`: `Epc` - Create an LTE EPC.
- `createExpiringService`: `Service` - Create a new expiring service.
- `createExternalMarketingProvider`: `ExternalMarketingProvider` - Create an external marketing integration.
- `createFccForm477Report`: `FccForm477Report` - Create a FCC Form 477 report.
- `createFibermapIntegration`: `FibermapIntegration` - Create a FiberMap Integration.
- `createGeneralLedgerCode`: `GeneralLedgerCode` - Create a new general ledger code.
- `createGenericInventoryAssignee`: `GenericInventoryAssignee` - Create a generic inventory assignee.
- `createGenericInventoryItems`: `GenericInventoryItem` - Create new generic inventory items.
- `createGeoTaxZone`: `GeoTaxZone` - Create a new geo tax zone.
- `createGeofence`: `Geofence` - Create a geofence.
- `createGlobalInventoryModelMinMax`: `GlobalInventoryModelMinMax` - Create a Global Inventory Model Min/Max.
- `createGpsTrackingProvider`: `GpsTrackingProvider` - Create a GPS tracking provider.
- `createIdentityProviderActiveDirectory`: `IdentityProvider` - Create an ActiveDirectory identity provider.
- `createIdentityProviderGoogle`: `IdentityProvider` - Create a Google identity provider.
- `createIdentityProviderMicrosoft`: `IdentityProvider` - Create a Microsoft identity provider.
- `createIdentityProviderSaml`: `IdentityProvider` - Create a SAML identity provider.
- `createInboundMailbox`: `InboundMailbox` - Create a new inbound mailbox.
- `createInlineDevice`: `InlineDevice` - Create an inline device.
- `createInternalLocation`: `InternalLocation` - Create a new internal location.
- `createInternalTicket`: `Ticket` - Create an internal ticket.
- `createInventoryItemSegment`: `InventoryItem` - Create an inventory item segment.
- `createInventoryItems`: `InventoryItem` (list) - Create one or many inventory items.
- `createInventoryLocation`: `InventoryLocation` - Create a new inventory location.
- `createInventoryModel`: `InventoryModel` - Create a new inventory model.
- `createInventoryModelCategory`: `InventoryModelCategory` - Create a new inventory model category.
- `createInventoryModelField`: `InventoryModelField` - Create a new inventory model field.
- `createInventoryModelMinMax`: `InventoryModelMinMax` - Create an Inventory Model Min/Max.
- `createInvoice`: `Invoice` - Create a new invoice.
- `createInvoiceAttachment`: `InvoiceAttachment` - Create an invoice attachment.
- `createInvoiceMessage`: `InvoiceMessage` - Create an invoice message.
- `createInvoiceTemplate`: `InvoiceTemplate` - Create an invoice template.
- `createIpAssignment`: `IpAssignment` - Create a new IP assignment.
- `createIpAssignmentFromDhcpReservation`: `SuccessResponse` - Create a new IP assignment from a MAC/IP address pair.
- `createIpPool`: `IpPool` - Create a new IP pool.
- `createJob`: `Job` - Create a job.
- `createJobService`: `JobService` - Associate a service with a job.
- `createJobType`: `JobType` - Create a job type.
- `createLinkedAddresses`: `CreateLinkedAddressesResponse` - Create linked addresses in bulk.
- `createLocalPrefix`: `LocalPrefix` - Create a new local prefix.
- `createLteProvider`: `LteProvider` - Create an LTE provider.
- `createMailingAddress`: `Address` - Create a new account mailing address.
- `createManufacturer`: `Manufacturer` - Create a new manufacturer.
- `createMapOverlay`: `MapOverlay` - Create a map overlay.
- `createMassEmail`: `MassEmail` - Create a mass email communication.
- `createMassMessage`: `SuccessResponseWithId` - Create a mass message communication.
- `createMessageCategory`: `MessageCategory` - Create a messaging category.
- `createNetflowAllowedSubnet`: `NetflowAllowedSubnet` - Create a Netflow allowed subnet.
- `createNetflowEndpoint`: `NetflowEndpoint` - Create a Netflow endpoint.
- `createNetflowOnPremise`: `NetflowOnPremise` - Create a Netflow on premise record.
- `createNetflowWhitelist`: `NetflowWhitelist` - Create a Netflow whitelist.
- `createNetworkMonitoringGraph`: `NetworkMonitoringGraph` - Create a Network Monitoring Graph.
- `createNetworkMonitoringTemplate`: `NetworkMonitoringTemplate` - Create a Network Monitoring Template.
- `createNetworkSite`: `NetworkSite` - Create a network site.
- `createNonInventoryItem`: `NonInventoryItem` - Create a non-inventory item.
- `createNote`: `Note` - Create a new note.
- `createOneTimeService`: `Service` - Create a new one time service.
- `createOrderGroup`: `OrderGroup` - Create an order group.
- `createOverageService`: `Service` - Create an overage service.
- `createPackage`: `Package` - Create a package.
- `createPayPalCredential`: `PayPalCredential` - Create a new PayPal credential.
- `createPayment`: `Payment` - Create a new payment without a payment method.
- `createPayments`: `PaymentResultConnection` (required) (connection) - Create a multiple new payment without a payment method.
- `createPersonalAccessToken`: `PersonalAccessToken` - Create a personal access token.
- `createPhoneNumber`: `PhoneNumber` - Create a new phone number.
- `createPhoneNumberType`: `PhoneNumberType` - Create a new phone number type.
- `createPoller`: `Poller` - Create a poller.
- `createPrintedInvoiceBatch`: `SuccessResponse` - Create a new printed invoice batch.
- `createPublicTicket`: `Ticket` - Create a public ticket.
- `createPurchaseOrder`: `PurchaseOrder` - Create a purchase order.
- `createRadiusAccount`: `RadiusAccount` - Create a new RADIUS account.
- `createRadiusGroup`: `RadiusGroup` - Create a RADIUS group.
- `createRadiusGroupReplyAttribute`: `RadiusGroupReplyAttribute` - Create a RADIUS group reply attribute.
- `createRadiusServer`: `RadiusServer` - Create a RADIUS server.
- `createRateCenter`: `RateCenter` - Create a rate center.
- `createRecentItem`: `RecentItem` (list) - Add an entity to your recent items list.
- `createRecurringService`: `Service` - Create a new recurring service.
- `createReport`: `AvailableReport` - Create a report.
- `createRole`: `Role` - Create a new role.
- `createSavedMessageCategory`: `SavedMessageCategory` - Create a saved message category.
- `createScheduleAddress`: `ScheduleAddress` - Create a schedule address.
- `createScheduleAvailability`: `ScheduleAvailability` - Create a schedule availability.
- `createScheduleAvailabilityDayTime`: `ScheduleAvailabilityDayTime` - Create a schedule availability day/time.
- `createScheduleBlocker`: `ScheduleBlocker` - Create a schedule blocker.
- `createScheduleBlockerDayTime`: `ScheduleBlockerDayTime` - Create a schedule blocker day/time.
- `createScheduleTimeOff`: `ScheduleTimeOff` - Create a schedule time off.
- `createScheduledEvent`: `ScheduledEvent` - Create a scheduled event.
- `createSearchFilter`: `SearchFilter` - Create a saved search filter for the current user.
- `createServiceMetadata`: `ServiceMetadata` - Create service metadata.
- `createServiceableAddress`: `Address` - Create a new serviceable address.
- `createServiceableAddressAccountAssignmentFuture`: `ServiceableAddressAccountAssignmentFuture` - Create a serviceable address account assignment future
- `createSignature`: `Signature` - Create a Signature.
- `createSnmpOid`: `SnmpOid` - Create an SNMP OID.
- `createSnmpOidThreshold`: `SnmpOidThreshold` - Create an SNMP OID threshold.
- `createSnmpOverride`: `SnmpOverride` - Create an SNMP override.
- `createSonarImport`: `ImportRecipe` - Create a Sonar Import.
- `createStoredView`: `StoredView` - Create a stored view.
- `createSubnet`: `Subnet` - Create a new subnet.
- `createSubscription`: `Subscription` - Create a subscription.
- `createSupernet`: `Supernet` - Create a new supernet.
- `createSystemBackup`: `SystemBackup` - Directly trigger a system backup of all database tables.
- `createSystemBackupDestination`: `SystemBackupDestination` - Create a destination that system backups can be exported to.
- `createTask`: `Task` - Create a new task.
- `createTaskTemplate`: `TaskTemplate` - Create a task template.
- `createTaskTemplateItem`: `TaskTemplateItem` - Create a task template item.
- `createTax`: `Tax` - Create a new tax.
- `createTaxExemption`: `TaxExemption` - Create a tax exemption.
- `createTaxOverride`: `TaxOverride` - Create a tax override.
- `createTaxProvider`: `TaxProvider` - Create a tax provider.
- `createTicketCategory`: `TicketCategory` - Create a new ticket category.
- `createTicketComment`: `TicketComment` - Create a ticket comment.
- `createTicketGroup`: `TicketGroup` - Create a new ticket group.
- `createTicketRecipient`: `TicketRecipient` - Create a ticket recipient.
- `createTicketReply`: `TicketReply` - Create a new ticket reply.
- `createTokenizedBankAccount`: `BankAccount` - Create a new bank account that has already been tokenized.
- `createTokenizedCreditCard`: `CreditCard` - Create a new credit card that has already been tokenized.
- `createTriggeredEmail`: `TriggeredEmail` - DEPRECATED: Create a new triggered email. See createTriggeredMessageMutation.
- `createTriggeredMessage`: `TriggeredMessage` - Create a triggered message.
- `createUninventoriedMacAddress`: `UninventoriedMacAddress` - Create a new uninventoried MAC address.
- `createUsageBasedBillingPolicy`: `UsageBasedBillingPolicy` - Create a usage based billing policy.
- `createUsageBasedBillingPolicyFreePeriod`: `UsageBasedBillingPolicyFreePeriod` - Create a free period in a `UsageBasedBillingPolicy`.
- `createUser`: `User` - Create a new user. The user will be sent an email with a temporary password after creation.
- `createVehicle`: `Vehicle` - Create a new vehicle.
- `createVendor`: `Vendor` - Create a vendor.
- `createVendorItem`: `VendorItem` - Create a vendor item.
- `createVoiceProvider`: `VoiceProvider` - Create a voice provider.
- `createVoiceProviderRate`: `VoiceProviderRate` - Create a voice provider rate.
- `createVoiceProviderRateImportFlatfile`: `VoiceProviderRateImportRecipe` - Create a Flatfile import of voice provider rates.
- `createVoiceService`: `Service` - Create a voice service.
- `createVoiceServiceGenericParameter`: `VoiceServiceGenericParameter` - Create a single voice service configuration parameter.
- `createWebhookEndpoint`: `WebhookEndpoint` - Create a webhook endpoint.
- `createWebhookEndpointEvent`: `WebhookEndpointEvent` - Create a webhook endpoint event.
- `deleteAccountAdtranMosaicServiceDetail`: `SuccessResponse` - Delete account Adtran Mosaic service details.
- `deleteAccountCalixServiceDetail`: `SuccessResponse` - Delete an account calix service detail.
- `deleteAccountGroup`: `SuccessResponse` - Delete an account group.
- `deleteAccountPackage`: `SuccessResponse` - Delete a package from an account.
- `deleteAccountService`: `SuccessResponse` - Delete a service from an account.
- `deleteAccountStatus`: `SuccessResponse` - Delete an account status.
- `deleteAccountType`: `SuccessResponse` - Delete an account type.
- `deleteAccountVoiceServiceDetail`: `SuccessResponse` - Delete an account voice service detail.
- `deleteAchBatch`: `SuccessResponse` - Delete an ACH batch.
- `deleteAddressList`: `SuccessResponse` - Delete an address list.
- `deleteAddressStatus`: `SuccessResponse` - Delete an address status.
- `deleteAdtranMosaicSetting`: `SuccessResponse` - Delete Adtran Mosaic settings.
- `deleteAlertingRotation`: `SuccessResponse` - Delete an alerting rotation.
- `deleteAlertingRotationDay`: `SuccessResponse` - Delete an alerting rotation day.
- `deleteApplicationFirewallRule`: `SuccessResponse` - Delete an application firewall rule.
- `deleteAuthenticationFactor`: `SuccessResponse` - Delete an authentication factor.
- `deleteBankAccount`: `SuccessResponse` - Delete a bank account.
- `deleteBankAccountProcessor`: `SuccessResponse` - Delete a bank account processor.
- `deleteBillingDefault`: `SuccessResponse` - Delete a billing default.
- `deleteCableModemProvisioner`: `SuccessResponse` - Delete a cable modem provisioner.
- `deleteCalendarIcal`: `SuccessResponse` - Delete a calendar - iCalendar.
- `deleteCalixCloudSetting`: `SuccessResponse` - Delete a Calix Cloud setting.
- `deleteCalixIntegration`: `SuccessResponse` - Delete a Calix integration
- `deleteCallDetailRecord`: `SuccessResponse` - Delete a call detail record (CDR).
- `deleteCallLog`: `SuccessResponse` - Delete a call log.
- `deleteCannedReply`: `SuccessResponse` - Delete a canned reply.
- `deleteCannedReplyCategory`: `SuccessResponse` - Delete a canned reply category.
- `deleteContact`: `SuccessResponse` - Delete a contact.
- `deleteContract`: `SuccessResponse` - Delete an unsigned contract.
- `deleteContractTemplate`: `SuccessResponse` - Delete a contract template.
- `deleteCreditCard`: `SuccessResponse` - Delete a credit card.
- `deleteCreditCardProcessor`: `SuccessResponse` - Delete a credit card processor.
- `deleteCustomField`: `SuccessResponse` - Delete a custom field.
- `deleteCustomLink`: `SuccessResponse` - Delete a custom link.
- `deleteDebit`: `SuccessResponse` - Delete a debit.
- `deleteDelinquencyExclusion`: `SuccessResponse` - Delete a delinquency exclusion.
- `deleteDepartment`: `SuccessResponse` - Delete a department.
- `deleteDeploymentType`: `SuccessResponse` - Delete a deployment type.
- `deleteDepositSlip`: `SuccessResponse` - Delete a deposit slip.
- `deleteDhcpServer`: `SuccessResponse` - Delete a DHCP server.
- `deleteDhcpServerIdentifier`: `SuccessResponse` - Delete a DHCP server identifier.
- `deleteDid`: `SuccessResponse` - Delete a DID.
- `deleteDidAssignment`: `SuccessResponse` - Delete a DID assignment.
- `deleteDiscount`: `SuccessResponse` - Delete a discount.
- `deleteEmailCategory`: `SuccessResponse` - Delete n messaging category.
- `deleteEmailDomain`: `SuccessResponse` - Delete an email domain.
- `deleteEmailMessage`: `SuccessResponse` - Delete a saved message.
- `deleteEmailMessageContent`: `SuccessResponse` - Delete saved message contents.
- `deleteEpc`: `SuccessResponse` - Delete an LTE EPC.
- `deleteExternalMarketingProvider`: `SuccessResponse` - Delete an external marketing integration.
- `deleteFibermapIntegration`: `SuccessResponse` - Delete a FiberMap Integration.
- `deleteFile`: `SuccessResponse` - Delete a file.
- `deleteGeneralLedgerCode`: `SuccessResponse` - Delete a general ledger code.
- `deleteGenericInventoryAssignee`: `SuccessResponse` - Delete a generic inventory assignee.
- `deleteGenericInventoryItems`: `GenericInventoryItem` - Delete generic inventory items.
- `deleteGeoTaxZone`: `SuccessResponse` - Delete a geo tax zone.
- `deleteGeofence`: `SuccessResponse` - Delete a geofence.
- `deleteGlobalInventoryModelMinMax`: `SuccessResponse` - Delete a Global Inventory Model Min/Max.
- `deleteGpsTrackingProvider`: `SuccessResponse` - Delete a GPS tracking provider.
- `deleteIdentityProvider`: `SuccessResponse` - Delete an identity provider.
- `deleteInboundMailbox`: `SuccessResponse` - Delete an inbound mailbox.
- `deleteInlineDevice`: `SuccessResponse` - Delete an inline device.
- `deleteInternalLocation`: `SuccessResponse` - Delete an internal location.
- `deleteInventoryItem`: `SuccessResponse` - Delete an inventory item.
- `deleteInventoryItemSegment`: `SuccessResponse` - Delete an inventory item segment.
- `deleteInventoryLocation`: `SuccessResponse` - Delete an inventory location.
- `deleteInventoryModel`: `SuccessResponse` - Delete an inventory model.
- `deleteInventoryModelCategory`: `SuccessResponse` - Delete an inventory model category.
- `deleteInventoryModelField`: `SuccessResponse` - Delete an inventory model field.
- `deleteInventoryModelMinMax`: `SuccessResponse` - Delete an Inventory Model Min/Max.
- `deleteInvoice`: `SuccessResponse` - Delete an invoice.
- `deleteInvoiceAttachment`: `SuccessResponse` - Delete an invoice attachment.
- `deleteInvoiceMessage`: `SuccessResponse` - Delete an invoice message.
- `deleteInvoiceTemplate`: `SuccessResponse` - Delete an invoice template.
- `deleteIpAssignment`: `SuccessResponse` - Delete an IP assignment.
- `deleteIpPool`: `SuccessResponse` - Delete an IP pool.
- `deleteJob`: `SuccessResponse` - Delete a job.
- `deleteJobService`: `SuccessResponse` - Delete a service from a job.
- `deleteJobType`: `SuccessResponse` - Delete a job type.
- `deleteLocalPrefix`: `SuccessResponse` - Delete a local prefix.
- `deleteLteProvider`: `SuccessResponse` - Delete an LTE provider.
- `deleteMailingAddress`: `SuccessResponse` - Delete an account mailing address.
- `deleteManufacturer`: `SuccessResponse` - Delete a manufacturer.
- `deleteMapOverlay`: `SuccessResponse` - Delete a map overlay.
- `deleteMessageCategory`: `SuccessResponse` - Delete a messaging category.
- `deleteNetflowAllowedSubnet`: `SuccessResponse` - Delete a Netflow allowed subnet.
- `deleteNetflowEndpoint`: `SuccessResponse` - Delete a Netflow endpoint.
- `deleteNetflowOnPremise`: `SuccessResponse` - Delete a Netflow on premise record.
- `deleteNetflowWhitelist`: `SuccessResponse` - Delete a Netflow whitelist.
- `deleteNetworkMonitoringGraph`: `SuccessResponse` - Delete a Network Monitoring Graph.
- `deleteNetworkMonitoringTemplate`: `SuccessResponse` - Delete a Network Monitoring Template.
- `deleteNetworkSite`: `SuccessResponse` - Delete a network site.
- `deleteNonInventoryItem`: `SuccessResponse` - Delete a non-inventory item.
- `deleteNote`: `SuccessResponse` - Delete a note.
- `deleteOrderGroup`: `SuccessResponse` - Delete an order group.
- `deletePackage`: `SuccessResponse` - Delete a package.
- `deletePayPalCredential`: `SuccessResponse` - Delete a PayPal credential.
- `deletePayment`: `SuccessResponse` - Delete a payment that was created without a payment method.
- `deletePersonalAccessToken`: `SuccessResponse` - Delete a personal access token.
- `deletePhoneNumber`: `SuccessResponse` - Delete a phone number.
- `deletePhoneNumberType`: `SuccessResponse` - Delete a phone number type.
- `deletePoller`: `SuccessResponse` - Delete a poller.
- `deleteRadiusAccount`: `SuccessResponse` - Delete a RADIUS account.
- `deleteRadiusGroup`: `SuccessResponse` - Delete a RADIUS group.
- `deleteRadiusGroupReplyAttribute`: `SuccessResponse` - Delete a RADIUS group reply attribute.
- `deleteRadiusServer`: `SuccessResponse` - Delete a RADIUS server.
- `deleteRateCenter`: `SuccessResponse` - Delete a rate center.
- `deleteRefundedPayment`: `SuccessResponse` - Delete a refunded payment.
- `deleteReversedPayment`: `SuccessResponse` - Delete a reversed payment.
- `deleteRole`: `SuccessResponse` - Delete a role.
- `deleteSavedMessageCategory`: `SuccessResponse` - Delete a saved message category.
- `deleteScheduleAddress`: `SuccessResponse` - Delete a schedule address.
- `deleteScheduleAvailability`: `SuccessResponse` - Delete a schedule availability.
- `deleteScheduleAvailabilityDayTime`: `SuccessResponse` - Delete a schedule availability day/time.
- `deleteScheduleBlocker`: `SuccessResponse` - Delete a schedule blocker.
- `deleteScheduleBlockerDayTime`: `SuccessResponse` - Delete a schedule blocker day/time.
- `deleteScheduleTimeOff`: `SuccessResponse` - Delete a schedule time off.
- `deleteScheduledEvent`: `SuccessResponse` - Delete a scheduled event.
- `deleteSearchFilter`: `SuccessResponse` - Delete a saved search filter for the current user.
- `deleteService`: `SuccessResponse` - Delete a service.
- `deleteServiceMetadata`: `SuccessResponse` - Delete service metadata.
- `deleteServiceableAddress`: `SuccessResponse` - Delete a serviceable address.
- `deleteServiceableAddressAccountAssignmentFuture`: `SuccessResponse` - Delete a serviceable address account assignment future
- `deleteSignature`: `SuccessResponse` - Delete a Signature.
- `deleteSnmpOid`: `SuccessResponse` - Delete an SNMP OID.
- `deleteSnmpOidThreshold`: `SuccessResponse` - Delete an SNMP OID threshold.
- `deleteSnmpOverride`: `SuccessResponse` - Delete an SNMP override.
- `deleteStoredView`: `SuccessResponse` - Delete a stored view.
- `deleteSubnet`: `SuccessResponse` - Delete a subnet.
- `deleteSubscription`: `SuccessResponse` - Delete a subscription.
- `deleteSupernet`: `SuccessResponse` - Delete a supernet.
- `deleteSystemBackupDestination`: `SuccessResponse` - Delete a system backup destination.
- `deleteTask`: `SuccessResponse` - Delete a task.
- `deleteTaskTemplate`: `SuccessResponse` - Delete a task template.
- `deleteTaskTemplateItem`: `SuccessResponse` - Delete a task template item.
- `deleteTax`: `SuccessResponse` - Delete a tax.
- `deleteTaxExemption`: `SuccessResponse` - Delete a tax exemption.
- `deleteTaxOverride`: `SuccessResponse` - Delete a tax override.
- `deleteTaxProvider`: `SuccessResponse` - Delete a tax provider.
- `deleteTicket`: `SuccessResponse` - Delete a ticket.
- `deleteTicketCategory`: `SuccessResponse` - Delete a ticket category.
- `deleteTicketComment`: `SuccessResponse` - Delete a ticket comment.
- `deleteTicketGroup`: `SuccessResponse` - Delete a ticket group.
- `deleteTicketRecipient`: `SuccessResponse` - Delete a ticket recipient.
- `deleteTickets`: `SuccessResponse` - Delete multiple tickets.
- `deleteTriggeredEmail`: `SuccessResponse` - DEPRECATED: Delete a triggered email. See deleteTriggeredMessageMutation.
- `deleteTriggeredMessage`: `SuccessResponse` - Delete a triggered message.
- `deleteUninventoriedMacAddress`: `SuccessResponse` - Delete an uninventoried MAC address.
- `deleteUsageBasedBillingPolicy`: `SuccessResponse` - Delete a usage based billing policy.
- `deleteUsageBasedBillingPolicyFreePeriod`: `SuccessResponse` - Delete a usage based billing policy free period.
- `deleteVehicle`: `SuccessResponse` - Delete a vehicle.
- `deleteVendorItem`: `SuccessResponse` - Delete a vendor item.
- `deleteVoiceProvider`: `SuccessResponse` - Delete a voice provider.
- `deleteVoiceProviderRate`: `SuccessResponse` - Delete a voice provider rate.
- `deleteVoiceServiceGenericParameter`: `SuccessResponse` - Delete a single voice service configuration parameter.
- `deleteWebhookEndpoint`: `SuccessResponse` - Delete a webhook endpoint.
- `deleteWebhookEndpointEvent`: `SuccessResponse` - Delete a webhook endpoint event.
- `disconnectAccount`: `Account` - Disconnect an account.
- `disconnectRadiusSession`: `RadiusSessionHistory` - Disconnect a RADIUS session.
- `emailInvoiceBatch`: `SuccessResponse` - Resend emailed invoices.
- `emailInvoiceToContact`: `SuccessResponse` - Email an invoice to a contact manually.
- `emailPurchaseOrderToVendor`: `SuccessResponse` - Email an approved purchase order to its vendor.
- `generateImportCredentialsFlatfile`: `ImportCredentialsFlatfile` - Generate import credentials for use with Flatfile.
- `generateSpliceReport`: `SuccessResponse` - Generate Splice Report from Vetro FiberMap.
- `generateTestWebhook`: `WebhookTestResponse` - mutations.generateTestWebhookMutation
- `linkAccounts`: `Account` - Link a parent and child account.
- `linkCalixCloudSubscriberToAccount`: `SuccessResponse` - Link Calix Cloud subscriber to Sonar account.
- `linkEntityToTicket`: `Ticket` - Link an entity to a ticket.
- `linkFibermapPlanToNetworkSite`: `NetworkSite` - Link Fibermap Plan To Network Site
- `linkFibermapServiceLocationToAddress`: `Address` - Link Fibermap Service Location To Address
- `linkFileToEntity`: `FileableInterface` - Link a file to an entity.
- `linkInventoryItemToAccountService`: `SuccessResponse` - Link an inventory item to an account service.
- `linkInventoryModelToAccountServices`: `SuccessResponse` - Link inventory model to account services.
- `linkInvoices`: `Invoice` - Link a parent and child invoice.
- `linkTowercoverageSubmissionToServiceableAddressMutation`: `TowercoverageSubmission` - Link a TowerCoverage submission to a new or existing serviceable address.
- `makeAccountServicePrimary`: `SuccessResponse` - Make the additional service provided primary and the current primary an additional service.
- `mergeSubnets`: `Subnet` - Merge two subnets together.
- `mergeTickets`: `Ticket` - Merge multiple tickets into one.
- `publishReport`: `AvailableReport` - Publish a report.
- `rebootInventoryItem`: `InventoryItem` - Forced reboot of an inventory item
- `recalculateNextRecurringChargeAmount`: `SuccessResponse` - Recalculate the next recurring charge amount of an account.
- `receivePurchaseOrderItems`: `InventoryItem` (list) - Receive a list of purchase order items into an inventory location.
- `reenrollAuthenticationFactor`: `SuccessResponse` - Re-enroll an authentication factor, resending the one-time password verification message if applicable.
- `refundPayment`: `RefundedPayment` - Refund a payment.
- `reindexModel`: `SuccessResponse` - Reindex a model in elastic.
- `rescheduleScheduleBlocker`: `ScheduleBlockerOverride` - Reschedule a schedule blocker.
- `resendAutoreply`: `SuccessResponse` - Resend a ticket autoreply email.
- `resendContract`: `SuccessResponse` - Resend a copy of a contract.
- `resendPrintToMailBatch`: `SuccessResponse` - Resend a failed print to mail batch.
- `resendUserCreationEmail`: `SuccessResponse` - Resend the initial setup email to a newly created user.
- `resetInventoryItem`: `InventoryItem` - Software reset connection of an inventory item
- `respondToInstanceManagementRequest`: `InstanceManagementRequest` - Respond to an instance management request.
- `resyncFibermapServiceLocationToAddress`: `FibermapServiceLocation` - Retries the creation of an address from a specific unmapped Vetro Fibermap Service location.
- `reverseDebit`: `Debit` - Reverse a debit.
- `reverseDiscount`: `Discount` - Reverse a discount.
- `reversePayment`: `ReversedPayment` - Reverse a payment.
- `scheduleManyJobsAndScheduleBlockerOverrides`: `SuccessResponse` - Schedule many jobs and schedule blocker overrides at the same time.
- `scheduleManyJobsAndScheduleBlockerOverridesSkipsValidation`: `SuccessResponse` - Schedule jobs and schedule blocker overrides and skip scheduling validations
- `sendEmailDomainVerificationEmail`: `SuccessResponse` - Send an email to verify an email domain.
- `sendTestEmail`: `SuccessResponse` - mutations.sendTestEmailMutation
- `sendTestTriggeredEmail`: `SuccessResponse` - mutations.sendTestTriggeredEmailMutation
- `setActiveStoredView`: `SuccessResponse` - Set the active stored view.
- `splitSubnet`: `Subnet` (list) - Split a subnet in half.
- `synchronizeCableModemProvisioner`: `CableModemProvisioner` - Synchronize a cable modem provisioner.
- `synchronizeCalixCloud`: `CalixCloudSetting` - Synchronize Calix Cloud setting.
- `synchronizeCalixIntegration`: `CalixIntegration` - Full synchronization of a Calix integration
- `synchronizeDhcpServer`: `DhcpServer` - Removes all existing leases and writes new ones based on existing IP assignments.
- `synchronizeFibermapIntegration`: `FibermapIntegration` - Synchronize a Fibermap Integration
- `synchronizeInlineDevice`: `InlineDevice` - Synchronize an inline device.
- `synchronizeLteProvider`: `LteProvider` - Synchronize an LTE provider.
- `synchronizeRadiusServer`: `RadiusServer` - Synchronize a RADIUS server.
- `takeoverAdtranMosaic`: `AdtranMosaicSetting` - Perform Sonar takeover of Adtran Mosaic Cloud.
- `toggleAllNotifications`: `SuccessResponse` - Toggle all notifications as read or unread.
- `toggleNotifications`: `SuccessResponse` - Toggle notifications as read or unread.
- `unarchiveAccount`: `Account` - Unarchive an account.
- `unclaimInventoryItems`: `SuccessResponse` - Unclaim one or many inventory items.
- `unlinkAccounts`: `Account` - Unlink a parent and child account.
- `unlinkEntityFromTicket`: `Ticket` - Unlink an entity from a ticket.
- `unlinkInvoices`: `Invoice` - Unlink a parent and child invoice.
- `updateAccount`: `Account` - Update an account.
- `updateAccountActivationDate`: `Account` - Update a previously activated accounts activation date.
- `updateAccountAdtranMosaicServiceDetail`: `AccountAdtranMosaicServiceDetail` - Update account Adtran Mosaic service details.
- `updateAccountBillingParameter`: `AccountBillingParameter` - Update a variety of account billing parameters.
- `updateAccountCalixServiceDetail`: `AccountCalixServiceDetail` - Update an account calix service detail.
- `updateAccountGroup`: `AccountGroup` - Update an account group.
- `updateAccountService`: `AccountService` - Update an account service.
- `updateAccountStatus`: `AccountStatus` - Update an account status.
- `updateAccountType`: `AccountType` - Update an account type.
- `updateAccountVoiceServiceDetail`: `AccountVoiceServiceDetail` - Update an account voice service detail.
- `updateAddressList`: `AddressList` - Update an address list.
- `updateAddressStatus`: `AddressStatus` - Update an address status.
- `updateAdjustmentService`: `Service` - Update an adjustment service.
- `updateAdtranMosaicAudit`: `AdtranMosaicAudit` - Update Adtran Mosaic audit.
- `updateAdtranMosaicSetting`: `AdtranMosaicSetting` - Update Adtran Mosaic settings.
- `updateAlertingRotation`: `AlertingRotation` - Update an alerting rotation.
- `updateAlertingRotationDay`: `AlertingRotationDay` - Update an alerting rotation day.
- `updateApplicationFirewallRule`: `ApplicationFirewallRule` - Update an application firewall rule.
- `updateAuthProvider`: `AuthProvider` - Update an auth provider.
- `updateAuthenticationFactor`: `AuthenticationFactor` - Update an authentication factor.
- `updateAvalaraTaxDefinition`: `AvalaraTaxDefinition` - Update an Avalara bundled tax definition.
- `updateBankAccount`: `BankAccount` - Update a bank account.
- `updateBankAccountProcessor`: `BankAccountProcessor` - Update a bank account processor.
- `updateBillingDefault`: `BillingDefault` - Update a billing default.
- `updateBillingSettings`: `BillingSetting` - Update the system billing settings.
- `updateCableModemProvisioner`: `CableModemProvisioner` - Update a cable modem provisioner.
- `updateCalendarIcal`: `CalendarIcal` - Update a calendar - iCalendar.
- `updateCalendarIcalToken`: `CalendarIcal` - Update a iCalendar calendar token
- `updateCalendarSystemSettings`: `SystemSetting` - Update system settings related to calendars.
- `updateCalixCloudSetting`: `CalixCloudSetting` - Update a Calix Cloud setting.
- `updateCalixIntegration`: `CalixIntegration` - Update a Calix integration
- `updateCallDetailRecord`: `CallDetailRecord` - Update a call detail record (CDR).
- `updateCallLog`: `CallLog` - Update a call log.
- `updateCannedReply`: `CannedReply` - Update a canned reply.
- `updateCannedReplyCategory`: `CannedReplyCategory` - Update a canned reply category.
- `updateCompany`: `Company` - Update a company.
- `updateContact`: `Contact` - Update a contact.
- `updateContract`: `Contract` - Update a contract.
- `updateContractTemplate`: `ContractTemplate` - Update a contract template.
- `updateCreditCard`: `CreditCard` - Update a credit card.
- `updateCreditCardProcessor`: `CreditCardProcessor` - Update a credit card processor.
- `updateCustomField`: `CustomField` - Update a custom field.
- `updateCustomLink`: `CustomLink` - Update a custom link.
- `updateDataService`: `Service` - Update a data service.
- `updateDataUsageHistory`: `DataUsageHistory` - Update a data usage history record.
- `updateDebit`: `Debit` - Update a debit.
- `updateDelinquencyExclusion`: `DelinquencyExclusion` - Update a delinquency exclusion.
- `updateDepartment`: `Department` - Update a department.
- `updateDeploymentType`: `DeploymentType` - Update a deployment type.
- `updateDepositSlip`: `DepositSlip` - Update a deposit slip.
- `updateDhcpServer`: `DhcpServer` - Update a DHCP server.
- `updateDhcpServerIdentifier`: `DhcpServerIdentifier` - Update a DHCP server identifier.
- `updateDid`: `Did` - Update a DID.
- `updateDidAssignment`: `DidAssignment` - Update a DID assignment.
- `updateDiscount`: `Discount` - Update a discount.
- `updateDrivers`: `Vehicle` - Update the assigned drivers on a vehicle.
- `updateEmailCategory`: `EmailCategory` - Update a messaging category.
- `updateEmailMessage`: `EmailMessage` - Update a saved message.
- `updateEmailMessageContent`: `EmailMessageContent` - Update saved message contents.
- `updateEntityCustomFields`: `CustomFieldData` (list) - Update the custom fields on an entity.
- `updateEpc`: `Epc` - Update an LTE EPC.
- `updateExpiringService`: `Service` - Update an expiring service.
- `updateExternalMarketingProvider`: `ExternalMarketingProvider` - Update an external marketing integration.
- `updateFibermapIntegration`: `FibermapIntegration` - Update a FiberMap Integration.
- `updateFibermapPlan`: `FibermapPlan` - Update a Fibermap Plan.
- `updateFibermapServiceLocation`: `FibermapServiceLocation` - Update a Fibermap Service Location.
- `updateFile`: `File` - Update a file.
- `updateGeneralLedgerCode`: `GeneralLedgerCode` - Update a general ledger code.
- `updateGenericInventoryAssignee`: `GenericInventoryAssignee` - Update a generic inventory assignee.
- `updateGeoTaxZone`: `GeoTaxZone` - Update a geo tax zone.
- `updateGeofence`: `Geofence` - Update a geofence.
- `updateGlobalInventoryModelMinMax`: `GlobalInventoryModelMinMax` - Update a Global Inventory Model Min/Max.
- `updateGpsTrackingProvider`: `GpsTrackingProvider` - Update a GPS tracking provider.
- `updateIdentityProviderActiveDirectory`: `IdentityProvider` - Update an ActiveDirectory identity provider.
- `updateIdentityProviderGoogle`: `IdentityProvider` - Update a Google identity provider.
- `updateIdentityProviderMicrosoft`: `IdentityProvider` - Update a Microsoft identity provider.
- `updateIdentityProviderSaml`: `IdentityProvider` - Update a SAML identity provider.
- `updateInboundMailbox`: `InboundMailbox` - Update an inbound mailbox.
- `updateInlineDevice`: `InlineDevice` - Update an inline device.
- `updateInstanceServiceFundAutoPay`: `InstanceServiceFundAutoPay` (required) - Update the autopay setting for an instance service fund.
- `updateInternalLocation`: `InternalLocation` - Update an internal location.
- `updateInventoryItem`: `InventoryItem` - Update an inventory item.
- `updateInventoryItemFields`: `InventoryItem` - Update the contents of inventory item model fields.
- `updateInventoryItemSegment`: `InventoryItem` (list) - Update an inventory item segment.
- `updateInventoryItemStatus`: `InventoryItem` - Update an Inventory Item status.
- `updateInventoryItems`: `InventoryItem` (list) - Update one or more inventory items.
- `updateInventoryLocation`: `InventoryLocation` - Update an inventory location.
- `updateInventoryModel`: `InventoryModel` - Update an inventory model.
- `updateInventoryModelCategory`: `InventoryModelCategory` - Update an inventory model category.
- `updateInventoryModelField`: `InventoryModelField` - Update an inventory model field.
- `updateInventoryModelMinMax`: `InventoryModelMinMax` - Update an Inventory Model Min/Max.
- `updateInvoice`: `Invoice` - Update an invoice.
- `updateInvoiceAttachment`: `InvoiceAttachment` - Update an invoice attachment.
- `updateInvoiceMessage`: `InvoiceMessage` - Update an invoice message.
- `updateInvoiceTemplate`: `InvoiceTemplate` - Update an invoice template.
- `updateIpAssignment`: `IpAssignment` - Update an IP assignment.
- `updateIpPool`: `IpPool` - Update an IP pool.
- `updateJob`: `Job` - Update a job.
- `updateJobService`: `JobService` - Update the quantity of a service associated with a job.
- `updateJobSkipsValidation`: `Job` - Update a job skipping validation.
- `updateJobType`: `JobType` - Update a job type.
- `updateLocalPrefix`: `LocalPrefix` - Update a local prefix.
- `updateLookerExploreLicense`: `LookerExploreLicense` - Update a report builder license.
- `updateLookerViewLicense`: `LookerViewLicense` - Update a report viewer license.
- `updateLteProvider`: `LteProvider` - Update an LTE provider.
- `updateMailingAddress`: `Address` - Update an account mailing address.
- `updateManufacturer`: `Manufacturer` - Update a manufacturer.
- `updateMapOverlay`: `MapOverlay` - Update a map overlay.
- `updateMe`: `Me` - Update your user profile.
- `updateMessageCategory`: `MessageCategory` - Update a messaging category.
- `updateMfaAdminSettings`: `MfaAdminSetting` - Update the multi-factor authentication admin settings.
- `updateNetflowAllowedSubnet`: `NetflowAllowedSubnet` - Update a Netflow allowed subnet.
- `updateNetflowEndpoint`: `NetflowEndpoint` - Update a Netflow endpoint.
- `updateNetflowOnPremise`: `NetflowOnPremise` - Update a Netflow on premise record.
- `updateNetflowWhitelist`: `NetflowWhitelist` - Update a Netflow whitelist.
- `updateNetworkMonitoringGraph`: `NetworkMonitoringGraph` - Update a Network Monitoring Graph.
- `updateNetworkMonitoringTemplate`: `NetworkMonitoringTemplate` - Update a Network Monitoring Template.
- `updateNetworkSite`: `NetworkSite` - Update a network site.
- `updateNonInventoryItem`: `NonInventoryItem` - Update a non-inventory item.
- `updateNote`: `Note` - Update a note.
- `updateOneTimeService`: `Service` - Update a one time service.
- `updateOrderGroup`: `OrderGroup` - Update an order group.
- `updateOverageService`: `Service` - Update an overage service.
- `updatePackage`: `Package` - Update a package.
- `updatePasswordPolicy`: `PasswordPolicy` - Update the password policy that is applied to users.
- `updatePayPalCredential`: `PayPalCredential` - Update a PayPal credential.
- `updatePayment`: `Payment` - Update a payment that was created without a payment method.
- `updatePhoneNumber`: `PhoneNumber` - Update a phone number.
- `updatePhoneNumberType`: `PhoneNumberType` - Update a phone number type.
- `updatePoller`: `Poller` - Update a poller.
- `updatePollerSettings`: `PollerSetting` - Update the system poller settings.
- `updatePreseem`: `Preseem` - Update the Preseem integration.
- `updatePrintToMailOrderError`: `PrintToMailOrderError` - Update a print to mail order error.
- `updatePrintToMailSettings`: `PrintToMailSetting` - Update the print to mail settings.
- `updatePurchaseOrder`: `PurchaseOrder` - Update a purchase order.
- `updatePurchaseOrderSystemSettings`: `SuccessResponse` - Update system settings related to purchase orders.
- `updateRadiusAccount`: `RadiusAccount` - Update a RADIUS account.
- `updateRadiusGroup`: `RadiusGroup` - Update a RADIUS group.
- `updateRadiusGroupReplyAttribute`: `RadiusGroupReplyAttribute` - Update a RADIUS group reply attribute.
- `updateRadiusServer`: `RadiusServer` - Update a RADIUS server.
- `updateRateCenter`: `RateCenter` - Update a rate center.
- `updateRecurringService`: `Service` - Update a recurring service.
- `updateRole`: `Role` - Update a role.
- `updateSavedMessageCategory`: `SavedMessageCategory` - Update a saved message category.
- `updateScheduleAddress`: `ScheduleAddress` - Update a schedule address.
- `updateScheduleAvailability`: `ScheduleAvailability` - Update a schedule availability.
- `updateScheduleAvailabilityDayTime`: `ScheduleAvailabilityDayTime` - Update a schedule availability day/time.
- `updateScheduleBlocker`: `ScheduleBlocker` - Update a schedule blocker.
- `updateScheduleBlockerDayTime`: `ScheduleBlockerDayTime` - Update a schedule blocker day/time.
- `updateScheduleTimeOff`: `ScheduleTimeOff` - Update a schedule time off.
- `updateScheduledEvent`: `ScheduledEvent` - Update a scheduled event.
- `updateSearchFilter`: `SearchFilter` - Update a saved search filter for the current user, or enable it for all users (superadmin only).
- `updateServiceMetadata`: `ServiceMetadata` - Update service metadata.
- `updateServiceableAddress`: `Address` - Update a serviceable address.
- `updateServiceableAddressAccountAssignmentFuture`: `ServiceableAddressAccountAssignmentFuture` - Update a serviceable address account assignment future
- `updateSignature`: `Signature` - Update a Signature.
- `updateSmsSettings`: `SmsSetting` - Update the SMS settings.
- `updateSnmpOid`: `SnmpOid` - Update an SNMP OID.
- `updateSnmpOidThreshold`: `SnmpOidThreshold` - Update an SNMP OID threshold.
- `updateSnmpOverride`: `SnmpOverride` - Update an SNMP override.
- `updateStoredView`: `StoredView` - Update a stored view.
- `updateSubnet`: `Subnet` - Update a subnet.
- `updateSupernet`: `Supernet` - Update supernet mutation.
- `updateSystemBackupDestination`: `SystemBackupDestination` - Update a system backup destination.
- `updateSystemBackupSettings`: `SystemBackupSetting` - Update settings for system backups.
- `updateSystemSettings`: `SystemSetting` - Update system configuration.
- `updateTask`: `Task` - Update a task.
- `updateTaskTemplate`: `TaskTemplate` - Update a task template.
- `updateTaskTemplateItem`: `TaskTemplateItem` - Update a task template item.
- `updateTax`: `Tax` - Update a tax.
- `updateTaxExemption`: `TaxExemption` - Update a tax exemption.
- `updateTaxOverride`: `TaxOverride` - Update a tax override.
- `updateTaxProvider`: `TaxProvider` - Update a tax provider.
- `updateTicket`: `Ticket` - Update a ticket.
- `updateTicketCategory`: `TicketCategory` - Update a ticket category.
- `updateTicketComment`: `TicketComment` - Update a ticket comment.
- `updateTicketGroup`: `TicketGroup` - Update a ticket group.
- `updateTicketRecipient`: `TicketRecipient` - Update a ticket recipient.
- `updateTicketingSettings`: `TicketingSetting` - Update the ticketing settings.
- `updateTowercoverageConfiguration`: `TowercoverageConfiguration` - Update the TowerCoverage integration.
- `updateTowercoverageSubmission`: `TowercoverageSubmission` - Update a Towercoverage submission.
- `updateTriggeredEmail`: `TriggeredEmail` - DEPRECATED: Update a triggered email. See updateTriggeredMessageMutation.
- `updateTriggeredMessage`: `TriggeredMessage` - Update a triggered message.
- `updateUninventoriedMacAddress`: `UninventoriedMacAddress` - Update an uninventoried MAC address.
- `updateUsageBasedBillingPolicy`: `UsageBasedBillingPolicy` - Update a usage based billing policy.
- `updateUsageBasedBillingPolicyFreePeriod`: `UsageBasedBillingPolicyFreePeriod` - Update a usage based billing policy free period.
- `updateUser`: `User` - Update a user.
- `updateVehicle`: `Vehicle` - Update a vehicle.
- `updateVendor`: `Vendor` - Update a vendor.
- `updateVendorItem`: `VendorItem` - Update a vendor item.
- `updateVoiceProvider`: `VoiceProvider` - Update a voice provider.
- `updateVoiceProviderRate`: `VoiceProviderRate` - Update a voice provider rate.
- `updateVoiceProviderRateChargePercentMutation`: `SuccessResponse` - Update the charge percent for all rates of a voice provider.
- `updateVoiceService`: `Service` - Update a voice service.
- `updateVoiceServiceGenericParameter`: `VoiceServiceGenericParameter` - Create a single voice service configuration parameter.
- `updateWebhookEndpoint`: `WebhookEndpoint` - Update a webhook endpoint.
- `validateCableModemProvisionerCredentials`: `CredentialValidationResponse` - Validate the credentials for a cable modem provisioner. This will update the `status` of the cable modem provisioner.
- `validateCalixCredentials`: `CredentialValidationResponse` - Validate credentials of a Calix integration
- `validateDhcpServerCredentials`: `CredentialValidationResponse` - Validate the entered DHCP server credentials. This will update the `status` of the DHCP server.
- `validateEmailDomain`: `EmailDomain` - Validate an email domain's DNS records and email verification status.
- `validateFibermapIntegrationCredentials`: `CredentialValidationResponse` - Validate the entered Fibermap Integration API Token.
- `validateGpsTrackingProviderCredentials`: `CredentialValidationResponse` - Validate GPS tracking provider credentials validate against external provider.
- `validateInlineDeviceCredentials`: `CredentialValidationResponse` - Validate the credentials for an inline device. This will update the `status` of the inline device.
- `validateLteProviderCredentials`: `CredentialValidationResponse` - Validate the entered LTE provider credentials. This will update the `status` of the LTE provider.
- `validateRadiusServerCredentials`: `CredentialValidationResponse` - Validate the entered RADIUS server credentials. This will update the `status` of the RADIUS server.
- `validateTaxProviderCredentials`: `CredentialValidationResponse` - Validate the entered tax provider credentials.
- `verifyOneTimePasswordForAuthenticationFactor`: `SuccessResponse` - Verify a one-time password for an authentication factor.
- `verifySystemBackupDestinationConnection`: `SuccessResponse` - Verify the credentials for a system backup destination.
- `voidCredit`: `Credit` - Void a credit on an invoice.
- `voidInvoice`: `Invoice` - Void an invoice.
- `voidPayment`: `VoidedPayment` - Void a payment.

---

### BankAccountProcessorCredentialConnection

**Description**: The connection wrapper around the `BankAccountProcessorCredentialConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `BankAccountProcessorCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### BankAccountProcessorConnection

**Description**: The connection wrapper around the `BankAccountProcessorConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `BankAccountProcessor` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### BankAccountConnection

**Description**: The connection wrapper around the `BankAccountConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `BankAccount` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountVoiceServiceDetailConnection

**Description**: The connection wrapper around the `AccountVoiceServiceDetailConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountVoiceServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountTypeConnection

**Description**: The connection wrapper around the `AccountTypeConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountType` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountStatusConnection

**Description**: The connection wrapper around the `AccountStatusConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountStatus` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountServiceConnection

**Description**: The connection wrapper around the `AccountServiceConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountService` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountGroupConnection

**Description**: The connection wrapper around the `AccountGroupConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountGroup` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountConnection

**Description**: The connection wrapper around the `AccountConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Account` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountCalixServiceDetailConnection

**Description**: The connection wrapper around the `AccountCalixServiceDetailConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountCalixServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountBillingParameterConnection

**Description**: The connection wrapper around the `AccountBillingParameterConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountBillingParameter` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AccountAdtranMosaicServiceDetailConnection

**Description**: The connection wrapper around the `AccountAdtranMosaicServiceDetailConnection` type.

**Category**: accounts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccountAdtranMosaicServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Authentication Entities (14 total)


### AuthProvider

**Description**: An authentication provider.

**Category**: authentication
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `auth0_client_id`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 4 (`id`, `type`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `auth0_client_id`: `String` - The Auth0 client ID.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `type`: `AuthProviderType` (required) (enum) - The type.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PayPalCredential

**Description**: Paypal credentials for external payments.

**Category**: authentication
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `client_id`

**Relationship Fields**: 4 (`id`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `client_id`: `String` (required) - The client ID for PayPal.
- `client_secret`: `String` (required) - The client secret for PayPal.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AuthenticationFactor

**Description**: A user's authentication factors.

**Category**: authentication
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `user_id`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 8 (`id`, `data`, `secret_data`, `type`, `user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `data`: `Text` - The configuration data of the authentication factor.
- `is_verified`: `Boolean` (required) - Whether or not the authentication factor is verified.
- `secret_data`: `Text` - The secret configuration data of the authentication factor.
- `type`: `AuthenticationFactorType` (required) (enum) - The type of authentication factor this is.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SystemBackupDestinationCredential

**Description**: A credential used to authenticate against configured destinations to export system backups to.

**Category**: authentication
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `system_backup_destination_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 8 (`id`, `credential`, `system_backup_destination_id`, `value`, `system_backup_destination`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `SystemBackupDestinationProviderCredential` (required) (enum) - The credential name.
- `system_backup_destination_id`: `Int64Bit` (required) - The ID of a destination that a system backup can be exported to.
- `value`: `Text` (required) - The value.
- `system_backup_destination`: `SystemBackupDestination` - A configured destination to export system backups to.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PasswordPolicy

**Description**: A password policy that defines password requirements.

**Category**: authentication
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 3 (`id`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `minimum_length`: `Int` (required) - The minimum length a password must be.
- `minimum_password_strength`: `Int` (required) - A score for the zxcvbn password strength estimation library that this password must match. 0 allows all passwords, 4 requires a very strong password. See https://github.com/dropbox/zxcvbn for details.
- `requires_alpha_numeric`: `Boolean` (required) - Must a password be alpha-numeric (contain at least one letter and one number) or can it have any combination of characters?
- `requires_at_least_one_special_character`: `Boolean` (required) - Does a password require at least one special (non alpha-numeric) character?
- `requires_upper_and_lower_case_characters`: `Boolean` (required) - Does a password require both upper and lower case characters?
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### LteProviderCredential

**Description**: Credentials for an `LteProvider`.

**Category**: authentication
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `lte_provider_id`, `lte_provider`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 7 (`id`, `credential`, `lte_provider_id`, `lte_provider`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `LteProviderAuthenticationCredential` (required) (enum) - The credential name.
- `lte_provider_id`: `Int64Bit` (required) - The ID of an `LteProvider`.
- `value`: `String` (required) - The value.
- `lte_provider`: `LteProvider` - A provider of LTE provisioning.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ExternalMarketingProviderCredential

**Description**: The `ExternalMarketingProvider` credentials for integration.

**Category**: authentication
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `external_marketing_provider_id`, `key`, `external_marketing_provider`

**Enum Fields**: 1 (`key`)

**Relationship Fields**: 7 (`id`, `external_marketing_provider_id`, `key`, `external_marketing_provider`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `external_marketing_provider_id`: `Int64Bit` (required) - The ID of an `ExternalMarketingProvider`.
- `key`: `ExternalMarketingProviderAuthCredential` (required) (enum) - Key for a specific value.
- `value`: `String` (required) - The value.
- `external_marketing_provider`: `ExternalMarketingProvider` - A `ExternalMarketingProviderType` for `ExternalMarketingProvider` 3rd party integration.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CredentialValidationResponse

**Description**: types.credential_validation_response

**Category**: authentication
**Relevance Score**: 3 (Primary: 1, Secondary: 0, Operational: 0)
**Total Fields**: 2

**All Fields**:

- `status`: `Boolean` (required) - The status of the validation attempt.
- `message`: `String` - Any message returned from the device upon attempted credential validation.

---

### SystemBackupDestinationCredentialConnection

**Description**: The connection wrapper around the `SystemBackupDestinationCredentialConnection` type.

**Category**: authentication
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SystemBackupDestinationCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PayPalCredentialConnection

**Description**: The connection wrapper around the `PayPalCredentialConnection` type.

**Category**: authentication
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PayPalCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### LteProviderCredentialConnection

**Description**: The connection wrapper around the `LteProviderCredentialConnection` type.

**Category**: authentication
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `LteProviderCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ExternalMarketingProviderCredentialConnection

**Description**: The connection wrapper around the `ExternalMarketingProviderCredentialConnection` type.

**Category**: authentication
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ExternalMarketingProviderCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AuthenticationFactorConnection

**Description**: The connection wrapper around the `AuthenticationFactorConnection` type.

**Category**: authentication
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AuthenticationFactor` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AuthProviderConnection

**Description**: The connection wrapper around the `AuthProviderConnection` type.

**Category**: authentication
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AuthProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Availability Entities (4 total)


### ScheduleAvailability

**Description**: Availability for `Job`s to be scheduled.

**Category**: availability
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `geofence_id`, `name`

**Relationship Fields**: 9 (`id`, `geofence_id`, `geofence`, `job_types`, `users`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `available`: `Boolean` (required) - Whether this `ScheduleAvailability` creates available time, or blocks available time.
- `geofence_id`: `Int64Bit` - The ID of a `Geofence`.
- `infinite_repetitions`: `Boolean` (required) - Whether this repeats forever or not.
- `name`: `String` (required) - A descriptive name.
- `repetitions`: `Int` - The number of times this repeats.
- `start_date`: `Date` (required) - The start date for this `ScheduleAvailability`.
- `weeks_between_repetitions`: `Int` (required) - The number of weeks between repetitions.
- `geofence`: `Geofence` - A geographical restriction.
- `job_types`: `JobTypeConnection` (required) (connection) - The type of a `Job`.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `schedule_availability_day_times`: `ScheduleAvailabilityDayTimeConnection` (required) (connection) - A day and time associated with a `ScheduleAvailability`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleAvailabilityDayTime

**Description**: A day and time associated with a `ScheduleAvailability`.

**Category**: availability
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `schedule_availability_id`

**Enum Fields**: 1 (`day`)

**Relationship Fields**: 6 (`id`, `day`, `schedule_availability_id`, `schedule_availability`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `all_day`: `Boolean` (required) - Whether this day is available from start to finish.
- `day`: `Day` (required) (enum) - A day.
- `end_time`: `Time` - The end time for the day.
- `schedule_availability_id`: `Int64Bit` (required) - The ID of a `ScheduleAvailability`.
- `start_time`: `Time` - The start time for the day.
- `schedule_availability`: `ScheduleAvailability` - Availability for `Job`s to be scheduled.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleAvailabilityDayTimeConnection

**Description**: The connection wrapper around the `ScheduleAvailabilityDayTimeConnection` type.

**Category**: availability
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleAvailabilityDayTime` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ScheduleAvailabilityConnection

**Description**: The connection wrapper around the `ScheduleAvailabilityConnection` type.

**Category**: availability
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleAvailability` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Backup Entities (4 total)


### SystemBackup

**Description**: A backup of your Sonar instance's data.

**Category**: backup
**Relevance Score**: 15 (Primary: 5, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 9 (`id`, `password`, `status`, `system_backup_exports`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `password`: `Text` - A password.
- `status`: `SystemBackupStatus` (required) (enum) - The status.
- `system_backup_exports`: `SystemBackupExportConnection` (required) (connection) - A log of a system backup export attempt.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SystemBackupDestination

**Description**: A configured destination to export system backups to.

**Category**: backup
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `provider`

**Enum Fields**: 2 (`last_export_status`, `provider`)

**Relationship Fields**: 9 (`id`, `base_path`, `last_export_status`, `provider`, `system_backup_destination_credentials`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `base_path`: `Text` - The base path to the directory that the file will be stored in.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `last_export_at`: `Datetime` - When last system backup export was attempted.
- `last_export_status`: `SystemBackupExportStatus` (enum) - The status of the last system backup export.
- `provider`: `SystemBackupDestinationProvider` (required) (enum) - The service that a system backup will be exported to.
- `system_backup_destination_credentials`: `SystemBackupDestinationCredentialConnection` (required) (connection) - A credential used to authenticate against configured destinations to export system backups to.
- `system_backup_exports`: `SystemBackupExportConnection` (required) (connection) - A log of a system backup export attempt.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SystemBackupDestinationConnection

**Description**: The connection wrapper around the `SystemBackupDestinationConnection` type.

**Category**: backup
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SystemBackupDestination` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SystemBackupConnection

**Description**: The connection wrapper around the `SystemBackupConnection` type.

**Category**: backup
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SystemBackup` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Billing Entities (67 total)


### TaxProvider

**Description**: A tax provider.

**Category**: billing
**Relevance Score**: 16 (Primary: 4, Secondary: 2, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `name`, `tax_provider_credentials`

**Enum Fields**: 2 (`subdivisions`, `type`)

**Relationship Fields**: 8 (`id`, `subdivisions`, `type`, `tax_exemptions`, `tax_provider_credentials`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` (required) - A descriptive name.
- `subdivisions`: `Subdivision` (list) (enum) - The list of subdivisions where this tax provider will collect taxes.
- `type`: `TaxProviderType` (required) (enum) - The type.
- `tax_exemptions`: `TaxExemptionConnection` (required) (connection) - A tax exemption.
- `tax_provider_credentials`: `TaxProviderCredentialConnection` (required) (connection) - Credentials for a `TaxProvider`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Tax

**Description**: A tax.

**Category**: billing
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `name`, `tax_overrides`

**Enum Fields**: 2 (`application`, `type`)

**Relationship Fields**: 12 (`id`, `application`, `type`, `geo_tax_zones`, `service_taxes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `application`: `TaxApplication` (required) (enum) - Whether this `Tax` is applied as a percentage of the `Service` charge, or as a flat rate.
- `name`: `String` (required) - A descriptive name.
- `rate`: `Float` (required) - The rate for a tax. For a percentage based tax, this is a percentage. For a flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
- `type`: `TaxType` (required) (enum) - Whether this tax is applied based on the account being in a specific geography, or whether it is applied to all accounts.
- `geo_tax_zones`: `GeoTaxZoneConnection` (required) (connection) - A geographical tax zone.
- `service_taxes`: `ServiceTaxConnection` (required) (connection) - The relationship between a `Service` and a `Tax`.
- `tax_overrides`: `TaxOverrideConnection` (required) (connection) - An override to the default taxation rate.
- `voice_service_generic_parameter_taxes`: `VoiceServiceGenericParameterTaxConnection` (required) (connection) - The relationship between a `VoiceServiceGenericParameter` and a `Tax`.
- `vendors`: `VendorConnection` (required) (connection) - A third party vendor of inventory models.
- `purchase_order_items`: `PurchaseOrderItemConnection` (required) (connection) - A line item on a purchase order.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Payment

**Description**: A payment.

**Category**: billing
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 44

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `bank_account_id`, `company_id`, `credit_card_id`, `deposit_slip_id`, `payment_tracker_id`, `transaction_id`, `user_id`, `voided_payments`

**Enum Fields**: 2 (`payment_type`, `status`)

**Relationship Fields**: 22 (`id`, `account_id`, `bank_account_id`, `company_id`, `credit_card_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `amount`: `Int` (required) - The amount of the payment, in the smallest currency value.
- `amount_remaining`: `Int` (required) - The amount remaining that can be used.
- `bank_account_id`: `Int64Bit` - The ID of a BankAccount.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `creation_token`: `String` - A token sent to the payment provider during payment creation.
- `credit_card_id`: `Int64Bit` - The ID of a CreditCard.
- `deposit_slip_id`: `Int64Bit` - The deposit slip ID.
- `description`: `String` - A description of the payment, used for internal reference.
- `fee`: `Int` - The fee for this transaction.
- `fractional_fee`: `Int` - The fee for this transaction in fractional cents
- `full_processor_response`: `String` - The entire response back from the company that processed the transaction. Not typically human readable.
- `is_autopay`: `Boolean` - Whether or not this was an autopay payment.
- `passed_3ds_check`: `Boolean` - Whether or not this payment passed the 3DS security check.
- `passed_avs_check`: `Boolean` - Whether or not this payment passed the AVS security check.
- `passed_cvv_check`: `Boolean` - Whether or not this payment passed the CVV security check.
- `payment_datetime`: `Datetime` (required) - The date and time the payment was made.
- `payment_tracker_id`: `String` - The unique tracking ID for this payment.
- `payment_type`: `PaymentType` (required) (enum) - The type of payment (e.g. cash, credit card.)
- `processor_message`: `String` - The message returned back from the company that processed the transaction.
- `processor_status`: `String` - The status of the payment provided by the payment processor.
- `reference`: `String` - A payment reference like a check number, or wire transfer confirmation number.
- `status`: `PaymentStatus` (enum) - The status.
- `successful`: `Boolean` (required) - Whether or not this was successful.
- `transaction_id`: `String` - The transaction ID from the credit card provider.
- `user_id`: `Int64Bit` - The ID of a User.
- `credit_card`: `CreditCard` - A credit card.
- `bank_account`: `BankAccount` - A bank account.
- `account`: `Account` - A customer account.
- `company`: `Company` - A company you do business as.
- `deposit_slip`: `DepositSlip` - A deposit slip.
- `credits`: `CreditConnection` (required) (connection) - The application of a `Discount` or `Payment` against an `Invoice`.
- `disbursement_details`: `DisbursementDetailConnection` (required) (connection) - A disbursement detail.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `reversed_payments`: `ReversedPaymentConnection` (required) (connection) - A record a `Payment` reversal.
- `refunded_payments`: `RefundedPaymentConnection` (required) (connection) - A record of a refund applied to a `Payment`.
- `voided_payments`: `VoidedPaymentConnection` (required) (connection) - A record of a `Payment` that was voided.
- `disputes`: `DisputeConnection` (required) (connection) - A dispute.

---

### InvoiceTemplate

**Description**: A template for generating invoices.

**Category**: billing
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 7 (`id`, `invoice_template_versions`, `account_types`, `companies`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` (required) - A descriptive name.
- `protected`: `Boolean` (required) - If an item is protected, it cannot be modified or deleted.
- `with_remittance`: `String` - The content of an Invoice Template which includes a remittance slip.
- `without_remittance`: `String` - The content of an Invoice Template which does not include a remittance slip.
- `invoice_template_versions`: `InvoiceTemplateVersionConnection` (required) (connection) - A version of a template for generating invoices, preserved for historical purposes.
- `account_types`: `AccountTypeConnection` (required) (connection) - The account type.
- `companies`: `CompanyConnection` (required) (connection) - A company you do business as.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Invoice

**Description**: An invoice.

**Category**: billing
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 45

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `company_id`, `invoice_template_version_id`, `number_of_months`, `parent_invoice_id`, `pending_email`, `tax_provider_id`, `void`, `voided_at`, `tax_provider`

**Relationship Fields**: 21 (`id`, `account_id`, `company_id`, `invoice_template_version_id`, `message`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `auto_pay_attempts`: `Int` (required) - The number of times that autopay has been attempted.
- `auto_pay_date`: `Date` - The date that autopay will be attempted.
- `child_invoice_remaining_due`: `Int` (required) - The sum of all due amounts on child invoices.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `date`: `Date` (required) - A date
- `delinquency_date`: `Date` - The date that this became delinquent.
- `delinquent`: `Boolean` (required) - Whether or not this entity is delinquent.
- `due_date`: `Date` (required) - The date this invoice is due by.
- `end_date`: `Date` (required) - The date that this ends.
- `frozen`: `Boolean` (required) - If an invoice is frozen, payments will not be automatically applied to it, and it cannot be modified.
- `invoice_template_version_id`: `Int64Bit` - The ID of the Invoice Template Version which was active when this invoice was generated.
- `late_fee_applied`: `Boolean` (required) - Whether or not a late fee has been applied.
- `late_fee_only`: `Boolean` (required) - Whether or not the invoice includes only late fees.
- `message`: `Text` - The message.
- `number_of_months`: `Int` (required) - The number of months of service this invoice was billed for.
- `parent_invoice_id`: `Int64Bit` - The ID of the `Invoice` that is this `Invoice`s master.
- `pending_email`: `Boolean` (required) - Used by system to indicate the invoice has been marked to be sent to email contacts.
- `remaining_due`: `Int` (required) - The amount remaining to be paid.
- `status`: `String` (required) - The phase of the invoice moving through creation.
- `tax_committed`: `Boolean` (required) - Whether this entity's taxes have been committed or not.
- `tax_provider_id`: `Int64Bit` - The ID of an `TaxProvider`.
- `total_debits`: `Int` (required) - The sum of all debits that make up this invoice.
- `total_taxes`: `Int` (required) - The sum of all taxes on debits that make up this invoice.
- `void`: `Boolean` (required) - Whether or not this entity has been voided.
- `voided_at`: `Datetime` - When this was voided.
- `account`: `Account` - A customer account.
- `company`: `Company` - A company you do business as.
- `invoice_template_version`: `InvoiceTemplateVersion` - A version of a template for generating invoices, preserved for historical purposes.
- `tax_provider`: `TaxProvider` - A tax provider.
- `parent_invoice`: `Invoice` - The `Invoice` that is the parent of this `Invoice`.
- `debits`: `DebitConnection` (required) (connection) - A debit.
- `credits`: `CreditConnection` (required) (connection) - The application of a `Discount` or `Payment` against an `Invoice`.
- `child_invoices`: `InvoiceConnection` (required) (connection) - A list of `Invoice`s that this `Invoice` is a parent of.
- `print_to_mail_order_errors`: `PrintToMailOrderErrorConnection` (required) (connection) - An error associated with the print to mail order.
- `monthly_billing_completion`: `MonthlyBillingCompletion` - A record of a monthly billing cycle.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `print_to_mail_batches`: `PrintToMailBatchConnection` (required) (connection) - A batch of invoices to mail and print.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CorePayment

**Description**: A Sonar payment.

**Category**: billing
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 33

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `bank_account_id`, `company_id`, `credit_card_id`, `deposit_slip_id`, `payment_tracker_id`, `transaction_id`, `user_id`

**Enum Fields**: 2 (`payment_type`, `status`)

**Relationship Fields**: 11 (`id`, `account_id`, `bank_account_id`, `company_id`, `credit_card_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `amount`: `Int` (required) - The amount of the payment, in the smallest currency value.
- `amount_remaining`: `Int` (required) - The amount remaining that can be used.
- `bank_account_id`: `Int64Bit` - The ID of a BankAccount.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `creation_token`: `String` - A token sent to the payment provider during payment creation.
- `credit_card_id`: `Int64Bit` - The ID of a CreditCard.
- `deposit_slip_id`: `Int64Bit` - The deposit slip ID.
- `description`: `String` - A description of the payment, used for internal reference.
- `fee`: `Int` - The fee for this transaction.
- `fractional_fee`: `Int` - The fee for this transaction in fractional cents
- `full_processor_response`: `String` - The entire response back from the company that processed the transaction. Not typically human readable.
- `is_autopay`: `Boolean` - Whether or not this was an autopay payment.
- `passed_3ds_check`: `Boolean` - Whether or not this payment passed the 3DS security check.
- `passed_avs_check`: `Boolean` - Whether or not this payment passed the AVS security check.
- `passed_cvv_check`: `Boolean` - Whether or not this payment passed the CVV security check.
- `payment_datetime`: `Datetime` (required) - The date and time the payment was made.
- `payment_tracker_id`: `String` - The unique tracking ID for this payment.
- `payment_type`: `PaymentType` (required) (enum) - The type of payment (e.g. cash, credit card.)
- `processor_message`: `String` - The message returned back from the company that processed the transaction.
- `processor_status`: `String` - The status of the payment provided by the payment processor.
- `reference`: `String` - A payment reference like a check number, or wire transfer confirmation number.
- `status`: `PaymentStatus` (enum) - The status.
- `successful`: `Boolean` (required) - Whether or not this was successful.
- `transaction_id`: `String` - The transaction ID from the credit card provider.
- `user_id`: `Int64Bit` - The ID of a User.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Transaction

**Description**: types.transaction

**Category**: billing
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `account_id`, `sonar_unique_id`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 7 (`id`, `account_id`, `type`, `debit`, `discount`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `amount`: `Int` (required) - The type.
- `description`: `String` - A description for the transaction.
- `datetime`: `Datetime` - The date and time of the transaction.
- `running_balance`: `Int` (required) - The balance in relation to prior transactions.
- `type`: `TransactionType` (required) (enum) - The type of transaction this is.
- `tax_total`: `Int` (required) - The total of all taxes on this transaction.
- `debit`: `Debit` - A debit.
- `discount`: `Discount` - A discount.
- `payment`: `Payment` - A payment.
- `account`: `Account` (required) - A customer account.
- `successful`: `Boolean` - Whether or not this was successful.

---

### FractionalTaxTransaction

**Description**: A fractional tax transaction, stored to accurately calculate multi month billing.

**Category**: billing
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `tax_transaction_id`

**Relationship Fields**: 6 (`id`, `tax_transaction_id`, `tax_transaction`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `amount_taxed`: `Int` (required) - The amount of this `Debit` that was taxed.
- `date`: `Date` (required) - A date
- `description`: `String` (required) - A human readable description.
- `tax_transaction_id`: `Int64Bit` (required) - The ID of a `TaxTransactions`.
- `tax_transaction`: `TaxTransaction` - A tax transaction.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Debit

**Description**: A debit.

**Category**: billing
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 44

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `company_id`, `general_ledger_code`, `general_ledger_code_description`, `invoice_id`, `linked_debit_id`, `number_of_months`, `reversed_by_user_id`, `service_id`, `service_name`, `service_override_name`, `user_id`, `voice_service_generic_parameter_id`

**Enum Fields**: 2 (`service_transaction_type`, `type`)

**Relationship Fields**: 25 (`id`, `account_id`, `company_id`, `invoice_id`, `linked_debit_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `description`: `String` - A human readable description.
- `general_ledger_code`: `String` - A general ledger code.
- `general_ledger_code_description`: `String` - A general ledger code description.
- `invoice_id`: `Int64Bit` - The ID of an `Invoice`.
- `linked_debit_id`: `Int64Bit` - The ID of the Debit which is linked to the current Debit.
- `minutes`: `Float` - The total number of minutes.
- `number_of_months`: `Int` (required) - The number of months of service this invoice was billed for.
- `prorated_from`: `Date` - The date this transaction was prorated from.
- `prorated_to`: `Date` - The date this transaction was prorated to.
- `quantity`: `Int` (required) - The quantity for this service.
- `quantity_prorated_from`: `Int` - The quantity the associated service had before the quantity was changed and prorated.
- `quantity_prorated_to`: `Int` - The quantity the associated service was changed to when the quantity was changed and prorated.
- `reversed`: `Boolean` (required) - Whether or not this has been reversed.
- `reversed_at`: `Datetime` - When this was reversed.
- `reversed_by_user_id`: `Int64Bit` - The user ID that reversed this.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service_name`: `String` (required) - The name of a service.
- `service_override_name`: `String` - The override name of a service.
- `service_transaction_type`: `ServiceTransactionType` (enum) - The type of transaction on this service.
- `type`: `ServiceType` (required) (enum) - The type.
- `user_id`: `Int64Bit` - The ID of the user who created this transaction.
- `voice_service_generic_parameter_id`: `Int64Bit` - The ID of a voice service configuration parameter.
- `account`: `Account` - A customer account.
- `company`: `Company` - A company you do business as.
- `service`: `Service` - A service.
- `voice_service_generic_parameter`: `VoiceServiceGenericParameter` - A configurable attribute for a voice service.
- `invoice`: `Invoice` - An invoice.
- `user`: `User` - A user that can login to Sonar.
- `reversed_by_user`: `User` - The user that caused a reversal.
- `linked_debit`: `Debit` - The `Debit` linked to subsidy.
- `discount`: `Discount` - A discount.
- `data_usage_top_off`: `DataUsageTopOff` - A data usage top off.
- `tax_transactions`: `TaxTransactionConnection` (required) (connection) - A tax transaction.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `fractional_debits`: `FractionalDebitConnection` (required) (connection) - A fractional debit, stored to accurately calculate multi month billing.

---

### UsageBasedBillingPolicy

**Description**: A usage based billing policy.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 21

**Key Fields**: `id`, `sonar_unique_id`, `name`, `service_id`

**Relationship Fields**: 10 (`id`, `service_id`, `service`, `data_service_details`, `usage_based_billing_policy_free_periods`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `allow_purchase_of_additional_capacity_during_billing_period`: `Boolean` (required) - Whether or not a customer can purchase additional data usage capacity during a billing period.
- `assess_charges_at_end_of_billing_period`: `Boolean` (required) - Whether or not to assess charges for usage over the bandwidth limit at the end of the billing period.
- `cap_in_gigabytes`: `Int` (required) - The available data usage in this policy, measured in gigabytes.
- `name`: `String` (required) - A descriptive name.
- `rollover_enabled`: `Boolean` (required) - Whether or not rollover is enabled.
- `rollover_expiration_enabled`: `Boolean` - Whether or not rollover expiration is enabled.
- `rollover_expiration_months`: `Int` - Rollover expires after this many months, if rollover expiration is enabled.
- `service_id`: `Int64Bit` - The ID of a Service.
- `service`: `Service` - A service.
- `data_service_details`: `DataServiceDetailConnection` (required) (connection) - Details regarding a specific data `Service`.
- `usage_based_billing_policy_free_periods`: `UsageBasedBillingPolicyFreePeriodConnection` (required) (connection) - A period of free time in a `UsageBasedBillingPolicy`.
- `address_lists`: `AddressListConnection` (required) (connection) - An address list defines some criteria by which to group accounts for network policy enforcement.
- `radius_groups`: `RadiusGroupConnection` (required) (connection) - A RADIUS group.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TaxExemption

**Description**: A tax exemption.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `name`, `tax_provider_id`, `tax_provider`

**Enum Fields**: 1 (`jurisdictions`)

**Relationship Fields**: 10 (`id`, `account_id`, `jurisdictions`, `tax_provider_id`, `tax_provider`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `jurisdictions`: `TaxJurisdiction` (list) (enum) - The jurisdictions of this `TaxExemption`.
- `name`: `String` (required) - A descriptive name.
- `tax_provider_id`: `Int64Bit` (required) - The ID of an `TaxProvider`.
- `tax_provider`: `TaxProvider` - A tax provider.
- `account`: `Account` - A customer account.
- `avalara_tax_categories`: `AvalaraTaxCategoryConnection` (required) (connection) - A tax category defined by Avalara.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PurchaseOrder

**Description**: A purchase order for items from a third party vendor.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 35

**Key Fields**: `id`, `sonar_unique_id`, `approved_by_user_id`, `canceled_by_user_id`, `company_id`, `created_by_user_id`, `inventory_location_id`, `is_paid`, `order_group_id`, `order_number`, `vendor_id`, `vendor_name`, `emails`

**Enum Fields**: 3 (`currency`, `payment_terms`, `status`)

**Relationship Fields**: 25 (`id`, `approved_by_user_id`, `canceled_by_user_id`, `company_id`, `created_by_user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `approved_by_user_id`: `Int64Bit` - The ID of the user that approved this purchase order.
- `canceled_at`: `Datetime` - The date/time that this purchase order was cancelled.
- `canceled_by_user_id`: `Int64Bit` - The ID of the user that cancelled this purchase order.
- `company_id`: `Int64Bit` (required) - The ID of the company that will be used in the header of this purchase order.
- `created_by_user_id`: `Int64Bit` (required) - The ID of the user that created this purchase order.
- `currency`: `Currency` (enum) - The currency the system displays money in.
- `external_message`: `String` - A message to be included on purchase orders when sent to vendors.
- `inventory_location_id`: `Int64Bit` (required) - The source of the shipping address for a purchase order.
- `is_paid`: `Boolean` - Whether or not the purchase order has been marked as being paid.
- `last_status_change`: `Datetime` (required) - The date and time that the inventory item status last changed.
- `order_group_id`: `Int64Bit` - The ID of an order group related to this purchase order.
- `order_number`: `Int` - A unique number identifying an approved purchase order.
- `payment_terms`: `PaymentTerm` (enum) - The terms of payment for deliveries from this vendor.
- `status`: `PurchaseOrderStatus` (required) (enum) - The current status of this purchase order.
- `vendor_id`: `Int64Bit` (required) - The ID of a vendor.
- `vendor_name`: `String` - The name of a vendor.
- `canceled_by_user`: `User` - The ID of the user that canceled this purchase order.
- `created_by_user`: `User` - The ID of the user that created this entity.
- `approved_by_user`: `User` - The ID of the user that approved this purchase order.
- `vendor`: `Vendor` - A third party vendor of inventory models.
- `inventory_location`: `InventoryLocation` - A location that inventory is stored in.
- `company`: `Company` - A company you do business as.
- `order_group`: `OrderGroup` - An order group.
- `purchase_order_items`: `PurchaseOrderItemConnection` (required) (connection) - A line item on a purchase order.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InvoiceMessage

**Description**: A message that is appended to specific invoices.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `account_types`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `message`: `String` (required) - The message.
- `name`: `String` (required) - A descriptive name.
- `account_types`: `AccountTypeConnection` (required) (connection) - The account type.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InvoiceAttachment

**Description**: A PDF to attach to invoices.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `notes`, `files`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `end`: `Date` - The date to stop attaching this PDF to invoices.
- `name`: `String` (required) - A descriptive name.
- `start`: `Date` - The date to start attaching this PDF to invoices.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GeoTaxZone

**Description**: A geographical tax zone.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `name`, `tax_id`

**Enum Fields**: 3 (`country`, `county`, `subdivision`)

**Relationship Fields**: 10 (`id`, `country`, `county`, `subdivision`, `tax_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `city`: `String` - A city.
- `country`: `Country` (enum) - A two character country code.
- `county`: `UsCounty` (enum) - A US county. Only used for US addresses.
- `name`: `String` (required) - A descriptive name.
- `rate`: `Float` (required) - The rate.
- `subdivision`: `Subdivision` (enum) - A state, province, or other country subdivision.
- `tax_id`: `Int64Bit` (required) - The ID of a Tax.
- `zip`: `String` - A ZIP or postal code.
- `zip_partial_match`: `Boolean` (required) - Whether to match on partial ZIP/postal codes.
- `tax`: `Tax` - A tax.
- `accounts`: `AccountConnection` (required) (connection) - A customer account.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Dispute

**Description**: A dispute.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `case_id`, `external_id`, `payment_id`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 9 (`id`, `payment_id`, `reason`, `status`, `payment`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `case_id`: `String` - The dispute's case ID.
- `cycle`: `String` - The current dispute cycle.
- `dispute_date`: `Date` (required) - The date the dispute was issued.
- `external_id`: `String` (required) - The payment processor's external ID.
- `payment_id`: `Int64Bit` (required) - The ID of a `Payment`.
- `reason`: `Text` - The reason.
- `reply_by_date`: `Date` - The date the dispute must be replied to by.
- `status`: `DisputeStatus` (required) (enum) - The status.
- `payment`: `Payment` - A payment.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### BillingDefault

**Description**: Default billing settings that are applied to some accounts on creation.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 42

**Key Fields**: `id`, `sonar_unique_id`, `account_type_id`, `anchor_default_id`, `delinquency_account_status_id`, `delinquency_removal_account_status_id`, `name`

**Enum Fields**: 6 (`anchor_delinquency_logic`, `auto_pay_day`, `bill_day_mode`, `bill_mode`, `default_for`, `due_days_day`)

**Relationship Fields**: 20 (`id`, `account_type_id`, `anchor_default_id`, `anchor_delinquency_logic`, `auto_pay_day`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_type_id`: `Int64Bit` - The ID of an AccountType.
- `aggregate_invoice_taxes`: `Boolean` (required) - Whether or not to aggregate invoice taxes instead of printing with each charge.
- `aggregate_linked_debits`: `Boolean` (required) - Whether or not to aggregate linked debits on Anchor invoices.
- `anchor_default_id`: `Int64Bit` - The ID of a BillingDefault acting as an Anchor default.
- `anchor_delinquency_logic`: `AnchorDelinquencyLogic` (enum) - Determines if delinquency settings on an Anchor default is applied only to the Anchor account or the Linked accounts as well.
- `auto_pay_day`: `BillingParameterDayOption` (required) (enum) - If `invoice_day` is not null, this allows you to select whether `auto_pay_days` is calculated from the billing day, or the invoice day.
- `auto_pay_days`: `Int` (required) - The number of days after `auto_pay_day` that autopay runs for an invoice.
- `bill_day`: `Int` - The day that billing runs.
- `bill_day_mode`: `BillDayModeOption` (required) (enum) - Whether the account bill and invoice day are fixed, the account activation day is used as bill day, or the account activation day is used as the invoice day.
- `bill_mode`: `BillMode` (required) (enum) - The type of bill this account receives.
- `days_of_delinquency_for_status_switch`: `Int` - If `switch_status_after_delinquency` is `true`, then this is the number of days of delinquency to allow before the status switch.
- `default`: `Boolean` (required) - If this is `true`, then this is the default billing default that is used, if there is no more specific billing default option for an account.
- `default_for`: `BillingDefaultFor` (required) (enum) - Determines if the billing parameters apply by account type or for anchor / linked types.
- `delinquency_account_status_id`: `Int64Bit` - If `switch_status_after_delinquency` is true, this is the account status that the account will be moved into after `days_of_delinquency_for_status_switch` days of delinquency.
- `delinquency_removal_account_status_id`: `Int64Bit` - If `switch_status_after_delinquency` is `true`, then this is the status the account will be moved back into if delinquency is cleared while the account is set to the `delinquency_account_status_id` account status.
- `due_days`: `Int` (required) - The number of days after the invoice date that it is due.
- `due_days_day`: `BillingParameterDayOption` (required) (enum) - If `invoice_day` is not null, this allows you to select whether `due_days` is calculated from the billing day, or the invoice day.
- `fixed_bill_day`: `Boolean` - Whether or not to use a fixed bill day, versus anniversary day billing. Use `bill_day_mode` for further customization.
- `grace_days`: `Int` (required) - The number of days after the invoice due date that the invoice is marked delinquent.
- `invoice_day`: `Int` - The day that automatic billing invoices are generated for. If this is `null`, then `bill_day` is used.
- `lifeline`: `Boolean` (required) - Whether or not this account participates in the federal Lifeline program.
- `months_to_bill`: `Int` (required) - The number of months to bill at a time.
- `name`: `String` (required) - A descriptive name.
- `print_invoice`: `Boolean` (required) - Whether this account receives a printed invoice.
- `service_period_duration`: `Int` - The length of the service period in days when using a Flexible Bill Day Mode.
- `service_period_offset`: `Int` - The offset between the service period and the billing period in days when using a Flexible Bill Day Mode.
- `switch_status_after_delinquency`: `Boolean` (required) - Whether or not this account should be moved into another status after being delinquent for a preset period.
- `tax_exempt`: `Boolean` (required) - Whether or not this account is tax exempt.
- `delinquency_account_status`: `AccountStatus` - The status that an `Account` is moved into after a certain length of delinquency.
- `delinquency_removal_account_status`: `AccountStatus` - The `AccountStatus` an account is moved back into after no longer being delinquent, if it is currently in the delinquency account status defined on the `AccountBillingParameter`.
- `account_type`: `AccountType` - The account type.
- `billing_default`: `BillingDefault` - Default billing settings that are applied to some accounts on creation.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `account_billing_parameters`: `AccountBillingParameterConnection` (required) (connection) - Parameters that define the billing settings for an `Account`.
- `billing_services`: `BillingServiceConnection` (required) (connection) - The service items and overrides for linked billing defaults.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AvalaraTaxCategory

**Description**: A tax category defined by Avalara.

**Category**: billing
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `tax_exemptions`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `value`: `Int` (required) - The value.
- `tax_exemptions`: `TaxExemptionConnection` (required) (connection) - A tax exemption.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoidedPayment

**Description**: A record of a `Payment` that was voided.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `payment_id`, `payment_tracker_id`, `transaction_id`, `user_id`

**Relationship Fields**: 9 (`id`, `payment_id`, `user_id`, `payment`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `description`: `String` - A human readable description.
- `payment_id`: `Int64Bit` (required) - The ID of a `Payment`.
- `payment_tracker_id`: `String` - The unique tracking ID for this payment.
- `processor_response_message`: `String` - The response from the payment processor when this payment was submitted.
- `transaction_id`: `String` - The transaction ID from the credit card provider.
- `user_id`: `Int64Bit` - The ID of a User.
- `payment`: `Payment` - A payment.
- `user`: `User` - A user that can login to Sonar.
- `disbursement_details`: `DisbursementDetailConnection` (required) (connection) - A disbursement detail.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TaxTransaction

**Description**: A tax transaction.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `tax_provider_id`, `taxdefinitionable_id`, `taxtransactionable_id`, `tax_provider`

**Enum Fields**: 2 (`taxdefinitionable_type`, `taxtransactionable_type`)

**Relationship Fields**: 13 (`id`, `description`, `tax_provider_id`, `taxdefinitionable_id`, `taxdefinitionable_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `amount_taxed`: `Int` (required) - The amount of this `Debit` that was taxed.
- `description`: `Text` (required) - A human readable description.
- `tax_provider_id`: `Int64Bit` - The ID of an `TaxProvider`.
- `taxdefinitionable_id`: `Int64Bit` - The ID of entity this tax definition is related to.
- `taxdefinitionable_type`: `TaxdefinitionableType` (enum) - The type of entity this tax definition is related to.
- `taxtransactionable_id`: `Int64Bit` (required) - The ID of the entity this tax transaction is related to.
- `taxtransactionable_type`: `TaxtransactionableType` (required) (enum) - The type of entity this tax transaction is related to.
- `tax_provider`: `TaxProvider` - A tax provider.
- `taxtransactionable`: `TaxtransactionableInterface` - The entity that this `TaxTransaction` was generated for.
- `taxdefinitionable`: `TaxdefinitionableInterface` - The entity that this `TaxDefinition` is assigned to.
- `fractional_tax_transactions`: `FractionalTaxTransactionConnection` (required) (connection) - A fractional tax transaction, stored to accurately calculate multi month billing.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ReversedPayment

**Description**: A record a `Payment` reversal.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `payment_id`, `user_id`

**Relationship Fields**: 8 (`id`, `payment_id`, `user_id`, `payment`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `description`: `String` - A human readable description.
- `payment_id`: `Int64Bit` (required) - The ID of a `Payment`.
- `user_id`: `Int64Bit` - The ID of a User.
- `payment`: `Payment` - A payment.
- `user`: `User` - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RefundedPayment

**Description**: A record of a refund applied to a `Payment`.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `payment_id`, `payment_tracker_id`, `transaction_id`, `user_id`

**Relationship Fields**: 9 (`id`, `payment_id`, `user_id`, `payment`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `description`: `String` - A human readable description.
- `payment_id`: `Int64Bit` (required) - The ID of a `Payment`.
- `payment_tracker_id`: `String` - The unique tracking ID for this payment.
- `processor_response_message`: `String` - The response from the payment processor when this payment was submitted.
- `transaction_id`: `String` - The transaction ID from the credit card provider.
- `transaction_successful`: `Boolean` - Whether or not the refund transaction was successful.
- `user_id`: `Int64Bit` - The ID of a User.
- `payment`: `Payment` - A payment.
- `user`: `User` - A user that can login to Sonar.
- `disbursement_details`: `DisbursementDetailConnection` (required) (connection) - A disbursement detail.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PrintedInvoiceBatch

**Description**: A single PDF containing multiple invoices for printing.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `user_id`

**Relationship Fields**: 7 (`id`, `user_id`, `user`, `notes`, `files`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `date`: `Date` (required) - A date
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### MonthlyBillingCompletion

**Description**: A record of a monthly billing cycle.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `invoice_id`

**Relationship Fields**: 9 (`id`, `account_id`, `invoice_id`, `account`, `invoice`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `date`: `Date` (required) - A date
- `invoice_id`: `Int64Bit` (required) - The ID of an `Invoice`.
- `account`: `Account` - A customer account.
- `invoice`: `Invoice` - An invoice.
- `call_detail_records`: `CallDetailRecordConnection` (required) (connection) - A call detail record (CDR).
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### FractionalDebit

**Description**: A fractional debit, stored to accurately calculate multi month billing.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `debit_id`

**Relationship Fields**: 6 (`id`, `debit_id`, `debit`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `date`: `Date` (required) - A date
- `debit_id`: `Int64Bit` (required) - The ID of a `Debit`.
- `debit`: `Debit` - A debit.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CreditCardProcessor

**Description**: A company that processes `CreditCard` transactions.

**Category**: billing
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 26

**Key Fields**: `id`, `sonar_unique_id`, `provider`

**Enum Fields**: 1 (`provider`)

**Relationship Fields**: 8 (`id`, `provider`, `credit_card_processor_credentials`, `credit_cards`, `disbursements`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amex`: `Boolean` (required) - American Express.
- `dankort`: `Boolean` (required) - Dankort.
- `dinersclub`: `Boolean` (required) - Diner's Club.
- `discover`: `Boolean` (required) - Discover.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `forbrugsforeningen`: `Boolean` (required) - Forbrugsforeningen.
- `jcb`: `Boolean` (required) - JCB
- `maestro`: `Boolean` (required) - Maestro.
- `mastercard`: `Boolean` (required) - MasterCard.
- `moto_enabled`: `Boolean` (required) - Enables processor specific `Mail Or Telephone Order` functionality. Currently only applicable for `Stripe`.
- `primary`: `Boolean` (required) - Whether or not this is the primary type of entity.
- `provider`: `CreditCardProvider` (required) (enum) - The company that provides credit card processing services.
- `unionpay`: `Boolean` (required) - Union Pay.
- `visa`: `Boolean` (required) - Visa
- `visaelectron`: `Boolean` (required) - VISA Electron.
- `credit_card_processor_credentials`: `CreditCardProcessorCredentialConnection` (required) (connection) - Credentials for a `CreditCardProcessor`.
- `credit_cards`: `CreditCardConnection` (required) (connection) - A credit card.
- `disbursements`: `DisbursementConnection` (required) (connection) - A disbursement.
- `companies`: `CompanyConnection` (required) (connection) - A company you do business as.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### UsageBasedBillingPolicyFreePeriod

**Description**: A period of free time in a `UsageBasedBillingPolicy`.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `usage_based_billing_policy_id`

**Enum Fields**: 1 (`day`)

**Relationship Fields**: 7 (`id`, `day`, `usage_based_billing_policy_id`, `usage_based_billing_policy`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `day`: `Day` (required) (enum) - A day.
- `end`: `Time` (required) - The end.
- `start`: `Time` (required) - The start.
- `usage_based_billing_policy_id`: `Int64Bit` (required) - The ID of a `UsageBasedBillingPolicy`.
- `usage_based_billing_policy`: `UsageBasedBillingPolicy` - A usage based billing policy.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TaxProviderCredential

**Description**: Credentials for a `TaxProvider`.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `tax_provider_id`, `tax_provider`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 7 (`id`, `credential`, `tax_provider_id`, `tax_provider`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `TaxProviderCredentialType` (required) (enum) - The credential name.
- `tax_provider_id`: `Int64Bit` (required) - The ID of an `TaxProvider`.
- `value`: `String` (required) - The value.
- `tax_provider`: `TaxProvider` - A tax provider.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TaxOverride

**Description**: An override to the default taxation rate.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `tax_id`

**Relationship Fields**: 8 (`id`, `account_id`, `tax_id`, `account`, `tax`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `rate`: `Float` (required) - The rate.
- `tax_id`: `Int64Bit` (required) - The ID of a Tax.
- `account`: `Account` - A customer account.
- `tax`: `Tax` - A tax.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PrintToMailOrderError

**Description**: An error associated with the print to mail order.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `invoice_id`, `print_to_mail_order_id`

**Enum Fields**: 1 (`error_type`)

**Relationship Fields**: 8 (`id`, `error_type`, `invoice_id`, `print_to_mail_order_id`, `print_to_mail_order`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `error_message`: `String` (required) - An error message associated with a print to mail order.
- `error_type`: `PrintToMailOrderErrorType` (required) (enum) - The error type.
- `invoice_id`: `Int64Bit` - The ID of the invoice that has the error.
- `print_to_mail_order_id`: `Int64Bit` (required) - The print to mail order ID.
- `resolved`: `Boolean` (required) - Whether or not the error has been marked as resolved.
- `print_to_mail_order`: `PrintToMailOrder` - The print to mail order.
- `invoice`: `Invoice` - An invoice.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InvoiceTemplateVersion

**Description**: A version of a template for generating invoices, preserved for historical purposes.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `invoice_template_id`

**Relationship Fields**: 7 (`id`, `invoice_template_id`, `invoice_template`, `invoices`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `invoice_template_id`: `Int64Bit` - The ID of an Invoice Template.
- `with_remittance`: `String` (required) - The content of an Invoice Template which includes a remittance slip.
- `without_remittance`: `String` (required) - The content of an Invoice Template which does not include a remittance slip.
- `invoice_template`: `InvoiceTemplate` - A template for generating invoices.
- `invoices`: `InvoiceConnection` (required) (connection) - An invoice.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CreditCardProcessorCredential

**Description**: Credentials for a `CreditCardProcessor`.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `credit_card_processor_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 6 (`id`, `credential`, `credit_card_processor_id`, `credit_card_processor`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `CreditCardProviderCredential` (required) (enum) - The credential name.
- `credit_card_processor_id`: `Int64Bit` (required) - The ID of a CreditCardProcessor.
- `value`: `String` (required) - The value.
- `credit_card_processor`: `CreditCardProcessor` - A company that processes `CreditCard` transactions.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CreditCard

**Description**: A credit card.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 24

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `credit_card_processor_id`, `customer_profile_id`, `masked_number`, `name_on_card`, `token_id`

**Enum Fields**: 2 (`card_payment_type`, `credit_card_type`)

**Relationship Fields**: 12 (`id`, `account_id`, `card_payment_type`, `credit_card_processor_id`, `credit_card_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `auto`: `Boolean` (required) - Whether or not this payment method is enabled for automatic payments.
- `card_payment_type`: `CardPaymentType` (enum) - The type of payment made by the card (e.g. Credit, Debit, Prepaid).
- `credit_card_processor_id`: `Int64Bit` (required) - The ID of a CreditCardProcessor.
- `credit_card_type`: `CreditCardType` (required) (enum) - The type of a credit card (e.g. Visa, Mastercard.)
- `customer_profile_id`: `String` - The profile ID provided by a credit card processing service.
- `expiration_month`: `Int` (required) - The month the credit card expires.
- `expiration_year`: `Int` (required) - The year the credit card expires.
- `masked_number`: `String` (required) - A partial credit card number that can be used for identification.
- `name_on_card`: `String` - The name on the credit card.
- `token`: `String` (required) - The tokenized value that represents a credit card, provided by a credit card processing service.
- `token_id`: `String` - The tokenized credit card ID
- `account`: `Account` - A customer account.
- `credit_card_processor`: `CreditCardProcessor` - A company that processes `CreditCard` transactions.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `payments`: `PaymentConnection` (required) (connection) - A payment.

---

### Credit

**Description**: The application of a `Discount` or `Payment` against an `Invoice`.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `creditable_id`, `invoice_id`, `void`, `voided_at`

**Enum Fields**: 1 (`creditable_type`)

**Relationship Fields**: 10 (`id`, `account_id`, `creditable_id`, `creditable_type`, `invoice_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `creditable_id`: `Int64Bit` (required) - The ID the transaction that created this credit.
- `creditable_type`: `CreditableType` (required) (enum) - The type of transaction that created this credit.
- `invoice_id`: `Int64Bit` (required) - The ID of an `Invoice`.
- `void`: `Boolean` (required) - Whether or not this entity has been voided.
- `voided_at`: `Datetime` - When this was voided.
- `account`: `Account` - A customer account.
- `invoice`: `Invoice` - An invoice.
- `creditable`: `CreditableInterface` - The entity this `Credit` is associated with.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CoreCreditCard

**Description**: A Sonar credit card.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `credit_card_processor_id`, `customer_profile_id`, `masked_number`, `name_on_card`, `token_id`

**Enum Fields**: 2 (`card_payment_type`, `credit_card_type`)

**Relationship Fields**: 7 (`id`, `account_id`, `card_payment_type`, `credit_card_processor_id`, `credit_card_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `auto`: `Boolean` (required) - Whether or not this payment method is enabled for automatic payments.
- `card_payment_type`: `CardPaymentType` (enum) - The type of payment made by the card (e.g. Credit, Debit, Prepaid).
- `credit_card_processor_id`: `Int64Bit` (required) - The ID of a CreditCardProcessor.
- `credit_card_type`: `CreditCardType` (required) (enum) - The type of a credit card (e.g. Visa, Mastercard.)
- `customer_profile_id`: `String` - The profile ID provided by a credit card processing service.
- `expiration_month`: `Int` (required) - The month the credit card expires.
- `expiration_year`: `Int` (required) - The year the credit card expires.
- `masked_number`: `String` (required) - A partial credit card number that can be used for identification.
- `name_on_card`: `String` - The name on the credit card.
- `token`: `String` (required) - The tokenized value that represents a credit card, provided by a credit card processing service.
- `token_id`: `String` - The tokenized credit card ID
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### BillingSetting

**Description**: Billing configuration settings.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 58

**Key Fields**: `id`, `sonar_unique_id`, `delinquency_check_day_friday`, `disconnect_account_status_id`, `invoice_and_email_late_fees_immediately`, `late_fee_service_id`, `printed_invoice_fee_service_id`, `unarchive_account_status_id`

**Enum Fields**: 2 (`accounting_period_auto_close`, `late_fee_mode`)

**Relationship Fields**: 14 (`id`, `accounting_period_auto_close`, `disconnect_account_status_id`, `late_fee_mode`, `late_fee_service_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `accounting_period_auto_close`: `AccountingPeriodCloseOption` (required) (enum) - How often the accounting period automatically closes.
- `accounting_period_close_date`: `Date` - The date that the accounting period was closed.
- `always_round_taxes_up`: `Boolean` (required) - Always round taxes up.
- `apply_late_fees`: `Boolean` (required) - Whether or not to apply a late fee to past due invoices.
- `apply_late_fees_to_child_invoices`: `Boolean` (required) - Whether late fees should be applied to child invoices.
- `autopay_bank_account_attempts`: `Int` (required) - The number of times to attempt a bank account automatic payment.
- `autopay_bank_account_retry_interval_in_days`: `Int` (required) - The number of days between retries for bank account automatic payments.
- `autopay_credit_card_attempts`: `Int` (required) - The number of times to attempt a credit card automatic payment.
- `autopay_credit_card_retry_interval_in_days`: `Int` (required) - The number of days between retries for credit card automatic payments.
- `autopay_disconnect_invoice`: `Boolean` - Autopay the account disconnect invoice.
- `autopay_disconnect_invoice_days`: `Int` - The number of days between invoice date and the Autopay date.
- `autopay_initial_invoice`: `Boolean` - Autopay the initial invoice.
- `autopay_initial_invoice_days`: `Int` - The number of days between invoice date and the Autopay date.
- `autopay_runs_entire_amount_due`: `Boolean` (required) - Whether the automatic payment process should just run the invoice amount, or the entire amount due on the account.
- `daily_billing`: `Boolean` (required) - Whether or not the daily billing process is enabled.
- `days_after_invoice_due_for_late_fee_application`: `Int` - The number of days after the due date on a delinquent invoice for a late fee to be applied.
- `delete_expired_credit_cards`: `Boolean` (required) - Whether or not to delete expired credit cards from Sonar.
- `delinquency_check_day_friday`: `Boolean` (required) - Friday.
- `delinquency_check_day_monday`: `Boolean` (required) - Monday.
- `delinquency_check_day_saturday`: `Boolean` (required) - Saturday.
- `delinquency_check_day_sunday`: `Boolean` (required) - Sunday.
- `delinquency_check_day_thursday`: `Boolean` (required) - Thursday.
- `delinquency_check_day_tuesday`: `Boolean` (required) - Tuesday.
- `delinquency_check_day_wednesday`: `Boolean` (required) - Wednesday.
- `disconnect_account_status_id`: `Int64Bit` (required) - The `AccountStatus` for disconnected accounts.
- `exclude_inactive_accounts_from_late_fees`: `Boolean` (required) - Whether to exclude inactive accounts from late fee application.
- `generate_invoice_on_initial_activation`: `Boolean` (required) - Generate an invoice on an account when it is first activated, if there are any uninvoiced debits.
- `include_late_fee_invoices_in_printed_batches`: `Boolean` (required) - Whether or not to include late fee invoices in printed batches.
- `invoice_and_email_late_fees_immediately`: `Boolean` (required) - Whether to invoice and email late fees immediately, or add them to the next invoice.
- `late_fee_minimum_delinquency_amount`: `Int` - The minimum amount an invoice must be past due for a late fee to be applied.
- `late_fee_mode`: `LateFeeMode` (required) (enum) - The mode for late fee application.
- `late_fee_percentage`: `Float` - If late fees are applied as a percentage, the percentage of the past due balance to apply.
- `late_fee_service_id`: `Int64Bit` - The ID of a one time `Service` to use for late fee application.
- `minimum_amount_due_for_delinquency`: `Int` (required) - The minimum account an invoice must be delinquent for before being flagged delinquent.
- `minimum_bank_account_payment`: `Int` (required) - The smallest bank account payment amount allowed.
- `minimum_credit_card_payment`: `Int` (required) - The smallest credit card payment amount allowed.
- `printed_invoice_batch_duplex`: `Boolean` (required) - Printed invoice batch duplex.
- `printed_invoice_fee_service_id`: `Int64Bit` - The service ID of a one time `Service` to charge for accounts with `print_invoice` enabled in their `AccountBillingParameter`.
- `prorate_account_delinquency_status_change`: `Boolean` - Whether or not an account going delinquent or no longer delinquent is prorated by default.
- `prorate_account_status_change`: `Boolean` (required) - Whether or not changing the status from an active to inactive status is prorated by default.
- `prorate_billing_day_change`: `Boolean` (required) - Whether or not changing an account bill day is prorated by default.
- `prorate_service_quantity`: `Boolean` (required) - Whether or not service quantity changes are prorated by default.
- `prorate_services`: `Boolean` (required) - Whether or not service addition and removal is prorated by default.
- `round_prorated_amounts`: `Boolean` (required) - Whether or not to round prorated transactions to the nearest major unit (e.g. to the nearest dollar, euro, pound, etc.)
- `unarchive_account_status_id`: `Int64Bit` - The `AccountStatus` for unarchived accounts.
- `use_invoice_templates`: `Boolean` (required) - Use modular invoice templates for all invoices.
- `late_fee_service`: `Service` - The service used for late fee application.
- `printed_invoice_service`: `Service` - The service used for printed invoices.
- `disconnect_account_status`: `AccountStatus` - The account status used when moving accounts into the post-delinquency state.
- `unarchive_account_status`: `AccountStatus` - The account status used when unarchiving accounts.
- `account_types`: `AccountTypeConnection` (required) (connection) - The account type.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AvalaraTaxDefinition

**Description**: A tax Transaction/Service pair defined by Avalara.

**Category**: billing
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `service_name`, `transaction_name`

**Relationship Fields**: 4 (`id`, `service_tax_definitions`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `archived`: `Boolean` (required) - Whether or not this entity is archived.
- `is_custom`: `Boolean` (required) - Whether or not this tax definition is custom.
- `service_name`: `String` (required) - The service name as defined by Avalara.
- `service_type`: `Int` (required) - The service type as defined by Avalara.
- `transaction_name`: `String` (required) - The transaction name as defined by Avalara.
- `transaction_type`: `Int` (required) - The transaction type as defined by Avalara.
- `service_tax_definitions`: `ServiceTaxDefinitionConnection` (required) (connection) - The relationship between a `Service` and a `TaxDefinition`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoidedPaymentConnection

**Description**: The connection wrapper around the `VoidedPaymentConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoidedPayment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### UsageBasedBillingPolicyFreePeriodConnection

**Description**: The connection wrapper around the `UsageBasedBillingPolicyFreePeriodConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `UsageBasedBillingPolicyFreePeriod` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### UsageBasedBillingPolicyConnection

**Description**: The connection wrapper around the `UsageBasedBillingPolicyConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `UsageBasedBillingPolicy` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaxTransactionConnection

**Description**: The connection wrapper around the `TaxTransactionConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaxTransaction` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaxProviderCredentialConnection

**Description**: The connection wrapper around the `TaxProviderCredentialConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaxProviderCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaxProviderConnection

**Description**: The connection wrapper around the `TaxProviderConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaxProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaxOverrideConnection

**Description**: The connection wrapper around the `TaxOverrideConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaxOverride` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaxExemptionConnection

**Description**: The connection wrapper around the `TaxExemptionConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaxExemption` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaxConnection

**Description**: The connection wrapper around the `TaxConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Tax` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ReversedPaymentConnection

**Description**: The connection wrapper around the `ReversedPaymentConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ReversedPayment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RefundedPaymentConnection

**Description**: The connection wrapper around the `RefundedPaymentConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RefundedPayment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PrintedInvoiceBatchConnection

**Description**: The connection wrapper around the `PrintedInvoiceBatchConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PrintedInvoiceBatch` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PaymentConnection

**Description**: The connection wrapper around the `PaymentConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Payment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### MonthlyBillingCompletionConnection

**Description**: The connection wrapper around the `MonthlyBillingCompletionConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `MonthlyBillingCompletion` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InvoiceTemplateVersionConnection

**Description**: The connection wrapper around the `InvoiceTemplateVersionConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InvoiceTemplateVersion` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InvoiceTemplateConnection

**Description**: The connection wrapper around the `InvoiceTemplateConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InvoiceTemplate` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InvoiceMessageConnection

**Description**: The connection wrapper around the `InvoiceMessageConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InvoiceMessage` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InvoiceConnection

**Description**: The connection wrapper around the `InvoiceConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Invoice` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InvoiceAttachmentConnection

**Description**: The connection wrapper around the `InvoiceAttachmentConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InvoiceAttachment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GeoTaxZoneConnection

**Description**: The connection wrapper around the `GeoTaxZoneConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GeoTaxZone` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### FractionalTaxTransactionConnection

**Description**: The connection wrapper around the `FractionalTaxTransactionConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `FractionalTaxTransaction` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### FractionalDebitConnection

**Description**: The connection wrapper around the `FractionalDebitConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `FractionalDebit` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DebitConnection

**Description**: The connection wrapper around the `DebitConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Debit` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CreditConnection

**Description**: The connection wrapper around the `CreditConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Credit` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CreditCardProcessorCredentialConnection

**Description**: The connection wrapper around the `CreditCardProcessorCredentialConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CreditCardProcessorCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CreditCardProcessorConnection

**Description**: The connection wrapper around the `CreditCardProcessorConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CreditCardProcessor` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CreditCardConnection

**Description**: The connection wrapper around the `CreditCardConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CreditCard` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### BillingDefaultConnection

**Description**: The connection wrapper around the `BillingDefaultConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `BillingDefault` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AvalaraTaxDefinitionConnection

**Description**: The connection wrapper around the `AvalaraTaxDefinitionConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AvalaraTaxDefinition` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AvalaraTaxCategoryConnection

**Description**: The connection wrapper around the `AvalaraTaxCategoryConnection` type.

**Category**: billing
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AvalaraTaxCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Configuration Entities (8 total)


### SmsSetting

**Description**: SMS configuration settings.

**Category**: configuration
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 4 (`id`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `auto_pay`: `Boolean` (required) - Whether the SMS funds are paid for automatically.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `low_funds_threshold`: `Int` (required) - A notification is sent if SMS funds fall below this value.
- `triggered_quiet_end_time`: `Time` - End of quiet time for sending SMS triggered messages.
- `triggered_quiet_start_time`: `Time` - Start of quiet time for sending SMS triggered messages.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PrintToMailSetting

**Description**: Print to mail configuration settings.

**Category**: configuration
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`

**Enum Fields**: 2 (`print_method`, `print_type`)

**Relationship Fields**: 5 (`id`, `print_method`, `print_type`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `auto_pay`: `Boolean` (required) - Whether the print to mail orders are paid for automatically.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `low_funds_threshold`: `Int` (required) - A notification is sent if Print to Mail funds fall below this value.
- `print_method`: `PrintToMailPrintMethod` (required) (enum) - The print method for the print to mail batch.
- `print_type`: `PrintToMailPrintType` (required) (enum) - The print type for the print to mail batch.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CalixCloudSetting

**Description**: A Calix Cloud setting.

**Category**: configuration
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 30

**Key Fields**: `id`, `sonar_unique_id`, `client_id`, `company_id`, `subscriber_field1_id`, `subscriber_field2_id`, `subscriber_field3_id`, `subscriber_field4_id`, `subscriber_field5_id`

**Enum Fields**: 3 (`subscriber_location`, `subscriber_region`, `synchronization_status`)

**Relationship Fields**: 18 (`id`, `company_id`, `service_group_tiers`, `subscriber_field1_id`, `subscriber_field2_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `client_id`: `String` (required) - The Auth0 client ID.
- `client_secret`: `String` (required) - The Auth0 client secret.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `service_group_tiers`: `Text` - An array of Calix service group definitions.
- `subscriber_field1_id`: `Int64Bit` - The ID of a `CustomField` that will map to Calix subscriber field1.
- `subscriber_field2_id`: `Int64Bit` - The ID of a `CustomField` that will map to Calix subscriber field2.
- `subscriber_field3_id`: `Int64Bit` - The ID of a `CustomField` that will map to Calix subscriber field3.
- `subscriber_field4_id`: `Int64Bit` - The ID of a `CustomField` that will map to Calix subscriber field4.
- `subscriber_field5_id`: `Int64Bit` - The ID of a `CustomField` that will map to Calix subscriber field5.
- `subscriber_location`: `CalixSubscriberAreaType` (enum) - The area type to be used for the location.
- `subscriber_region`: `CalixSubscriberAreaType` (enum) - The area type to be used for the region.
- `synchronization_audit_ran`: `Boolean` (required) - Whether or not a synchronization audit has been run.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `synchronization_status`: `SynchronizationStatus` (required) (enum) - Status of the synchronization process.
- `synchronization_status_message`: `String` - Details regarding the current synchronization status if any.
- `company`: `Company` - A company you do business as.
- `custom_field`: `CustomField` - A user defined field.
- `calix_cloud_audits`: `CalixCloudAuditConnection` (required) (connection) - A Calix Cloud audit record.
- `integration_field_mappings`: `IntegrationFieldMappingConnection` (required) (connection) - An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AdtranMosaicSetting

**Description**: An Adtran Mosaic settings record.

**Category**: configuration
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 46

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `default_downlink_interface_name`, `default_uplink_content_provider_name`, `residential_delinquency_profile_vector`, `residential_delinquency_suspends`, `username`

**Enum Fields**: 1 (`synchronization_status`)

**Relationship Fields**: 11 (`id`, `company_id`, `synchronization_status`, `company`, `account_adtran_mosaic_service_details`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `alarms_change_device_status`: `Boolean` (required) - Controls if Sonar updates the ICMP device status from SMx alarms
- `alarms_create_logs`: `Boolean` (required) - Controls if Sonar should add SMx device alarms to inventory item logs
- `api_url`: `String` (required) - The base API URL.
- `auto_suspend_unattached_services`: `Boolean` (required) - Whether or not to suspend unattached services.
- `bounce_ports`: `Boolean` (required) - Disable, pause, then re-enable Calix ONT ports after creating or removing service.  Recommended for deployments using DHCP within SMx.
- `bounce_ports_disable_profile`: `String` (required) - Bounce ports disable profile.
- `bounce_ports_enable_profile`: `String` (required) - Bounce ports enable profile.
- `commercial_delinquency_profile_vector`: `String` - Commercial account type delinquency profile vector.
- `commercial_delinquency_suspends`: `Boolean` (required) - Whether or not commercial account type suspends.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `default_downlink_inner_tag_vlan`: `String` - The name of the default Adtran Mosaic downlink inner tag vlan.
- `default_downlink_interface_name`: `String` - The name of the default Adtran Mosaic downlink interface.
- `default_downlink_outer_tag_vlan`: `String` - The name of the default Adtran Mosaic downlink outer tag vlan.
- `default_uplink_content_provider_name`: `String` - The name of the default Adtran Mosaic content provider.
- `default_uplink_inner_tag_vlan`: `String` - The name of the default Adtran Mosaic uplink inner tag vlan.
- `default_uplink_outer_tag_vlan`: `String` (required) - The name of the default Adtran Mosaic uplink outer tag vlan.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `government_delinquency_profile_vector`: `String` - Government account type delinquency profile vector.
- `government_delinquency_suspends`: `Boolean` (required) - Whether or not government account type suspends.
- `industrial_delinquency_profile_vector`: `String` - Industrial account type delinquency profile vector.
- `industrial_delinquency_suspends`: `Boolean` (required) - Whether or not industrial account type suspends.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `password`: `String` (required) - A password.
- `residential_delinquency_profile_vector`: `String` - Residential account type delinquency profile vector.
- `residential_delinquency_suspends`: `Boolean` (required) - Whether or not residential account type suspends.
- `senior_citizen_delinquency_profile_vector`: `String` - Senior citizen account type delinquency profile vector.
- `senior_citizen_delinquency_suspends`: `Boolean` (required) - Whether or not senior citizen account type suspends.
- `synchronization_audit_ran`: `Boolean` (required) - Whether or not a synchronization audit has been run.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `synchronization_status`: `SynchronizationStatus` (required) (enum) - Status of the synchronization process.
- `synchronization_status_message`: `String` - Details regarding the current synchronization status if any.
- `username`: `String` (required) - A username, used for authentication.
- `company`: `Company` - A company you do business as.
- `account_adtran_mosaic_service_details`: `AccountAdtranMosaicServiceDetailConnection` (required) (connection) - An account Adtran Mosaic service detail.
- `integration_field_mappings`: `IntegrationFieldMappingConnection` (required) (connection) - An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
- `integration_service_mappings`: `IntegrationServiceMappingConnection` (required) (connection) - An entity which maps a service to a vendor specific service name
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SystemSetting

**Description**: System configuration settings.

**Category**: configuration
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 45

**Key Fields**: `id`, `sonar_unique_id`, `default_message_from_email_domain_id`, `default_message_from_email_user_prefix`, `default_message_from_name`, `default_message_from_phone_number_id`, `initial_purchase_order_number`, `instance_id`, `mass_message_signature_id`, `single_recipient_signature_id`, `triggered_message_signature_id`

**Enum Fields**: 11 (`country`, `currency`, `customer_portal_contact_access`, `date_format`, `decimal_separator`, `digit_separator`, `language`, `subdivision`, `time_format`, `timezone`, `units`)

**Relationship Fields**: 23 (`id`, `country`, `currency`, `customer_portal_contact_access`, `date_format`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `application_firewall_enabled`: `Boolean` (required) - Application firewall enabled.
- `bilingual_invoices`: `Boolean` - Invoices will be created in both English and French for all customers.
- `calendar_allow_external_sync`: `Boolean` (required) - If enabled allow external calendar integrations to sync.
- `calendar_history_sync_maximum`: `Int` (required) - Number of months to sync calendar history, 0-3 allowed.  Future will always sync.
- `city`: `String` - A city.
- `country`: `Country` (required) (enum) - A two character country code.
- `create_radius_account_on_account_creation`: `Boolean` (required) - Automatically create a RADIUS account when a new account is created.
- `currency`: `Currency` (required) (enum) - The currency the system displays money in.
- `customer_portal_contact_access`: `CustomerPortalContactAccess` (required) (enum) - Whether all or only primary contacts may access the customer portal.
- `date_format`: `DateFormat` (required) (enum) - The date format to use.
- `decimal_separator`: `DecimalSeparator` (required) (enum) - The character used to separate decimals in numbers.
- `default_message_from_email_domain_id`: `Int64Bit` - The id of the Email Domain to use in email From address.
- `default_message_from_email_user_prefix`: `String` - The default user name to use in email From address.  For example the 'jane' in jane@domain.com
- `default_message_from_name`: `String` - The default name to use in email From fields
- `default_message_from_phone_number_id`: `Int64Bit` - the id of the Phone Number to use as default sender for SMS messages.
- `default_message_language`: `String` - The default language for messages.
- `digit_separator`: `DigitSeparator` (required) (enum) - The character used to separate digits in numbers.
- `enable_additional_services`: `Boolean` - Whether or not to enable additional services.
- `fcc_form_477_company_source`: `String` (required) - The source for the company used to populate the DBA name on the FCC Form 477. Supports one of service, account, or default.
- `force_sso_login_web`: `Boolean` (required) - Whether or not to disable the default sonar login and require the use of SSO.
- `initial_purchase_order_number`: `Int64Bit` (required) - The starting number for system generated purchase order numbers.
- `instance_id`: `Int64Bit` (required) - An ID that uniquely identifies this Sonar instance.
- `language`: `Language` (required) (enum) - A supported language.
- `latitude`: `Latitude` - A decimal latitude.
- `longitude`: `Longitude` - A decimal longitude.
- `mass_message_signature_id`: `Int64Bit` - The id of the default signature to use for Mass Messages.
- `option_82_assign_to_customer_mac`: `Boolean` - If true then DHCP leases with Option82 remote_id will assign the IP address to a matching customer MAC address instead of a matching remote_id MAC address.
- `past_due_stamp_invoice`: `Boolean` - If an invoice is past due, will include red watermark stamp saying "Past Due" in the local language.
- `radius_account_prefix`: `String` (required) - A text prefix to use when automatically creating a new RADIUS account.
- `single_recipient_signature_id`: `Int64Bit` - The id of the default signature to use for Single Recipient Messages.
- `subdivision`: `Subdivision` (required) (enum) - A state, province, or other country subdivision.
- `suppress_alerts_until_datetime`: `Datetime` - The date and time to suppress inventory item status alerts until.
- `test_billing_run`: `Boolean` (required) - Whether or not a test billing run has been executed for this instance.
- `test_mode`: `Boolean` (required) - Whether or not the system is in test mode. In test mode, credit card and bank payments cannot be processed, and emails will not be sent.
- `time_format`: `TimeFormat` (required) (enum) - The time format to use.
- `timezone`: `Timezone` (required) (enum) - The timezone you want times in the system displayed in.
- `triggered_message_signature_id`: `Int64Bit` - The id of the default signature to use for Triggered Messages.
- `units`: `Units` (required) (enum) - The system of units.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PollerSetting

**Description**: Poller configuration settings.

**Category**: configuration
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 4 (`id`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_polling_frequency_in_minutes`: `Int` (required) - How often to poll account equipment (minutes).
- `infrastructure_polling_frequency_in_minutes`: `Int` (required) - How often to poll infrastructure equipment (minutes).
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CalixCloudSettingConnection

**Description**: The connection wrapper around the `CalixCloudSettingConnection` type.

**Category**: configuration
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CalixCloudSetting` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AdtranMosaicSettingConnection

**Description**: The connection wrapper around the `AdtranMosaicSettingConnection` type.

**Category**: configuration
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AdtranMosaicSetting` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Contacts Entities (22 total)


### TriggeredEmail

**Description**: An `Email` that is sent when a particular event occurs.

**Category**: contacts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 22

**Key Fields**: `id`, `sonar_unique_id`, `email_message_id`, `job_type_id`, `name`, `email_message`, `email_categories`

**Enum Fields**: 1 (`trigger`)

**Relationship Fields**: 13 (`id`, `email_message_id`, `job_type_id`, `trigger`, `email_message`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `allow_children`: `Boolean` (required) - Whether or not child accounts are allowed.
- `count`: `Int` - The count associated with this `TriggeredEmail`. This is defined by the trigger, and could be something like a number of days, months, gigabytes, etc.
- `email_message_id`: `Int64Bit` (required) - The ID of an EmailMessage.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `job_type_id`: `Int64Bit` - The ID of a `JobType`.
- `name`: `String` (required) - A descriptive name.
- `protected`: `Boolean` (required) - If an item is protected, it cannot be modified or deleted.
- `trigger`: `EmailTrigger` (required) (enum) - The trigger for this message.
- `email_message`: `EmailMessage` - An email message.
- `job_type`: `JobType` - The type of a `Job`.
- `message_categories`: `MessageCategoryConnection` (required) (connection) - A categorization of a message by type.
- `email_categories`: `EmailCategoryConnection` (required) (connection) - A categorization of an `Email` by type.
- `invoices`: `InvoiceConnection` (required) (connection) - An invoice.
- `accounts_exceeding_usage_triggers`: `AccountConnection` (required) (connection) - Accounts exceeding a data usage triggered email.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PhoneNumberType

**Description**: A phone number type (e.g. mobile, home, work.)

**Category**: contacts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `name`, `phone_numbers`

**Relationship Fields**: 4 (`id`, `phone_numbers`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `sms_capable`: `Boolean` (required) - Whether or not phone numbers of this type are capable of sending and receiving SMS messages.
- `phone_numbers`: `PhoneNumberConnection` (required) (connection) - A phone number.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailMessage

**Description**: An email message.

**Category**: contacts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `from_email_address`, `from_name`, `name`, `saved_message_category_id`, `email_message_contents`

**Relationship Fields**: 9 (`id`, `from_email_address`, `saved_message_category_id`, `email_message_contents`, `triggered_messages`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `from_email_address`: `EmailAddress` (required) - The email address to send from when using this email message. If `null`, then the system default will be used.
- `from_name`: `String` - The name to send from when using this email message. If `null`, then the system default will be used.
- `name`: `String` (required) - A descriptive name.
- `saved_message_category_id`: `Int64Bit` - ID of the Saved Message Category.
- `email_message_contents`: `EmailMessageContentConnection` (required) (connection) - The localized content of an `EmailMessage`.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `saved_message_category`: `SavedMessageCategory` - Saved message category.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Email

**Description**: An email.

**Category**: contacts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `email_address`, `emailable_id`, `emailable_type`, `to_name`, `emailable`, `email_opens`, `email_clicks`

**Enum Fields**: 2 (`emailable_type`, `status`)

**Relationship Fields**: 13 (`id`, `body`, `email_address`, `emailable_id`, `emailable_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `body`: `Text` - The body.
- `email_address`: `EmailAddress` (required) - An email address.
- `emailable_id`: `Int64Bit` (required) - The ID of the entity that this email was sent to.
- `emailable_type`: `EmailableType` (required) (enum) - The type of entity that this email was sent to.
- `reject_reason`: `String` - If rejected, the reason for rejection.
- `status`: `EmailStatus` (required) (enum) - The status.
- `subject`: `String` (required) - The subject.
- `to_name`: `String` - The name of the recipient.
- `emailable`: `EmailableInterface` - The recipient of this `Email`.
- `smtp_events`: `SmtpEventConnection` (required) (connection) - A single SMTP event for an email.
- `email_opens`: `EmailOpenConnection` (required) (connection) - A single open for a sent email.
- `email_clicks`: `EmailClickConnection` (required) (connection) - A single click for a sent email.
- `produced_tickets`: `TicketConnection` (required) (connection) - The `Ticket` that was created by this `Email`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Contact

**Description**: A contact person.

**Category**: contacts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 26

**Key Fields**: `id`, `sonar_unique_id`, `contactable_id`, `email_address`, `name`, `username`, `phone_numbers`, `email_categories`, `mass_emails`, `emails`

**Enum Fields**: 2 (`contactable_type`, `language`)

**Relationship Fields**: 17 (`id`, `contactable_id`, `contactable_type`, `email_address`, `language`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `contactable_id`: `Int64Bit` (required) - The ID of the entity that owns this contact.
- `contactable_type`: `ContactableType` (required) (enum) - The type of entity that owns this contact.
- `email_address`: `EmailAddress` - An email address.
- `language`: `Language` (enum) - A supported language.
- `marketing_opt_in`: `Boolean` - Whether or not marketing messages accepted.
- `name`: `String` (required) - A descriptive name.
- `primary`: `Boolean` (required) - Whether or not this is the primary type of entity.
- `role`: `String` - The role of the contact, e.g. "CEO" or "Network Engineer".
- `username`: `String` - A username, used for authentication.
- `contactable`: `ContactableInterface` - The owner of this `Contact`.
- `phone_numbers`: `PhoneNumberConnection` (required) (connection) - A phone number.
- `contracts`: `ContractConnection` (required) (connection) - A contract.
- `message_categories`: `MessageCategoryConnection` (required) (connection) - A categorization of a message by type.
- `email_categories`: `EmailCategoryConnection` (required) (connection) - A categorization of an `Email` by type.
- `mass_emails`: `MassEmailConnection` (required) (connection) - A mass email communication.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `sms_outbound_messages`: `SmsOutboundMessageConnection` (required) (connection) - An SMS outbound message.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PhoneNumber

**Description**: A phone number.

**Category**: contacts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `contact_id`, `number`, `number_formatted`, `phone_number_type_id`, `phone_number_type`

**Enum Fields**: 1 (`country`)

**Relationship Fields**: 10 (`id`, `contact_id`, `country`, `extension`, `number`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `contact_id`: `Int64Bit` (required) - The ID of the contact that owns this.
- `country`: `Country` (required) (enum) - A two character country code for this phone number.
- `extension`: `Numeric` - The extension.
- `number`: `Numeric` (required) - The number.
- `number_formatted`: `String` - A phone number formatted for human readability.
- `phone_number_type_id`: `Int64Bit` (required) - The ID of the PhoneNumberType associated with this phone number.
- `sms_opt_in`: `Boolean` (required) - Whether or not SMS messages accepted.
- `phone_number_type`: `PhoneNumberType` - A phone number type (e.g. mobile, home, work.)
- `contact`: `Contact` - A contact person.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### MassEmail

**Description**: A mass email communication.

**Category**: contacts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `from_email_address`, `from_name`, `user_id`

**Relationship Fields**: 10 (`id`, `from_email_address`, `message`, `user_id`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `from_email_address`: `EmailAddress` (required) - The email address to send from when using this email message. If `null`, then the system default will be used.
- `from_name`: `String` (required) - The name to send from when using this email message. If `null`, then the system default will be used.
- `inbox_preview`: `String` - A short sentence that will be shown as a preview in compatible email clients.
- `message`: `Text` (required) - The message.
- `subject`: `String` (required) - The subject.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `files`: `FileConnection` (required) (connection) - A file.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailOpen

**Description**: A single open for a sent email.

**Category**: contacts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `email_id`, `email_location_id`, `email`, `email_location`

**Relationship Fields**: 8 (`id`, `email_id`, `email_location_id`, `ip`, `email`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `email_id`: `Int64Bit` (required) - The ID of an email.
- `email_location_id`: `Int64Bit` - The ID of a location associated with a record in EmailClick and EmailOpen.
- `event_datetime`: `Datetime` (required) - The date and time of an event sent from Mandrill
- `ip`: `IP` (required) - An IPv4/IPv6 address.
- `user_agent`: `String` (required) - The user agent string of a user that opened or clicked on a sent email.
- `email`: `Email` - An email.
- `email_location`: `EmailLocation` - The location of a single opened or clicked email.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailMessageContent

**Description**: The localized content of an `EmailMessage`.

**Category**: contacts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `email_message_id`, `email_message`

**Enum Fields**: 1 (`language`)

**Relationship Fields**: 8 (`id`, `body`, `email_message_id`, `language`, `email_message`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `body`: `Text` (required) - The body.
- `email_message_id`: `Int64Bit` (required) - The ID of an EmailMessage.
- `inbox_preview`: `String` - A short sentence that will be shown as a preview in compatible email clients.
- `language`: `Language` (required) (enum) - A supported language.
- `subject`: `String` (required) - The subject.
- `email_message`: `EmailMessage` - An email message.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailDomain

**Description**: An email domain.

**Category**: contacts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `provider_domain_id`

**Relationship Fields**: 7 (`id`, `domain`, `provider_domain_id`, `inbound_mailboxes`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `dkim`: `Boolean` (required) - Whether or not the DKIM record is valid.
- `dns_requirements`: `String` - The DNS requirements for domain validation.
- `domain`: `DomainName` (required) - A domain name.
- `provider_domain_id`: `Int64Bit` - The domain ID from the email provider.
- `ready_for_migration`: `Boolean` - Indicates that the domain has been verified for migration.
- `spf`: `Boolean` (required) - Whether or not the SPF record is valid.
- `verified`: `Boolean` (required) - Whether or not the record is verified.
- `inbound_mailboxes`: `InboundMailboxConnection` (required) (connection) - An inbound mailbox.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailClick

**Description**: A single click for a sent email.

**Category**: contacts
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `email_id`, `email_location_id`, `email`, `email_location`

**Relationship Fields**: 9 (`id`, `email_id`, `email_location_id`, `ip`, `url`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `email_id`: `Int64Bit` (required) - The ID of an email.
- `email_location_id`: `Int64Bit` - The ID of a location associated with a record in EmailClick and EmailOpen.
- `event_datetime`: `Datetime` (required) - The date and time of an event sent from Mandrill
- `ip`: `IP` (required) - An IPv4/IPv6 address.
- `url`: `URL` (required) - The URL that a user clicked on in a sent email.
- `user_agent`: `String` (required) - The user agent string of a user that opened or clicked on a sent email.
- `email`: `Email` - An email.
- `email_location`: `EmailLocation` - The location of a single opened or clicked email.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TriggeredEmailConnection

**Description**: The connection wrapper around the `TriggeredEmailConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TriggeredEmail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PhoneNumberTypeConnection

**Description**: The connection wrapper around the `PhoneNumberTypeConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PhoneNumberType` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PhoneNumberConnection

**Description**: The connection wrapper around the `PhoneNumberConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PhoneNumber` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### MassEmailConnection

**Description**: The connection wrapper around the `MassEmailConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `MassEmail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailOpenConnection

**Description**: The connection wrapper around the `EmailOpenConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailOpen` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailMessageContentConnection

**Description**: The connection wrapper around the `EmailMessageContentConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailMessageContent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailMessageConnection

**Description**: The connection wrapper around the `EmailMessageConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailMessage` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailDomainConnection

**Description**: The connection wrapper around the `EmailDomainConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailDomain` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailConnection

**Description**: The connection wrapper around the `EmailConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Email` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailClickConnection

**Description**: The connection wrapper around the `EmailClickConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailClick` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ContactConnection

**Description**: The connection wrapper around the `ContactConnection` type.

**Category**: contacts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Contact` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Contracts Entities (4 total)


### ContractTemplate

**Description**: A contract template.

**Category**: contracts
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `name`, `ticket_group_id`

**Relationship Fields**: 11 (`id`, `body`, `company_id`, `ticket_group_id`, `company`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `body`: `Text` (required) - The body.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` (required) - A descriptive name.
- `term_in_months`: `Int` - The term in months.
- `ticket_group_id`: `Int64Bit` - The ID of a `TicketGroup`.
- `company`: `Company` - A company you do business as.
- `ticket_group`: `TicketGroup` - A ticket group.
- `contracts`: `ContractConnection` (required) (connection) - A contract.
- `job_types`: `JobTypeConnection` (required) (connection) - The type of a `Job`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Contract

**Description**: A contract.

**Category**: contracts
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 22

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `contact_id`, `contract_template_id`, `handwritten_signature_id`, `name`, `unique_link_key`

**Relationship Fields**: 14 (`id`, `account_id`, `body`, `contact_id`, `contract_template_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `body`: `Text` (required) - The body.
- `contact_id`: `Int64Bit` - The ID of the contact that owns this.
- `contract_template_id`: `Int64Bit` - The ID of a `ContractTemplate`.
- `custom_message`: `Text` - The custom message.
- `expiration_date`: `Date` - The expiration date.
- `handwritten_signature_id`: `Int64Bit` - The ID of a `HandwrittenSignature`.
- `name`: `String` (required) - A descriptive name.
- `term_in_months`: `Int` - The term in months.
- `unique_link_key`: `String` (required) - Part of the unique URL used for signing.
- `account`: `Account` - A customer account.
- `contact`: `Contact` - A contact person.
- `contract_template`: `ContractTemplate` - A contract template.
- `handwritten_signature`: `HandwrittenSignature` - The signature on a contract.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ContractTemplateConnection

**Description**: The connection wrapper around the `ContractTemplateConnection` type.

**Category**: contracts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ContractTemplate` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ContractConnection

**Description**: The connection wrapper around the `ContractConnection` type.

**Category**: contracts
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Contract` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Devices Entities (22 total)


### InlineDevice

**Description**: A device that sits inline with customer traffic to impose network policy.

**Category**: devices
**Relevance Score**: 19 (Primary: 5, Secondary: 2, Operational: 0)
**Total Fields**: 24

**Key Fields**: `id`, `sonar_unique_id`, `bandwidth_collection_queued`, `bandwidth_collection_start`, `name`

**Enum Fields**: 2 (`status`, `type`)

**Relationship Fields**: 11 (`id`, `ip_address`, `port`, `status`, `type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `all_subnets`: `Boolean` (required) - Whether this device should write entries for all subnets or not.
- `bandwidth_collection_queued`: `Boolean` (required) - Whether or not a bandwidth collection request is queued.
- `bandwidth_collection_start`: `Datetime` - The date/time that bandwidth collection started.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `ip_address`: `IP` (required) - An IPv4/IPv6 address.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `name`: `String` (required) - A descriptive name.
- `port`: `Port` - A TCP port.
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `type`: `InlineDeviceType` (required) (enum) - The type.
- `subnets`: `SubnetConnection` (required) (connection) - An IPv4/IPv6 subnet.
- `inline_device_credentials`: `InlineDeviceCredentialConnection` (required) (connection) - An inline device credential.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PrintToMailOrder

**Description**: The print to mail order.

**Category**: devices
**Relevance Score**: 15 (Primary: 5, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `name`, `print_to_mail_batch_id`, `provider_order_id`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 7 (`id`, `print_to_mail_batch_id`, `status`, `print_to_mail_order_errors`, `print_to_mail_batch`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `last_status_check`: `Datetime` (required) - The last time the order status was checked.
- `name`: `String` (required) - The name of the print to mail order.
- `print_to_mail_batch_id`: `Int64Bit` (required) - The print to mail batch ID.
- `provider_order_id`: `String` (required) - The provider ID.
- `status`: `PrintToMailOrderStatus` (required) (enum) - The current status of the print to mail order.
- `print_to_mail_order_errors`: `PrintToMailOrderErrorConnection` (required) (connection) - An error associated with the print to mail order.
- `print_to_mail_batch`: `PrintToMailBatch` - A batch of invoices to mail and print.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### WebhookEndpointEventDispatchAttempt

**Description**: A send attempt of a dispatched webhook for a model and event.

**Category**: devices
**Relevance Score**: 13 (Primary: 4, Secondary: 0, Operational: 1)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `response_code`, `webhook_endpoint_event_dispatch_id`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 8 (`id`, `response`, `status`, `webhook_endpoint_event_dispatch_id`, `webhook_endpoint_event_dispatch`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `response`: `Text` - The message of the SMTP response.
- `response_at`: `Datetime` - The date and time of when a response was received.
- `response_code`: `Int` - The HTTP status code of the last response.
- `status`: `WebhookEndpointEventDispatchAttemptStatus` (required) (enum) - The status.
- `webhook_endpoint_event_dispatch_id`: `Int64Bit` (required) - The ID of a dispatch for a webhook model event.
- `webhook_endpoint_event_dispatch`: `WebhookEndpointEventDispatch` - A webhook for a model and event that has been queued to be sent.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IdentityProvider

**Description**: An identity provider.

**Category**: devices
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `auth0_connection_id`, `auth0_connection_name`, `display_name`, `identity_provider_active_directory_detail`, `identity_provider_google_detail`, `identity_provider_microsoft_detail`, `identity_provider_saml_detail`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 8 (`id`, `type`, `identity_provider_active_directory_detail`, `identity_provider_google_detail`, `identity_provider_microsoft_detail`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `auth0_connection_id`: `String` - The Auth0 connection ID.
- `auth0_connection_name`: `String` - Name of connection in Auth0.
- `display_name`: `String` (required) - The display name.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `type`: `IdentityProviderType` (required) (enum) - The type.
- `identity_provider_active_directory_detail`: `IdentityProviderActiveDirectoryDetail` - Details regarding an ActiveDirectory `IdentityProvider`.
- `identity_provider_google_detail`: `IdentityProviderGoogleDetail` - Details regarding a Google `IdentityProvider`.
- `identity_provider_microsoft_detail`: `IdentityProviderMicrosoftDetail` - Details regarding a Microsoft `IdentityProvider`.
- `identity_provider_saml_detail`: `IdentityProviderSamlDetail` - Details regarding a SAML `IdentityProvider`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SmsOutboundMessage

**Description**: An SMS outbound message.

**Category**: devices
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `mobile_number`, `provider_message_id`, `smsable_id`

**Enum Fields**: 3 (`category`, `smsable_type`, `status`)

**Relationship Fields**: 8 (`id`, `category`, `smsable_id`, `smsable_type`, `status`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `category`: `SmsOutboundCategory` (required) (enum) - The category of the message.
- `cost_in_hundredths`: `Int` (required) - The cost associated with the SMS message. Stored as one hundredth of the smallest currency value (e.g. cents, pence, pesos.)
- `destination_country`: `String` - The country code of the destination mobile phone number.
- `error_message`: `String` (required) - The error message.
- `last_status_check`: `Datetime` - The provider message ID.
- `message_text`: `String` (required) - The message text.
- `mobile_number`: `String` (required) - The destination mobile phone number.
- `provider_message_id`: `String` - The provider message ID.
- `segments`: `Int` (required) - The number of segments needed to deliver message text.
- `smsable_id`: `Int64Bit` (required) - The ID of the entity that this SMS was sent to.
- `smsable_type`: `SmsableType` (required) (enum) - The type of entity that this SMS was sent to.
- `status`: `SmsOutboundStatus` (required) (enum) - The current status of the message.
- `smsable`: `SmsableInterface` - An SMS message.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SmsMessage

**Description**: An SMS message.

**Category**: devices
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 6 (`id`, `sms_message_contents`, `triggered_messages`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `is_trigger`: `Boolean` (required) - Whether or not SMS message is used for triggers.
- `name`: `String` (required) - A descriptive name.
- `sms_message_contents`: `SmsMessageContentConnection` (required) (connection) - An SMS message content.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SearchFilter

**Description**: A user-defined search filter that applies to a specific type of entity.

**Category**: devices
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`, `user_id`

**Relationship Fields**: 6 (`id`, `filter`, `user_id`, `user`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `all_users`: `Boolean` (required) - Whether the filter is available to every user (admins only).
- `entity_type`: `String` (required) - The type of entity this filter belongs to.
- `filter`: `Text` (required) - The actual filter, as JSON.
- `name`: `String` (required) - The filter's name.
- `user_id`: `Int64Bit` (required) - The ID of the user that created this entity.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Geofence

**Description**: A geographical restriction.

**Category**: devices
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 6 (`id`, `polygons`, `schedule_availabilities`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `polygons`: `PolygonConnection` (required) (connection) - A list of polygons.
- `schedule_availabilities`: `ScheduleAvailabilityConnection` (required) (connection) - Availability for `Job`s to be scheduled.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DelinquencyExclusion

**Description**: A period of time when invoices are not evaluated for delinquency.

**Category**: devices
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 4 (`id`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `day`: `Int` (required) - A day.
- `month`: `Int` (required) - A month.
- `name`: `String` (required) - A descriptive name.
- `year`: `Int` - A year.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CannedReply

**Description**: A canned reply.

**Category**: devices
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `canned_reply_category_id`, `name`

**Relationship Fields**: 7 (`id`, `body`, `canned_reply_category_id`, `canned_reply_category`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `body`: `Text` (required) - The body.
- `canned_reply_category_id`: `Int64Bit` (required) - The ID of a `CannedReplyCategory`.
- `name`: `String` (required) - A descriptive name.
- `canned_reply_category`: `CannedReplyCategory` - A canned reply category.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DailyAggregateValue

**Description**: An aggregated value calculated for a given date.

**Category**: devices
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `key`

**Enum Fields**: 1 (`key`)

**Relationship Fields**: 5 (`id`, `context`, `key`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `context`: `Text` - Additional context regarding the item.
- `date`: `Date` (required) - A date
- `key`: `AggregateKey` (required) (enum) - Key for a specific value.
- `value`: `Float` (required) - The value.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### WebhookEndpointEventDispatch

**Description**: A webhook for a model and event that has been queued to be sent.

**Category**: devices
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `webhook_endpoint_event_id`

**Enum Fields**: 1 (`last_status`)

**Relationship Fields**: 9 (`id`, `last_status`, `payload`, `webhook_endpoint_event_id`, `webhook_endpoint_event`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `last_attempted_at`: `Datetime` - The date and time of when this was last attempted to be sent.
- `last_status`: `WebhookEndpointEventDispatchAttemptStatus` (required) (enum) - The last status of the last send attempt.
- `payload`: `Text` (required) - The request payload of a fired webhook being sent to an endpoint.
- `sent_at`: `Datetime` - The date and time of when this was successfully sent.
- `test`: `Boolean` (required) - Indicates of this is a test or not.
- `webhook_endpoint_event_id`: `Int64Bit` (required) - The model and event attached to the webhook endpoint
- `webhook_endpoint_event`: `WebhookEndpointEvent` - An event on a model that can fire a webhook
- `webhook_endpoint_event_dispatch_attempts`: `WebhookEndpointEventDispatchAttemptConnection` (required) (connection) - A send attempt of a dispatched webhook for a model and event.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### StoredFilter

**Description**: A filter applied in a `StoredView`.

**Category**: devices
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `stored_group_id`

**Enum Fields**: 1 (`operator`)

**Relationship Fields**: 6 (`id`, `operator`, `stored_group_id`, `stored_group`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `field`: `String` (required) - The field that is being filtered.
- `operator`: `StoredFilterOperator` (required) (enum) - The operator being applied.
- `order`: `Int` - The order in which the filter is applied.
- `stored_group_id`: `Int64Bit` (required) - The ID of a StoredGroup entity.
- `value`: `String` - The value being filtered against.
- `stored_group`: `StoredGroup` - A group of filters in a `StoredView`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Note

**Description**: A note.

**Category**: devices
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `noteable_id`, `user_id`

**Enum Fields**: 2 (`noteable_type`, `priority`)

**Relationship Fields**: 10 (`id`, `message`, `noteable_id`, `noteable_type`, `priority`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `message`: `Text` (required) - The message.
- `noteable_id`: `Int64Bit` (required) - The ID of the entity that owns this note.
- `noteable_type`: `NoteableType` (required) (enum) - The type of entity that owns this note.
- `priority`: `NotePriority` (required) (enum) - The priority of this item.
- `user_id`: `Int64Bit` - The ID of a User.
- `noteable`: `NoteableInterface` - The owner of this `Note`.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### LookerViewLicense

**Description**: A report viewer license.

**Category**: devices
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `user_id`

**Relationship Fields**: 6 (`id`, `user_id`, `user`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `user_id`: `Int64Bit` - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### LookerExploreLicense

**Description**: A report builder license.

**Category**: devices
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `user_id`

**Relationship Fields**: 6 (`id`, `user_id`, `user`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `user_id`: `Int64Bit` - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InlineDeviceCredential

**Description**: An inline device credential.

**Category**: devices
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `inline_device_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 7 (`id`, `credential`, `inline_device_id`, `inline_device`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `InlineDeviceAuthenticationCredential` (required) (enum) - An individual credential to authenticate to an inline device.
- `inline_device_id`: `Int64Bit` (required) - The ID of an `InlineDevice`.
- `value`: `String` (required) - The credential value (e.g. username, password, etc.)
- `inline_device`: `InlineDevice` - A device that sits inline with customer traffic to impose network policy.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IdentityProviderSamlDetail

**Description**: Details regarding a SAML `IdentityProvider`.

**Category**: devices
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `identity_provider_id`, `user_id_attribute`, `identity_provider`

**Enum Fields**: 3 (`digest_algorithm`, `protocol_binding`, `signature_algorithm`)

**Relationship Fields**: 13 (`id`, `certificate`, `digest_algorithm`, `identity_provider_id`, `protocol_binding`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `auth_domains`: `String` (required) - Authentication domains.
- `certificate`: `Text` (required) - The X.509 signing certificate contents.
- `debug`: `Boolean` (required) - Whether to include more verbose logging during the authentication process or not.
- `digest_algorithm`: `SamlDigestAlgorithm` (required) (enum) - The sign request algorithm digest.
- `identity_provider_id`: `Int64Bit` (required) - The ID of an `IdentityProvider`.
- `protocol_binding`: `SamlProtocolBinding` (required) (enum) - The SAML protocol binding.
- `sign_in_endpoint`: `URL` (required) - The SAML sign in URL.
- `sign_out_endpoint`: `URL` - The SAML sign out URL.
- `sign_saml_request`: `Boolean` (required) - Whether to sign the SAML request or not.
- `signature_algorithm`: `SamlSignatureAlgorithm` (required) (enum) - The sign request algorithm.
- `user_id_attribute`: `URL` - The attribute in the SAML token that will be mapped to the user_id property.
- `identity_provider`: `IdentityProvider` - An identity provider.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### WebhookEndpointEventDispatchConnection

**Description**: The connection wrapper around the `WebhookEndpointEventDispatchConnection` type.

**Category**: devices
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `WebhookEndpointEventDispatch` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### WebhookEndpointEventDispatchAttemptConnection

**Description**: The connection wrapper around the `WebhookEndpointEventDispatchAttemptConnection` type.

**Category**: devices
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `WebhookEndpointEventDispatchAttempt` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InlineDeviceCredentialConnection

**Description**: The connection wrapper around the `InlineDeviceCredentialConnection` type.

**Category**: devices
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InlineDeviceCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InlineDeviceConnection

**Description**: The connection wrapper around the `InlineDeviceConnection` type.

**Category**: devices
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InlineDevice` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Documents Entities (3 total)


### File

**Description**: A file.

**Category**: documents
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `fileable_id`, `filename`, `user_id`

**Enum Fields**: 1 (`fileable_type`)

**Relationship Fields**: 10 (`id`, `file_size_in_bytes`, `fileable_id`, `fileable_type`, `user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `description`: `String` - A human readable description.
- `file_size_in_bytes`: `Int64Bit` (required) - The file size, in bytes.
- `fileable_id`: `Int64Bit` - The ID of the entity that owns this file.
- `fileable_type`: `FileableType` (enum) - The type of entity that owns this file.
- `filename`: `String` (required) - The file name.
- `mime_type`: `String` (required) - The MIME type of the file.
- `primary_image`: `Boolean` (required) - An image file may be set to the primary image. This will be used as the displayed image for the object that this file is associated to throughout Sonar.
- `user_id`: `Int64Bit` - The ID of a User.
- `fileable`: `FileableInterface` - The entity that this `File` is associated with.
- `user`: `User` - A user that can login to Sonar.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PrintToMailDocumentCostEstimate

**Description**: The print to mail cost estimate for a single document/invoice.

**Category**: documents
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 4

**Key Fields**: `number_of_digital_pages`

**Enum Fields**: 2 (`print_method`, `print_type`)

**Relationship Fields**: 2 (`print_method`, `print_type`)

**All Fields**:

- `print_method`: `PrintToMailPrintMethod` (required) (enum) - The print method for the print to mail batch.
- `print_type`: `PrintToMailPrintType` (required) (enum) - The print type for the print to mail batch.
- `number_of_digital_pages`: `Int` (required) - The number of digital pages in the document/invoice.
- `cost_estimate`: `Int` (required) - The estimated print to mail cost for a single document/invoice.

---

### FileConnection

**Description**: The connection wrapper around the `FileConnection` type.

**Category**: documents
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `File` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Financial Entities (2 total)


### GeneralLedgerCode

**Description**: A general ledger code.

**Category**: financial
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `code`

**Relationship Fields**: 5 (`id`, `services`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `code`: `String` (required) - A code.
- `description`: `String` (required) - A human readable description.
- `services`: `ServiceConnection` (required) (connection) - A service.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GeneralLedgerCodeConnection

**Description**: The connection wrapper around the `GeneralLedgerCodeConnection` type.

**Category**: financial
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GeneralLedgerCode` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Geographic Entities (17 total)


### ScheduleAddress

**Description**: The geographical point that a technician starts or ends their day at.

**Category**: geographic
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 4 (`country`, `subdivision`, `timezone`, `type`)

**Relationship Fields**: 11 (`id`, `country`, `latitude`, `longitude`, `subdivision`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `city`: `String` - A city.
- `country`: `Country` (enum) - A two character country code.
- `latitude`: `Latitude` (required) - A decimal latitude.
- `line1`: `String` - Address line 1.
- `line2`: `String` - Address line 2.
- `longitude`: `Longitude` (required) - A decimal longitude.
- `name`: `String` (required) - A descriptive name.
- `subdivision`: `Subdivision` (enum) - A state, province, or other country subdivision.
- `timezone`: `Timezone` (enum) - The timezone you want times in the system displayed in.
- `type`: `ScheduleAddressType` (required) (enum) - The type.
- `zip`: `String` - A ZIP or postal code.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AddressStatus

**Description**: An address status.

**Category**: geographic
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 1 (`icon`)

**Relationship Fields**: 7 (`id`, `color`, `icon`, `addresses`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `color`: `HtmlHexColor` (required) - Color.
- `icon`: `Icon` (required) (enum) - An icon.
- `name`: `String` (required) - A descriptive name.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AddressList

**Description**: An address list defines some criteria by which to group accounts for network policy enforcement.

**Category**: geographic
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 2 (`account_status`, `delinquency`)

**Relationship Fields**: 11 (`id`, `account_status`, `delinquency`, `account_groups`, `account_statuses`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_status`: `AddressListAccountStatus` (required) (enum) - The types of account statuses for accounts that are part of this grouping.
- `delinquency`: `AddressListDelinquency` (required) (enum) - The delinquency state for accounts that are part of this grouping.
- `name`: `String` (required) - A descriptive name.
- `account_groups`: `AccountGroupConnection` (required) (connection) - An account group.
- `account_statuses`: `AccountStatusConnection` (required) (connection) - The status of an account.
- `account_types`: `AccountTypeConnection` (required) (connection) - The account type.
- `services`: `ServiceConnection` (required) (connection) - A service.
- `usage_based_billing_policies`: `UsageBasedBillingPolicyConnection` (required) (connection) - A usage based billing policy.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GpsTrackingProvider

**Description**: A `GpsTrackingProvider`.

**Category**: geographic
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `provider`, `gps_tracking_provider_credentials`

**Enum Fields**: 1 (`provider`)

**Relationship Fields**: 6 (`id`, `provider`, `gps_tracking_provider_credentials`, `vehicles`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `oauth_required`: `Boolean` (required) - Whether OAuth authentication required.
- `provider`: `GpsTrackingProviderType` (required) (enum) - A type of GPS tracking provider.
- `gps_tracking_provider_credentials`: `GpsTrackingProviderCredentialConnection` (required) (connection) - `GpsTrackingProvider` credentials.
- `vehicles`: `VehicleConnection` (required) (connection) - A vehicle.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Address

**Description**: A geographical address.

**Category**: geographic
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 46

**Key Fields**: `id`, `sonar_unique_id`, `address_status_id`, `addressable_id`, `anchor_address_id`, `avalara_pcode`, `billing_default_id`

**Enum Fields**: 7 (`addressable_type`, `country`, `county`, `fips_source`, `subdivision`, `timezone`, `type`)

**Relationship Fields**: 31 (`id`, `address_status_id`, `addressable_id`, `addressable_type`, `anchor_address_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `address_status_id`: `Int64Bit` - Address status ID.
- `addressable_id`: `Int64Bit` - The ID of the entity that owns this address.
- `addressable_type`: `AddressableType` (enum) - The type of entity that owns this address.
- `anchor_address_id`: `Int64Bit` - The address ID for the Anchor address
- `attainable_download_speed`: `Int` - The attainable download speed in kilobits per second.
- `attainable_upload_speed`: `Int` - The attainable upload speed in kilobits per second.
- `avalara_pcode`: `String` - Avalara PCode.
- `billing_default_id`: `Int64Bit` - The ID of a BillingDefault.
- `census_year`: `Int` - The year used for calculating fips and census tract information.
- `city`: `String` - A city.
- `country`: `Country` (enum) - A two character country code.
- `county`: `UsCounty` (enum) - A US county. Only used for US addresses.
- `fips`: `String` - Only used in the USA, this is the census tract information used for calculating things like FCC Form 477.
- `fips_source`: `FipsSource` (enum) - Identifies the source used to obtain the FIPS code
- `is_anchor`: `Boolean` (required) - Whether or not this address is an anchor
- `latitude`: `Latitude` - A decimal latitude.
- `line1`: `String` - Address line 1.
- `line2`: `String` - Address line 2.
- `longitude`: `Longitude` - A decimal longitude.
- `serviceable`: `Boolean` (required) - Whether or not the address is serviceable, and can be used for new accounts.
- `subdivision`: `Subdivision` (enum) - A state, province, or other country subdivision.
- `timezone`: `Timezone` (enum) - The timezone you want times in the system displayed in.
- `type`: `AddressType` (required) (enum) - The type.
- `zip`: `String` - A ZIP or postal code.
- `anchor_address`: `Address` - The serviceable address that is a anchor of this linked account.
- `address_status`: `AddressStatus` - An address status.
- `billing_default`: `BillingDefault` - Default billing settings that are applied to some accounts on creation.
- `addressable`: `AddressableInterface` - The owner of this `Address`.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `linked_addresses`: `AddressConnection` (required) (connection) - A list of linked addresses that this address is a anchor for.
- `serviceable_address_account_assignment_histories`: `ServiceableAddressAccountAssignmentHistoryConnection` (required) (connection) - A `ServiceableAddressAccountAssignmentHistory` for accounts and addresses.
- `disconnection_logs`: `DisconnectionLogConnection` (required) (connection) - The `Account` disconnections log.
- `serviceable_address_account_assignment_futures`: `ServiceableAddressAccountAssignmentFutureConnection` (required) (connection) - An expected change of serviceable address account assignment.
- `towercoverage_submission`: `TowercoverageSubmission` - A TowerCoverage submission.
- `network_site_serviceable_address_lists`: `NetworkSiteServiceableAddressListConnection` (required) (connection) - Network site serviceable address list.

---

### GpsTrackingProviderCredential

**Description**: `GpsTrackingProvider` credentials.

**Category**: geographic
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `gps_tracking_provider_id`, `key`, `gps_tracking_provider`

**Enum Fields**: 1 (`key`)

**Relationship Fields**: 6 (`id`, `gps_tracking_provider_id`, `key`, `gps_tracking_provider`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `gps_tracking_provider_id`: `Int64Bit` (required) - A `GpsTrackingProvider` ID.
- `key`: `GpsTrackingProviderAuthCredential` (required) (enum) - Key for a specific value.
- `value`: `String` (required) - The value.
- `gps_tracking_provider`: `GpsTrackingProvider` - A `GpsTrackingProvider`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CreateLinkedAddresses

**Description**: The linked address details for each item processed in createLinkedAddresses mutation.

**Category**: geographic
**Relevance Score**: 3 (Primary: 1, Secondary: 0, Operational: 0)
**Total Fields**: 4

**Key Fields**: `serviceable_address_id`, `serviceable_address_name`, `account_id`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 3 (`serviceable_address_id`, `status`, `account_id`)

**All Fields**:

- `serviceable_address_id`: `Int64Bit` - The ID of the serviceable address to use for this account.
- `serviceable_address_name`: `String` - The name of the serviceable address to use for this account.
- `status`: `LinkedAddressesStatus` (enum) - The status of each specific linked address during bulk creation.
- `account_id`: `Int64Bit` - The ID of an Account.

---

### IcmpResult

**Description**: types.icmp_result

**Category**: geographic
**Relevance Score**: 2 (Primary: 0, Secondary: 1, Operational: 0)
**Total Fields**: 6

**Relationship Fields**: 1 (`epoch_system_timezone`)

**All Fields**:

- `time`: `Datetime` - The time.
- `high`: `Float` - The high latency.
- `low`: `Float` - The low latency.
- `median`: `Float` - The median latency.
- `loss`: `Float` - The loss percentage.
- `epoch_system_timezone`: `EpochTimestamp` - A Unix timestamp in the same timezone as this Sonar instance

---

### ValidatedAddress

**Description**: types.validated_address

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 8

**Enum Fields**: 2 (`subdivision`, `country`)

**Relationship Fields**: 4 (`subdivision`, `country`, `latitude`, `longitude`)

**All Fields**:

- `line1`: `String` (required) - Address line 1.
- `line2`: `String` - Address line 2.
- `city`: `String` (required) - A city.
- `subdivision`: `Subdivision` (required) (enum) - A state, province, or other country subdivision.
- `zip`: `String` (required) - A ZIP or postal code.
- `country`: `Country` (required) (enum) - A two character country code.
- `latitude`: `Latitude` (required) - A decimal latitude.
- `longitude`: `Longitude` (required) - A decimal latitude.

---

### ScheduleAddressConnection

**Description**: The connection wrapper around the `ScheduleAddressConnection` type.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleAddress` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GpsTrackingProviderCredentialConnection

**Description**: The connection wrapper around the `GpsTrackingProviderCredentialConnection` type.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GpsTrackingProviderCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GpsTrackingProviderConnection

**Description**: The connection wrapper around the `GpsTrackingProviderConnection` type.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GpsTrackingProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DriveTimeResult

**Description**: types.drive_time_result

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 7

**Relationship Fields**: 5 (`start_latitude`, `start_longitude`, `end_latitude`, `end_longitude`, `error`)

**All Fields**:

- `start_latitude`: `Latitude` (required) - The starting latitude.
- `start_longitude`: `Longitude` (required) - The starting longitude.
- `end_latitude`: `Latitude` (required) - The ending latitude.
- `end_longitude`: `Longitude` (required) - The ending longitude.
- `drive_time_in_minutes`: `Int` - The amount of time it takes to drive from the start to the end, in minutes.
- `success`: `Boolean` (required) - Whether the drive time lookup succeeded.
- `error`: `Text` - If the drive time lookup failed, the error that was provided.

---

### CreateLinkedAddressesResponse

**Description**: The results from the createLinkedAddresses mutation.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`addresses_total`, `addresses_created`, `linked_addresses`)

**All Fields**:

- `addresses_total`: `Int64Bit` - The total number of address(es) in the range provided.
- `addresses_created`: `Int64Bit` - The number of address(es) created in the range provided.
- `linked_addresses`: `CreateLinkedAddresses` (list) - The list of address(es) processed in the range provided and details on each.

---

### AddressStatusConnection

**Description**: The connection wrapper around the `AddressStatusConnection` type.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AddressStatus` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AddressListConnection

**Description**: The connection wrapper around the `AddressListConnection` type.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AddressList` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AddressConnection

**Description**: The connection wrapper around the `AddressConnection` type.

**Category**: geographic
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Address` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Integration Entities (5 total)


### WebhookEndpoint

**Description**: A URL to an endpoint that a webhook can be sent to.

**Category**: integration
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 6 (`id`, `endpoint`, `webhook_endpoint_events`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `endpoint`: `HttpsUrl` (required) - The URL to the remote resource that webhooks will be sent to.
- `name`: `String` (required) - A descriptive name.
- `webhook_endpoint_events`: `WebhookEndpointEventConnection` (required) (connection) - An event on a model that can fire a webhook
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ExternalMarketingProvider

**Description**: A `ExternalMarketingProviderType` for `ExternalMarketingProvider` 3rd party integration.

**Category**: integration
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `provider`, `external_marketing_provider_credentials`

**Enum Fields**: 1 (`provider`)

**Relationship Fields**: 5 (`id`, `provider`, `external_marketing_provider_credentials`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `provider`: `ExternalMarketingProviderType` (required) (enum) - The `ExternalMarketingProviderType` for 3rd party external marketing integration.
- `external_marketing_provider_credentials`: `ExternalMarketingProviderCredentialConnection` (required) (connection) - The `ExternalMarketingProvider` credentials for integration.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### WebhookTestResponse

**Description**: The result of a test webhook send attempt. Contains the success state, status code, and response body.

**Category**: integration
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Key Fields**: `status_code`

**All Fields**:

- `success`: `Boolean` (required) - Will be true if the operation succeeded.
- `status_code`: `Int` (required) - The HTTP status code of the response.
- `response`: `String` (required) - The response body of the webhook test.

---

### WebhookEndpointConnection

**Description**: The connection wrapper around the `WebhookEndpointConnection` type.

**Category**: integration
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `WebhookEndpoint` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ExternalMarketingProviderConnection

**Description**: The connection wrapper around the `ExternalMarketingProviderConnection` type.

**Category**: integration
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ExternalMarketingProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Inventory Entities (44 total)


### PurchaseOrderItem

**Description**: A line item on a purchase order.

**Category**: inventory
**Relevance Score**: 15 (Primary: 5, Secondary: 0, Operational: 0)
**Total Fields**: 24

**Key Fields**: `id`, `sonar_unique_id`, `name`, `part_number`, `purchase_order_id`, `vendor_item_id`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 13 (`id`, `price`, `purchase_order_id`, `status`, `vendor_item_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `calculated_tax`: `Int` - The tax transaction that was created for this purchase order item the last time it was modified.
- `generic_quantity_received`: `Int` (required) - The quantity of a generic purchase order item that has already been received.
- `list_order`: `Int` - The order this item is shown in a list.
- `name`: `String` - A descriptive name.
- `part_number`: `String` - Part number used by the vendor to identify this vendor item.
- `price`: `Int64Bit` (required) - The price of the vendor item at the time the purchase order was created.
- `purchase_order_id`: `Int64Bit` (required) - The ID of a purchase order.
- `quantity_per_unit`: `Int` - Number of inventory models that are included in a single unit of this vendors product.
- `status`: `PurchaseOrderItemStatus` (required) (enum) - The current status of a purchase order item.
- `units`: `Int` (required) - The quantity of a vendor item on a purchase order.
- `vendor_item_id`: `Int64Bit` (required) - The ID of a vendor item.
- `purchase_order`: `PurchaseOrder` - A purchase order for items from a third party vendor.
- `vendor_item`: `VendorItem` - An item that can be purchased from a particular vendor.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `taxes`: `TaxConnection` (required) (connection) - A tax.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryModelField

**Description**: A field on an inventory model.

**Category**: inventory
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `inventory_model_id`, `name`

**Enum Fields**: 3 (`secondary_type`, `type`, `unique`)

**Relationship Fields**: 11 (`id`, `inventory_model_id`, `secondary_type`, `type`, `unique`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `name`: `String` (required) - A descriptive name.
- `primary`: `Boolean` (required) - A single inventory model field can be set to be the primary field. This will be used as the primary identifier for items of this model throughout Sonar.
- `regexp`: `String` - A PCRE regular expression. Omit the leading and closing /.
- `required`: `Boolean` (required) - Whether or not this field is required.
- `secondary_type`: `InventoryModelFieldSecondaryType` (enum) - Secondary types that inventory model fields can be set to.
- `type`: `InventoryModelFieldType` (required) (enum) - Types that inventory model fields can be set to.
- `unique`: `Uniqueness` (required) (enum) - Whether or not the field contents must be unique.
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `inventory_model_field_data`: `InventoryModelFieldDataConnection` (required) (connection) - Data contained within an inventory item field.
- `integration_field_mappings`: `IntegrationFieldMappingConnection` (required) (connection) - An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryModel

**Description**: A type of item stored in inventory.

**Category**: inventory
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 40

**Key Fields**: `id`, `sonar_unique_id`, `default_vendor_id`, `inventory_model_category_id`, `manufacturer_id`, `model_name`, `name`, `network_monitoring_template_id`

**Enum Fields**: 5 (`device_type`, `icon`, `lte_sim_type`, `protocol`, `unit_of_measurement`)

**Relationship Fields**: 29 (`id`, `default_vendor_id`, `device_type`, `icon`, `inventory_model_category_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `default_vendor_id`: `Int64Bit` - Sets the default vendor to be used for purchasing this inventory model.
- `device_type`: `InventoryModelDeviceType` (required) (enum) - The type of inventory model.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `generic`: `Boolean` (required) - Whether or not this is generic.
- `icon`: `Icon` (required) (enum) - An icon.
- `inventory_model_category_id`: `Int64Bit` (required) - The ID of an InventoryModelCategory.
- `is_segmentable`: `Boolean` (required) - Whether or not inventory item can be broken down into segments.
- `lte_sim_type`: `LteProviderType` (enum) - If this is a SIM card for LTE provisioning, which provider this SIM is for.
- `manufacturer_id`: `Int64Bit` (required) - The ID of a Manufacturer.
- `model_name`: `String` - The actual model name/part number.
- `name`: `String` (required) - A descriptive name.
- `network_monitoring_template_id`: `Int64Bit` - The ID of a `NetworkMonitoringTemplate`.
- `port`: `Int` - The TCP port that the web interface of this type of device is available on.
- `protocol`: `Protocol` (enum) - The protocol used to access the web interface.
- `quantity`: `Int` - The quantity of this inventory model.
- `unit_of_measurement`: `UnitOfMeasurementType` (enum) - The unit of measurement for this inventory model.
- `manufacturer`: `Manufacturer` - A manufacturer of an item stored in inventory.
- `inventory_model_category`: `InventoryModelCategory` - A category of item stored in inventory.
- `network_monitoring_template`: `NetworkMonitoringTemplate` - A `NetworkMonitoringTemplate`.
- `default_vendor`: `Vendor` - The default vendor that should be used for restocking this inventory model.
- `vendor_items`: `VendorItemConnection` (required) (connection) - An item that can be purchased from a particular vendor.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `adtran_mosaic_audits`: `AdtranMosaicAuditConnection` (required) (connection) - An Adtran Mosaic audit record.
- `inventory_model_fields`: `InventoryModelFieldConnection` (required) (connection) - A field on an inventory model.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `deployment_types`: `DeploymentTypeConnection` (required) (connection) - The mode that an inventory item is deployed in.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `integration_field_mappings`: `IntegrationFieldMappingConnection` (required) (connection) - An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
- `global_inventory_model_min_maxes`: `GlobalInventoryModelMinMaxConnection` (required) (connection) - Defines the minimum and maximum of an inventory level for all locations per inventory model.
- `inventory_model_min_maxes`: `InventoryModelMinMaxConnection` (required) (connection) - Defines the minimum and maximum of an inventory level per location per inventory model.
- `alerting_rotations`: `AlertingRotationConnection` (required) (connection) - An alerting rotation.

---

### CustomField

**Description**: A user defined field.

**Category**: inventory
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 2 (`entity_type`, `type`)

**Relationship Fields**: 10 (`id`, `entity_type`, `type`, `custom_field_data`, `companies`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `entity_type`: `CustomfielddataableType` (required) (enum) - The type of entity this custom field will be associated with.
- `enum_options`: `String` (list) - A list of values that are valid for this field, if this is a TEXT field. If this is empty, and the field is a TEXT type, then any value will be allowed.
- `name`: `String` (required) - A descriptive name.
- `required`: `Boolean` (required) - Whether or not this field is required.
- `type`: `CustomFieldType` (required) (enum) - The type.
- `unique`: `Boolean` (required) - Whether or not the value of this custom field must be unique throughout the system.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `companies`: `CompanyConnection` (required) (connection) - A company you do business as.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `task_template_items`: `TaskTemplateItemConnection` (required) (connection) - A `task template item`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VendorItem

**Description**: An item that can be purchased from a particular vendor.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 25

**Key Fields**: `id`, `sonar_unique_id`, `name`, `part_number`, `retail_item_service_id`, `vendor_id`, `vendoritemable_id`

**Enum Fields**: 1 (`vendoritemable_type`)

**Relationship Fields**: 14 (`id`, `retail_item_service_id`, `vendor_id`, `vendoritemable_id`, `vendoritemable_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `archived`: `Boolean` (required) - Archived vendor items may not be used for creating new purchase orders or product requests.
- `name`: `String` (required) - A descriptive name.
- `part_number`: `String` - Part number used by the vendor to identify this vendor item.
- `price`: `Int` (required) - The purchase price of this item from the vendor.
- `quantity_per_unit`: `Int` (required) - Number of inventory models that are included in a single unit of this vendors product.
- `retail_item`: `Boolean` (required) - Flag for vendor items that should create a one-time service for retail sale to customers.
- `retail_item_price`: `Int` - The price of the one-time service created for this vendor item
- `retail_item_service_id`: `Int64Bit` - The ID of the one-time service created when this vendor item was created.
- `vendor_id`: `Int64Bit` - The ID of the vendor that sells this item
- `vendoritemable_id`: `Int64Bit` - The ID of the entity that is referred to by this vendor item.
- `vendoritemable_type`: `VendoritemableType` (enum) - The type of entity that is referred to by this vendor item.
- `vendoritemable`: `VendoritemableInterface` - An entity that is associated to a vendor item.
- `vendor`: `Vendor` - A third party vendor of inventory models.
- `retail_item_service`: `Service` - A one-time service associated with a vendor item.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `package_service`: `PackageService` - The relationship between a `Package` and a `Service`.
- `purchase_order_items`: `PurchaseOrderItemConnection` (required) (connection) - A line item on a purchase order.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Vendor

**Description**: A third party vendor of inventory models.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `name`, `emails`

**Enum Fields**: 2 (`currency`, `payment_terms`)

**Relationship Fields**: 13 (`id`, `currency`, `payment_terms`, `addresses`, `contacts`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `archived`: `Boolean` (required) - Archived vendors may not be used for creating new Purchase Orders or Product Requests.
- `automate_approved_purchase_orders`: `Boolean` (required) - Determines if approved purchase orders for this vendor should automatically dispatch an email to the vendor.
- `currency`: `Currency` (required) (enum) - The currency used for all transactions with this vendor.
- `name`: `String` (required) - A descriptive name.
- `payment_terms`: `PaymentTerm` (required) (enum) - The terms of payment for deliveries from this vendor.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `vendor_items`: `VendorItemConnection` (required) (connection) - An item that can be purchased from a particular vendor.
- `purchase_orders`: `PurchaseOrderConnection` (required) (connection) - A purchase order for items from a third party vendor.
- `taxes`: `TaxConnection` (required) (connection) - A tax.

---

### NonInventoryItem

**Description**: An item purchasable from vendors that does not have an `Inventory Model` associated with it

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `general_ledger_code_id`, `name`, `general_ledger_code`

**Relationship Fields**: 7 (`id`, `general_ledger_code_id`, `general_ledger_code`, `vendor_items`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `general_ledger_code_id`: `Int64Bit` - The ID of a GeneralLedgerCode.
- `name`: `String` (required) - A descriptive name.
- `general_ledger_code`: `GeneralLedgerCode` - A general ledger code.
- `vendor_items`: `VendorItemConnection` (required) (connection) - An item that can be purchased from a particular vendor.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Manufacturer

**Description**: A manufacturer of an item stored in inventory.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `inventory_models`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `inventory_models`: `InventoryModelConnection` (required) (connection) - A type of item stored in inventory.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryModelCategory

**Description**: A category of item stored in inventory.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `general_ledger_code_id`, `name`, `general_ledger_code`

**Enum Fields**: 1 (`icon`)

**Relationship Fields**: 8 (`id`, `general_ledger_code_id`, `icon`, `general_ledger_code`, `inventory_models`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `general_ledger_code_id`: `Int64Bit` - The ID of a GeneralLedgerCode.
- `icon`: `Icon` (required) (enum) - An icon.
- `name`: `String` (required) - A descriptive name.
- `general_ledger_code`: `GeneralLedgerCode` - A general ledger code.
- `inventory_models`: `InventoryModelConnection` (required) (connection) - A type of item stored in inventory.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryItem

**Description**: An inventory item.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 60

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `claimed_user_id`, `deployment_type_id`, `inventory_model_id`, `inventoryitemable_id`, `override_status`, `override_status_last_change`, `parent_inventory_item_id`, `purchase_order_item_id`, `segment_parent_id`, `snmp_oid_threshold_violations`, `snmp_override`

**Enum Fields**: 8 (`icmp_device_status`, `icmp_threshold_violation`, `inventoryitemable_type`, `overall_status`, `override_status`, `preseem_status`, `snmp_device_status`, `status`)

**Relationship Fields**: 45 (`id`, `account_service_id`, `claimed_user_id`, `deployment_type_id`, `icmp_device_status`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `claimed_user_id`: `Int64Bit` - The ID of the `User` that claimed this.
- `deployment_type_id`: `Int64Bit` - The ID of a `DeploymentType`.
- `flapping`: `Boolean` (required) - Whether this inventory item is flapping or not.
- `icmp_device_status`: `InventoryItemDeviceStatus` (enum) - The current ICMP monitoring status of an `InventoryItem`.
- `icmp_status_flap_count`: `Int` (required) - The number of times the ICMP status has flapped.
- `icmp_status_last_change`: `Datetime` - The timestamp of when the ICMP status last changed.
- `icmp_threshold_violation`: `InventoryItemIcmpThresholdViolation` (enum) - The ICMP monitoring threshold violation type.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `inventoryitemable_id`: `Int64Bit` (required) - The ID of the entity that this inventory item is assigned to.
- `inventoryitemable_type`: `InventoryitemableType` (required) (enum) - The type of entity that this inventory item is assigned to.
- `latitude`: `Latitude` - A decimal latitude.
- `longitude`: `Longitude` - A decimal longitude.
- `metadata`: `String` - The metadata.
- `overall_status`: `InventoryItemDeviceStatus` (enum) - The overall status of an `InventoryItem` (the worse of ICMP/SNMP status).
- `override_status`: `InventoryItemDeviceStatus` (enum) - The overridden status of an `InventoryItem`.
- `override_status_last_change`: `Datetime` - The timestamp of when the override status last changed.
- `parent_inventory_item_id`: `Int64Bit` - The ID of the parent `InventoryItem`.
- `preseem_status`: `PreseemStatus` (enum) - The status of the device, as read from Preseem.
- `purchase_order_item_id`: `Int64Bit` - The ID of a purchase order item
- `purchase_price`: `Int` - The purchase price of this item.
- `quantity`: `Int` - The quantity of this inventory model.
- `segment_parent_id`: `Int64Bit` - The ID of the `InventoryItem` that this segment is a child of.
- `snmp_device_status`: `InventoryItemDeviceStatus` (enum) - The current SNMP monitoring status of an `InventoryItem`.
- `snmp_status_flap_count`: `Int` (required) - The number of times the SNMP status has flapped.
- `snmp_status_last_change`: `Datetime` - The timestamp of when the SNMP status last changed.
- `snmp_status_message`: `String` - The SNMP monitoring status message.
- `status`: `InventoryItemStatus` (required) (enum) - The physical status of this item.
- `um_price`: `Int` - The unit of measurement price for this inventory item.
- `inventoryitemable`: `InventoryitemableInterface` - The entity that this `InventoryItem` is associated with.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `deployment_type`: `DeploymentType` - The mode that an inventory item is deployed in.
- `purchase_order_item`: `PurchaseOrderItem` - A line item on a purchase order.
- `parent_inventory_item`: `InventoryItem` - The parent `InventoryItem`.
- `claimed_user`: `User` - The user that claimed this `InventoryItem`.
- `segment_parent`: `InventoryItem` - The parent inventory item of a segment.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `adtran_mosaic_audits`: `AdtranMosaicAuditConnection` (required) (connection) - An Adtran Mosaic audit record.
- `inventory_model_field_data`: `InventoryModelFieldDataConnection` (required) (connection) - Data contained within an inventory item field.
- `snmp_oid_threshold_violations`: `SnmpOidThresholdViolationConnection` (required) (connection) - An `SnmpOidThresholdViolation`.
- `device_interface_mappings`: `DeviceInterfaceMappingConnection` (required) (connection) - The interfaces on a device.
- `child_inventory_items`: `InventoryItemConnection` (required) (connection) - The child `InventoryItem`s.
- `alerting_rotation_inventory_items`: `AlertingRotationInventoryItemConnection` (required) (connection) - An `InventoryItem` associated with an `AlertingRotation`.
- `inventory_item_events`: `InventoryItemEventConnection` (required) (connection) - A tracked event that has occurred for an `InventoryItem`.
- `segments`: `InventoryItemConnection` (required) (connection) - A list of segments that this inventory item is parent of.
- `snmp_override`: `SnmpOverride` - An `SnmpOverride`.
- `alerting_rotation_inventory_item`: `AlertingRotationInventoryItem` - An `InventoryItem` associated with an `AlertingRotation`.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `files`: `FileConnection` (required) (connection) - A file.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GenericInventoryAssignee

**Description**: A generic assignee for inventory items.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 8 (`id`, `inventory_items`, `generic_inventory_items`, `generic_inventory_item_action_logs`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Department

**Description**: A department.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 6 (`id`, `company_departments`, `signatures`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `company_departments`: `CompanyDepartmentConnection` (required) (connection) - A department in a company.
- `signatures`: `SignatureConnection` (required) (connection) - A signature.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CustomLink

**Description**: A user defined link.

**Category**: inventory
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 1 (`model`)

**Relationship Fields**: 6 (`id`, `icon_color`, `model`, `url`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `icon`: `String` - An icon.
- `icon_color`: `HtmlHexColor` - The color of the icon.
- `label`: `String` - A title that will be displayed for this item.
- `model`: `CustomLinkModel` (required) (enum) - The model.
- `name`: `String` (required) - A descriptive name.
- `url`: `URL` (required) - The URL to navigate to.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryItemEvent

**Description**: A tracked event that has occurred for an `InventoryItem`.

**Category**: inventory
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `inventory_item_id`

**Enum Fields**: 1 (`event`)

**Relationship Fields**: 8 (`id`, `current`, `event`, `inventory_item_id`, `previous`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `current`: `Text` (required) - Current data.
- `event`: `InventoryItemUpdateEvent` (required) (enum) - An event.
- `event_datetime`: `Datetime` (required) - The date and time of an event sent from Mandrill
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `previous`: `Text` - Previous data.
- `inventory_item`: `InventoryItem` - An inventory item.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TaskTemplateItem

**Description**: A `task template item`.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `completable_id`, `task_template_id`

**Enum Fields**: 2 (`completable_type`, `completion_type`)

**Relationship Fields**: 9 (`id`, `completable_id`, `completable_type`, `completion_type`, `task_template_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `completable_id`: `Int64Bit` - The ID of the entity that completes or completed this task.
- `completable_type`: `CompletableType` (enum) - The type of entity that completes this task.
- `completion_type`: `TaskCompletionType` (required) (enum) - How this task gets marked as completed.
- `list_order`: `Int` - The order this item is shown in a list.
- `task`: `String` (required) - The task to be performed.
- `task_template_id`: `Int64Bit` (required) - The ID of a `TaskTemplate`.
- `completable`: `CompletableInterface` - An entity that can complete a task.
- `task_template`: `TaskTemplate` - A `task template`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RecentItem

**Description**: A recently viewed entity.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `recentitemable_id`, `user_id`

**Enum Fields**: 1 (`recentitemable_type`)

**Relationship Fields**: 7 (`id`, `recentitemable_id`, `recentitemable_type`, `user_id`, `recentitemable`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `recentitemable_id`: `Int64Bit` (required) - The ID of the entity that this recent item entry is for.
- `recentitemable_type`: `RecentitemableType` (required) (enum) - The entity that a recent item entry is for.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `recentitemable`: `RecentitemableInterface` - The entity associated with a `RecentItem` entry.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryModelMinMax

**Description**: Defines the minimum and maximum of an inventory level per location per inventory model.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `inventory_location_id`, `inventory_model_id`

**Relationship Fields**: 8 (`id`, `inventory_location_id`, `inventory_model_id`, `inventory_model`, `inventory_location`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_location_id`: `Int64Bit` (required) - The ID of an `InventoryLocation`.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `maximum`: `Int` - Maximum value
- `minimum`: `Int` (required) - Minimum value
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `inventory_location`: `InventoryLocation` - A location that inventory is stored in.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InventoryModelFieldData

**Description**: Data contained within an inventory item field.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `inventory_item_id`, `inventory_model_field_id`

**Relationship Fields**: 8 (`id`, `inventory_item_id`, `inventory_model_field_id`, `inventory_model_field`, `inventory_item`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `inventory_model_field_id`: `Int64Bit` (required) - The ID of an `InventoryModelField`.
- `value`: `String` (required) - The value.
- `inventory_model_field`: `InventoryModelField` - A field on an inventory model.
- `inventory_item`: `InventoryItem` - An inventory item.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GlobalInventoryModelMinMax

**Description**: Defines the minimum and maximum of an inventory level for all locations per inventory model.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `inventory_model_id`

**Relationship Fields**: 6 (`id`, `inventory_model_id`, `inventory_model`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `maximum`: `Int` - Maximum value
- `minimum`: `Int` (required) - Minimum value
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GenericInventoryItem

**Description**: A generic inventory item.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `genericinventoryitemable_id`, `inventory_model_id`

**Enum Fields**: 1 (`genericinventoryitemable_type`)

**Relationship Fields**: 9 (`id`, `genericinventoryitemable_id`, `genericinventoryitemable_type`, `inventory_model_id`, `genericinventoryitemable`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `genericinventoryitemable_id`: `Int64Bit` (required) - The type of entity that owns this generic `InventoryItem`.
- `genericinventoryitemable_type`: `InventoryitemableType` (required) (enum) - The ID of the entity that owns this generic `InventoryItem`.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `quantity`: `Int` (required) - The quantity for this service.
- `genericinventoryitemable`: `GenericinventoryitemableInterface` - The entity that this `GenericInventoryItem` is associated with.
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CompanyDepartment

**Description**: A department in a company.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `department_id`, `email_address`, `number`, `number_formatted`

**Enum Fields**: 1 (`country`)

**Relationship Fields**: 11 (`id`, `company_id`, `country`, `department_id`, `email_address`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `country`: `Country` (enum) - A two character country code for this phone number.
- `department_id`: `Int64Bit` (required) - The ID of a department.
- `email_address`: `EmailAddress` - An email address.
- `extension`: `Numeric` - The extension.
- `number`: `Numeric` - The number.
- `number_formatted`: `String` - A phone number formatted for human readability.
- `company`: `Company` - A company you do business as.
- `department`: `Department` - A department.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AlertingRotationInventoryItem

**Description**: An `InventoryItem` associated with an `AlertingRotation`.

**Category**: inventory
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `alerting_rotation_id`, `inventory_item_id`

**Enum Fields**: 1 (`last_overall_status`)

**Relationship Fields**: 8 (`id`, `alerting_rotation_id`, `inventory_item_id`, `last_overall_status`, `alerting_rotation`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `alerting_rotation_id`: `Int64Bit` (required) - The alerting rotation ID.
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `last_alerted_datetime`: `Datetime` - The date and time that this rotation was last notified of a status change.
- `last_overall_status`: `InventoryItemDeviceStatus` (enum) - The last monitoring status of an inventory item.
- `last_status_change_datetime`: `Datetime` - The date and time that the inventory item status last changed.
- `next_alert_datetime`: `Datetime` - The next date and time to send a status alert for this rotation.
- `alerting_rotation`: `AlertingRotation` - An alerting rotation.
- `inventory_item`: `InventoryItem` - An inventory item.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### StandardizedVehicle

**Description**: A standardized vehicle.

**Category**: inventory
**Relevance Score**: 3 (Primary: 1, Secondary: 0, Operational: 0)
**Total Fields**: 6

**Key Fields**: `uid`, `name`

**All Fields**:

- `uid`: `String` - A GPS Tracking Provider vehicle unique identifier.
- `vin`: `String` - The vehicle identification number.
- `manufacturer`: `String` - The manufacturer.
- `model`: `String` - The model.
- `year`: `String` - A year.
- `name`: `String` - A descriptive name.

---

### WebhookModelEventResultConnection

**Description**: The connection wrapper around the `WebhookModelEventResultConnection` type.

**Category**: inventory
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 1

**Relationship Fields**: 1 (`entities`)

**All Fields**:

- `entities`: `WebhookModelEventResult` (required) (list) - A list of the entities provided by this connection.

---

### WebhookModelEventResult

**Description**: A model that can fire webhooks and its supported events.

**Category**: inventory
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 2

**Enum Fields**: 1 (`events`)

**Relationship Fields**: 1 (`events`)

**All Fields**:

- `model`: `String` (required) - The model.
- `events`: `WebhookEndpointModelEvent` (required) (list) (enum) - A list of events.

---

### InventoryItemEventConnection

**Description**: The connection wrapper around the `InventoryItemEventConnection` type.

**Category**: inventory
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryItemEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VendorItemConnection

**Description**: The connection wrapper around the `VendorItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VendorItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VendorConnection

**Description**: The connection wrapper around the `VendorConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Vendor` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaskTemplateItemConnection

**Description**: The connection wrapper around the `TaskTemplateItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaskTemplateItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RecentItemConnection

**Description**: The connection wrapper around the `RecentItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RecentItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PurchaseOrderItemConnection

**Description**: The connection wrapper around the `PurchaseOrderItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PurchaseOrderItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NonInventoryItemConnection

**Description**: The connection wrapper around the `NonInventoryItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NonInventoryItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryModelMinMaxConnection

**Description**: The connection wrapper around the `InventoryModelMinMaxConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryModelMinMax` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryModelFieldDataConnection

**Description**: The connection wrapper around the `InventoryModelFieldDataConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryModelFieldData` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryModelFieldConnection

**Description**: The connection wrapper around the `InventoryModelFieldConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryModelField` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryModelConnection

**Description**: The connection wrapper around the `InventoryModelConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryModel` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryModelCategoryConnection

**Description**: The connection wrapper around the `InventoryModelCategoryConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryModelCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryItemConnection

**Description**: The connection wrapper around the `InventoryItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GlobalInventoryModelMinMaxConnection

**Description**: The connection wrapper around the `GlobalInventoryModelMinMaxConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GlobalInventoryModelMinMax` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GenericInventoryItemConnection

**Description**: The connection wrapper around the `GenericInventoryItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GenericInventoryItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GenericInventoryAssigneeConnection

**Description**: The connection wrapper around the `GenericInventoryAssigneeConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GenericInventoryAssignee` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DepartmentConnection

**Description**: The connection wrapper around the `DepartmentConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Department` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CompanyDepartmentConnection

**Description**: The connection wrapper around the `CompanyDepartmentConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CompanyDepartment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AlertingRotationInventoryItemConnection

**Description**: The connection wrapper around the `AlertingRotationInventoryItemConnection` type.

**Category**: inventory
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AlertingRotationInventoryItem` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Ip_Management Entities (33 total)


### DhcpServer

**Description**: A DHCP server.

**Category**: ip_management
**Relevance Score**: 19 (Primary: 5, Secondary: 2, Operational: 0)
**Total Fields**: 24

**Key Fields**: `id`, `sonar_unique_id`, `api_key`, `name`

**Enum Fields**: 2 (`status`, `type`)

**Relationship Fields**: 11 (`id`, `ip_address`, `port`, `status`, `type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `api_key`: `String` (required) - An API key.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `ip_address`: `IP` (required) - An IPv4/IPv6 address.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `name`: `String` (required) - A descriptive name.
- `port`: `Port` (required) - A TCP port.
- `serves_all_pools`: `Boolean` (required) - Does this `DhcpServer` provide DHCP for all IP pools?
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `type`: `DhcpServerType` (required) (enum) - The type.
- `use_source_mac_address`: `Boolean` (required) - If this is `true`, then Sonar will use the MAC address of the DHCP relay rather than the MAC address of the requesting device when writing a lease. This should generally be disabled unless you have a specific reason to enable it.
- `ip_pools`: `IpPoolConnection` (required) (connection) - An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)
- `dhcp_server_credentials`: `DhcpServerCredentialConnection` (required) (connection) - A credential for a `DhcpServer`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Subnet

**Description**: An IPv4/IPv6 subnet.

**Category**: ip_management
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `largest_cidr_available`, `name`, `poller_id`, `supernet_id`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 13 (`id`, `poller_id`, `subnet`, `supernet_id`, `type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `largest_cidr_available`: `Int` - The largest subnet available, as a CIDR mask.
- `name`: `String` - A descriptive name.
- `poller_id`: `Int64Bit` - The ID of a `Poller`.
- `polling_priority`: `Int` (required) - Polling priority.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `supernet_id`: `Int64Bit` (required) - The ID of a `Supernet`.
- `type`: `SubnetType` (required) (enum) - The type.
- `supernet`: `Supernet` - The largest example of a unique subnet on your network. A supernet contains many subnets. An example of a supernet is 10.0.0.0/8.
- `poller`: `Poller` - A `Poller`.
- `ip_pools`: `IpPoolConnection` (required) (connection) - An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `inline_devices`: `InlineDeviceConnection` (required) (connection) - A device that sits inline with customer traffic to impose network policy.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TicketRecipient

**Description**: A ticket recipient.

**Category**: ip_management
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `email_address`, `name`, `ticket_id`

**Relationship Fields**: 7 (`id`, `email_address`, `ticket_id`, `ticket`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `email_address`: `EmailAddress` (required) - An email address.
- `name`: `String` (required) - A descriptive name.
- `ticket_id`: `Int64Bit` (required) - The ID of a `Ticket`.
- `ticket`: `Ticket` - A ticket.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Supernet

**Description**: The largest example of a unique subnet on your network. A supernet contains many subnets. An example of a supernet is 10.0.0.0/8.

**Category**: ip_management
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `largest_cidr_available`, `name`

**Relationship Fields**: 6 (`id`, `subnet`, `subnets`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `largest_cidr_available`: `Int` - The largest subnet available, as a CIDR mask.
- `name`: `String` - A descriptive name.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `subnets`: `SubnetConnection` (required) (connection) - An IPv4/IPv6 subnet.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetflowOnPremise

**Description**: A Netflow on premise record.

**Category**: ip_management
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `last_processed_filename`, `name`

**Relationship Fields**: 6 (`id`, `ip`, `statistics`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `ip`: `IP` (required) - An IPv4/IPv6 address.
- `last_processed_filename`: `String` - The file name of the last processed records.
- `last_processed_size`: `Int` - The size of the last processed records file.
- `last_processed_timestamp`: `Datetime` - The date and time of the last processed records.
- `name`: `String` (required) - A descriptive name.
- `statistics`: `Text` - A JSON object of tracked statistics.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IpPool

**Description**: An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)

**Category**: ip_management
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `dhcp_server_identifier_id`, `name`, `subnet_id`, `dhcp_server_identifier`

**Relationship Fields**: 12 (`id`, `dhcp_server_identifier_id`, `ip_range`, `subnet_id`, `subnet`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `dhcp_server_identifier_id`: `Int64Bit` - The ID of a `DhcpServerIdentifier`.
- `ip_range`: `IpRange` (required) - A range of IPv4 addresses.
- `ips_available`: `Int` (required) - The number of IP addresses available.
- `name`: `String` - A descriptive name.
- `subnet_id`: `Int64Bit` (required) - The ID of a `Subnet`.
- `subnet`: `Subnet` - An IPv4/IPv6 subnet.
- `dhcp_server_identifier`: `DhcpServerIdentifier` - A specific identifier for a DHCP server.
- `dhcp_servers`: `DhcpServerConnection` (required) (connection) - A DHCP server.
- `epcs`: `EpcConnection` (required) (connection) - An LTE EPC.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IpAssignmentHistory

**Description**: A historical record of an IP assignment.

**Category**: ip_management
**Relevance Score**: 12 (Primary: 3, Secondary: 1, Operational: 1)
**Total Fields**: 24

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `ip_assignment_id`, `ipassignmentable_id`, `ipassignmenthistoryable_id`, `unique_identifier`

**Enum Fields**: 2 (`ipassignmentable_type`, `ipassignmenthistoryable_type`)

**Relationship Fields**: 15 (`id`, `account_service_id`, `ip_assignment_id`, `ipassignmentable_id`, `ipassignmentable_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `assigned_datetime`: `Datetime` (required) - The date and time of assignment.
- `description`: `String` - A human readable description.
- `ip_assignment_id`: `Int64Bit` - The ID of an `IpAssignment`.
- `ipassignmentable_id`: `Int64Bit` - The ID of the owner of this `IpAssignment`.
- `ipassignmentable_type`: `IpassignmentableType` (required) (enum) - The owner of this `IpAssignment`.
- `ipassignmenthistoryable_id`: `Int64Bit` (required) - The ID of the entity that the IP address was assigned to.
- `ipassignmenthistoryable_type`: `IpassignmenthistoryableType` (required) (enum) - The parent entity that the IP address was assigned to (e.g. `Account`, `NetworkSite`.)
- `reference`: `Text` - Some reference data regarding this IP assignment.
- `removed_datetime`: `Datetime` - The date and time of removal.
- `soft`: `Boolean` (required) - If this IP was assigned automatically (e.g. via DHCP or RADIUS) then it will be marked as a soft assignment.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `unique_identifier`: `String` - Some unique identifier that was related to the IP (e.g. a MAC address, IMSI, RADIUS username.)
- `ipassignmenthistoryable`: `IpassignmenthistoryableInterface` - The parent of the `IpAssignment` referenced by the `IpAssignmentHistory`.
- `ipassignmentable`: `IpassignmentableInterface` - The owner of this `IpAssignment`.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `ip_assignment`: `IpAssignment` - An IP address assignment.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Epc

**Description**: An LTE EPC.

**Category**: ip_management
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `identifier`, `name`

**Relationship Fields**: 5 (`id`, `ip_pools`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `identifier`: `String` (required) - The identifier used by the EPC, this is typically numeric.
- `name`: `String` (required) - A descriptive name.
- `ip_pools`: `IpPoolConnection` (required) (connection) - An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DhcpServerIdentifier

**Description**: A specific identifier for a DHCP server.

**Category**: ip_management
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `ip_pools`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `ip_pools`: `IpPoolConnection` (required) (connection) - An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IpAssignment

**Description**: An IP address assignment.

**Category**: ip_management
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 21

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `ip_pool_id`, `ipassignmentable_id`, `subnet_id`

**Enum Fields**: 1 (`ipassignmentable_type`)

**Relationship Fields**: 15 (`id`, `account_service_id`, `ip_pool_id`, `ipassignmentable_id`, `ipassignmentable_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `description`: `String` - A human readable description.
- `ip_pool_id`: `Int64Bit` - The ID of an `IpPool`.
- `ipassignmentable_id`: `Int64Bit` (required) - The ID of the owner of this `IpAssignment`.
- `ipassignmentable_type`: `IpassignmentableType` (required) (enum) - The owner of this `IpAssignment`.
- `reference`: `Text` - Some reference data regarding this IP assignment.
- `soft`: `Boolean` (required) - If this IP was assigned automatically (e.g. via DHCP or RADIUS) then it will be marked as a soft assignment.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `subnet_id`: `Int64Bit` (required) - The ID of a `Subnet`.
- `ipassignmentable`: `IpassignmentableInterface` - The owner of this `IpAssignment`.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `parent_subnet`: `Subnet` - The `Subnet` this IP assignment falls within.
- `ip_pool`: `IpPool` - An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DepositSlip

**Description**: A deposit slip.

**Category**: ip_management
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 6 (`id`, `payments`, `files`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `bank_account_line`: `String` (required) - The bank account name/number
- `date`: `Date` (required) - A date
- `memo`: `String` - The memo.
- `payments`: `PaymentConnection` (required) (connection) - A payment.
- `files`: `FileConnection` (required) (connection) - A file.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### GenericInventoryItemActionLog

**Description**: A log of an action taken against a set of generic inventory items.

**Category**: ip_management
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `genericinventoryitemactionloggable_id`, `inventory_model_id`, `user_id`

**Enum Fields**: 2 (`action`, `genericinventoryitemactionloggable_type`)

**Relationship Fields**: 10 (`id`, `action`, `genericinventoryitemactionloggable_id`, `genericinventoryitemactionloggable_type`, `inventory_model_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `action`: `GenericInventoryItemActionLogAction` (required) (enum) - The action that was performed.
- `genericinventoryitemactionloggable_id`: `Int64Bit` (required) - The ID of the entity that this `GenericInventoryItemActionLog` is for.
- `genericinventoryitemactionloggable_type`: `InventoryitemableType` (required) (enum) - The type of entity that this `GenericInventoryItemActionLog` is for.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `purchase_price`: `Float` - The purchase price of this item.
- `quantity`: `Int` (required) - The quantity for this service.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `genericinventoryitemactionloggable`: `GenericinventoryitemactionloggableInterface` - The entity that this `GenericInventoryItemActionLog` is associated with.
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DidAssignmentHistory

**Description**: A historical record of a direct inward dial (DID) assignment.

**Category**: ip_management
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `did_assignment_id`, `did_id`, `service_id`, `did_assignment`, `did`

**Relationship Fields**: 11 (`id`, `account_id`, `did_assignment_id`, `did_id`, `service_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `assigned_datetime`: `Datetime` (required) - The date and time of assignment.
- `did_assignment_id`: `Int64Bit` - The ID of a `DidAssignment`.
- `did_id`: `Int64Bit` (required) - The ID of a `Did`.
- `removed_datetime`: `Datetime` - The date and time of removal.
- `service_id`: `Int64Bit` - The ID of a Service.
- `did_assignment`: `DidAssignment` - A direct inward dial (DID) assignment.
- `did`: `Did` - A direct inward dial (DID).
- `account`: `Account` - A customer account.
- `service`: `Service` - A service.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### UninventoriedMacAddress

**Description**: A MAC address that is not recorded in the inventory system.

**Category**: ip_management
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `account_service_id`

**Relationship Fields**: 11 (`id`, `account_id`, `account_service_id`, `mac_address`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `mac_address`: `MacAddress` (required) - A MAC address.
- `account`: `Account` - A customer account.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `ip_assignment_histories`: `IpAssignmentHistoryConnection` (required) (connection) - A historical record of an IP assignment.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetflowWhitelist

**Description**: A whitelisted subnet for a Netflow endpoint.

**Category**: ip_management
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `netflow_endpoint_id`

**Relationship Fields**: 7 (`id`, `netflow_endpoint_id`, `subnet`, `netflow_endpoint`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `netflow_endpoint_id`: `Int64Bit` (required) - The ID of a `NetflowEndpoint`.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `netflow_endpoint`: `NetflowEndpoint` - A Netflow endpoint.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetflowAllowedSubnet

**Description**: A subnet allowed to send data to a Netflow endpoint.

**Category**: ip_management
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `netflow_endpoint_id`

**Relationship Fields**: 7 (`id`, `netflow_endpoint_id`, `subnet`, `netflow_endpoint`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `netflow_endpoint_id`: `Int64Bit` (required) - The ID of a `NetflowEndpoint`.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `netflow_endpoint`: `NetflowEndpoint` - A Netflow endpoint.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IdentityProviderActiveDirectoryDetail

**Description**: Details regarding an ActiveDirectory `IdentityProvider`.

**Category**: ip_management
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `identity_provider_id`, `identity_provider`

**Relationship Fields**: 8 (`id`, `icon_url`, `identity_provider_id`, `ticket_url`, `identity_provider`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `cert_auth`: `Boolean` (required) - Whether to use client SSL certificate authentication or not.
- `disable_cache`: `Boolean` (required) - Whether to disable the cache or not.
- `domain_aliases`: `String` (list) - The list of domains that can be authenticated.
- `icon_url`: `URL` - The ActiveDirectory icon URL.
- `identity_provider_id`: `Int64Bit` (required) - The ID of an `IdentityProvider`.
- `ips`: `String` (list) - The range of IPs with which to use Windows Integrated Auth (Kerberos).
- `kerberos`: `Boolean` (required) - Whether to use Windows Integrated Auth (Kerberos) or not.
- `ticket_url`: `URL` - The ActiveDirectory provisioning ticket URL.
- `identity_provider`: `IdentityProvider` - An identity provider.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DidAssignment

**Description**: A direct inward dial (DID) assignment.

**Category**: ip_management
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `did_id`, `service_id`, `did`

**Relationship Fields**: 10 (`id`, `account_id`, `did_id`, `service_id`, `did`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `did_id`: `Int64Bit` (required) - The ID of a `Did`.
- `service_id`: `Int64Bit` - The ID of a Service.
- `did`: `Did` - A direct inward dial (DID).
- `account`: `Account` - A customer account.
- `service`: `Service` - A service.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DhcpServerCredential

**Description**: A credential for a `DhcpServer`.

**Category**: ip_management
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `dhcp_server_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 6 (`id`, `credential`, `dhcp_server_id`, `dhcp_server`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `DhcpServerAuthenticationCredential` (required) (enum) - A credential for a `DhcpServer`.
- `dhcp_server_id`: `Int64Bit` (required) - The ID of a `DhcpServer`.
- `value`: `String` (required) - The value of a credential for a `DhcpServer`.
- `dhcp_server`: `DhcpServer` - A DHCP server.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IpAssignmentHistoryConnection

**Description**: The connection wrapper around the `IpAssignmentHistoryConnection` type.

**Category**: ip_management
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IpAssignmentHistory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GenericInventoryItemActionLogConnection

**Description**: The connection wrapper around the `GenericInventoryItemActionLogConnection` type.

**Category**: ip_management
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `GenericInventoryItemActionLog` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DidAssignmentHistoryConnection

**Description**: The connection wrapper around the `DidAssignmentHistoryConnection` type.

**Category**: ip_management
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DidAssignmentHistory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### UninventoriedMacAddressConnection

**Description**: The connection wrapper around the `UninventoriedMacAddressConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `UninventoriedMacAddress` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TicketRecipientConnection

**Description**: The connection wrapper around the `TicketRecipientConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TicketRecipient` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SubnetConnection

**Description**: The connection wrapper around the `SubnetConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Subnet` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetflowAllowedSubnetConnection

**Description**: The connection wrapper around the `NetflowAllowedSubnetConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetflowAllowedSubnet` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IpPoolConnection

**Description**: The connection wrapper around the `IpPoolConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IpPool` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IpAssignmentConnection

**Description**: The connection wrapper around the `IpAssignmentConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IpAssignment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DidAssignmentConnection

**Description**: The connection wrapper around the `DidAssignmentConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DidAssignment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DhcpServerIdentifierConnection

**Description**: The connection wrapper around the `DhcpServerIdentifierConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DhcpServerIdentifier` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DhcpServerCredentialConnection

**Description**: The connection wrapper around the `DhcpServerCredentialConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DhcpServerCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DhcpServerConnection

**Description**: The connection wrapper around the `DhcpServerConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DhcpServer` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DepositSlipConnection

**Description**: The connection wrapper around the `DepositSlipConnection` type.

**Category**: ip_management
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DepositSlip` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Jobs Entities (11 total)


### JobType

**Description**: The type of a `Job`.

**Category**: jobs
**Relevance Score**: 15 (Primary: 4, Secondary: 1, Operational: 1)
**Total Fields**: 37

**Key Fields**: `id`, `sonar_unique_id`, `account_status_id_completion`, `account_status_id_failure`, `contract_template_id`, `name`, `task_template_id`, `ticket_group_id_completion`, `ticket_group_id_failure`

**Enum Fields**: 5 (`action_on_completion`, `action_on_failure`, `icon`, `ticket_status_on_completion`, `ticket_status_on_failure`)

**Relationship Fields**: 27 (`id`, `account_status_id_completion`, `account_status_id_failure`, `action_on_completion`, `action_on_failure`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_status_id_completion`: `Int64Bit` - If this is set, any `Job` using this `JobType` that is completed successfully while associated with an `Account` will change the `Account` to this `AccountStatus`.
- `account_status_id_failure`: `Int64Bit` - If this is set, any `Job` using this `JobType` that is completed unsuccessfully while associated with an `Account` will change the `Account` to this `AccountStatus`.
- `action_on_completion`: `JobTypeAction` (required) (enum) - Completion ticket action.
- `action_on_failure`: `JobTypeAction` (required) (enum) - Failure ticket action.
- `all_companies`: `Boolean` (required) - Whether or not this `JobType` is valid for all `Companies`.
- `allow_completion_with_incomplete_tasks`: `Boolean` (required) - Whether `Job`s associated with this `JobType` should be able to be completed with incomplete tasks.
- `color`: `HtmlHexColor` (required) - Color.
- `contract_template_id`: `Int64Bit` - The ID of a `ContractTemplate`.
- `default_length_in_minutes`: `Int` (required) - The default length for a `Job` created using this `JobType`.
- `disconnects_account`: `Boolean` - If this is set, any `Job` using this `JobType` that is completed successfully while associated with an `Account` will trigger the disconnection of the `Account`.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `icon`: `Icon` (required) (enum) - An icon.
- `name`: `String` (required) - A descriptive name.
- `task_template_id`: `Int64Bit` - The ID of a `TaskTemplate`.
- `ticket_group_id_completion`: `Int64Bit` - If this is set, any `Job` using this `JobType` that is completed successfully will create a `Ticket` and assign it to this `TicketGroup`.
- `ticket_group_id_failure`: `Int64Bit` - If this is set, any `Job` using this `JobType` that is completed unsuccessfully will create a `Ticket` and assign it to this `TicketGroup`.
- `ticket_status_on_completion`: `TicketStatus` (required) (enum) - Ticket status on completion.
- `ticket_status_on_failure`: `TicketStatus` (required) (enum) - Ticket status on failure.
- `services`: `ServiceConnection` (required) (connection) - A service.
- `companies`: `CompanyConnection` (required) (connection) - A company you do business as.
- `schedule_availabilities`: `ScheduleAvailabilityConnection` (required) (connection) - Availability for `Job`s to be scheduled.
- `account_status_completion`: `AccountStatus` - The status that an `Account` will be changed to upon successful completion.
- `account_status_failure`: `AccountStatus` - The status that an `Account` will be changed to upon unsuccessful completion.
- `ticket_group_completion`: `TicketGroup` - The `TicketGroup` for a `Ticket` created upon successful completion.
- `ticket_group_failure`: `TicketGroup` - The `TicketGroup` for a `Ticket` created upon unsuccessful completion.
- `contract_template`: `ContractTemplate` - A contract template.
- `task_template`: `TaskTemplate` - A `task template`.
- `jobs`: `JobConnection` (required) (connection) - A job, typically in the field.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PrintToMailBatch

**Description**: A batch of invoices to mail and print.

**Category**: jobs
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`

**Enum Fields**: 4 (`batch_type`, `print_method`, `print_type`, `status`)

**Relationship Fields**: 10 (`id`, `batch_type`, `print_method`, `print_type`, `status`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `batch_type`: `PrintToMailBatchType` (required) (enum) - How the invoices for the batch were generated.
- `billing_completion_date`: `Date` - The completion date of the billing run if the batch type is 'BILLING_RUN'.
- `cost`: `Int` (required) - The cost associated with the print to mail batch.
- `print_method`: `PrintToMailPrintMethod` (required) (enum) - The print method for the print to mail batch.
- `print_type`: `PrintToMailPrintType` (required) (enum) - The print type for the print to mail batch.
- `status`: `PrintToMailBatchStatus` (required) (enum) - The current status of the print to mail batch.
- `print_to_mail_orders`: `PrintToMailOrderConnection` (required) (connection) - The print to mail order.
- `invoices`: `InvoiceConnection` (required) (connection) - An invoice.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AchBatch

**Description**: An ACH batch file.

**Category**: jobs
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`

**Enum Fields**: 2 (`format`, `type`)

**Relationship Fields**: 8 (`id`, `ach_sequence`, `format`, `type`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `ach_sequence`: `Int64Bit` (required) - The batch ID that gets inserted into the ACH file on generation.
- `format`: `BankAccountProvider` (required) (enum) - The provider to use when transacting against bank accounts.
- `payments_after`: `Datetime` (required) - This batch includes payments after this date.
- `payments_before`: `Datetime` (required) - This batch includes payments before this date.
- `type`: `AchBatchType` (required) (enum) - Whether this is a batch of debits or credits.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### JobCheckIn

**Description**: The record of a check in to a `Job`.

**Category**: jobs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `checked_in_by_user_id`, `checked_out_by_user_id`, `job_id`, `user_id`

**Relationship Fields**: 11 (`id`, `checked_in_by_user_id`, `checked_out_by_user_id`, `job_id`, `user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `check_in_datetime`: `Datetime` (required) - The date and time that this `Job` was checked into.
- `check_out_datetime`: `Datetime` - The date and time that this `Job` was checked out of.
- `checked_in_by_user_id`: `Int64Bit` (required) - The ID of the `User` that created this check in.
- `checked_out_by_user_id`: `Int64Bit` - The ID of the `User` that updated this check in with a check out date and time.
- `job_id`: `Int64Bit` (required) - The ID of a `Job`.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `job`: `Job` - A job, typically in the field.
- `user`: `User` - A user that can login to Sonar.
- `checked_in_by_user`: `User` - The `User` that created a `JobCheckIn`.
- `checked_out_by_user`: `User` - The `User` that checked out a `JobCheckIn`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Job

**Description**: A job, typically in the field.

**Category**: jobs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 36

**Key Fields**: `id`, `sonar_unique_id`, `completed_by_user_id`, `created_by_user_id`, `job_type_id`, `jobbable_id`, `serviceable_address_account_assignment_future_id`, `skips_validation`, `ticket_id`

**Enum Fields**: 1 (`jobbable_type`)

**Relationship Fields**: 25 (`id`, `completed_by_user_id`, `completion_notes`, `created_by_user_id`, `job_type_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `address_on_completion`: `String` - The serviceable address where this job was completed.
- `complete`: `Boolean` (required) - Whether or not this is complete.
- `completed_by_user_id`: `Int64Bit` - The `User` that completed this.
- `completed_successfully`: `Boolean` - Whether this `Job` was completed successfully or not.
- `completion_datetime`: `Datetime` - The date and time this `Job` was completed.
- `completion_notes`: `Text` - Any notes entered when this `Job` was completed.
- `created_by_user_id`: `Int64Bit` - The ID of the user that created this entity.
- `job_type_id`: `Int64Bit` (required) - The ID of a `JobType`.
- `jobbable_id`: `Int64Bit` (required) - The ID of the entity that this `Job` is associated with.
- `jobbable_type`: `JobbableType` (required) (enum) - The type of entity that this `Job` is associated with.
- `length_in_minutes`: `Int` (required) - The length in minutes for this `Job`.
- `scheduled_datetime`: `Datetime` - The date and time this `Job` is scheduled for.
- `serviceable_address_account_assignment_future_id`: `Int64Bit` - The ID of the serviceable address account assignment future.
- `skips_validation`: `Boolean` (required) - Indicates this entity has skipped the validations which would normally apply.
- `ticket_id`: `Int64Bit` - The ID of a `Ticket`.
- `jobbable`: `JobbableInterface` - The entity that this `Job` is associated with.
- `job_type`: `JobType` - The type of a `Job`.
- `ticket`: `Ticket` - A ticket.
- `completed_by_user`: `User` - The user that completed this `Job`.
- `created_by_user`: `User` - The ID of the user that created this entity.
- `serviceable_address_account_assignment_future`: `ServiceableAddressAccountAssignmentFuture` - An expected change of serviceable address account assignment.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `job_check_ins`: `JobCheckInConnection` (required) (connection) - The record of a check in to a `Job`.
- `job_services`: `JobServiceConnection` (required) (connection) - A `Service` associated with a `Job`.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `files`: `FileConnection` (required) (connection) - A file.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### JobTypeConnection

**Description**: The connection wrapper around the `JobTypeConnection` type.

**Category**: jobs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `JobType` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### JobConnection

**Description**: The connection wrapper around the `JobConnection` type.

**Category**: jobs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Job` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### JobCheckInConnection

**Description**: The connection wrapper around the `JobCheckInConnection` type.

**Category**: jobs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `JobCheckIn` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### JobAvailableTimes

**Description**: types.job_available_times

**Category**: jobs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 2

**Key Fields**: `user_ids`

**Relationship Fields**: 2 (`available_times`, `user_ids`)

**All Fields**:

- `available_times`: `DateTimeRange` (list) - A list of `DateTimeRange`s which indicate the available times.
- `user_ids`: `Int64Bit` (list) - IDs of `User`s.

---

### PrintToMailBatchConnection

**Description**: The connection wrapper around the `PrintToMailBatchConnection` type.

**Category**: jobs
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PrintToMailBatch` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AchBatchConnection

**Description**: The connection wrapper around the `AchBatchConnection` type.

**Category**: jobs
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AchBatch` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Logs Entities (20 total)


### AdtranMosaicWorkflowEvent

**Description**: An Adtran Mosaic workflow event record.

**Category**: logs
**Relevance Score**: 13 (Primary: 4, Secondary: 0, Operational: 1)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `adtran_mosaic_setting_id`, `trans_id`

**Relationship Fields**: 6 (`id`, `adtran_mosaic_setting_id`, `adtran_mosaic_setting`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `adtran_mosaic_setting_id`: `Int64Bit` (required) - The ID of an Adtran Mosaic setting.
- `completion_status`: `String` - The completion status of the event.
- `event_object`: `String` (required) - The complete event object of the event.
- `status`: `String` - The status of the event.
- `timestamp`: `Datetime` - The timestamp of the event.
- `trans_id`: `String` - The transaction ID of the event.
- `adtran_mosaic_setting`: `AdtranMosaicSetting` - An Adtran Mosaic settings record.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SmtpEvent

**Description**: A single SMTP event for an email.

**Category**: logs
**Relevance Score**: 12 (Primary: 3, Secondary: 1, Operational: 1)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `email_id`, `email`

**Relationship Fields**: 8 (`id`, `destination_ip`, `email_id`, `size`, `source_ip`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `destination_ip`: `IP` (required) - The remote IP address of the server Mandrill was connected to for message relay when attempting to send an email.
- `email_id`: `Int64Bit` (required) - The ID of an email.
- `event_datetime`: `Datetime` (required) - The date and time of an event sent from Mandrill
- `response`: `String` (required) - The message of the SMTP response.
- `size`: `Int64Bit` (required) - The size of a SMTP message that Mandrill attempted to relay.
- `source_ip`: `IP` (required) - The IP address of the Mandrill server that attempted to send an email.
- `type`: `String` (required) - The type.
- `email`: `Email` - An email.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Log

**Description**: A log entry.

**Category**: logs
**Relevance Score**: 12 (Primary: 3, Secondary: 1, Operational: 1)
**Total Fields**: 22

**Key Fields**: `id`, `sonar_unique_id`, `loggable_id`, `logged_entity_id`, `user_id`

**Enum Fields**: 2 (`level`, `type`)

**Relationship Fields**: 14 (`id`, `current`, `level`, `loggable_id`, `logged_entity_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `current`: `Text` (required) - Current data.
- `legacy`: `Boolean` (required) - Whether or not this log was transferred from a Sonar v1 instance. If so, the formatting will not match current version logs.
- `legacy_title`: `String` - A title which is only populated on logs that were imported from Sonar v1.
- `level`: `LogLevel` (required) (enum) - The severity level.
- `loggable_id`: `Int64Bit` (required) - The ID of the entity that this log is attached to.
- `loggable_type`: `String` (required) - The type of entity that this log is attached to.
- `logged_entity_id`: `Int64Bit` (required) - The entity ID that triggered the log.
- `logged_entity_type`: `String` (required) - The entity that triggered the log.
- `message`: `Text` - The message.
- `previous`: `Text` - Previous data.
- `relation_data`: `Text` - Data from objects related to this change.
- `type`: `LogType` (required) (enum) - The type.
- `user_id`: `Int64Bit` - The ID of a User.
- `loggable`: `LoggableInterface` - The entity that this `Log` entry was generated for.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### WebhookEndpointEvent

**Description**: An event on a model that can fire a webhook

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `webhook_endpoint_id`

**Enum Fields**: 1 (`event`)

**Relationship Fields**: 8 (`id`, `event`, `webhook_endpoint_id`, `webhook_endpoint`, `webhook_endpoint_event_dispatches`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `event`: `WebhookEndpointModelEvent` (required) (enum) - An event.
- `model`: `String` (required) - The model.
- `webhook_endpoint_id`: `Int64Bit` (required) - The ID of a webhook endpoint.
- `webhook_endpoint`: `WebhookEndpoint` - A URL to an endpoint that a webhook can be sent to.
- `webhook_endpoint_event_dispatches`: `WebhookEndpointEventDispatchConnection` (required) (connection) - A webhook for a model and event that has been queued to be sent.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DisconnectionLog

**Description**: The `Account` disconnections log.

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `disconnected_by_user_id`, `serviceable_address_id`

**Relationship Fields**: 11 (`id`, `account_id`, `disconnected_by_user_id`, `serviceable_address_id`, `serviceable_address_reference_record`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `disconnected_at`: `Datetime` (required) - The date and time that the account was disconnected.
- `disconnected_by_user_id`: `Int64Bit` (required) - The `User` that disconnected the `Account`.
- `serviceable_address_id`: `Int64Bit` - The ID of the serviceable address to use for this account.
- `serviceable_address_reference_record`: `Text` - The deleted address object, as a formatted single line, that was disconnected. Used for historical reporting when address is deleted.
- `account`: `Account` - A customer account.
- `disconnected_by_user`: `User` - The user that disconnected this `Account`.
- `serviceable_address`: `Address` - The serviceable address.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DataUsageHistory

**Description**: A data usage history entry.

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 27

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `account_service_id`

**Relationship Fields**: 21 (`id`, `account_id`, `account_service_id`, `billable_in_bytes`, `billable_out_bytes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `billable_in_bytes`: `Int64Bit` (required) - The total billable inbound data in bytes.
- `billable_out_bytes`: `Int64Bit` (required) - The total billable outbound data in bytes.
- `end_time`: `Datetime` - The end time of this data usage history interval.
- `free_in_bytes`: `Int64Bit` (required) - The total free inbound data in bytes.
- `free_out_bytes`: `Int64Bit` (required) - The total free outbound data in bytes.
- `policy_cap_at_close_in_bytes`: `Int64Bit` (required) - The policy cap when this data usage history interval was closed.
- `rollover_available_in_bytes`: `Int64Bit` (required) - The total available rollover data in bytes.
- `rollover_remainder_bytes`: `Int64Bit` (required) - The total remaining rollover data in bytes.
- `rollover_unconsumed_bytes`: `Int64Bit` (required) - The total unconsumed rollover data in bytes.
- `rollover_used_at_close_in_bytes`: `Int64Bit` (required) - The rollover used when this data usage history interval was closed.
- `start_time`: `Datetime` (required) - The start time of this data usage history interval.
- `top_off_total_at_close_in_bytes`: `Int64Bit` (required) - The top off total when this data usage history interval was closed.
- `account`: `Account` - A customer account.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `data_usage_top_offs`: `DataUsageTopOffConnection` (required) (connection) - A data usage top off.
- `available_rollover_histories`: `DataUsageHistoryConnection` (required) (connection) - The `DataUsageHistory`(s) that were rolled over.
- `rollover_parent_histories`: `DataUsageHistoryConnection` (required) (connection) - The parent `DataUsageHistory`(s) for which this `DataUsageHistory` is counted as a rollover for.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CallLog

**Description**: A call log.

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `user_id`

**Relationship Fields**: 9 (`id`, `account_id`, `body`, `user_id`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `body`: `Text` (required) - The body.
- `subject`: `String` (required) - The subject.
- `time_in_seconds`: `String` (required) - The time in seconds.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `account`: `Account` - A customer account.
- `user`: `User` - A user that can login to Sonar.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CalixCloudAudit

**Description**: A Calix Cloud audit record.

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `calix_cloud_setting_id`

**Relationship Fields**: 6 (`id`, `calix_cloud_setting_id`, `calix_cloud_setting`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `calix_cloud_setting_id`: `Int64Bit` (required) - The ID of a `CalixCloudSetting`.
- `subscriber`: `String` (required) - The Calix Cloud subscriber json object.
- `calix_cloud_setting`: `CalixCloudSetting` - A Calix Cloud setting.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AdtranMosaicKafkaEvent

**Description**: An Adtran Mosaic Kafka event record.

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `adtran_mosaic_setting_id`, `key`

**Relationship Fields**: 6 (`id`, `adtran_mosaic_setting_id`, `adtran_mosaic_setting`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `adtran_mosaic_setting_id`: `Int64Bit` (required) - The ID of an Adtran Mosaic setting.
- `kafka_topic`: `String` - The Kafka topic to for the event.
- `key`: `String` - Key for a specific value.
- `value`: `String` - The value.
- `adtran_mosaic_setting`: `AdtranMosaicSetting` - An Adtran Mosaic settings record.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AdtranMosaicAudit

**Description**: An Adtran Mosaic audit record.

**Category**: logs
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 23

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `adtran_device_name`, `adtran_device_serial_number`, `adtran_interface_name`, `adtran_mosaic_setting_id`, `adtran_service_id`, `adtran_service_interface_name`, `audit_reason_code`, `inventory_item_id`

**Relationship Fields**: 10 (`id`, `account_service_id`, `adtran_mosaic_setting_id`, `inventory_item_id`, `account_service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `adtran_device_name`: `String` - The Adtran assigned device name.
- `adtran_device_serial_number`: `String` - The serial number associated with the Adtran device.
- `adtran_interface_name`: `String` - The Adtran interface name.
- `adtran_mosaic_setting_id`: `Int64Bit` (required) - The ID of an Adtran Mosaic setting.
- `adtran_object`: `String` - The Adtran object returned by the API.
- `adtran_service_id`: `String` - The Adtran service ID.
- `adtran_service_interface_name`: `String` - The interface name associated with the Adtran service.
- `audit_message`: `String` - The audit message describing why item included.
- `audit_reason_code`: `String` - The audit reason code of why item included.
- `inventory_item_id`: `Int64Bit` - The ID of an `InventoryItem`.
- `is_visible`: `Boolean` (required) - is_visible of the information
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `adtran_mosaic_setting`: `AdtranMosaicSetting` - An Adtran Mosaic settings record.
- `inventory_item`: `InventoryItem` - An inventory item.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### WebhookEndpointEventConnection

**Description**: The connection wrapper around the `WebhookEndpointEventConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `WebhookEndpointEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SmtpEventConnection

**Description**: The connection wrapper around the `SmtpEventConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SmtpEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### LogConnection

**Description**: The connection wrapper around the `LogConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Log` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DisconnectionLogConnection

**Description**: The connection wrapper around the `DisconnectionLogConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DisconnectionLog` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DataUsageHistoryConnection

**Description**: The connection wrapper around the `DataUsageHistoryConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DataUsageHistory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CallLogConnection

**Description**: The connection wrapper around the `CallLogConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CallLog` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CalixCloudAuditConnection

**Description**: The connection wrapper around the `CalixCloudAuditConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CalixCloudAudit` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AdtranMosaicWorkflowEventConnection

**Description**: The connection wrapper around the `AdtranMosaicWorkflowEventConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AdtranMosaicWorkflowEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AdtranMosaicKafkaEventConnection

**Description**: The connection wrapper around the `AdtranMosaicKafkaEventConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AdtranMosaicKafkaEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AdtranMosaicAuditConnection

**Description**: The connection wrapper around the `AdtranMosaicAuditConnection` type.

**Category**: logs
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AdtranMosaicAudit` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Maintenance Entities (2 total)


### ScheduledEvent

**Description**: An `Account` event that is run at a specific time.

**Category**: maintenance
**Relevance Score**: 12 (Primary: 3, Secondary: 1, Operational: 1)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `primary_event_object_id`

**Enum Fields**: 2 (`additional_service_action`, `event`)

**Relationship Fields**: 9 (`id`, `account_id`, `additional_service_action`, `event`, `account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `additional_service_action`: `AdditionalServiceActionType` (enum) - The action to take when this service is added to an account when additional services are enabled in system settings and more than on service will exist.
- `amount`: `Int` - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `complete`: `Boolean` (required) - Whether or not this is complete.
- `datetime`: `Datetime` (required) - The date and time in UTC.
- `description`: `String` - A human readable description.
- `event`: `ScheduledEventEvent` (required) (enum) - An event.
- `primary_event_object_id`: `String` - The ID of an object described by the `event` field.
- `prorate`: `Boolean` - Whether or not to prorate the transaction.
- `account`: `Account` - A customer account.
- `scheduled_event_account_voice_service_details`: `ScheduledEventAccountVoiceServiceDetailConnection` (required) (connection) - The `AccountVoiceServiceDetail` records used to configure a voice service when a `ScheduledEvent` is executed.
- `scheduled_event_account_calix_service_details`: `ScheduledEventAccountCalixServiceDetailConnection` (required) (connection) - The `AccountCalixServiceDetail` records used to configure the Calix integrations when a `ScheduledEvent` is executed.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduledEventConnection

**Description**: The connection wrapper around the `ScheduledEventConnection` type.

**Category**: maintenance
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduledEvent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Monitoring Entities (12 total)


### AlertingRotation

**Description**: An alerting rotation.

**Category**: monitoring
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 28

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 11 (`id`, `alerting_rotation_days`, `alerting_rotation_inventory_items`, `account_groups`, `account_types`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `all_accounts`: `Boolean` (required) - Whether to include all account equipment in this rotation.
- `all_inventory_models`: `Boolean` (required) - Whether to include all inventory models in this rotation.
- `all_network_sites`: `Boolean` (required) - Whether to include all network site equipment in this rotation.
- `down_time_in_minutes_before_alerting`: `Int` (required) - The number of minutes a device can be in a down state before generating alert.
- `down_time_in_minutes_before_repeat`: `Int` (required) - The number of minutes a device can remain in a down state before sending a repeat alert.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `infinite_repetitions`: `Boolean` (required) - Whether this repeats forever or not.
- `name`: `String` (required) - A descriptive name.
- `repetitions`: `Int` - The number of times this repeats.
- `start`: `Date` (required) - The start.
- `warning_time_in_minutes_before_alerting`: `Int` (required) - The number of minutes a device can be in a warning state before generating alert.
- `warning_time_in_minutes_before_repeat`: `Int` (required) - The number of minutes a device can remain in a warning state before sending a repeat alert.
- `weeks_between_repetitions`: `Int` (required) - The number of weeks between repetitions.
- `alerting_rotation_days`: `AlertingRotationDayConnection` (required) (connection) - An alerting rotation day.
- `alerting_rotation_inventory_items`: `AlertingRotationInventoryItemConnection` (required) (connection) - An `InventoryItem` associated with an `AlertingRotation`.
- `account_groups`: `AccountGroupConnection` (required) (connection) - An account group.
- `account_types`: `AccountTypeConnection` (required) (connection) - The account type.
- `inventory_models`: `InventoryModelConnection` (required) (connection) - A type of item stored in inventory.
- `network_sites`: `NetworkSiteConnection` (required) (connection) - A network site.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetworkMonitoringTemplate

**Description**: A `NetworkMonitoringTemplate`.

**Category**: monitoring
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 25

**Key Fields**: `id`, `sonar_unique_id`, `name`, `snmp3_context_engineid`, `snmp3_context_name`

**Enum Fields**: 4 (`snmp3_auth_protocol`, `snmp3_priv_protocol`, `snmp3_sec_level`, `snmp_version`)

**Relationship Fields**: 16 (`id`, `snmp3_auth_passphrase`, `snmp3_auth_protocol`, `snmp3_context_engineid`, `snmp3_context_name`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `collect_interface_statistics`: `Boolean` (required) - Whether or not to collect interface statistics.
- `icmp_latency_threshold`: `Int` - ICMP latency threshold (ms).
- `icmp_loss_threshold`: `Int` - ICMP loss threshold (%).
- `icmp_monitoring`: `Boolean` (required) - Whether or not ICMP monitoring is enabled.
- `name`: `String` (required) - A descriptive name.
- `snmp3_auth_passphrase`: `Text` - SNMPv3 auth passphrase
- `snmp3_auth_protocol`: `Snmp3AuthProtocol` (enum) - SNMPv3 auth protocol
- `snmp3_context_engineid`: `Text` - SNMPv3 context engine ID
- `snmp3_context_name`: `Text` - SNMPv3 context name
- `snmp3_priv_passphrase`: `Text` - SNMPv3 privacy passphrase
- `snmp3_priv_protocol`: `Snmp3PrivProtocol` (enum) - SNMPv3 privacy protocol
- `snmp3_sec_level`: `Snmp3SecurityLevel` (enum) - SNMPv3 security level
- `snmp_community`: `Text` - SNMP community/securityName
- `snmp_version`: `SnmpVersion` (enum) - SNMP version
- `inventory_models`: `InventoryModelConnection` (required) (connection) - A type of item stored in inventory.
- `deployment_types`: `DeploymentTypeConnection` (required) (connection) - The mode that an inventory item is deployed in.
- `network_monitoring_graphs`: `NetworkMonitoringGraphConnection` (required) (connection) - A `NetworkMonitoringGraph`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Notification

**Description**: A `Notification`.

**Category**: monitoring
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `notifiable_id`, `user_id`

**Enum Fields**: 2 (`notifiable_type`, `type`)

**Relationship Fields**: 9 (`id`, `notifiable_id`, `notifiable_type`, `type`, `user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `is_read`: `Boolean` (required) - Whether this notification is read or unread.
- `notifiable_id`: `Int64Bit` - The ID of the entity that the notification is related to.
- `notifiable_type`: `NotifiableType` (enum) - The type of entity that the notification is related to.
- `type`: `NotificationType` (required) (enum) - The type.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `notifiable`: `NotifiableInterface` - The entity that is related to this `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NotificationSetting

**Description**: A user's notification setting.

**Category**: monitoring
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `user_id`

**Enum Fields**: 2 (`channels`, `notification_type`)

**Relationship Fields**: 7 (`id`, `channels`, `notification_type`, `user_id`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `channels`: `NotificationChannel` (required) (list) (enum) - The notification channels.
- `notification_type`: `NotificationType` (required) (enum) - The type of notification.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AlertingRotationDay

**Description**: An alerting rotation day.

**Category**: monitoring
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `alerting_rotation_id`

**Enum Fields**: 1 (`day`)

**Relationship Fields**: 7 (`id`, `alerting_rotation_id`, `day`, `alerting_rotation`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `alerting_rotation_id`: `Int64Bit` (required) - The alerting rotation ID.
- `day`: `Day` (required) (enum) - A day.
- `end_time`: `Time` (required) - The end time for the day.
- `start_time`: `Time` (required) - The start time for the day.
- `alerting_rotation`: `AlertingRotation` - An alerting rotation.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IcmpStatusResult

**Description**: types.icmp_status_result

**Category**: monitoring
**Relevance Score**: 5 (Primary: 1, Secondary: 1, Operational: 0)
**Total Fields**: 4

**Relationship Fields**: 1 (`epoch_system_timezone`)

**All Fields**:

- `time`: `Datetime` - The time.
- `status`: `String` - The status.
- `reason`: `String` - The reason.
- `epoch_system_timezone`: `EpochTimestamp` - A Unix timestamp in the same timezone as this Sonar instance

---

### NotificationSettingConnection

**Description**: The connection wrapper around the `NotificationSettingConnection` type.

**Category**: monitoring
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NotificationSetting` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NotificationConnection

**Description**: The connection wrapper around the `NotificationConnection` type.

**Category**: monitoring
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Notification` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetworkMonitoringTemplateConnection

**Description**: The connection wrapper around the `NetworkMonitoringTemplateConnection` type.

**Category**: monitoring
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetworkMonitoringTemplate` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IcmpNetworkMonitoringResultConnection

**Description**: types.icmp_network_monitoring_result_connection

**Category**: monitoring
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 4

**Key Fields**: `inventory_item_id`

**Relationship Fields**: 4 (`network_monitoring_template`, `inventory_item_id`, `icmp_results`, `icmp_status_results`)

**All Fields**:

- `network_monitoring_template`: `NetworkMonitoringTemplate` - fields.network_monitoring_template
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `icmp_results`: `IcmpResult` (required) (list) - fields.icmp_results
- `icmp_status_results`: `IcmpStatusResult` (required) (list) - fields.icmp_status_results

---

### AlertingRotationDayConnection

**Description**: The connection wrapper around the `AlertingRotationDayConnection` type.

**Category**: monitoring
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AlertingRotationDay` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AlertingRotationConnection

**Description**: The connection wrapper around the `AlertingRotationConnection` type.

**Category**: monitoring
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AlertingRotation` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Network_Equipment Entities (18 total)


### CableModemProvisioner

**Description**: A cable modem provisioner.

**Category**: network_equipment
**Relevance Score**: 19 (Primary: 5, Secondary: 2, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `hostname`, `name`

**Enum Fields**: 2 (`status`, `type`)

**Relationship Fields**: 7 (`id`, `status`, `type`, `cable_modem_provisioner_credentials`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `hostname`: `String` (required) - Hostname.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `name`: `String` (required) - A descriptive name.
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `type`: `CableModemProvisionerType` (required) (enum) - The type.
- `cable_modem_provisioner_credentials`: `CableModemProvisionerCredentialConnection` (required) (connection) - A cable modem provisioner credential.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### FibermapIntegration

**Description**: FiberMap integration.

**Category**: network_equipment
**Relevance Score**: 17 (Primary: 5, Secondary: 1, Operational: 0)
**Total Fields**: 28

**Key Fields**: `id`, `sonar_unique_id`, `account_status_id`, `account_type_id`, `api_token_name`, `company_id`, `name`, `zone_status_attribute_name`

**Enum Fields**: 2 (`api_version`, `status`)

**Relationship Fields**: 10 (`id`, `account_status_id`, `account_type_id`, `api_version`, `company_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_status_id`: `Int64Bit` (required) - The ID of an AccountStatus.
- `account_type_id`: `Int64Bit` (required) - The ID of an AccountType.
- `always_create_new_network_sites`: `Boolean` (required) - Always create new network sites
- `api_token`: `String` (required) - An API token.
- `api_token_name`: `String` - An API token`s name.
- `api_version`: `FibermapIntegrationApiVersion` (required) (enum) - The API`s version.
- `company_id`: `Int64Bit` (required) - The ID of the company that this entity operates under.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `import_accounts_and_contacts`: `Boolean` (required) - Import plans and contacts
- `import_serviceable_addresses`: `Boolean` (required) - Import serviceable addresses
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `name`: `String` (required) - A descriptive name.
- `read_serviceability_from_features`: `Boolean` (required) - Allow serviceability status to be read from map features
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `update_service_locations`: `Boolean` - Update service locations in Vetro Fibermap
- `zone_status_attribute_name`: `String` (required) - The name Sonar will use to retrive the Zone Status.
- `fibermap_plans`: `FibermapPlanConnection` (required) (connection) - FiberMap plan.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetworkMonitoringGraph

**Description**: A `NetworkMonitoringGraph`.

**Category**: network_equipment
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `name`, `network_monitoring_template_id`, `snmp_oids`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 8 (`id`, `network_monitoring_template_id`, `type`, `network_monitoring_template`, `snmp_oids`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `network_monitoring_template_id`: `Int64Bit` (required) - The ID of a `NetworkMonitoringTemplate`.
- `stacked`: `Boolean` (required) - Stacked
- `type`: `NetworkMonitoringGraphType` (required) (enum) - The type.
- `network_monitoring_template`: `NetworkMonitoringTemplate` - A `NetworkMonitoringTemplate`.
- `snmp_oids`: `SnmpOidConnection` (required) (connection) - An `SnmpOid`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InboundMailbox

**Description**: An inbound mailbox.

**Category**: network_equipment
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 26

**Key Fields**: `id`, `sonar_unique_id`, `email_domain_id`, `from_name`, `name`, `post_email_body_to_slack`, `ticket_group_id`, `email_domain`

**Enum Fields**: 1 (`priority`)

**Relationship Fields**: 13 (`id`, `auto_reply`, `email_domain_id`, `priority`, `signature`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `append_signature`: `Boolean` (required) - Whether or not to append a signature.
- `auto_reply`: `Text` - The auto reply to send.
- `email_domain_id`: `Int64Bit` (required) - The ID of an `EmailDomain`.
- `enable_slack_integration`: `Boolean` (required) - Whether or not to enable Slack integration.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `from_mailbox`: `String` (required) - The mailbox email is sent from.
- `from_name`: `String` (required) - The name to send from when using this email message. If `null`, then the system default will be used.
- `inbound_mailbox`: `String` (required) - The inbound mailbox.
- `name`: `String` (required) - A descriptive name.
- `post_email_body_to_slack`: `Boolean` - Whether the email body should be posted to Slack, or just the email subject.
- `priority`: `TicketPriority` (required) (enum) - The priority of this item.
- `send_auto_reply`: `Boolean` (required) - Whether or not an auto reply should be sent.
- `signature`: `Text` - The signature to append. You can include `[PUBLIC_NAME]` as a variable to insert the user's public name when the signature is appended.
- `slack_webhook_url`: `URL` - The URL of a Slack webhook. You can generate one at https://my.slack.com/services/new/incoming-webhook.
- `ticket_group_id`: `Int64Bit` (required) - The ID of a `TicketGroup`.
- `email_domain`: `EmailDomain` - An email domain.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DeviceInterfaceMapping

**Description**: The interfaces on a device.

**Category**: network_equipment
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `inventory_item_id`

**Relationship Fields**: 8 (`id`, `inventory_item_id`, `mac_address`, `metadata`, `inventory_item`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `description`: `String` (required) - A human readable description.
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `mac_address`: `MacAddress` - A MAC address.
- `metadata`: `Text` (required) - The metadata.
- `speed_mbps_in`: `Int` - The interface in speed in Mbps.
- `speed_mbps_out`: `Int` - The interface out speed in Mbps.
- `type`: `String` - The type.
- `up`: `Boolean` (required) - Whether or not this interface is up.
- `inventory_item`: `InventoryItem` - An inventory item.
- `connected_interfaces`: `DeviceInterfaceMappingConnection` (required) (connection) - The interfaces connected to this interface.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### MapOverlay

**Description**: Map Overlay.

**Category**: network_equipment
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `name`, `network_site_id`

**Enum Fields**: 1 (`file_type`)

**Relationship Fields**: 10 (`id`, `file_type`, `latitude`, `longitude`, `network_site_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `contents`: `String` (required) - Map Overlay Language (KML) file contents.
- `file_type`: `MapOverlayFileType` (required) (enum) - file type
- `latitude`: `Latitude` (required) - A decimal latitude.
- `longitude`: `Longitude` (required) - A decimal longitude.
- `name`: `String` (required) - A descriptive name.
- `network_site_id`: `Int64Bit` - Network site id.
- `radius`: `Float` (required) - Radius in KM.
- `network_site`: `NetworkSite` - A network site.
- `fibermap_plans`: `FibermapPlanConnection` (required) (connection) - FiberMap plan.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Preseem

**Description**: Preseem integration.

**Category**: network_equipment
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `api_key_present`

**Relationship Fields**: 4 (`id`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `api_key_present`: `Boolean` (required) - Indicates if an API key, which is hidden from results, has been set.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ApplicationFirewallRule

**Description**: An application firewall IP address or subnet rule.

**Category**: network_equipment
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 5 (`id`, `subnet`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `description`: `String` - A human readable description.
- `subnet`: `SubnetScalar` (required) - An IPv4/IPv6 subnet.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IntegrationFieldMapping

**Description**: An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)

**Category**: network_equipment
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `integrationconfigurable_id`, `inventory_model_field_id`, `inventory_model_id`

**Enum Fields**: 1 (`integration_field_type`)

**Relationship Fields**: 11 (`id`, `integration_field_type`, `integrationconfigurable_id`, `inventory_model_field_id`, `inventory_model_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `integration_field_type`: `IntegrationFieldType` (required) (enum) - The vendor specific type for field.
- `integrationconfigurable_id`: `Int64Bit` - The ID of the configuration entity which owns this mapping.
- `integrationconfigurable_type`: `String` - The type of the configuration entity which owns this mapping.
- `inventory_model_field_id`: `Int64Bit` (required) - The ID of an `InventoryModelField`.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `inventory_model_field`: `InventoryModelField` - A field on an inventory model.
- `integrationconfigurable`: `IntegrationconfigurableInterface` - The owner of the integration mapping
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CableModemProvisionerCredential

**Description**: A cable modem provisioner credential.

**Category**: network_equipment
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `cable_modem_provisioner_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 7 (`id`, `cable_modem_provisioner_id`, `credential`, `cable_modem_provisioner`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `cable_modem_provisioner_id`: `Int64Bit` (required) - The ID of a `CableModemProvisioner`.
- `credential`: `CableModemProvisionerAuthenticationCredential` (required) (enum) - An individual credential to authenticate to a cable modem provisioner.
- `value`: `String` (required) - The credential value (e.g. username, password, etc.)
- `cable_modem_provisioner`: `CableModemProvisioner` - A cable modem provisioner.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetworkMonitoringGraphConnection

**Description**: The connection wrapper around the `NetworkMonitoringGraphConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetworkMonitoringGraph` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### MapOverlayConnection

**Description**: The connection wrapper around the `MapOverlayConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `MapOverlay` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IntegrationFieldMappingConnection

**Description**: The connection wrapper around the `IntegrationFieldMappingConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IntegrationFieldMapping` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### FibermapIntegrationConnection

**Description**: The connection wrapper around the `FibermapIntegrationConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `FibermapIntegration` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DeviceInterfaceMappingConnection

**Description**: The connection wrapper around the `DeviceInterfaceMappingConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DeviceInterfaceMapping` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CableModemProvisionerCredentialConnection

**Description**: The connection wrapper around the `CableModemProvisionerCredentialConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CableModemProvisionerCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CableModemProvisionerConnection

**Description**: The connection wrapper around the `CableModemProvisionerConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CableModemProvisioner` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ApplicationFirewallRuleConnection

**Description**: The connection wrapper around the `ApplicationFirewallRuleConnection` type.

**Category**: network_equipment
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ApplicationFirewallRule` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Network_Interfaces Entities (18 total)


### SystemBackupExport

**Description**: A log of a system backup export attempt.

**Category**: network_interfaces
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `system_backup_destination_id`, `system_backup_id`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 11 (`id`, `response`, `status`, `system_backup_destination_id`, `system_backup_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `pruned`: `Boolean` (required) - Indicates that this entity has been deleted as part of a pruning.
- `response`: `Text` - The message of the SMTP response.
- `status`: `SystemBackupExportStatus` (required) (enum) - The status.
- `system_backup_destination_id`: `Int64Bit` (required) - The ID of a destination that a system backup can be exported to.
- `system_backup_id`: `Int64Bit` (required) - The ID of a system backup.
- `system_backup`: `SystemBackup` - A backup of your Sonar instance's data.
- `system_backup_destination`: `SystemBackupDestination` - A configured destination to export system backups to.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetflowEndpoint

**Description**: A Netflow endpoint.

**Category**: network_interfaces
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `hostname`, `name`

**Relationship Fields**: 8 (`id`, `hostname`, `port`, `netflow_allowed_subnets`, `netflow_whitelists`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `hostname`: `DomainName` (required) - Hostname.
- `name`: `String` (required) - A descriptive name.
- `port`: `Port` (required) - A TCP port.
- `whitelist_mode`: `Boolean` (required) - Whitelist mode.
- `netflow_allowed_subnets`: `NetflowAllowedSubnetConnection` (required) (connection) - A subnet allowed to send data to a Netflow endpoint.
- `netflow_whitelists`: `NetflowWhitelistConnection` (required) (connection) - A whitelisted subnet for a Netflow endpoint.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DidImportRecipe

**Description**: A recipe for importing DIDs.

**Category**: network_interfaces
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 24

**Key Fields**: `id`, `sonar_unique_id`, `flatfile_batch_identifier`, `rate_center_id`, `sonar_batch_identifier`, `user_id`, `voice_provider_id`, `voice_provider`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 13 (`id`, `errors`, `rate_center_id`, `status`, `user_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `clean_records`: `Int` - How many records passed validation checks during import.
- `errors`: `Clob` - Any errors encountered for this import.
- `failed_records`: `Int` - How many records did not pass validation checks during import.
- `flatfile_batch_identifier`: `String` - The identifier of a unique batch at Flatfile.
- `hash`: `String` - A hash of the data content of an import.
- `progress`: `Int` - The progress of an import as a percentage.
- `rate_center_id`: `Int64Bit` (required) - The ID of a `RateCenter`.
- `sonar_batch_identifier`: `String` - The unique identifier of an import at Sonar.
- `start_datetime`: `Datetime` - The start date and time for the import.
- `status`: `ImportStatus` (required) (enum) - The status.
- `user_id`: `Int64Bit` - The ID of a User.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `rate_center`: `RateCenter` - A rate center.
- `user`: `User` - A user that can login to Sonar.
- `imports`: `ImportConnection` (required) (connection) - An import.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CallDetailRecordImportRecipe

**Description**: A recipe for importing call detail records (CDRs).

**Category**: network_interfaces
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 22

**Key Fields**: `id`, `sonar_unique_id`, `flatfile_batch_identifier`, `sonar_batch_identifier`, `user_id`, `voice_provider_id`, `voice_provider`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 11 (`id`, `errors`, `status`, `user_id`, `voice_provider_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `clean_records`: `Int` - How many records passed validation checks during import.
- `errors`: `Clob` - Any errors encountered for this import.
- `failed_records`: `Int` - How many records did not pass validation checks during import.
- `flatfile_batch_identifier`: `String` - The identifier of a unique batch at Flatfile.
- `hash`: `String` - A hash of the data content of an import.
- `progress`: `Int` - The progress of an import as a percentage.
- `sonar_batch_identifier`: `String` - The unique identifier of an import at Sonar.
- `start_datetime`: `Datetime` - The start date and time for the import.
- `status`: `ImportStatus` (required) (enum) - The status.
- `user_id`: `Int64Bit` - The ID of a User.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `user`: `User` - A user that can login to Sonar.
- `imports`: `ImportConnection` (required) (connection) - An import.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CallDetailRecordImport

**Description**: An import of call detail records (CDRs).

**Category**: network_interfaces
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `call_data_record_import_id`, `voice_provider_id`, `voice_provider`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 11 (`id`, `call_data_record_import_id`, `errors`, `status`, `voice_provider_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `call_data_record_import_id`: `Int64Bit` - The ID of a call data record (CDR) import.
- `clean_records`: `Int` - How many records passed validation checks during import.
- `errors`: `Text` - Any errors encountered for this import.
- `failed_records`: `Int` - How many records did not pass validation checks during import.
- `status`: `AsyncImportStatus` (required) (enum) - The status.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### FccForm477Report

**Description**: A generated FCC Form 477 report.

**Category**: network_interfaces
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `user_id`

**Enum Fields**: 1 (`format`)

**Relationship Fields**: 7 (`id`, `format`, `user_id`, `user`, `files`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `date`: `Date` (required) - A date
- `format`: `FccForm477Format` (required) (enum) - The format of the reporting for FCC Form 477.
- `user_id`: `Int64Bit` - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SmsMessageContent

**Description**: An SMS message content.

**Category**: network_interfaces
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `sms_message_id`

**Enum Fields**: 1 (`language`)

**Relationship Fields**: 7 (`id`, `language`, `sms_message_id`, `sms_message`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `language`: `Language` (required) (enum) - A supported language.
- `non_portal_body`: `String` (required) - SMS message body for customers without portal.
- `portal_body`: `String` (required) - SMS message body for customers with portal.
- `sms_message_id`: `Int64Bit` (required) - The ID of the SMS message.
- `sms_message`: `SmsMessage` - An SMS message.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Import

**Description**: An import.

**Category**: network_interfaces
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `importrecipeable_id`

**Enum Fields**: 1 (`importrecipeable_type`)

**Relationship Fields**: 8 (`id`, `importrecipeable_id`, `importrecipeable_type`, `importrecipeable`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `global_updated_at`: `Datetime` - The last date and time this entity was updated, or was the subject of a log.
- `importrecipeable_id`: `Int64Bit` (required) - The ID of the entity that owns this import.
- `importrecipeable_type`: `ImportrecipeableType` (required) (enum) - The type of entity that owns this import.
- `importrecipeable`: `ImportrecipeableInterface` - The recipe for this `Import`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Me

**Description**: You!

**Category**: network_interfaces
**Relevance Score**: 6 (Primary: 2, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `name`, `username`, `public_name`, `role_id`, `email_address`, `mobile_number`

**Enum Fields**: 1 (`language`)

**Relationship Fields**: 11 (`id`, `role_id`, `email_address`, `mobile_number`, `language`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `name`: `String` (required) - A descriptive name.
- `username`: `String` (required) - A username, used for authentication.
- `public_name`: `String` (required) - The publicly viewable name of this user.
- `super_admin`: `Boolean` (required) - Super admins receive all system permissions automatically, regardless of their role.
- `role_id`: `Int64Bit` - The ID of a Role.
- `email_address`: `EmailAddress` (required) - An email address.
- `mobile_number`: `Numeric` - A mobile phone number. This will be used to send SMS messages.
- `language`: `Language` (required) (enum) - The preferred language for this user. If none is set, then the system default will be used. This will affect the interface, as well as communications sent to this user.
- `role`: `Role` - A role defines the permission set that a user has.
- `notification_settings`: `NotificationSettingConnection` (required) (connection) - Your personal notification settings.
- `user_preferences`: `UserPreference` (required) - Your personal preferences. Affects the look and behavior of Sonar specifically for you.
- `report_builder`: `Boolean` (required) - Whether or not a report builder license is granted.
- `report_viewer`: `Boolean` (required) - Whether or not a report viewer license is granted.
- `recent_items`: `RecentItemConnection` (required) (connection) - A list of `RecentItem`s that you've viewed.
- `vehicles`: `VehicleConnection` (required) (connection) - A vehicle.
- `authentication_factors`: `AuthenticationFactorConnection` (required) (connection) - Your personal authentication factors.

---

### ImportRecipe

**Description**: types.import_recipe

**Category**: network_interfaces
**Relevance Score**: 6 (Primary: 2, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `user_id`, `flatfile_batch_identifier`, `sonar_batch_identifier`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 8 (`id`, `user_id`, `status`, `progress`, `errors`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `user_id`: `Int64Bit` - The ID of a User.
- `flatfile_batch_identifier`: `String` - The identifier of a unique batch at Flatfile.
- `sonar_batch_identifier`: `String` - The unique identifier of an import at Sonar.
- `status`: `ImportStatus` (enum) - The status.
- `progress`: `Int64Bit` - The progress of an import as a percentage.
- `errors`: `Clob` - Any errors encountered for this import.
- `clean_records`: `Int64Bit` - How many records passed validation checks during import.
- `failed_records`: `Int64Bit` - How many records did not pass validation checks during import.
- `hash`: `String` - A hash of the data content of an import.
- `start_datetime`: `Datetime` - The date and time that this starts.
- `imports`: `ImportConnection` (required) (connection) - The connection wrapper around the `Import` type.

---

### SnmpInterfaceNumericResult

**Description**: types.snmp_interface_numeric_result

**Category**: network_interfaces
**Relevance Score**: 4 (Primary: 0, Secondary: 2, Operational: 0)
**Total Fields**: 6

**Key Fields**: `inventory_item_id`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 3 (`inventory_item_id`, `type`, `epoch_system_timezone`)

**All Fields**:

- `time`: `Datetime` - The time.
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `type`: `InterfaceMetric` (enum) - The metric being tracked (e.g. packets per second inbound, errors outbound.)
- `interface`: `String` - The interface.
- `value`: `Float` - The value.
- `epoch_system_timezone`: `EpochTimestamp` - A Unix timestamp in the same timezone as this Sonar instance

---

### AvailableReport

**Description**: An available report.

**Category**: network_interfaces
**Relevance Score**: 3 (Primary: 1, Secondary: 0, Operational: 0)
**Total Fields**: 6

**Key Fields**: `name`

**Relationship Fields**: 4 (`name`, `category`, `endpoint`, `thumbnail_url`)

**All Fields**:

- `name`: `Text` (required) - A descriptive name.
- `category`: `Text` (required) - The category.
- `endpoint`: `Text` (required) - The endpoint.
- `thumbnail_url`: `URL` (required) - The URL to a thumbnail image.
- `is_custom`: `Boolean` (required) - Whether or not this is a custom report.
- `is_user`: `Boolean` (required) - Whether or not this is a personal report.

---

### SystemBackupExportConnection

**Description**: The connection wrapper around the `SystemBackupExportConnection` type.

**Category**: network_interfaces
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SystemBackupExport` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ImportConnection

**Description**: The connection wrapper around the `ImportConnection` type.

**Category**: network_interfaces
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Import` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### FccForm477ReportConnection

**Description**: The connection wrapper around the `FccForm477ReportConnection` type.

**Category**: network_interfaces
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `FccForm477Report` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DidImportRecipeConnection

**Description**: The connection wrapper around the `DidImportRecipeConnection` type.

**Category**: network_interfaces
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DidImportRecipe` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CallDetailRecordImportRecipeConnection

**Description**: The connection wrapper around the `CallDetailRecordImportRecipeConnection` type.

**Category**: network_interfaces
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CallDetailRecordImportRecipe` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CallDetailRecordImportConnection

**Description**: The connection wrapper around the `CallDetailRecordImportConnection` type.

**Category**: network_interfaces
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CallDetailRecordImport` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Network_Protocols Entities (22 total)


### RadiusServer

**Description**: A RADIUS server.

**Category**: network_protocols
**Relevance Score**: 19 (Primary: 5, Secondary: 2, Operational: 0)
**Total Fields**: 23

**Key Fields**: `id`, `sonar_unique_id`, `collect_bandwidth`, `name`

**Enum Fields**: 2 (`status`, `type`)

**Relationship Fields**: 8 (`id`, `ip_address`, `status`, `type`, `radius_server_credentials`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `coa_secret`: `String` - The secret used to send a change of authorization to this device.
- `collect_bandwidth`: `Boolean` (required) - Whether or not Sonar should track bandwidth usage data from this RADIUS server.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `ip_address`: `IP` (required) - An IPv4/IPv6 address.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `name`: `String` (required) - A descriptive name.
- `send_change_auth_on_delinquency`: `Boolean` (required) - Send a change of authorization on account delinquency to this device.
- `send_change_auth_on_service_change`: `Boolean` (required) - Send a change of authorization on account service change to this device.
- `send_change_auth_on_status_change`: `Boolean` (required) - Send a change of authorization on account status change to this device.
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `type`: `RadiusServerType` (required) (enum) - The type.
- `radius_server_credentials`: `RadiusServerCredentialConnection` (required) (connection) - A RADIUS server credential.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SnmpOid

**Description**: An `SnmpOid`.

**Category**: network_protocols
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `divide_by`, `name`, `network_monitoring_graph_id`, `oid`, `snmp_oid_thresholds`

**Relationship Fields**: 8 (`id`, `color`, `network_monitoring_graph_id`, `network_monitoring_graph`, `snmp_oid_thresholds`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `auto_scale`: `Boolean` (required) - Whether or not to auto scale.
- `color`: `HtmlHexColor` (required) - Color.
- `display_as_table`: `Boolean` (required) - Display as table
- `divide_by`: `Int` - Divide by
- `name`: `String` (required) - A descriptive name.
- `network_monitoring_graph_id`: `Int64Bit` (required) - The ID of a `NetworkMonitoringGraph`.
- `oid`: `String` (required) - An OID
- `unit_of_measurement`: `String` - Unit of measurement
- `network_monitoring_graph`: `NetworkMonitoringGraph` - A `NetworkMonitoringGraph`.
- `snmp_oid_thresholds`: `SnmpOidThresholdConnection` (required) (connection) - An `SnmpOidThreshold`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RadiusGroupReplyAttribute

**Description**: A RADIUS group reply attribute.

**Category**: network_protocols
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`, `radius_group_id`

**Enum Fields**: 1 (`operator`)

**Relationship Fields**: 7 (`id`, `operator`, `radius_group_id`, `radius_group`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `operator`: `RadiusReplyOperator` (required) (enum) - A RADIUS reply operator.
- `radius_group_id`: `Int64Bit` (required) - The ID of a `RadiusGroup`.
- `reply`: `String` (required) - A RADIUS reply.
- `radius_group`: `RadiusGroup` - A RADIUS group.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RadiusGroup

**Description**: A RADIUS group.

**Category**: network_protocols
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 19

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 2 (`account_status`, `delinquency`)

**Relationship Fields**: 12 (`id`, `account_status`, `delinquency`, `account_groups`, `account_statuses`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_status`: `AddressListAccountStatus` (required) (enum) - The types of account statuses for accounts that are part of this grouping.
- `delinquency`: `AddressListDelinquency` (required) (enum) - The delinquency state for accounts that are part of this grouping.
- `fall_through`: `Boolean` (required) - Whether or not this is a fall through group.
- `name`: `String` (required) - A descriptive name.
- `priority`: `Int` (required) - The RADIUS priority.
- `account_groups`: `AccountGroupConnection` (required) (connection) - An account group.
- `account_statuses`: `AccountStatusConnection` (required) (connection) - The status of an account.
- `account_types`: `AccountTypeConnection` (required) (connection) - The account type.
- `services`: `ServiceConnection` (required) (connection) - A service.
- `usage_based_billing_policies`: `UsageBasedBillingPolicyConnection` (required) (connection) - A usage based billing policy.
- `radius_group_reply_attributes`: `RadiusGroupReplyAttributeConnection` (required) (connection) - A RADIUS group reply attribute.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SnmpOverride

**Description**: An `SnmpOverride`.

**Category**: network_protocols
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `inventory_item_id`, `snmp3_context_engineid`, `snmp3_context_name`

**Enum Fields**: 4 (`snmp3_auth_protocol`, `snmp3_priv_protocol`, `snmp3_sec_level`, `snmp_version`)

**Relationship Fields**: 15 (`id`, `inventory_item_id`, `snmp3_auth_passphrase`, `snmp3_auth_protocol`, `snmp3_context_engineid`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `snmp3_auth_passphrase`: `Text` - SNMPv3 auth passphrase
- `snmp3_auth_protocol`: `Snmp3AuthProtocol` (enum) - SNMPv3 auth protocol
- `snmp3_context_engineid`: `Text` - SNMPv3 context engine ID
- `snmp3_context_name`: `Text` - SNMPv3 context name
- `snmp3_priv_passphrase`: `Text` - SNMPv3 privacy passphrase
- `snmp3_priv_protocol`: `Snmp3PrivProtocol` (enum) - SNMPv3 privacy protocol
- `snmp3_sec_level`: `Snmp3SecurityLevel` (enum) - SNMPv3 security level
- `snmp_community`: `Text` - SNMP community/securityName
- `snmp_version`: `SnmpVersion` (enum) - SNMP version
- `inventory_item`: `InventoryItem` - An inventory item.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RadiusSessionHistory

**Description**: The history of a RADIUS session.

**Category**: network_protocols
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `account_session_id`, `called_station_id`, `calling_station_id`, `radius_account_id`, `real_session_id`

**Relationship Fields**: 8 (`id`, `ip_address`, `nas_ip_address`, `radius_account_id`, `radius_account`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_session_id`: `String` (required) - Account session ID.
- `called_station_id`: `String` - Called station ID.
- `calling_station_id`: `String` - Calling station ID.
- `disconnect_requested`: `Datetime` - The time that a disconnect was requested.
- `end`: `Datetime` - The end.
- `ip_address`: `IP` - An IPv4/IPv6 address.
- `nas_ip_address`: `IP` - The IP address of the NAS.
- `radius_account_id`: `Int64Bit` (required) - The ID of a `RadiusAccount`.
- `real_session_id`: `String` - The real session ID.
- `start`: `Datetime` (required) - The start.
- `terminate_reason`: `String` - The reason for the session termination.
- `radius_account`: `RadiusAccount` - A RADIUS account.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SnmpOidThresholdViolation

**Description**: An `SnmpOidThresholdViolation`.

**Category**: network_protocols
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `inventory_item_id`, `snmp_oid_threshold_id`, `snmp_oid_threshold`

**Relationship Fields**: 7 (`id`, `inventory_item_id`, `snmp_oid_threshold_id`, `snmp_oid_threshold`, `inventory_item`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `snmp_oid_threshold_id`: `Int64Bit` (required) - The ID of an `SnmpOidThreshold`.
- `snmp_oid_threshold`: `SnmpOidThreshold` - An `SnmpOidThreshold`.
- `inventory_item`: `InventoryItem` - An inventory item.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SnmpOidThreshold

**Description**: An `SnmpOidThreshold`.

**Category**: network_protocols
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `snmp_oid_id`, `snmp_oid_threshold_violations`, `snmp_oid`

**Enum Fields**: 1 (`operator`)

**Relationship Fields**: 8 (`id`, `operator`, `snmp_oid_id`, `snmp_oid_threshold_violations`, `snmp_oid`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `operator`: `RangeOperator` (required) (enum) - An operator.
- `snmp_oid_id`: `Int64Bit` (required) - The ID of an `SnmpOid`.
- `time_period_in_minutes`: `Int` (required) - The amount of time in minutes that the threshold must be violated before it is triggered.
- `value`: `String` (required) - The value.
- `snmp_oid_threshold_violations`: `SnmpOidThresholdViolationConnection` (required) (connection) - An `SnmpOidThresholdViolation`.
- `snmp_oid`: `SnmpOid` - An `SnmpOid`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RadiusServerCredential

**Description**: A RADIUS server credential.

**Category**: network_protocols
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `radius_server_id`

**Enum Fields**: 1 (`credential`)

**Relationship Fields**: 6 (`id`, `credential`, `radius_server_id`, `radius_server`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `credential`: `RadiusServerAuthCredential` (required) (enum) - The credential name.
- `radius_server_id`: `Int64Bit` (required) - The ID of a `RadiusServer`.
- `value`: `String` (required) - The value.
- `radius_server`: `RadiusServer` - A RADIUS server.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SnmpStatusResult

**Description**: types.snmp_status_result

**Category**: network_protocols
**Relevance Score**: 5 (Primary: 1, Secondary: 1, Operational: 0)
**Total Fields**: 4

**Relationship Fields**: 1 (`epoch_system_timezone`)

**All Fields**:

- `time`: `Datetime` - The time.
- `status`: `String` - The status.
- `reason`: `String` - The reason.
- `epoch_system_timezone`: `EpochTimestamp` - A Unix timestamp in the same timezone as this Sonar instance

---

### SnmpResultConnection

**Description**: types.snmp_result

**Category**: network_protocols
**Relevance Score**: 2 (Primary: 0, Secondary: 1, Operational: 0)
**Total Fields**: 3

**Key Fields**: `oid`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 2 (`type`, `results`)

**All Fields**:

- `oid`: `String` (required) - An OID
- `type`: `SnmpResultType` (required) (enum) - An SNMP monitoring result type.
- `results`: `SnmpResult` (required) (list) - SNMP monitoring results.

---

### SnmpResult

**Description**: The connection wrapper around the `SnmpResult` type.

**Category**: network_protocols
**Relevance Score**: 2 (Primary: 0, Secondary: 1, Operational: 0)
**Total Fields**: 7

**Relationship Fields**: 5 (`min_value`, `max_value`, `avg_value`, `count_value`, `epoch_system_timezone`)

**All Fields**:

- `value`: `String` (required) - The value.
- `min_value`: `Int64Bit` - The minimum value found in the period
- `max_value`: `Int64Bit` - The maximum value found in the period
- `avg_value`: `Int64Bit` - The average value found in the period
- `count_value`: `Int64Bit` - The number of datapoints found in the period
- `time`: `Datetime` (required) - The time.
- `epoch_system_timezone`: `EpochTimestamp` - A Unix timestamp in the same timezone as this Sonar instance

---

### RadiusSessionHistoryConnection

**Description**: The connection wrapper around the `RadiusSessionHistoryConnection` type.

**Category**: network_protocols
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RadiusSessionHistory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SnmpOverrideConnection

**Description**: The connection wrapper around the `SnmpOverrideConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SnmpOverride` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SnmpOidThresholdViolationConnection

**Description**: The connection wrapper around the `SnmpOidThresholdViolationConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SnmpOidThresholdViolation` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SnmpOidThresholdConnection

**Description**: The connection wrapper around the `SnmpOidThresholdConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SnmpOidThreshold` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SnmpOidConnection

**Description**: The connection wrapper around the `SnmpOidConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SnmpOid` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SnmpNetworkMonitoringResultConnection

**Description**: A wrapper around SNMP network monitoring results.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 4

**Key Fields**: `inventory_item_id`

**Relationship Fields**: 4 (`network_monitoring_template`, `inventory_item_id`, `snmp_result_connection`, `snmp_status_results`)

**All Fields**:

- `network_monitoring_template`: `NetworkMonitoringTemplate` - fields.network_monitoring_template
- `inventory_item_id`: `Int64Bit` (required) - The ID of an `InventoryItem`.
- `snmp_result_connection`: `SnmpResultConnection` (required) (list) (connection) - fields.snmp_result_connections
- `snmp_status_results`: `SnmpStatusResult` (required) (list) - fields.snmp_status_results

---

### RadiusServerCredentialConnection

**Description**: The connection wrapper around the `RadiusServerCredentialConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RadiusServerCredential` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RadiusServerConnection

**Description**: The connection wrapper around the `RadiusServerConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RadiusServer` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RadiusGroupReplyAttributeConnection

**Description**: The connection wrapper around the `RadiusGroupReplyAttributeConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RadiusGroupReplyAttribute` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RadiusGroupConnection

**Description**: The connection wrapper around the `RadiusGroupConnection` type.

**Category**: network_protocols
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RadiusGroup` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Other Entities (48 total)


### CustomLinksAllowedVariables

**Description**: Variables that are available to be used in Custom Links.

**Category**: other
**Relevance Score**: 6 (Primary: 2, Secondary: 0, Operational: 0)
**Total Fields**: 2

**Key Fields**: `id`, `name`

**Relationship Fields**: 1 (`id`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `name`: `String` (required) - A descriptive name.

---

### SuccessResponseWithId

**Description**: Returned when the result of a mutation is not consistent. The `message` property can sometimes contain a description of the failure, if `success` is false. The id may contain the model created if `success` is true.

**Category**: other
**Relevance Score**: 3 (Primary: 1, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Key Fields**: `id`

**Relationship Fields**: 2 (`message`, `id`)

**All Fields**:

- `success`: `Boolean` (required) - Will be true if the operation succeeded.
- `message`: `Text` - The message.
- `id`: `Int64Bit` - The ID of the entity.

---

### VehicleConnection

**Description**: The connection wrapper around the `VehicleConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Vehicle` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TriggeredMessageConnection

**Description**: The connection wrapper around the `TriggeredMessageConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TriggeredMessage` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SupernetConnection

**Description**: The connection wrapper around the `SupernetConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Supernet` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### StoredViewConnection

**Description**: The connection wrapper around the `StoredViewConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `StoredView` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### StoredFilterConnection

**Description**: The connection wrapper around the `StoredFilterConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `StoredFilter` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SmsOutboundMessageConnection

**Description**: The connection wrapper around the `SmsOutboundMessageConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SmsOutboundMessage` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SmsMessageContentConnection

**Description**: The connection wrapper around the `SmsMessageContentConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SmsMessageContent` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SmsMessageConnection

**Description**: The connection wrapper around the `SmsMessageConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SmsMessage` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SearchFilterConnection

**Description**: The connection wrapper around the `SearchFilterConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SearchFilter` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PurchaseOrderConnection

**Description**: The connection wrapper around the `PurchaseOrderConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PurchaseOrder` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PrintToMailOrderErrorConnection

**Description**: The connection wrapper around the `PrintToMailOrderErrorConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PrintToMailOrderError` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PrintToMailOrderConnection

**Description**: The connection wrapper around the `PrintToMailOrderConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PrintToMailOrder` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PollerConnection

**Description**: The connection wrapper around the `PollerConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Poller` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PageInfo

**Description**: An object that provides information about the current page of results.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 4

**All Fields**:

- `page`: `Int` (required) - The current page of results.
- `total_pages`: `Int` (required) - The total number of pages available.
- `total_count`: `Int` (required) - The total number of records available.
- `records_per_page`: `Int` (required) - The number of records displayed per page.

---

### NoteConnection

**Description**: The connection wrapper around the `NoteConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Note` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetflowWhitelistConnection

**Description**: The connection wrapper around the `NetflowWhitelistConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetflowWhitelist` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetflowOnPremiseConnection

**Description**: The connection wrapper around the `NetflowOnPremiseConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetflowOnPremise` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetflowEndpointConnection

**Description**: The connection wrapper around the `NetflowEndpointConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetflowEndpoint` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ManufacturerConnection

**Description**: The connection wrapper around the `ManufacturerConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Manufacturer` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### LteProviderConnection

**Description**: The connection wrapper around the `LteProviderConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `LteProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### LookerViewLicenseConnection

**Description**: The connection wrapper around the `LookerViewLicenseConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `LookerViewLicense` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### LookerExploreLicenseConnection

**Description**: The connection wrapper around the `LookerExploreLicenseConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `LookerExploreLicense` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### LocalPrefixConnection

**Description**: The connection wrapper around the `LocalPrefixConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `LocalPrefix` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InboundMailboxConnection

**Description**: The connection wrapper around the `InboundMailboxConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InboundMailbox` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IdentityProviderSamlDetailConnection

**Description**: The connection wrapper around the `IdentityProviderSamlDetailConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IdentityProviderSamlDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IdentityProviderMicrosoftDetailConnection

**Description**: The connection wrapper around the `IdentityProviderMicrosoftDetailConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IdentityProviderMicrosoftDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IdentityProviderGoogleDetailConnection

**Description**: The connection wrapper around the `IdentityProviderGoogleDetailConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IdentityProviderGoogleDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IdentityProviderConnection

**Description**: The connection wrapper around the `IdentityProviderConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IdentityProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IdentityProviderActiveDirectoryDetailConnection

**Description**: The connection wrapper around the `IdentityProviderActiveDirectoryDetailConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IdentityProviderActiveDirectoryDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GeofenceConnection

**Description**: The connection wrapper around the `GeofenceConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Geofence` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### GeneralSearchConnection

**Description**: The connection wrapper around the `GeneralSearchConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SearchableInterface` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EpcConnection

**Description**: The connection wrapper around the `EpcConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Epc` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DisputeConnection

**Description**: The connection wrapper around the `DisputeConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Dispute` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DiscountConnection

**Description**: The connection wrapper around the `DiscountConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Discount` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DisbursementDetailConnection

**Description**: The connection wrapper around the `DisbursementDetailConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DisbursementDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DisbursementConnection

**Description**: The connection wrapper around the `DisbursementConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Disbursement` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DidConnection

**Description**: The connection wrapper around the `DidConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Did` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DelinquencyExclusionConnection

**Description**: The connection wrapper around the `DelinquencyExclusionConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DelinquencyExclusion` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DailyAggregateValueConnection

**Description**: The connection wrapper around the `DailyAggregateValueConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DailyAggregateValue` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CustomLinkConnection

**Description**: The connection wrapper around the `CustomLinkConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CustomLink` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CustomFieldConnection

**Description**: The connection wrapper around the `CustomFieldConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CustomField` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CompanyConnection

**Description**: The connection wrapper around the `CompanyConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Company` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CannedReplyConnection

**Description**: The connection wrapper around the `CannedReplyConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CannedReply` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CalixIntegrationConnection

**Description**: The connection wrapper around the `CalixIntegrationConnection` type.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CalixIntegration` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AggregationBucketResult

**Description**: The results of an aggregation.

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 1 (`sub_aggregator_results`)

**All Fields**:

- `value`: `String` (required) - The string that was matched.
- `count`: `String` (required) - The quantity of items matching the string in `bucket_value`.
- `sub_aggregator_results`: `Aggregation` (list) - The results of a sub-aggregation query.

---

### Aggregation

**Description**: types.aggregation

**Category**: other
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 4

**Enum Fields**: 1 (`aggregation_function`)

**Relationship Fields**: 2 (`counts`, `aggregation_function`)

**All Fields**:

- `field`: `String` (required) - The field being aggregated.
- `value`: `String` - The aggregation value, if the aggregation type is anything other than `COUNT`. This is provided as a string to assist with 64bit integer handling in Javascript.
- `counts`: `AggregationBucketResult` (list) - A list of counts, if the aggregation type is `COUNT`.
- `aggregation_function`: `AggregationFunction` (required) (enum) - The AggregationFunction used.

---

## Physical_Assets Entities (1 total)


### SystemBackupSetting

**Description**: The settings for system backups in your Sonar instance.

**Category**: physical_assets
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 4 (`id`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `automatic_backups`: `Boolean` (required) - Whether or not to automatically perform a backup every day.
- `automatic_exports`: `Boolean` (required) - Whether or not to automatically export backups to configured destinations every day.
- `delete_exported_backups`: `Boolean` (required) - Whether or not to automatically delete an exported system backup on a destination configured by a client when pruning exports.
- `in_progress_backup_expire_minutes`: `Int` (required) - The number of minutes to wait until a backup in progress is considered to have failed and is ready to be marked as such.
- `maximum_backups`: `Int` (required) - The maximum number of backups allowed to exist at any given time.
- `maximum_exports`: `Int` (required) - The maximum number of backup exports allowed to exist at any given time.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

## Provisioning Entities (2 total)


### DeploymentType

**Description**: The mode that an inventory item is deployed in.

**Category**: provisioning
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `inventory_model_id`, `name`, `network_monitoring_template_id`

**Relationship Fields**: 9 (`id`, `inventory_model_id`, `network_monitoring_template_id`, `inventory_model`, `network_monitoring_template`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_model_id`: `Int64Bit` (required) - The ID of an `InventoryModel`.
- `name`: `String` (required) - A descriptive name.
- `network_monitoring_template_id`: `Int64Bit` - The ID of a `NetworkMonitoringTemplate`.
- `inventory_model`: `InventoryModel` - A type of item stored in inventory.
- `network_monitoring_template`: `NetworkMonitoringTemplate` - A `NetworkMonitoringTemplate`.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DeploymentTypeConnection

**Description**: The connection wrapper around the `DeploymentTypeConnection` type.

**Category**: provisioning
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DeploymentType` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Roles Entities (11 total)


### TicketGroup

**Description**: A ticket group.

**Category**: roles
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 8 (`id`, `tickets`, `inbound_mailboxes`, `contract_templates`, `users`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` (required) - A descriptive name.
- `private`: `Boolean` (required) - If a group is private, only members of the group can view emails within it.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `inbound_mailboxes`: `InboundMailboxConnection` (required) (connection) - An inbound mailbox.
- `contract_templates`: `ContractTemplateConnection` (required) (connection) - A contract template.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### OrderGroup

**Description**: An order group.

**Category**: roles
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 6 (`id`, `purchase_orders`, `order_group_users`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `automatic_approval_threshold`: `Int` (required) - The threshold at which requesters require approval of their purchase orders.
- `enabled`: `Boolean` (required) - Disabled order groups cannot be assigned users or used to create purchase orders.
- `name`: `String` (required) - The name of an order group.
- `purchase_orders`: `PurchaseOrderConnection` (required) (connection) - A purchase order for items from a third party vendor.
- `order_group_users`: `OrderGroupUserConnection` (required) (connection) - The relationship between an order group and a user.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Role

**Description**: A role defines the permission set that a user has.

**Category**: roles
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Enum Fields**: 1 (`applied_permissions`)

**Relationship Fields**: 7 (`id`, `applied_permissions`, `users`, `adjustment_service_details`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `applied_permissions`: `Permission` (required) (list) (enum) - A list of permissions associated with this role.
- `name`: `String` (required) - A descriptive name.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `adjustment_service_details`: `AdjustmentServiceDetailConnection` (required) (connection) - Details about an adjustment `Service`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PersonalAccessToken

**Description**: An access token for the API.

**Category**: roles
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `token`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `revoked`: `Boolean` (required) - Whether or not this token was revoked.
- `token`: `Text` - The token. Only visible at creation time.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccessLog

**Description**: An access log history on an entity.

**Category**: roles
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `accessloggable_id`, `entity_id`, `entity_name`, `user_id`

**Relationship Fields**: 9 (`id`, `accessloggable_id`, `entity_id`, `user_id`, `accessloggable`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `access_datetime`: `Datetime` (required) - The date and time that this entity was accessed.
- `accessloggable_id`: `Int64Bit` - The ID of the entity that this access log belongs to.
- `accessloggable_type`: `String` - The entity that this access log belongs to.
- `entity_id`: `Int64Bit` - The ID of the entity that this access log belongs to.
- `entity_name`: `String` - The entity that this access log belongs to.
- `user_id`: `Int64Bit` (required) - The ID of the user that accessed this entity.
- `accessloggable`: `AccessloggableInterface` - The entity that this `AccessLog` entry was generated for.
- `user`: `User` - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### StoredGroup

**Description**: A group of filters in a `StoredView`.

**Category**: roles
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `stored_view_id`

**Relationship Fields**: 6 (`id`, `stored_view_id`, `stored_view`, `stored_filters`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `stored_view_id`: `Int64Bit` (required) - The ID of a `StoredView` entity.
- `stored_view`: `StoredView` - A stored view.
- `stored_filters`: `StoredFilterConnection` (required) (connection) - A filter applied in a `StoredView`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AccessLogConnection

**Description**: The connection wrapper around the `AccessLogConnection` type.

**Category**: roles
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AccessLog` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TicketGroupConnection

**Description**: The connection wrapper around the `TicketGroupConnection` type.

**Category**: roles
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TicketGroup` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### StoredGroupConnection

**Description**: The connection wrapper around the `StoredGroupConnection` type.

**Category**: roles
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `StoredGroup` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RoleConnection

**Description**: The connection wrapper around the `RoleConnection` type.

**Category**: roles
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Role` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### OrderGroupConnection

**Description**: The connection wrapper around the `OrderGroupConnection` type.

**Category**: roles
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `OrderGroup` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Scheduling Entities (11 total)


### CalendarIcal

**Description**: An iCalendar calendar.

**Category**: scheduling
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`, `user_id`

**Relationship Fields**: 6 (`id`, `url`, `user_id`, `user`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` - A descriptive name.
- `url`: `URL` - The url that can be used on remote calendars for integration of Sonar events.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleTimeOff

**Description**: Time off that removes availability from a `ScheduleAvailability`.

**Category**: scheduling
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `users`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `end_datetime`: `Datetime` (required) - The date and time that this ends.
- `name`: `String` (required) - A descriptive name.
- `start_datetime`: `Datetime` (required) - The date and time that this starts.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleBlocker

**Description**: An event that blocks off part of a calendar otherwise availability due to `ScheduleAvailability`.

**Category**: scheduling
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `name`, `schedule_blocker_overrides`

**Relationship Fields**: 7 (`id`, `users`, `schedule_blocker_day_times`, `schedule_blocker_overrides`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `infinite_repetitions`: `Boolean` (required) - Whether this repeats forever or not.
- `name`: `String` (required) - A descriptive name.
- `repetitions`: `Int` - The number of times this repeats.
- `start_date`: `Date` (required) - The start date for this `ScheduleAvailability`.
- `weeks_between_repetitions`: `Int` (required) - The number of weeks between repetitions.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `schedule_blocker_day_times`: `ScheduleBlockerDayTimeConnection` (required) (connection) - A day and time associated with a `ScheduleBlocker`.
- `schedule_blocker_overrides`: `ScheduleBlockerOverrideConnection` (required) (connection) - An override to a particular day and time a `ScheduleBlocker` would otherwise cover.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleBlockerOverride

**Description**: An override to a particular day and time a `ScheduleBlocker` would otherwise cover.

**Category**: scheduling
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `schedule_blocker_id`, `user_id`

**Relationship Fields**: 8 (`id`, `schedule_blocker_id`, `user_id`, `user`, `schedule_blocker`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `schedule_blocker_id`: `Int64Bit` (required) - The ID of a `ScheduleBlocker`.
- `start_datetime`: `Datetime` (required) - The date and time that this starts.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `schedule_blocker`: `ScheduleBlocker` - An event that blocks off part of a calendar otherwise availability due to `ScheduleAvailability`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleBlockerDayTime

**Description**: A day and time associated with a `ScheduleBlocker`.

**Category**: scheduling
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `schedule_blocker_id`

**Enum Fields**: 1 (`day`)

**Relationship Fields**: 6 (`id`, `day`, `schedule_blocker_id`, `schedule_blocker`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `day`: `Day` (required) (enum) - A day.
- `end_time`: `Time` (required) - The end time for the day.
- `schedule_blocker_id`: `Int64Bit` (required) - The ID of a `ScheduleBlocker`.
- `start_time`: `Time` (required) - The start time for the day.
- `schedule_blocker`: `ScheduleBlocker` - An event that blocks off part of a calendar otherwise availability due to `ScheduleAvailability`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ScheduleTimeOffConnection

**Description**: The connection wrapper around the `ScheduleTimeOffConnection` type.

**Category**: scheduling
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleTimeOff` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ScheduleResult

**Description**: types.schedule_result

**Category**: scheduling
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 8

**Key Fields**: `schedule_blocker_overrides`

**Relationship Fields**: 7 (`geofences`, `job_types`, `schedule_availability_day_times`, `schedule_blocker_day_times`, `schedule_blocker_overrides`...)

**All Fields**:

- `scheduling_data`: `String` (required) - JSON encoded data used for scheduling.
- `geofences`: `Geofence` (required) (list) - A list of `Geofence`s.
- `job_types`: `JobType` (required) (list) - A list of `JobType`s.
- `schedule_availability_day_times`: `ScheduleAvailabilityDayTime` (required) (list) - A list of `ScheduleAvailabilityDayTime`s.
- `schedule_blocker_day_times`: `ScheduleBlockerDayTime` (required) (list) - A list of `ScheduleBlockerDayTime`s.
- `schedule_blocker_overrides`: `ScheduleBlockerOverride` (required) (list) - Schedule blocker overrides.
- `schedule_time_offs`: `ScheduleTimeOff` (required) (list) - A list of `ScheduleTimeOff`s.
- `users`: `User` (required) (list) - A list of `User`s.

---

### ScheduleBlockerOverrideConnection

**Description**: The connection wrapper around the `ScheduleBlockerOverrideConnection` type.

**Category**: scheduling
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleBlockerOverride` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ScheduleBlockerDayTimeConnection

**Description**: The connection wrapper around the `ScheduleBlockerDayTimeConnection` type.

**Category**: scheduling
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleBlockerDayTime` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ScheduleBlockerConnection

**Description**: The connection wrapper around the `ScheduleBlockerConnection` type.

**Category**: scheduling
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ScheduleBlocker` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CalendarIcalConnection

**Description**: The connection wrapper around the `CalendarIcalConnection` type.

**Category**: scheduling
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CalendarIcal` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Security Entities (4 total)


### Signature

**Description**: A signature.

**Category**: security
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `department_id`, `name`

**Enum Fields**: 1 (`sms_signature`)

**Relationship Fields**: 8 (`id`, `department_id`, `sms_signature`, `department`, `triggered_messages`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `department_id`: `Int64Bit` (required) - The ID of a department.
- `mass_default`: `Boolean` (required) - Whether or not signature is default for mass messages.
- `name`: `String` (required) - A descriptive name.
- `sms_signature`: `SmsContactPrefix` (required) (enum) - Body of an SMS signature.
- `triggered_default`: `Boolean` (required) - Whether or not signature is default for triggered messages.
- `department`: `Department` - A department.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### HandwrittenSignature

**Description**: The signature on a contract.

**Category**: security
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `contact_email_address`, `contact_name`, `signer_name`

**Relationship Fields**: 7 (`id`, `contact_email_address`, `signer_ip`, `contract`, `files`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `contact_email_address`: `EmailAddress` - The email address of the contact that the contract was originally sent to.
- `contact_name`: `String` (required) - The name of the contact that the contract was originally sent to.
- `contact_role`: `String` - The role of the contact that the contract was originally sent to.
- `signer_ip`: `IP` (required) - The IP address of the contract signatory.
- `signer_name`: `String` (required) - The name provided by the contract signatory.
- `contract`: `Contract` - A contract.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SignatureConnection

**Description**: The connection wrapper around the `SignatureConnection` type.

**Category**: security
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Signature` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### HandwrittenSignatureConnection

**Description**: The connection wrapper around the `HandwrittenSignatureConnection` type.

**Category**: security
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `HandwrittenSignature` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Services Entities (58 total)


### Service

**Description**: A service.

**Category**: services
**Relevance Score**: 16 (Primary: 4, Secondary: 2, Operational: 0)
**Total Fields**: 45

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `general_ledger_code_id`, `name`, `reverse_tax_definition_id`, `tax_definition_id`, `general_ledger_code`, `did_assignments`, `did_assignment_histories`

**Enum Fields**: 2 (`application`, `type`)

**Relationship Fields**: 37 (`id`, `application`, `company_id`, `general_ledger_code_id`, `reverse_tax_definition_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `application`: `ServiceApplication` (required) (enum) - How this is applied.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `display_if_zero`: `Boolean` (required) - If the amount for this service is zero, it will still display on invoices.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `general_ledger_code_id`: `Int64Bit` - The ID of a GeneralLedgerCode.
- `name`: `String` (required) - A descriptive name.
- `reverse_tax_definition_id`: `Int64Bit` - The ID of a tax definition on a reversed transaction.
- `tax_definition_id`: `Int64Bit` - The ID of a tax definition on a transaction.
- `type`: `ServiceType` (required) (enum) - The type.
- `recurring_service_detail`: `RecurringServiceDetail` - Details regarding a specific recurring `Service`.
- `expiring_service_detail`: `ExpiringServiceDetail` - Details regarding a specific expiring `Service`.
- `adjustment_service_detail`: `AdjustmentServiceDetail` - Details about an adjustment `Service`.
- `data_service_detail`: `DataServiceDetail` - Details regarding a specific data `Service`.
- `voice_service_detail`: `VoiceServiceDetail` - Details regarding a specific voice `Service`.
- `overage_service_detail`: `OverageServiceDetail` - Details regarding a specific overage `Service`.
- `general_ledger_code`: `GeneralLedgerCode` - A general ledger code.
- `company`: `Company` - A company you do business as.
- `account_services`: `AccountServiceConnection` (required) (connection) - The relationship between an `Account` and a `Service`.
- `billing_services`: `BillingServiceConnection` (required) (connection) - The service items and overrides for linked billing defaults.
- `service_metadata`: `ServiceMetadataConnection` (required) (connection) - Fields that store metadata about individual instances of `Service`s.
- `discounts`: `DiscountConnection` (required) (connection) - A discount.
- `debits`: `DebitConnection` (required) (connection) - A debit.
- `did_assignments`: `DidAssignmentConnection` (required) (connection) - A direct inward dial (DID) assignment.
- `did_assignment_histories`: `DidAssignmentHistoryConnection` (required) (connection) - A historical record of a direct inward dial (DID) assignment.
- `service_taxes`: `ServiceTaxConnection` (required) (connection) - The relationship between a `Service` and a `Tax`.
- `tax_definitions`: `ServiceTaxDefinitionConnection` (required) (connection) - The `TaxDefinition` pair associated to this entity.
- `job_services`: `JobServiceConnection` (required) (connection) - A `Service` associated with a `Job`.
- `package_services`: `PackageServiceConnection` (required) (connection) - The relationship between a `Package` and a `Service`.
- `usage_based_billing_policies`: `UsageBasedBillingPolicyConnection` (required) (connection) - A usage based billing policy.
- `vendor_items`: `VendorItemConnection` (required) (connection) - A set of vendor items attached to an entity.
- `integration_service_mappings`: `IntegrationServiceMappingConnection` (required) (connection) - An entity which maps a service to a vendor specific service name
- `account_groups`: `AccountGroupConnection` (required) (connection) - An account group.
- `radius_groups`: `RadiusGroupConnection` (required) (connection) - A RADIUS group.
- `address_lists`: `AddressListConnection` (required) (connection) - An address list defines some criteria by which to group accounts for network policy enforcement.
- `job_types`: `JobTypeConnection` (required) (connection) - The type of a `Job`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Package

**Description**: A collection of `Service`s.

**Category**: services
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `name`

**Relationship Fields**: 8 (`id`, `company_id`, `company`, `account_services`, `package_services`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` (required) - A descriptive name.
- `rollup_services`: `Boolean` (required) - Setting to indicate if services in this package should be rolled up into a package total when this package is displayed.
- `company`: `Company` - A company you do business as.
- `account_services`: `AccountServiceConnection` (required) (connection) - The relationship between an `Account` and a `Service`.
- `package_services`: `PackageServiceConnection` (required) (connection) - The relationship between a `Package` and a `Service`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceServiceGenericParameter

**Description**: A configurable attribute for a voice service.

**Category**: services
**Relevance Score**: 13 (Primary: 3, Secondary: 2, Operational: 0)
**Total Fields**: 21

**Key Fields**: `id`, `sonar_unique_id`, `reverse_tax_definition_id`, `tax_definition_id`, `voice_service_detail_id`

**Enum Fields**: 1 (`type`)

**Relationship Fields**: 13 (`id`, `reverse_tax_definition_id`, `tax_definition_id`, `type`, `voice_service_detail_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `addition_prorate_date`: `Date` - If this service was prorated when added, this is the date it was prorated from.
- `description`: `String` (required) - A human readable description.
- `price`: `Int` (required) - The price per unit of this item.
- `proratable`: `Boolean` (required) - Indicates if changes to this entity trigger proration.
- `reverse_tax_definition_id`: `Int64Bit` - The ID of a tax definition on a reversed transaction.
- `tax_definition_id`: `Int64Bit` - The ID of a tax definition on a transaction.
- `type`: `VoiceServiceGenericParameterType` (required) (enum) - The type.
- `voice_service_detail_id`: `Int64Bit` (required) - The ID of the `VoiceServiceDetail`.
- `voice_service_detail`: `VoiceServiceDetail` - Details regarding a specific voice `Service`.
- `account_voice_service_details`: `AccountVoiceServiceDetailConnection` (required) (connection) - A voice service configuration that links a service parameter to an account.
- `scheduled_event_account_voice_service_details`: `ScheduledEventAccountVoiceServiceDetailConnection` (required) (connection) - The `AccountVoiceServiceDetail` records used to configure a voice service when a `ScheduledEvent` is executed.
- `tax_definitions`: `VoiceServiceGenericParameterTaxDefinitionConnection` (required) (connection) - The `TaxDefinition` pair associated to this entity.
- `voice_service_generic_parameter_taxes`: `VoiceServiceGenericParameterTaxConnection` (required) (connection) - The relationship between a `VoiceServiceGenericParameter` and a `Tax`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceProviderRateImportRecipe

**Description**: A recipe for importing voice provider rates.

**Category**: services
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 23

**Key Fields**: `id`, `sonar_unique_id`, `flatfile_batch_identifier`, `sonar_batch_identifier`, `user_id`, `voice_provider_id`, `voice_provider`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 11 (`id`, `errors`, `status`, `user_id`, `voice_provider_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `charge_percent`: `Float` (required) - The percentage over the base rate to charge the customer.
- `clean_records`: `Int` - How many records passed validation checks during import.
- `errors`: `Clob` - Any errors encountered for this import.
- `failed_records`: `Int` - How many records did not pass validation checks during import.
- `flatfile_batch_identifier`: `String` - The identifier of a unique batch at Flatfile.
- `hash`: `String` - A hash of the data content of an import.
- `progress`: `Int` - The progress of an import as a percentage.
- `sonar_batch_identifier`: `String` - The unique identifier of an import at Sonar.
- `start_datetime`: `Datetime` - The start date and time for the import.
- `status`: `ImportStatus` (required) (enum) - The status.
- `user_id`: `Int64Bit` - The ID of a User.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `user`: `User` - A user that can login to Sonar.
- `imports`: `ImportConnection` (required) (connection) - An import.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceProviderRateImport

**Description**: An import of voice provider rates.

**Category**: services
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `voice_provider_id`, `voice_provider`

**Enum Fields**: 1 (`status`)

**Relationship Fields**: 10 (`id`, `errors`, `status`, `voice_provider_id`, `voice_provider`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `charge_percent`: `Float` (required) - The percentage over the base rate to charge the customer.
- `clean_records`: `Int` - How many records passed validation checks during import.
- `errors`: `Text` - Any errors encountered for this import.
- `failed_records`: `Int` - How many records did not pass validation checks during import.
- `status`: `AsyncImportStatus` (required) (enum) - The status.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceMetadata

**Description**: Fields that store metadata about individual instances of `Service`s.

**Category**: services
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`, `service_id`

**Relationship Fields**: 6 (`id`, `service_id`, `service`, `service_metadata_values`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service`: `Service` - A service.
- `service_metadata_values`: `ServiceMetadataValueConnection` (required) (connection) - The value of a `ServiceMetadata` field, as it relates to a specific `Service` on a specific `Account`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RateCenter

**Description**: A rate center.

**Category**: services
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `name`, `dids`, `did_import_recipes`

**Relationship Fields**: 6 (`id`, `dids`, `did_import_recipes`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `default`: `Boolean` (required) - Whether or not this entity is a default entry.
- `name`: `String` (required) - A descriptive name.
- `dids`: `DidConnection` (required) (connection) - A direct inward dial (DID).
- `did_import_recipes`: `DidImportRecipeConnection` (required) (connection) - A recipe for importing DIDs.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### FibermapPlan

**Description**: FiberMap plan.

**Category**: services
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 31

**Key Fields**: `id`, `sonar_unique_id`, `fibermap_integration_id`, `fibermap_plan_id`, `fibermap_project_id`, `fibermap_project_name`, `map_overlay_id`, `name`, `network_site_id`

**Relationship Fields**: 16 (`id`, `fibermap_integration_id`, `fibermap_plan_id`, `fibermap_project_id`, `latitude`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `build`: `String` - Build
- `country`: `String` - A two character country code.
- `drop`: `String` - Drop
- `fibermap_integration_id`: `Int64Bit` (required) - FiberMap integration ID
- `fibermap_plan_id`: `Int64Bit` (required) - FiberMap plan ID
- `fibermap_project_id`: `Int64Bit` (required) - Fibermap project ID.
- `fibermap_project_name`: `String` (required) - Fibermap project name.
- `fibermap_updated_at`: `Datetime` - FiberMap updated at
- `height_in_meters`: `Int` (required) - Height in meters.
- `is_visible`: `Boolean` (required) - is_visible of the information
- `latitude`: `Latitude` - A decimal latitude.
- `longitude`: `Longitude` - A decimal longitude.
- `map_overlay_id`: `Int64Bit` - The ID of a map overlay.
- `mapped_at`: `Datetime` - Mapped at
- `mapping_user`: `String` - Mapping user
- `name`: `String` (required) - A descriptive name.
- `network_site_id`: `Int64Bit` - Network site id.
- `subdivision`: `String` - A state, province, or other country subdivision.
- `fibermap_integration`: `FibermapIntegration` - FiberMap integration.
- `network_site`: `NetworkSite` - A network site.
- `map_overlay`: `MapOverlay` - Map Overlay.
- `fibermap_service_locations`: `FibermapServiceLocationConnection` (required) (connection) - FiberMap service location.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceProviderRate

**Description**: A voice provider rate.

**Category**: services
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `voice_provider_id`, `voice_provider`

**Relationship Fields**: 5 (`id`, `voice_provider_id`, `voice_provider`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `base_rate`: `Float` (required) - The rate that is imported from a rate deck.
- `charge_percent`: `Float` (required) - The percentage over the base rate to charge the customer.
- `charge_rate`: `Float` (required) - The rate that is charged to a customer.
- `description`: `String` - The description for the rate.
- `prefix`: `String` (required) - The prefix for the rate.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### JobService

**Description**: A `Service` associated with a `Job`.

**Category**: services
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `job_id`, `service_id`

**Relationship Fields**: 7 (`id`, `job_id`, `service_id`, `service`, `tax`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `job_id`: `Int64Bit` (required) - The ID of a `Job`.
- `quantity`: `Int` (required) - The quantity for this service.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service`: `Service` - A service.
- `tax`: `Tax` - A tax.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DisbursementDetail

**Description**: A disbursement detail.

**Category**: services
**Relevance Score**: 10 (Primary: 3, Secondary: 0, Operational: 1)
**Total Fields**: 26

**Key Fields**: `id`, `sonar_unique_id`, `disbursable_id`, `disbursement_id`, `external_id`, `transaction_id`

**Enum Fields**: 3 (`disbursable_type`, `event`, `fee_unit`)

**Relationship Fields**: 11 (`id`, `disbursable_id`, `disbursable_type`, `disbursement_id`, `event`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` (required) - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `amount_used`: `Int` (required) - The amount used.
- `disbursable_id`: `Int64Bit` - The id of the entity that the disbusement applies to.
- `disbursable_type`: `DisbursableType` (enum) - The type of entity that the disbursement applies to.
- `disbursement_id`: `Int64Bit` (required) - The ID of a `Disbursement`.
- `event`: `DisbursementDetailEvent` (required) (enum) - The event associated with the disbursement detail record.
- `external_id`: `String` (required) - The payment processor's external ID.
- `fee_amount`: `Int` - The amount for this fee.
- `fee_unit`: `SonarPayUnit` (enum) - The unit of measurement for this fee's amount.
- `fractional_amount`: `Int` (required) - The fractional portion of the amount.
- `fractional_amount_used`: `Int` (required) - The fractional portion of the amount used.
- `interchange_flat_rate_fee`: `Int` - The portion of the interchange fee that is a fixed amount. This is stored as the smallest currency value (e.g. cents, pence, pesos.).
- `interchange_percent_fee`: `Int` - The portion of the interchange fee that is based on a percentage of the transaction amount. This is stored as basis points (e.g. 260 represents 2.6%).
- `interchange_type`: `String` - The name of the interchange fee type.
- `is_fee`: `Boolean` (required) - Whether or not this record is a fee.
- `transaction_id`: `String` - The transaction ID from the credit card provider.
- `disbursement`: `Disbursement` - A disbursement.
- `disbursable`: `DisbursableInterface` - The entity for this `DisbursementDetail`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceServiceGenericParameterTaxDefinition

**Description**: The relationship between a `VoiceServiceGenericParameter` and a `TaxDefinition`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `taxdefinitionable_id`, `voice_service_generic_parameter_id`

**Enum Fields**: 1 (`taxdefinitionable_type`)

**Relationship Fields**: 8 (`id`, `taxdefinitionable_id`, `taxdefinitionable_type`, `voice_service_generic_parameter_id`, `voice_service_generic_parameter`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `discount`: `Boolean` (required) - Whether this tax definition is for a discount or not.
- `taxdefinitionable_id`: `Int64Bit` (required) - The ID of entity this tax definition is related to.
- `taxdefinitionable_type`: `TaxdefinitionableType` (required) (enum) - The type of entity this tax definition is related to.
- `voice_service_generic_parameter_id`: `Int64Bit` (required) - The ID of a voice service configuration parameter.
- `voice_service_generic_parameter`: `VoiceServiceGenericParameter` - A configurable attribute for a voice service.
- `taxdefinitionable`: `TaxdefinitionableInterface` - The entity that this `TaxDefinition` is assigned to.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceServiceGenericParameterTax

**Description**: The relationship between a `VoiceServiceGenericParameter` and a `Tax`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `tax_id`, `voice_service_generic_parameter_id`

**Relationship Fields**: 7 (`id`, `tax_id`, `voice_service_generic_parameter_id`, `voice_service_generic_parameter`, `tax`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `exemption_amount`: `Int` (required) - The amount of the service that is exempt from taxation in the smallest currency value (e.g. cents, pence, pesos.)
- `tax_id`: `Int64Bit` (required) - The ID of a Tax.
- `voice_service_generic_parameter_id`: `Int64Bit` (required) - The ID of a voice service configuration parameter.
- `voice_service_generic_parameter`: `VoiceServiceGenericParameter` - A configurable attribute for a voice service.
- `tax`: `Tax` - A tax.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceServiceDetail

**Description**: Details regarding a specific voice `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 26

**Key Fields**: `id`, `sonar_unique_id`, `service_id`

**Enum Fields**: 2 (`country`, `sub_type`)

**Relationship Fields**: 10 (`id`, `country`, `service_id`, `sub_type`, `service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `billing_frequency`: `Int` (required) - How often this service bills, in months.
- `cost_per_minute_local_in_thousandths`: `Int` - The cost per minute for local calls, in thousandths of the smallest currency value (e.g. cents, pence, pesos.).
- `cost_per_minute_long_distance_in_thousandths`: `Int` - The cost per minute for long distance calls, in thousandths of the smallest currency value (e.g. cents, pence, pesos.).
- `country`: `Country` (enum) - A two character country code.
- `first_interval_in_seconds`: `Int` (required) - This is the minimum amount of time the customer will be charged for a call.
- `inbound_toll_free_rate_per_minute_in_thousandths`: `Int` (required) - If a customer has a toll free number, this is the rate charged to them for inbound calls, in thousandths of the smallest currency value (e.g. cents, pence, pesos.).
- `local_minutes`: `Int` - The quantity of free local minutes provided, if `unlimited_local_minutes` is false.
- `long_distance_minutes`: `Int` - The quantity of free long distance minutes provided, if `unlimited_long_distance_minutes` is false.
- `rollup_generic_parameters`: `Boolean` (required) - Hide parameters of this service on customer invoices/statements and in the customer portal.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `show_call_detail_records_on_invoice`: `Boolean` (required) - Indicates if Call Detail Records (CDRs) for this service should be displayed on an invoice.
- `sub_interval_in_seconds`: `Int` (required) - After the `first_interval_in_seconds` time is exceeded, this is the minimum amount of subsequent time. For example, if `first_interval_in_seconds` is 30, and `sub_interval_in_seconds` is 6, then a 31 second call would be charged at 36 seconds, and a 37 second call would be charged at 42 seconds.
- `sub_type`: `VoiceServiceDetailSubType` (required) (enum) - The sub type of this voice service.
- `unlimited_local_minutes`: `Boolean` (required) - Whether this service provides unlimited local minutes.
- `unlimited_long_distance_minutes`: `Boolean` (required) - Whether this service provides unlimited long distance minutes.
- `service`: `Service` - A service.
- `local_prefixes`: `LocalPrefixConnection` (required) (connection) - A local prefix for a voice service.
- `voice_service_generic_parameters`: `VoiceServiceGenericParameterConnection` (required) (connection) - A configurable attribute for a voice service.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Subscription

**Description**: A subscription to notifications for an entity.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `subscribable_id`, `user_id`

**Enum Fields**: 1 (`subscribable_type`)

**Relationship Fields**: 8 (`id`, `subscribable_id`, `subscribable_type`, `user_id`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `is_suspended`: `Boolean` (required) - When suspended, the subscription will not send notifications. Permission changes and other actions may cause a subscription to become suspended.
- `subscribable_id`: `Int64Bit` (required) - The id of the entity that is being subscribed to.
- `subscribable_type`: `SubscribableType` (required) (enum) - The type of entity that is being subscribed to.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `subscribable`: `SubscribableInterface` - The entity that this `Subscription` is associated with.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceTaxDefinition

**Description**: The relationship between a `Service` and a `TaxDefinition`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `service_id`, `taxdefinitionable_id`

**Enum Fields**: 1 (`taxdefinitionable_type`)

**Relationship Fields**: 8 (`id`, `service_id`, `taxdefinitionable_id`, `taxdefinitionable_type`, `service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `discount`: `Boolean` (required) - Whether this tax definition is for a discount or not.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `taxdefinitionable_id`: `Int64Bit` (required) - The ID of entity this tax definition is related to.
- `taxdefinitionable_type`: `TaxdefinitionableType` (required) (enum) - The type of entity this tax definition is related to.
- `service`: `Service` - A service.
- `taxdefinitionable`: `TaxdefinitionableInterface` - The entity that this `TaxDefinition` is assigned to.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceTax

**Description**: The relationship between a `Service` and a `Tax`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `service_id`, `tax_id`

**Relationship Fields**: 7 (`id`, `service_id`, `tax_id`, `service`, `tax`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `exemption_amount`: `Int` (required) - The amount of the service that is exempt from taxation in the smallest currency value (e.g. cents, pence, pesos.)
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `tax_id`: `Int64Bit` (required) - The ID of a Tax.
- `service`: `Service` - A service.
- `tax`: `Tax` - A tax.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ServiceMetadataValue

**Description**: The value of a `ServiceMetadata` field, as it relates to a specific `Service` on a specific `Account`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `account_service_id`, `service_metadata_id`

**Relationship Fields**: 7 (`id`, `account_service_id`, `service_metadata_id`, `account_service`, `service_metadatum`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_service_id`: `Int64Bit` (required) - The ID of an AccountService.
- `service_metadata_id`: `Int64Bit` (required) - The ID of a ServiceMetadata field.
- `value`: `String` (required) - The value.
- `account_service`: `AccountService` - The relationship between an `Account` and a `Service`.
- `service_metadatum`: `ServiceMetadata` - Fields that store metadata about individual instances of `Service`s.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### RecurringServiceDetail

**Description**: Details regarding a specific recurring `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `service_id`

**Relationship Fields**: 5 (`id`, `service_id`, `service`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `billing_frequency`: `Int` (required) - How often this service bills, in months.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service`: `Service` - A service.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### PackageService

**Description**: The relationship between a `Package` and a `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `package_id`, `service_id`

**Relationship Fields**: 7 (`id`, `package_id`, `service_id`, `package`, `service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `package_id`: `Int64Bit` (required) - The ID of a `Package`.
- `quantity`: `Int` (required) - The quantity for this service.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `package`: `Package` - A collection of `Service`s.
- `service`: `Service` - A service.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### OverageServiceDetail

**Description**: Details regarding a specific overage `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `service_id`

**Relationship Fields**: 6 (`id`, `service_id`, `service`, `notes`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `gigabytes`: `Int` (required) - A value in gigabytes.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service`: `Service` - A service.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### NetworkSiteServiceableAddressList

**Description**: Network site serviceable address list.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `network_site_id`

**Relationship Fields**: 7 (`id`, `network_site_id`, `network_site`, `addresses`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `network_site_id`: `Int64Bit` (required) - Network site id.
- `network_site`: `NetworkSite` - A network site.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### LocalPrefix

**Description**: A local prefix for a voice service.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `voice_service_detail_id`

**Relationship Fields**: 7 (`id`, `prefix`, `voice_service_detail_id`, `voice_service_detail`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `prefix`: `Numeric` (required) - A telephone number prefix.
- `voice_service_detail_id`: `Int64Bit` (required) - The ID of the `VoiceServiceDetail`.
- `voice_service_detail`: `VoiceServiceDetail` - Details regarding a specific voice `Service`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### IntegrationServiceMapping

**Description**: An entity which maps a service to a vendor specific service name

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `integrationconfigurable_id`, `service_id`, `service_template_name`

**Relationship Fields**: 8 (`id`, `integrationconfigurable_id`, `service_id`, `service`, `integrationconfigurable`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `adtran_mosaic_profile_vector`: `String` - The profile vector name in Adtran Mosaic this mapping refers to.
- `integrationconfigurable_id`: `Int64Bit` - The ID of the configuration entity which owns this mapping.
- `integrationconfigurable_type`: `String` - The type of the configuration entity which owns this mapping.
- `policy_map`: `String` - Policy Map.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service_template_name`: `String` - The service name in vendor system this mapping refers to.
- `service`: `Service` - A service.
- `integrationconfigurable`: `IntegrationconfigurableInterface` - The owner of the integration mapping
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### FibermapServiceLocation

**Description**: FiberMap service location.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `address_id`, `child_vetro_id`, `fibermap_integration_id`, `fibermap_plan_id`, `vetro_id`

**Relationship Fields**: 10 (`id`, `address_id`, `fibermap_integration_id`, `fibermap_plan_id`, `properties_json`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `address_id`: `Int64Bit` - The ID of the address.
- `child_properties_json`: `String` (required) - Child properties JSON
- `child_vetro_id`: `String` - Child Vetro ID
- `fibermap_integration_id`: `Int64Bit` (required) - FiberMap integration ID
- `fibermap_plan_id`: `Int64Bit` (required) - FiberMap plan ID
- `is_visible`: `Boolean` (required) - is_visible of the information
- `properties_json`: `Text` (required) - Properties JSON
- `vetro_id`: `String` (required) - Vetro ID
- `address`: `Address` - A geographical address.
- `fibermap_plan`: `FibermapPlan` - FiberMap plan.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### ExpiringServiceDetail

**Description**: Details regarding a specific expiring `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `service_id`

**Relationship Fields**: 5 (`id`, `service_id`, `service`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `billing_frequency`: `Int` (required) - How often this service bills, in months.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `times_to_run`: `Int` (required) - The number of times this expiring service should run.
- `service`: `Service` - A service.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Did

**Description**: A direct inward dial (DID).

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `number`, `rate_center_id`, `voice_provider_id`, `voice_provider`, `did_assignments`, `did_assignment_histories`

**Relationship Fields**: 10 (`id`, `rate_center_id`, `voice_provider_id`, `voice_provider`, `rate_center`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `number`: `String` (required) - The number.
- `rate_center_id`: `Int64Bit` - The ID of a `RateCenter`.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `rate_center`: `RateCenter` - A rate center.
- `did_assignments`: `DidAssignmentConnection` (required) (connection) - A direct inward dial (DID) assignment.
- `did_assignment_histories`: `DidAssignmentHistoryConnection` (required) (connection) - A historical record of a direct inward dial (DID) assignment.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DataServiceDetail

**Description**: Details regarding a specific data `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `service_id`, `technology_code`, `telrad_global_service_profile_name`, `usage_based_billing_policy_id`

**Enum Fields**: 1 (`technology_code`)

**Relationship Fields**: 9 (`id`, `service_id`, `technology_code`, `usage_based_billing_policy_id`, `service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `billing_frequency`: `Int` (required) - How often this service bills, in months.
- `download_speed_kilobits_per_second`: `Int` (required) - The download speed of the service in kilobits per second.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `technology_code`: `TechnologyCode` (required) (enum) - The FCC technology code for the service. Only relevant to US ISPs filing FCC Form 477.
- `telrad_global_service_profile_name`: `String` - The global service profile name for this service if using Telrad provisioning.
- `upload_speed_kilobits_per_second`: `Int` (required) - The upload speed of the service in kilobits per second.
- `usage_based_billing_policy_id`: `Int64Bit` - The ID of a `UsageBasedBillingPolicy`.
- `service`: `Service` - A service.
- `usage_based_billing_policy`: `UsageBasedBillingPolicy` - A usage based billing policy.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### BillingService

**Description**: The service items and overrides for linked billing defaults.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `anchor_subsidy`, `billing_default_id`, `name_override`, `service_id`

**Relationship Fields**: 7 (`id`, `billing_default_id`, `service_id`, `billing_default`, `service`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `anchor_subsidy`: `Int` - The amount of the service that will be invoiced to the anchor account.  Cannot exceed price provided.
- `billing_default_id`: `Int64Bit` (required) - The ID of a BillingDefault.
- `name_override`: `String` - Overriding the service name will alter the service name printed on an invoice.
- `price`: `Int` - The price per unit of this item.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `billing_default`: `BillingDefault` - Default billing settings that are applied to some accounts on creation.
- `service`: `Service` - A service.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AdjustmentServiceDetail

**Description**: Details about an adjustment `Service`.

**Category**: services
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `service_id`

**Relationship Fields**: 6 (`id`, `service_id`, `service`, `roles`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `amount`: `Int` - The amount that can be adjusted using this service within the period defined in `adjustment_service_days`.
- `days`: `Int` - The period of time in which transactions are tracked to calculate against the total defined in `adjustment_service_amount`.
- `service_id`: `Int64Bit` (required) - The ID of a Service.
- `service`: `Service` - A service.
- `roles`: `RoleConnection` (required) (connection) - A role defines the permission set that a user has.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### JobServiceConnection

**Description**: The connection wrapper around the `JobServiceConnection` type.

**Category**: services
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `JobService` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceServiceGenericParameterTaxDefinitionConnection

**Description**: The connection wrapper around the `VoiceServiceGenericParameterTaxDefinitionConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceServiceGenericParameterTaxDefinition` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceServiceGenericParameterTaxConnection

**Description**: The connection wrapper around the `VoiceServiceGenericParameterTaxConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceServiceGenericParameterTax` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceServiceGenericParameterConnection

**Description**: The connection wrapper around the `VoiceServiceGenericParameterConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceServiceGenericParameter` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceServiceDetailConnection

**Description**: The connection wrapper around the `VoiceServiceDetailConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceProviderRateImportRecipeConnection

**Description**: The connection wrapper around the `VoiceProviderRateImportRecipeConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceProviderRateImportRecipe` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceProviderRateImportConnection

**Description**: The connection wrapper around the `VoiceProviderRateImportConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceProviderRateImport` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### VoiceProviderRateConnection

**Description**: The connection wrapper around the `VoiceProviderRateConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceProviderRate` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SubscriptionConnection

**Description**: The connection wrapper around the `SubscriptionConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Subscription` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ServiceTaxDefinitionConnection

**Description**: The connection wrapper around the `ServiceTaxDefinitionConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ServiceTaxDefinition` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ServiceTaxConnection

**Description**: The connection wrapper around the `ServiceTaxConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ServiceTax` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ServiceMetadataValueConnection

**Description**: The connection wrapper around the `ServiceMetadataValueConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ServiceMetadataValue` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ServiceMetadataConnection

**Description**: The connection wrapper around the `ServiceMetadataConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ServiceMetadata` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ServiceConnection

**Description**: The connection wrapper around the `ServiceConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Service` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RecurringServiceDetailConnection

**Description**: The connection wrapper around the `RecurringServiceDetailConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RecurringServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### RateCenterConnection

**Description**: The connection wrapper around the `RateCenterConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `RateCenter` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PackageServiceConnection

**Description**: The connection wrapper around the `PackageServiceConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `PackageService` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### PackageConnection

**Description**: The connection wrapper around the `PackageConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Package` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### OverageServiceDetailConnection

**Description**: The connection wrapper around the `OverageServiceDetailConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `OverageServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetworkSiteServiceableAddressListConnection

**Description**: The connection wrapper around the `NetworkSiteServiceableAddressListConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetworkSiteServiceableAddressList` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### IntegrationServiceMappingConnection

**Description**: The connection wrapper around the `IntegrationServiceMappingConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `IntegrationServiceMapping` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InstanceServiceFunds

**Description**: types.instance_service_funds

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 5

**Key Fields**: `core_service_id`

**Enum Fields**: 2 (`instance_service_fund_type`, `cost_precision`)

**Relationship Fields**: 3 (`core_service_id`, `instance_service_fund_type`, `cost_precision`)

**All Fields**:

- `core_service_id`: `Int64Bit` (required) - The service ID in core used to fund the instance service.
- `available_funds_in_hundredths`: `Int` (required) - The amount of funds currently available for the instance service. Stored as one hundredth of the smallest currency value (e.g. cents, pence, pesos.)
- `instance_service_fund_type`: `InstanceServiceFundType` (enum) - The instance service fund type.
- `auto_pay`: `Boolean` - Whether the instance service is paid for automatically.
- `cost_precision`: `FundedServiceCostPrecision` (enum) - The precision used for the costs associated with this funded service.

---

### FibermapServiceLocationConnection

**Description**: The connection wrapper around the `FibermapServiceLocationConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `FibermapServiceLocation` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### FibermapPlanConnection

**Description**: The connection wrapper around the `FibermapPlanConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `FibermapPlan` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### ExpiringServiceDetailConnection

**Description**: The connection wrapper around the `ExpiringServiceDetailConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `ExpiringServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### DataServiceDetailConnection

**Description**: The connection wrapper around the `DataServiceDetailConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DataServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### BillingServiceConnection

**Description**: The connection wrapper around the `BillingServiceConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `BillingService` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### AdjustmentServiceDetailConnection

**Description**: The connection wrapper around the `AdjustmentServiceDetailConnection` type.

**Category**: services
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `AdjustmentServiceDetail` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Sites Entities (13 total)


### LteProvider

**Description**: A provider of LTE provisioning.

**Category**: sites
**Relevance Score**: 19 (Primary: 5, Secondary: 2, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `name`, `lte_provider_credentials`

**Enum Fields**: 2 (`status`, `type`)

**Relationship Fields**: 7 (`id`, `status`, `type`, `lte_provider_credentials`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `deactivate_on_delinquency`: `Boolean` (required) - Automatically detach UE when account is changed to delinquency status.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `floating_license`: `Boolean` (required) - Whether or not a floating license model is used with BreezeVIEW.
- `last_synchronized`: `Datetime` - The date and time this device was last synchronized.
- `name`: `String` (required) - A descriptive name.
- `status`: `ProvisioningDeviceStatus` (enum) - The status.
- `status_message`: `String` - A message describing what caused the current status of this device.
- `synchronization_queued`: `Boolean` (required) - Whether or not a synchronization request is queued.
- `synchronization_start`: `Datetime` - The date/time that synchronization started.
- `type`: `LteProviderType` (required) (enum) - The type.
- `write_pdn_address_allocation`: `Boolean` (required) - Write PDN address allocation into BreezeVIEW.
- `lte_provider_credentials`: `LteProviderCredentialConnection` (required) (connection) - Credentials for an `LteProvider`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### StoredView

**Description**: A stored view.

**Category**: sites
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `created_by_user_id`, `name`

**Enum Fields**: 2 (`sort_direction`, `type`)

**Relationship Fields**: 10 (`id`, `created_by_user_id`, `sort_direction`, `type`, `created_by_user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `created_by_user_id`: `Int64Bit` - The ID of the user that created this entity.
- `is_global`: `Boolean` (required) - Whether or not this StoredView is available to all users.
- `location`: `String` (required) - The location in the UI that this view is available.
- `name`: `String` (required) - A name to identify this `StoredView`.
- `sort_column`: `String` - The column used to sort the filtered results.
- `sort_direction`: `SortDirection` (enum) - The direction to sort in.
- `type`: `StoredViewType` (required) (enum) - The type of `StoredView`.
- `created_by_user`: `User` - The ID of the user that created this entity.
- `stored_groups`: `StoredGroupConnection` (required) (connection) - A group of filters in a `StoredView`.
- `stored_view_users`: `StoredViewUserConnection` (required) (connection) - A `StoredView` associated with a `User`.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VehicleLocationHistory

**Description**: A history of where the vehicle has travelled.

**Category**: sites
**Relevance Score**: 13 (Primary: 4, Secondary: 0, Operational: 1)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `vehicle_id`

**Relationship Fields**: 7 (`id`, `latitude`, `longitude`, `vehicle_id`, `vehicle`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `latitude`: `Latitude` (required) - A decimal latitude.
- `longitude`: `Longitude` (required) - A decimal longitude.
- `odometer`: `Int` - Odometer without unit of measure.
- `odometer_um`: `String` - Unit of measure for odometer.
- `speed`: `Int` - Speed without unit of measure.
- `speed_um`: `String` - Unit of measure for speed.
- `status`: `String` - The status.
- `vehicle_id`: `Int64Bit` (required) - The ID of a `Vehicle`.
- `vehicle`: `Vehicle` - A vehicle.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Vehicle

**Description**: A vehicle.

**Category**: sites
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 34

**Key Fields**: `id`, `sonar_unique_id`, `gps_tracking_day_friday`, `gps_tracking_provider_id`, `gps_tracking_uid`, `name`, `gps_tracking_provider`

**Enum Fields**: 1 (`gps_tracking_timezone`)

**Relationship Fields**: 13 (`id`, `geopoint`, `gps_tracking_provider_id`, `gps_tracking_timezone`, `gps_tracking_provider`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `geopoint`: `Geopoint` - A geo-point.
- `gps_tracking_always`: `Boolean` (required) - Whether or not to always track the vehicle.
- `gps_tracking_day_friday`: `Boolean` (required) - If not always, then track on Friday.
- `gps_tracking_day_monday`: `Boolean` (required) - If not always, then track on Monday.
- `gps_tracking_day_saturday`: `Boolean` (required) - If not always, then track on Saturday.
- `gps_tracking_day_sunday`: `Boolean` (required) - If not always, then track on Sunday.
- `gps_tracking_day_thursday`: `Boolean` (required) - If not always, then track on Thursday.
- `gps_tracking_day_tuesday`: `Boolean` (required) - If not always, then track on Tuesday.
- `gps_tracking_day_wednesday`: `Boolean` (required) - If not always, then track on Wednesday.
- `gps_tracking_enabled`: `Boolean` (required) - Whether or not GPS Tracking enabled for vehicle.
- `gps_tracking_end_time`: `Time` (required) - If not always, end time for tracking.
- `gps_tracking_provider_id`: `Int64Bit` - A `GpsTrackingProvider` ID.
- `gps_tracking_start_time`: `Time` (required) - If not always, start time for tracking.
- `gps_tracking_timezone`: `Timezone` (enum) - If not always, timezone for start and end times.
- `gps_tracking_uid`: `String` - A GPS Tracking Provider vehicle unique identifier.
- `manufacturer`: `String` - The manufacturer.
- `model`: `String` - The model.
- `name`: `String` (required) - A descriptive name.
- `vin`: `String` - The vehicle identification number.
- `year`: `Int` - A year.
- `gps_tracking_provider`: `GpsTrackingProvider` - A `GpsTrackingProvider`.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `users`: `UserConnection` (required) (connection) - A user that can login to Sonar.
- `vehicle_location_histories`: `VehicleLocationHistoryConnection` (required) (connection) - A history of where the vehicle has travelled.

---

### NetworkSite

**Description**: A network site.

**Category**: sites
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 31

**Key Fields**: `id`, `sonar_unique_id`, `company_id`, `name`, `emails`

**Relationship Fields**: 25 (`id`, `company_id`, `geopoint`, `network_site_serviceable_address_list`, `company`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `geopoint`: `Geopoint` - A geo-point.
- `height_in_meters`: `Float` (required) - Height in meters.
- `name`: `String` (required) - A descriptive name.
- `network_site_serviceable_address_list`: `NetworkSiteServiceableAddressList` - Network site serviceable address list.
- `company`: `Company` - A company you do business as.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `jobs`: `JobConnection` (required) (connection) - A job, typically in the field.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `ip_assignments`: `IpAssignmentConnection` (required) (connection) - An IP address assignment.
- `ip_assignment_histories`: `IpAssignmentHistoryConnection` (required) (connection) - A historical record of an IP assignment.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `files`: `FileConnection` (required) (connection) - A file.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `alerting_rotations`: `AlertingRotationConnection` (required) (connection) - An alerting rotation.
- `linked_tickets`: `TicketConnection` (required) (connection) - Tickets that are linked to this item.
- `map_overlays`: `MapOverlayConnection` (required) (connection) - Map Overlay.
- `fibermap_plans`: `FibermapPlanConnection` (required) (connection) - FiberMap plan.

---

### InventoryLocation

**Description**: A location that inventory is stored in.

**Category**: sites
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 18

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 12 (`id`, `geopoint`, `addresses`, `inventory_items`, `generic_inventory_items`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `default_shipping_location`: `Boolean` (required) - Marks this inventory location as the default shipping location for purchase orders.
- `geopoint`: `Geopoint` - A geo-point.
- `name`: `String` (required) - A descriptive name.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `internal_locations`: `InternalLocationConnection` (required) (connection) - A location inside an `InventoryLocation` (e.g. a shelf or a room.)
- `purchase_orders`: `PurchaseOrderConnection` (required) (connection) - A purchase order for items from a third party vendor.
- `inventory_model_min_maxes`: `InventoryModelMinMaxConnection` (required) (connection) - Defines the minimum and maximum of an inventory level per location per inventory model.

---

### InternalLocation

**Description**: A location inside an `InventoryLocation` (e.g. a shelf or a room.)

**Category**: sites
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 14

**Key Fields**: `id`, `sonar_unique_id`, `inventory_location_id`, `name`

**Relationship Fields**: 9 (`id`, `inventory_location_id`, `inventory_location`, `inventory_items`, `generic_inventory_items`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `inventory_location_id`: `Int64Bit` (required) - The ID of an `InventoryLocation`.
- `name`: `String` (required) - A descriptive name.
- `inventory_location`: `InventoryLocation` - A location that inventory is stored in.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `generic_inventory_item_action_logs`: `GenericInventoryItemActionLogConnection` (required) (connection) - A log of an action taken against a set of generic inventory items.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailLocation

**Description**: The location of a single opened or clicked email.

**Category**: sites
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `postal_code`, `email_opens`, `email_clicks`

**Relationship Fields**: 7 (`id`, `latitude`, `longitude`, `email_opens`, `email_clicks`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `city`: `String` (required) - A city.
- `country`: `String` (required) - A two character country code.
- `latitude`: `Latitude` (required) - A decimal latitude.
- `longitude`: `Longitude` (required) - A decimal longitude.
- `postal_code`: `String` (required) - The zip code of an email location sent by a Mandrill event.
- `timezone`: `String` (required) - The timezone you want times in the system displayed in.
- `email_opens`: `EmailOpenConnection` (required) (connection) - A single open for a sent email.
- `email_clicks`: `EmailClickConnection` (required) (connection) - A single click for a sent email.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VehicleLocationHistoryConnection

**Description**: The connection wrapper around the `VehicleLocationHistoryConnection` type.

**Category**: sites
**Relevance Score**: 1 (Primary: 0, Secondary: 0, Operational: 1)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VehicleLocationHistory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### NetworkSiteConnection

**Description**: The connection wrapper around the `NetworkSiteConnection` type.

**Category**: sites
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `NetworkSite` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InventoryLocationConnection

**Description**: The connection wrapper around the `InventoryLocationConnection` type.

**Category**: sites
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InventoryLocation` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InternalLocationConnection

**Description**: The connection wrapper around the `InternalLocationConnection` type.

**Category**: sites
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InternalLocation` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailLocationConnection

**Description**: The connection wrapper around the `EmailLocationConnection` type.

**Category**: sites
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailLocation` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Tickets Entities (24 total)


### TicketCategory

**Description**: A ticket category.

**Category**: tickets
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 11

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `tickets`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `name`: `String` (required) - A descriptive name.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Ticket

**Description**: A ticket.

**Category**: tickets
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 45

**Key Fields**: `id`, `sonar_unique_id`, `closed_by_user_id`, `company_id`, `inbound_mailbox_id`, `parent_ticket_id`, `ticket_group_id`, `ticketable_id`, `user_id`, `originating_emails`, `emails`

**Enum Fields**: 3 (`priority`, `status`, `ticketable_type`)

**Relationship Fields**: 35 (`id`, `closed_by_user_id`, `company_id`, `description`, `inbound_mailbox_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `global_updated_at`: `Datetime` - The last date and time this entity was updated, or was the subject of a log.
- `closed_at`: `Datetime` - The time this was closed at.
- `closed_by_user_id`: `Int64Bit` - The ID of the `User` that closed this.
- `company_id`: `Int64Bit` - The ID of the company that this entity operates under.
- `description`: `Text` (required) - A human readable description.
- `due_date`: `Date` - The date this invoice is due by.
- `inbound_mailbox_id`: `Int64Bit` - The ID of an `InboundMailbox`.
- `is_spam`: `Boolean` - Indicates if this ticket is marked as spam.
- `parent_ticket_id`: `Int64Bit` - The ID of the `Ticket` that this `Ticket` is a child of.
- `priority`: `TicketPriority` (required) (enum) - The priority of this item.
- `spam_score`: `Float` - Mail processor's spam rating for whether or not this is spam.
- `status`: `TicketStatus` (required) (enum) - The status.
- `subject`: `String` (required) - The subject.
- `ticket_group_id`: `Int64Bit` - The ID of a `TicketGroup`.
- `ticketable_id`: `Int64Bit` - The ID of the entity that this `Ticket` is associated with.
- `ticketable_type`: `TicketableType` (enum) - The type of entity that this `Ticket` is associated with.
- `user_id`: `Int64Bit` - The ID of a User.
- `ticketable`: `TicketableInterface` - The entity that this `Ticket` is associated with.
- `ticket_group`: `TicketGroup` - A ticket group.
- `user`: `User` - A user that can login to Sonar.
- `inbound_mailbox`: `InboundMailbox` - An inbound mailbox.
- `parent_ticket`: `Ticket` - The `Ticket` that is a parent of this `Ticket`.
- `closed_by_user`: `User` - The `User` that closed this.
- `ticket_categories`: `TicketCategoryConnection` (required) (connection) - A ticket category.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `network_sites`: `NetworkSiteConnection` (required) (connection) - A network site.
- `originating_emails`: `EmailConnection` (required) (connection) - The originating `Email` for this `Ticket`.
- `ticket_recipients`: `TicketRecipientConnection` (required) (connection) - A ticket recipient.
- `ticket_replies`: `TicketReplyConnection` (required) (connection) - A reply on a `Ticket`.
- `child_tickets`: `TicketConnection` (required) (connection) - `Ticket`s that are children of this `Ticket`.
- `ticket_comments`: `TicketCommentConnection` (required) (connection) - A comment on a `Ticket`.
- `jobs`: `JobConnection` (required) (connection) - A job, typically in the field.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `files`: `FileConnection` (required) (connection) - A file.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `subscriptions`: `SubscriptionConnection` (required) (connection) - A subscription to notifications for an entity.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `custom_field_data`: `CustomFieldDataConnection` (required) (connection) - Data entered into a `CustomField`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TaskTemplate

**Description**: A `task template`.

**Category**: tickets
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `task_template_items`, `job_types`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `task_template_items`: `TaskTemplateItemConnection` (required) (connection) - A `task template item`.
- `job_types`: `JobTypeConnection` (required) (connection) - The type of a `Job`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### SavedMessageCategory

**Description**: Saved message category.

**Category**: tickets
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `name`, `email_messages`

**Relationship Fields**: 5 (`id`, `email_messages`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `email_messages`: `EmailMessageConnection` (required) (connection) - An email message.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### MessageCategory

**Description**: A categorization of a message by type.

**Category**: tickets
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`, `triggered_emails`

**Relationship Fields**: 7 (`id`, `contacts`, `triggered_messages`, `triggered_emails`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `default`: `Boolean` (required) - Whether or not this entity is a default entry.
- `name`: `String` (required) - A descriptive name.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `triggered_emails`: `TriggeredEmailConnection` (required) (connection) - An `Email` that is sent when a particular event occurs.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### EmailCategory

**Description**: A categorization of an `Email` by type.

**Category**: tickets
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `name`, `triggered_emails`

**Relationship Fields**: 7 (`id`, `contacts`, `triggered_messages`, `triggered_emails`, `notes`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `default`: `Boolean` (required) - Whether or not this entity is a default entry.
- `name`: `String` (required) - A descriptive name.
- `contacts`: `ContactConnection` (required) (connection) - A contact person.
- `triggered_messages`: `TriggeredMessageConnection` (required) (connection) - A message that is sent when a specific event occurs.
- `triggered_emails`: `TriggeredEmailConnection` (required) (connection) - An `Email` that is sent when a particular event occurs.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CannedReplyCategory

**Description**: A canned reply category.

**Category**: tickets
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `name`

**Relationship Fields**: 5 (`id`, `canned_replies`, `notes`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `canned_replies`: `CannedReplyConnection` (required) (connection) - A canned reply.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TicketingSetting

**Description**: Ticketing configuration settings.

**Category**: tickets
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 10

**Key Fields**: `id`, `sonar_unique_id`, `days_closed_before_inbound_email_creates_new_ticket`

**Relationship Fields**: 3 (`id`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `days_closed_before_inbound_email_creates_new_ticket`: `Int` - The number of days a ticket needs to be closed before new inbound emails will create a new ticket rather than re-open the existing one.
- `spam_score_maximum_for_autoreply`: `Int` - The highest spam score a ticket can have to be auto-replied.
- `spam_score_minimum_for_reject`: `Int` - The lowest spam score a ticket must pass or else be rejected.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TicketReply

**Description**: A reply on a `Ticket`.

**Category**: tickets
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 20

**Key Fields**: `id`, `sonar_unique_id`, `author_email`, `ticket_id`, `user_id`, `emails`

**Relationship Fields**: 14 (`id`, `author_email`, `body`, `headers`, `raw_body`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `author`: `String` - The author.
- `author_email`: `EmailAddress` - The email address of the author.
- `body`: `Text` (required) - The body.
- `headers`: `Text` - The email headers.
- `incoming`: `Boolean` (required) - Whether or not the reply was incoming (from an external party) or outgoing (from a Sonar `User`.)
- `raw_body`: `Text` - The raw body, before any Sonar parsing.
- `signature`: `Text` - The signature to append. You can include `[PUBLIC_NAME]` as a variable to insert the user's public name when the signature is appended.
- `ticket_id`: `Int64Bit` (required) - The ID of a `Ticket`.
- `user_id`: `Int64Bit` - The ID of a User.
- `ticket`: `Ticket` - A ticket.
- `user`: `User` - A user that can login to Sonar.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TicketComment

**Description**: A comment on a `Ticket`.

**Category**: tickets
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `ticket_id`, `user_id`

**Relationship Fields**: 9 (`id`, `body`, `ticket_id`, `user_id`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `body`: `Text` (required) - The body.
- `ticket_id`: `Int64Bit` (required) - The ID of a `Ticket`.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `ticket`: `Ticket` - A ticket.
- `files`: `FileConnection` (required) (connection) - A file.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### Task

**Description**: A task.

**Category**: tickets
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 23

**Key Fields**: `id`, `sonar_unique_id`, `completable_id`, `completed_by_user_id`, `taskable_id`, `user_id`

**Enum Fields**: 3 (`completable_type`, `completion_type`, `taskable_type`)

**Relationship Fields**: 15 (`id`, `completable_id`, `completable_type`, `completed_by_user_id`, `completion_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `completable_id`: `Int64Bit` - The ID of the entity that completes or completed this task.
- `completable_type`: `CompletableType` (enum) - The type of entity that completes this task.
- `complete`: `Boolean` (required) - Whether or not this is complete.
- `completed_at`: `Datetime` - The date and time this was completed.
- `completed_by_user_id`: `Int64Bit` - The `User` that completed this.
- `completion_type`: `TaskCompletionType` (required) (enum) - How this task gets marked as completed.
- `due`: `Date` - The date on which the task is due.
- `list_order`: `Int` - The order this item is shown in a list.
- `task`: `Text` (required) - The task to be performed.
- `taskable_id`: `Int64Bit` (required) - The ID of the entity that the task is associated with.
- `taskable_type`: `TaskableType` (required) (enum) - The entity that the task is associated with.
- `user_id`: `Int64Bit` - The ID of a User.
- `taskable`: `TaskableInterface` - The entity that this `Task` is associated with.
- `completable`: `CompletableInterface` - An entity that can complete a task.
- `user`: `User` - A user that can login to Sonar.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### InstanceManagementRequest

**Description**: Requests from Sonar staff to access your Sonar instance.

**Category**: tickets
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `authorization_valid_until`, `responded_by_user_id`

**Relationship Fields**: 6 (`id`, `reason`, `responded_by_user_id`, `responded_by_user`, `logs`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `authorization_valid_until`: `Date` - The date until which the authorization is valid.
- `reason`: `Text` (required) - The reason.
- `responded_at`: `Datetime` - The date and time responded.
- `responded_by_user_id`: `Int64Bit` - The id of the `User` that responded to the request.
- `responded_by_user`: `User` - A `User`.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### AvailableExplore

**Description**: types.available_explore

**Category**: tickets
**Relevance Score**: 3 (Primary: 1, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Key Fields**: `name`

**Relationship Fields**: 3 (`name`, `category`, `endpoint`)

**All Fields**:

- `name`: `Text` (required) - A descriptive name.
- `category`: `Text` (required) - The category.
- `endpoint`: `Text` (required) - The endpoint.

---

### TicketReplyConnection

**Description**: The connection wrapper around the `TicketReplyConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TicketReply` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TicketConnection

**Description**: The connection wrapper around the `TicketConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Ticket` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TicketCommentConnection

**Description**: The connection wrapper around the `TicketCommentConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TicketComment` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TicketCategoryConnection

**Description**: The connection wrapper around the `TicketCategoryConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TicketCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaskTemplateConnection

**Description**: The connection wrapper around the `TaskTemplateConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TaskTemplate` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### TaskConnection

**Description**: The connection wrapper around the `TaskConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `Task` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### SavedMessageCategoryConnection

**Description**: The connection wrapper around the `SavedMessageCategoryConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `SavedMessageCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### MessageCategoryConnection

**Description**: The connection wrapper around the `MessageCategoryConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `MessageCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### InstanceManagementRequestConnection

**Description**: The connection wrapper around the `InstanceManagementRequestConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `InstanceManagementRequest` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### EmailCategoryConnection

**Description**: The connection wrapper around the `EmailCategoryConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `EmailCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CannedReplyCategoryConnection

**Description**: The connection wrapper around the `CannedReplyCategoryConnection` type.

**Category**: tickets
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CannedReplyCategory` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Towers Entities (3 total)


### TowercoverageConfiguration

**Description**: TowerCoverage integration.

**Category**: towers
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 16

**Key Fields**: `id`, `sonar_unique_id`, `account_status_id`, `account_type_id`, `api_key`, `phone_number_type_id`, `phone_number_type`

**Relationship Fields**: 10 (`id`, `account_status_id`, `account_type_id`, `phone_number_type_id`, `account_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_status_id`: `Int64Bit` - The ID of an AccountStatus.
- `account_type_id`: `Int64Bit` - The ID of an AccountType.
- `api_key`: `String` - An API key.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `phone_number_type_id`: `Int64Bit` - The ID of the PhoneNumberType associated with this phone number.
- `account_type`: `AccountType` - The account type.
- `account_status`: `AccountStatus` - The status of an account.
- `phone_number_type`: `PhoneNumberType` - A phone number type (e.g. mobile, home, work.)
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TowercoverageSubmission

**Description**: A TowerCoverage submission.

**Category**: towers
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 21

**Key Fields**: `id`, `sonar_unique_id`, `email_address`, `full_name`, `phone_number`, `serviceable_address_id`

**Relationship Fields**: 13 (`id`, `email_address`, `message`, `note`, `phone_number`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `email_address`: `EmailAddress` - An email address.
- `full_name`: `String` - The full name.
- `is_visible`: `Boolean` (required) - is_visible of the information
- `message`: `Text` (required) - The message.
- `note`: `Text` - A note about this TowerCoverage submission.
- `phone_number`: `Numeric` - A telephone number.
- `raw_xml`: `Text` (required) - The raw XML.
- `received_at`: `Datetime` (required) - The time that the TowerCoverage submission was received.
- `serviceable_address_id`: `Int64Bit` - The ID of the serviceable address to use for this account.
- `success`: `Boolean` (required) - Will be true if the operation succeeded.
- `serviceable_address`: `Address` - The serviceable address.
- `addresses`: `AddressConnection` (required) (connection) - A geographical address.
- `files`: `FileConnection` (required) (connection) - A file.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### TowercoverageSubmissionConnection

**Description**: The connection wrapper around the `TowercoverageSubmissionConnection` type.

**Category**: towers
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `TowercoverageSubmission` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Usage Entities (6 total)


### DataUsageTopOff

**Description**: A data usage top off.

**Category**: usage
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 15

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `data_usage_history_id`, `debit_id`

**Relationship Fields**: 11 (`id`, `account_id`, `amount_in_bytes`, `data_usage_history_id`, `debit_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `amount_in_bytes`: `Int64Bit` (required) - The amount of top off data in bytes.
- `data_usage_history_id`: `Int64Bit` (required) - The ID of a `DataUsageHistory`.
- `debit_id`: `Int64Bit` - The ID of a `Debit`.
- `account`: `Account` - A customer account.
- `debit`: `Debit` - A debit.
- `data_usage_history`: `DataUsageHistory` - A data usage history entry.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CustomFieldData

**Description**: Data entered into a `CustomField`.

**Category**: usage
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 13

**Key Fields**: `id`, `sonar_unique_id`, `custom_field_id`, `customfielddataable_id`

**Enum Fields**: 1 (`customfielddataable_type`)

**Relationship Fields**: 8 (`id`, `custom_field_id`, `customfielddataable_id`, `customfielddataable_type`, `customfielddataable`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `custom_field_id`: `Int64Bit` (required) - The ID of a CustomField that is associated with this type of entity.
- `customfielddataable_id`: `Int64Bit` (required) - The ID of the entity that owns this custom field data.
- `customfielddataable_type`: `CustomfielddataableType` (required) (enum) - The type of entity that owns this custom field data.
- `value`: `String` (required) - The value.
- `customfielddataable`: `CustomfielddataableInterface` - The owner of this `CustomFieldData`.
- `custom_field`: `CustomField` - A user defined field.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### DataUsage

**Description**: types.data_usage

**Category**: usage
**Relevance Score**: 2 (Primary: 0, Secondary: 1, Operational: 0)
**Total Fields**: 8

**Key Fields**: `account_id`, `account_service_id`, `data_source_identifier`

**Relationship Fields**: 5 (`inbytes_per_second`, `outbytes_per_second`, `account_id`, `account_service_id`, `epoch_system_timezone`)

**All Fields**:

- `time`: `Datetime` - The time.
- `inbytes_per_second`: `Int64Bit` - The amount of inbound bytes per second.
- `outbytes_per_second`: `Int64Bit` - The amount of outbound bytes per second.
- `account_id`: `Int64Bit` (required) - The ID of an Account.
- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `data_source_identifier`: `String` - The data source identifier.
- `data_source_parent`: `String` - The data source parent.
- `epoch_system_timezone`: `EpochTimestamp` - A Unix timestamp in the same timezone as this Sonar instance

---

### DataUsageTotal

**Description**: A data usage history entry.

**Category**: usage
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 7

**Key Fields**: `account_service_id`, `data_source_identifier`

**Relationship Fields**: 5 (`account_service_id`, `billable_in_bytes`, `billable_out_bytes`, `free_in_bytes`, `free_out_bytes`)

**All Fields**:

- `account_service_id`: `Int64Bit` - The ID of an AccountService.
- `billable_in_bytes`: `Int64Bit` (required) - The ID of the entity.
- `billable_out_bytes`: `Int64Bit` (required) - The ID of an Account.
- `free_in_bytes`: `Int64Bit` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `free_out_bytes`: `Int64Bit` (required) - The date and time this entity was created.
- `data_source_identifier`: `String` - The last date and time this entity was modified.
- `data_source_parent`: `String` - The type.

---

### DataUsageTopOffConnection

**Description**: The connection wrapper around the `DataUsageTopOffConnection` type.

**Category**: usage
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `DataUsageTopOff` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CustomFieldDataConnection

**Description**: The connection wrapper around the `CustomFieldDataConnection` type.

**Category**: usage
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CustomFieldData` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Users Entities (8 total)


### User

**Description**: A user that can login to Sonar.

**Category**: users
**Relevance Score**: 14 (Primary: 4, Secondary: 1, Operational: 0)
**Total Fields**: 51

**Key Fields**: `id`, `sonar_unique_id`, `email_address`, `mobile_number`, `name`, `public_name`, `role_id`, `username`, `emails`, `voided_payments`, `schedule_blocker_overrides`

**Enum Fields**: 1 (`language`)

**Relationship Fields**: 40 (`id`, `email_address`, `language`, `mobile_number`, `role_id`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `completed_setup`: `Boolean` (required) - Whether or not the user has completed the setup process.
- `email_address`: `EmailAddress` (required) - An email address.
- `enabled`: `Boolean` (required) - Whether or not this is enabled.
- `is_sonar_staff`: `Boolean` - Whether or not this user is a Sonar employee.
- `language`: `Language` (enum) - A supported language.
- `mobile_number`: `Numeric` - A mobile phone number. This will be used to send SMS messages.
- `name`: `String` (required) - A descriptive name.
- `public_name`: `String` (required) - The publicly viewable name of this user.
- `role_id`: `Int64Bit` - The ID of a Role.
- `super_admin`: `Boolean` (required) - Super admins receive all system permissions automatically, regardless of their role.
- `username`: `String` (required) - A username, used for authentication.
- `role`: `Role` - A role defines the permission set that a user has.
- `emails`: `EmailConnection` (required) (connection) - An email.
- `inventory_items`: `InventoryItemConnection` (required) (connection) - An inventory item.
- `generic_inventory_items`: `GenericInventoryItemConnection` (required) (connection) - A generic inventory item.
- `sms_outbound_messages`: `SmsOutboundMessageConnection` (required) (connection) - An SMS outbound message.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.
- `archived_accounts`: `AccountConnection` (required) (connection) - The `Accounts` archived by a `User`.
- `calendar_icals`: `CalendarIcalConnection` (required) (connection) - An iCalendar calendar.
- `debits`: `DebitConnection` (required) (connection) - A debit.
- `discounts`: `DiscountConnection` (required) (connection) - A discount.
- `tasks`: `TaskConnection` (required) (connection) - A task.
- `notes`: `NoteConnection` (required) (connection) - A note.
- `reversed_payments`: `ReversedPaymentConnection` (required) (connection) - A record a `Payment` reversal.
- `refunded_payments`: `RefundedPaymentConnection` (required) (connection) - A record of a refund applied to a `Payment`.
- `voided_payments`: `VoidedPaymentConnection` (required) (connection) - A record of a `Payment` that was voided.
- `tickets`: `TicketConnection` (required) (connection) - A ticket.
- `ticket_replies`: `TicketReplyConnection` (required) (connection) - A reply on a `Ticket`.
- `ticket_comments`: `TicketCommentConnection` (required) (connection) - A comment on a `Ticket`.
- `subscriptions`: `SubscriptionConnection` (required) (connection) - A subscription to notifications for an entity.
- `schedule_blocker_overrides`: `ScheduleBlockerOverrideConnection` (required) (connection) - An override to a particular day and time a `ScheduleBlocker` would otherwise cover.
- `job_check_ins`: `JobCheckInConnection` (required) (connection) - The record of a check in to a `Job`.
- `printed_invoice_batches`: `PrintedInvoiceBatchConnection` (required) (connection) - A single PDF containing multiple invoices for printing.
- `notifications`: `NotificationConnection` (required) (connection) - A `Notification`.
- `search_filters`: `SearchFilterConnection` (required) (connection) - A user-defined search filter that applies to a specific type of entity.
- `order_group_users`: `OrderGroupUserConnection` (required) (connection) - The relationship between an order group and a user.
- `stored_view_users`: `StoredViewUserConnection` (required) (connection) - A `StoredView` associated with a `User`.
- `vehicles`: `VehicleConnection` (required) (connection) - A vehicle.
- `schedule_availabilities`: `ScheduleAvailabilityConnection` (required) (connection) - Availability for `Job`s to be scheduled.
- `schedule_time_offs`: `ScheduleTimeOffConnection` (required) (connection) - Time off that removes availability from a `ScheduleAvailability`.
- `schedule_blockers`: `ScheduleBlockerConnection` (required) (connection) - An event that blocks off part of a calendar otherwise availability due to `ScheduleAvailability`.
- `jobs`: `JobConnection` (required) (connection) - A job, typically in the field.
- `schedule_addresses`: `ScheduleAddressConnection` (required) (connection) - The geographical point that a technician starts or ends their day at.
- `alerting_rotations`: `AlertingRotationConnection` (required) (connection) - An alerting rotation.
- `ticket_groups`: `TicketGroupConnection` (required) (connection) - A ticket group.

---

### StoredViewUser

**Description**: A `StoredView` associated with a `User`.

**Category**: users
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `stored_view_id`, `user_id`

**Relationship Fields**: 7 (`id`, `stored_view_id`, `user_id`, `stored_view`, `user`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `location`: `String` (required) - The location in the UI that this view is available.
- `stored_view_id`: `Int64Bit` (required) - The ID of a `StoredView` entity.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `stored_view`: `StoredView` - A stored view.
- `user`: `User` - A user that can login to Sonar.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### OrderGroupUser

**Description**: The relationship between an order group and a user.

**Category**: users
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 12

**Key Fields**: `id`, `sonar_unique_id`, `order_group_id`, `user_id`

**Relationship Fields**: 7 (`id`, `order_group_id`, `user_id`, `user`, `order_group`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `is_approver`: `Boolean` (required) - Whether a user is authorized to approve purchase orders created in this order group.
- `order_group_id`: `Int64Bit` (required) - The ID of an order group.
- `user_id`: `Int64Bit` (required) - The ID of a User.
- `user`: `User` - A user that can login to Sonar.
- `order_group`: `OrderGroup` - An order group.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### MfaAdminSetting

**Description**: The multi-factor authentication admin settings

**Category**: users
**Relevance Score**: 9 (Primary: 3, Secondary: 0, Operational: 0)
**Total Fields**: 8

**Key Fields**: `id`, `sonar_unique_id`

**Relationship Fields**: 3 (`id`, `logs`, `access_logs`)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `is_mfa_required`: `Boolean` (required) - Whether or not users are required to use multi-factor authentication.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### UserPreference

**Category**: users
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 2 (`table_paginator_size`, `ui_preferences`)

**All Fields**:

- `table_paginator_size`: `Int64Bit` - The number of records shown in a paginated table at once.
- `navigation_expanded`: `Boolean` - Whether or not the navigation bar on the side is loaded in an expanded state.
- `ui_preferences`: `Text` - Saved settings for the web application. This field is meant to be user configurable.

---

### UserConnection

**Description**: The connection wrapper around the `UserConnection` type.

**Category**: users
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `User` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### StoredViewUserConnection

**Description**: The connection wrapper around the `StoredViewUserConnection` type.

**Category**: users
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `StoredViewUser` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### OrderGroupUserConnection

**Description**: The connection wrapper around the `OrderGroupUserConnection` type.

**Category**: users
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `OrderGroupUser` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Voip Entities (4 total)


### VoiceProvider

**Description**: A `VoiceProvider`.

**Category**: voip
**Relevance Score**: 12 (Primary: 4, Secondary: 0, Operational: 0)
**Total Fields**: 17

**Key Fields**: `id`, `sonar_unique_id`, `name`, `dids`, `did_import_recipes`, `voice_provider_rates`, `voice_provider_rate_imports`, `voice_provider_rate_import_recipes`

**Relationship Fields**: 12 (`id`, `dids`, `did_import_recipes`, `voice_provider_rates`, `voice_provider_rate_imports`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `name`: `String` (required) - A descriptive name.
- `dids`: `DidConnection` (required) (connection) - A direct inward dial (DID).
- `did_import_recipes`: `DidImportRecipeConnection` (required) (connection) - A recipe for importing DIDs.
- `voice_provider_rates`: `VoiceProviderRateConnection` (required) (connection) - A voice provider rate.
- `voice_provider_rate_imports`: `VoiceProviderRateImportConnection` (required) (connection) - An import of voice provider rates.
- `voice_provider_rate_import_recipes`: `VoiceProviderRateImportRecipeConnection` (required) (connection) - A recipe for importing voice provider rates.
- `call_detail_records`: `CallDetailRecordConnection` (required) (connection) - A call detail record (CDR).
- `call_detail_record_imports`: `CallDetailRecordImportConnection` (required) (connection) - An import of call detail records (CDRs).
- `call_detail_record_import_recipes`: `CallDetailRecordImportRecipeConnection` (required) (connection) - A recipe for importing call detail records (CDRs).
- `notes`: `NoteConnection` (required) (connection) - A note.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### CallDetailRecord

**Description**: A call detail record (CDR).

**Category**: voip
**Relevance Score**: 11 (Primary: 3, Secondary: 1, Operational: 0)
**Total Fields**: 25

**Key Fields**: `id`, `sonar_unique_id`, `account_id`, `monthly_billing_completion_id`, `originating_number`, `receiving_number`, `service_id`, `voice_provider_id`, `voice_provider`

**Enum Fields**: 2 (`direction`, `prefix_type`)

**Relationship Fields**: 13 (`id`, `account_id`, `direction`, `monthly_billing_completion_id`, `prefix_type`...)

**All Fields**:

- `id`: `Int64Bit` (required) - The ID of the entity.
- `sonar_unique_id`: `ID` (required) - An ID that uniquely identifies this entity across the whole Sonar system.
- `created_at`: `Datetime` (required) - The date and time this entity was created.
- `updated_at`: `Datetime` (required) - The last date and time this entity was modified.
- `_version`: `String` (required) - A string that shows the version of this entity. It will be incremented whenever the entity is modified.
- `account_id`: `Int64Bit` - The ID of an Account.
- `amount`: `Float` - The amount, in the smallest currency value (e.g. cents, pence, pesos.)
- `charge_rate`: `Float` - The rate that is charged to a customer.
- `description`: `String` - The prefix description for the call detail record having provider rated prefix.
- `direction`: `CallDetailRecordDirection` (enum) - The direction of the call.
- `length_in_seconds`: `Int` (required) - The total length of the call in seconds.
- `matched_prefix`: `String` - The matched prefix of this call record.
- `monthly_billing_completion_id`: `Int64Bit` - The ID of a `MonthlyBillingCompletion`.
- `originating_number`: `String` - The DID that initiated the call.
- `prefix_type`: `CallDetailRecordPrefixType` (enum) - The prefix type of this call record.
- `receiving_number`: `String` - The DID that received the call.
- `service_id`: `Int64Bit` - The ID of a Service.
- `started_at`: `Datetime` (required) - When the call was started.
- `voice_provider_id`: `Int64Bit` (required) - The ID of a `VoiceProvider`.
- `voice_provider`: `VoiceProvider` - A `VoiceProvider`.
- `account`: `Account` - A customer account.
- `service`: `Service` - A service.
- `monthly_billing_completion`: `MonthlyBillingCompletion` - A record of a monthly billing cycle.
- `logs`: `LogConnection` (required) (connection) - A log entry.
- `access_logs`: `AccessLogConnection` (required) (connection) - An access log history on an entity.

---

### VoiceProviderConnection

**Description**: The connection wrapper around the `VoiceProviderConnection` type.

**Category**: voip
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `VoiceProvider` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

### CallDetailRecordConnection

**Description**: The connection wrapper around the `CallDetailRecordConnection` type.

**Category**: voip
**Relevance Score**: 0 (Primary: 0, Secondary: 0, Operational: 0)
**Total Fields**: 3

**Relationship Fields**: 3 (`entities`, `page_info`, `aggregations`)

**All Fields**:

- `entities`: `CallDetailRecord` (required) (list) - A list of the entities provided by this connection.
- `page_info`: `PageInfo` (required) - An object providing information about the page of results being displayed, as well as the total amount of pages/records available.
- `aggregations`: `Aggregation` (required) (list) - Provides the ability to return aggregated mathematical data about your results.

---

## Mutations (640 total)


### addInstanceServiceFunds

Make additional funds available to the instance service fund.

**Returns**: `InstanceServiceFunds`

**Arguments**:

- `input`: `AddInstanceServiceFundsMutationInput`


### addPackageToAccount

Add a package to an account.

**Returns**: `AccountService`

**Arguments**:

- `input`: `AddPackageToAccountMutationInput`


### addServiceToAccount

Add a recurring or expiring service to an account.

**Returns**: `AccountService`

**Arguments**:

- `input`: `AddServiceToAccountMutationInput`


### allocateLookerExploreLicenseToUser

Allocate a report builder license to a user.

**Returns**: `LookerExploreLicense`

**Arguments**:

- `input`: `AllocateLookerExploreLicenseToUserMutationInput`


### allocateLookerViewLicenseToUser

Allocate a report viewer license to a user.

**Returns**: `LookerViewLicense`

**Arguments**:

- `input`: `AllocateLookerViewLicenseToUserMutationInput`


### applyCreditToInvoice

Apply a credit to an invoice with a due balance.

**Returns**: `Invoice`

**Arguments**:

- `input`: `ApplyCreditToInvoiceMutationInput`
- `id`: `Int64Bit` - The ID of an `Invoice`.


### archiveAccount

Archive an account.

**Returns**: `Account`

**Arguments**:

- `id`: `Int64Bit` - The ID of the entity.


### assignGenericInventoryItems

Assign generic inventory items to an assignee.

**Returns**: `GenericInventoryItem`

**Arguments**:

- `input`: `AssignGenericInventoryItemsMutationInput`
- `id`: `Int64Bit` - fields.generic_inventory_item_id


### assignInventoryItems

Assign one or more inventory items to a new assignee.

**Returns**: `InventoryItem`

**Arguments**:

- `input`: `AssignInventoryItemsMutationInput`
- `ids`: `Int64Bit` - The ID of an `InventoryItem`.


### auditAdtranMosaic

Perform manual Adtran Mosaic audit.

**Returns**: `AdtranMosaicSetting`

**Arguments**:

- `input`: `AuditAdtranMosaicMutationInput`


### auditCalixCloud

Audit Calix Cloud subscribers to Sonar accounts.

**Returns**: `CalixCloudSetting`

**Arguments**:

- `input`: `AuditCalixCloudMutationInput`


### auditRepairAdtranMosaic

Perform manual repair of Adtran Mosaic Cloud audit entries.

**Returns**: `SuccessResponse`

**Arguments**:

- `id`: `Int64Bit` - The ID of an Adtran Mosaic audit record.


### cancelPrintToMailBatch

Cancel a print to mail batch.

**Returns**: `SuccessResponse`

**Arguments**:

- `id`: `Int64Bit` - The ID of the print to mail batch.


### checkInToJob

Check in to a job.

**Returns**: `JobCheckIn`

**Arguments**:

- `input`: `CheckInToJobMutationInput`


### checkOutOfJob

Check out of a job.

**Returns**: `JobCheckIn`

**Arguments**:

- `input`: `CheckOutOfJobMutationInput`


### claimInventoryItems

Claim one or many inventory items.

**Returns**: `SuccessResponse`

**Arguments**:

- `input`: `ClaimInventoryItemsMutationInput`


### completeFileTask

Complete a task that requires a file for a completion type.

**Returns**: `Task`

**Arguments**:

- `input`: `CompleteFileTaskMutationInput`
- `id`: `Int64Bit` - The ID of the entity.


### completeJob

Complete a job.

**Returns**: `Job`

**Arguments**:

- `input`: `CompleteJobMutationInput`


### completeTask

Complete or uncomplete a task.

**Returns**: `Task`

**Arguments**:

- `input`: `CompleteTaskMutationInput`
- `id`: `Int64Bit` - The ID of the entity.


### consumeGenericInventoryItems

Consume generic inventory items.

**Returns**: `GenericInventoryItem`

**Arguments**:

- `input`: `ConsumeGenericInventoryItemsMutationInput`
- `id`: `Int64Bit` - fields.generic_inventory_item_id


## Schema Type Analysis

- **Object Types**: 621 (business entities, API types)
- **Scalar Types**: 27 (custom data types)
- **Enum Types**: 188 (predefined value sets)
- **Interface Types**: 30 (contracts)
- **Union Types**: 0 (polymorphic types)
- **Input Object Types**: 519 (mutation inputs)

## Entity Relationships

**Total Relationships Identified**: 5432


### Has-One Relationships (1)

- `Query` → `BillingSetting` (via `billing_setting`)

### Has-Many Relationships (49)

- `Query` → `AccessLogConnection` (via `access_logs`)
- `Query` → `AccountAdtranMosaicServiceDetailConnection` (via `account_adtran_mosaic_service_details`)
- `Query` → `AccountBillingParameterConnection` (via `account_billing_parameters`)
- `Query` → `AccountCalixServiceDetailConnection` (via `account_calix_service_details`)
- `Query` → `AccountEventConnection` (via `account_events`)
- `Query` → `AccountGroupConnection` (via `account_groups`)
- `Query` → `AccountIpAssignmentsConnection` (via `account_ip_assignments`)
- `Query` → `AccountServiceConnection` (via `account_services`)
- `Query` → `AccountStatusConnection` (via `account_statuses`)
- `Query` → `AccountTypeConnection` (via `account_types`)

## Migration Insights

### High-Priority Entities for Migration

**290 entities** identified as high-priority for migration:

- **RadiusServer** (network_protocols) - Score: 19, Fields: 23
- **LteProvider** (sites) - Score: 19, Fields: 20
- **InlineDevice** (devices) - Score: 19, Fields: 24
- **DhcpServer** (ip_management) - Score: 19, Fields: 24
- **CableModemProvisioner** (network_equipment) - Score: 19, Fields: 18
- **FibermapIntegration** (network_equipment) - Score: 17, Fields: 28
- **TaxProvider** (billing) - Score: 16, Fields: 14
- **Service** (services) - Score: 16, Fields: 45
- **SystemBackup** (backup) - Score: 15, Fields: 14
- **PurchaseOrderItem** (inventory) - Score: 15, Fields: 24

### Entity Categories Summary

- **Accounts**: 46 entities, 1601 total fields, avg score: 6.2
- **Authentication**: 14 entities, 102 total fields, avg score: 5.3
- **Availability**: 4 entities, 38 total fields, avg score: 5.2
- **Backup**: 4 entities, 35 total fields, avg score: 6.5
- **Billing**: 67 entities, 861 total fields, avg score: 6.3
- **Configuration**: 8 entities, 162 total fields, avg score: 7.8
- **Contacts**: 22 entities, 218 total fields, avg score: 5.3
- **Contracts**: 4 entities, 46 total fields, avg score: 6.5
- **Devices**: 22 entities, 266 total fields, avg score: 9.5
- **Documents**: 3 entities, 25 total fields, avg score: 3.7
- **Financial**: 2 entities, 14 total fields, avg score: 5.5
- **Geographic**: 17 entities, 163 total fields, avg score: 4.4
- **Integration**: 5 entities, 31 total fields, avg score: 5.0
- **Inventory**: 44 entities, 467 total fields, avg score: 5.8
- **Ip_Management**: 33 entities, 333 total fields, avg score: 6.5
- **Jobs**: 11 entities, 137 total fields, avg score: 5.6
- **Logs**: 20 entities, 200 total fields, avg score: 5.8
- **Maintenance**: 2 entities, 22 total fields, avg score: 6.5
- **Monitoring**: 12 entities, 114 total fields, avg score: 5.0
- **Network_Equipment**: 18 entities, 192 total fields, avg score: 7.2
- **Network_Interfaces**: 18 entities, 190 total fields, avg score: 6.0
- **Network_Protocols**: 22 entities, 194 total fields, avg score: 5.1
- **Other**: 48 entities, 145 total fields, avg score: 0.2
- **Physical_Assets**: 1 entities, 14 total fields, avg score: 9.0
- **Provisioning**: 2 entities, 17 total fields, avg score: 6.0
- **Roles**: 11 entities, 92 total fields, avg score: 6.5
- **Scheduling**: 11 entities, 88 total fields, avg score: 5.1
- **Security**: 4 entities, 35 total fields, avg score: 5.2
- **Services**: 58 entities, 572 total fields, avg score: 5.3
- **Sites**: 13 entities, 181 total fields, avg score: 8.0
- **Tickets**: 24 entities, 226 total fields, avg score: 5.7
- **Towers**: 3 entities, 40 total fields, avg score: 6.7
- **Usage**: 6 entities, 49 total fields, avg score: 3.3
- **Users**: 8 entities, 95 total fields, avg score: 5.1
- **Voip**: 4 entities, 48 total fields, avg score: 5.8
