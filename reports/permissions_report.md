Warning: Splynx API call failed; falling back to DB-only view
# Permissions Report

Sonar roles: 14
Splynx roles: 7

## Roles missing in Splynx
- admin
- batcher
- minim
- netflow_on_premises
- no_permissions
- portal
- portalv2
- preseem
- read_only
- sales
- serge
- serverplus
- supervisor

## Roles only in Splynx
- administrator
- customer-creator
- engineer
- financial-manager
- manager
- super-administrator

## Role Comparison
| Role | Sonar perms | Splynx rules |
| --- | ---: | ---: |
| admin | 171 | 0 |
| batcher | 57 | 0 |
| minim | 48 | 0 |
| netflow_on_premises | 11 | 0 |
| no_permissions | 0 | 0 |
| portal | 60 | 0 |
| portalv2 | 89 | 0 |
| preseem | 41 | 0 |
| read_only | 103 | 0 |
| sales | 30 | 0 |
| serge | 103 | 0 |
| serverplus | 82 | 0 |
| supervisor | 188 | 0 |
| technician | 68 | 0 |

## Permission Mapping Status
Total Sonar permission codes: 273
Mapped via config: 0
Unmapped (heuristic only): 273

### Unmapped permissions
- assign_account_inventory
- check_in_any_job
- check_in_own_job
- complete_any_job
- complete_own_job
- create_account
- create_account_transactions
- create_ach_batch
- create_address_list
- create_address_status
- create_alerting_rotation
- create_billing_default
- create_call_log
- create_canned_reply
- create_contact
- create_contract
- create_contract_template
- create_data_usage
- create_delinquency_exclusion
- create_deposit_slip
- create_dhcp_server
- create_file
- create_general_ledger_code
- create_geofence
- create_inbound_mailbox
- create_inline_device
- create_inventory_item
- create_invoice_attachment
- create_invoice_message
- create_invoice_template
- create_ip_assignment
- create_ipam_element
- create_job
- create_job_type
- create_lte_provider
- create_netflow_endpoint
- create_network_monitoring_template
- create_network_site
- create_note
- create_package
- create_payment
- create_payment_method
- create_payment_processor
- create_poller
- create_printed_invoice_batch
- create_radius_account
- create_radius_group
- create_radius_server
- create_schedule_address
- create_schedule_availability
- create_schedule_blocker
- create_schedule_time_off
- create_scheduled_event
- create_service
- create_serviceable_address
- create_snmp_override
- create_task
- create_tax
- create_tax_override
- create_ticket
- create_ticket_category
- create_ticket_group
- create_uninventoried_mac_address
- delete_account_transactions
- delete_ach_batch
- delete_billing_default
- delete_call_log
- delete_canned_reply
- delete_contact
- delete_contract
- delete_contract_template
- delete_delinquency_exclusion
- delete_deposit_slip
- delete_external_marketing
- delete_file
- delete_general_ledger_code
- delete_geofence
- delete_gps_tracking_provider
- delete_inbound_mailbox
- delete_inventory_item
- delete_invoice_attachment
- delete_invoice_message
- delete_invoice_template
- delete_ip_assignment
- delete_ipam_element
- delete_job
- delete_job_type
- delete_netflow_endpoint
- delete_note
- delete_package
- delete_payment_method
- delete_payment_processor
- delete_radius_account
- delete_schedule_address
- delete_schedule_availability
- delete_schedule_blocker
- delete_schedule_time_off
- delete_scheduled_event
- delete_service
- delete_snmp_override
- delete_task
- delete_tax
- delete_tax_override
- delete_ticket
- delete_ticket_category
- delete_ticket_group
- modify_account_services
- override_account_status_proration
- read_account
- read_account_group
- read_account_reports
- read_account_status
- read_account_transactions
- read_account_type
- read_ach_batch
- read_address_list
- read_address_status
- read_alerting_rotation
- read_all_inventory
- read_all_logs
- read_billing_default
- read_cable_modem_provisioner
- read_calendar
- read_call_detail_record
- read_call_log
- read_canned_reply
- read_contract
- read_contract_template
- read_custom_field
- read_custom_link
- read_data_usage_history
- read_delinquency_exclusion
- read_deposit_slip
- read_dhcp_server
- read_did
- read_did_assignment
- read_did_import_recipe
- read_dispute
- read_email_domain
- read_email_message
- read_external_marketing
- read_fcc_form_477_report
- read_file
- read_general_ledger_code
- read_geofence
- read_global_inventory_model_min_max
- read_gps_tracking_provider
- read_inbound_mailbox
- read_inline_device
- read_integration_field_mapping
- read_integration_service_mapping
- read_invoice_attachment
- read_invoice_message
- read_invoice_template
- read_ip_assignment
- read_job
- read_job_type
- read_lte_provider
- read_map_overlay
- read_mass_email
- read_message_category
- read_netflow_endpoint
- read_network_monitoring_template
- read_network_site
- read_network_site_serviceable_address_list
- read_non_inventory_item
- read_order_group
- read_package
- read_payment_method
- read_payment_processor
- read_phone_number_type
- read_poller
- read_print_to_mail_batch
- read_print_to_mail_order
- read_print_to_mail_order_error
- read_radius_account
- read_radius_group
- read_radius_server
- read_rate_center
- read_saved_message_category
- read_schedule_address
- read_schedule_availability
- read_schedule_blocker
- read_schedule_time_off
- read_scheduled_event
- read_service
- read_serviceable_address
- read_serviceable_address_account_assignment_future
- read_sms_message
- read_sms_outbound_message
- read_snmp_override
- read_task_template
- read_tax
- read_tax_exemption
- read_tax_provider
- read_ticket
- read_ticket_category
- read_ticket_group
- read_timeseries_data
- read_towercoverage_configuration
- read_towercoverage_submission
- read_triggered_email
- read_uninventoried_mac_address
- read_vendor
- read_vendor_item
- read_voice_provider
- read_voice_provider_rate
- read_voice_provider_rate_import_recipe
- read_webhook_endpoint
- read_webhook_endpoint_event
- refund_payments
- reschedule_schedule_blocker
- resend_contract
- reverse_account_transactions
- update_account
- update_account_billing_parameters
- update_account_group
- update_account_link
- update_account_service_parameters
- update_account_transactions
- update_address_list
- update_alerting_rotation
- update_billing_default
- update_billing_settings
- update_call_log
- update_canned_reply
- update_contact
- update_contract
- update_contract_template
- update_delinquency_exclusion
- update_deposit_slip
- update_dhcp_server
- update_file
- update_general_ledger_code
- update_geofence
- update_inbound_mailbox
- update_inline_device
- update_inventory_item
- update_invoice_attachment
- update_invoice_message
- update_invoice_template
- update_ip_assignment
- update_ipam_element
- update_job
- update_job_type
- update_lte_provider
- update_netflow_endpoint
- update_network_monitoring_template
- update_network_site
- update_note
- update_package
- update_payment_method
- update_payment_processor
- update_poller
- update_poller_settings
- update_radius_account
- update_radius_group
- update_radius_server
- update_schedule_address
- update_schedule_availability
- update_schedule_blocker
- update_schedule_time_off
- update_scheduled_event
- update_service
- update_serviceable_address
- update_snmp_override
- update_task
- update_tax
- update_tax_override
- update_ticket
- update_ticket_category
- update_ticket_group
- update_towercoverage_submission

## Missing permission rules
### technician
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- customers/customer:* (allow)
- finance/payments:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- finance/payments:* (allow)
- customers/customer:* (allow)
- networking/ipv4:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- customers/customer:* (allow)
- finance/payments:* (allow)
- customers/customer:* (allow)
- inventory/items:* (allow)
- networking/ipv4:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- customers/customer:* (allow)
- finance/payments:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- networking/ipv4:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- finance/payments:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- networking/ipv4:* (allow)
- customers/customer:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- inventory/items:* (allow)
- inventory/items:* (allow)
- networking/ipv4:* (allow)
- networking/ipv4:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- administration/roles:* (allow)
- support/tickets:* (allow)
- support/tickets:* (allow)
- support/tickets:* (allow)

## Sample Splynx rules
### administrator (Administrator)
- (no rules)

### customer-creator (Customer creator)
- (no rules)

### engineer (Engineer)
- (no rules)

### financial-manager (Financial manager)
- (no rules)

### manager (Manager)
- (no rules)

