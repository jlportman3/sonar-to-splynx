# Sonar REST API Complete Schema Analysis

Generated on: 2025-09-12T03:55:48.434479
API Base URL: https://alamobb.sonar.software/api/v1

## Executive Summary

- **Total Endpoints Discovered**: 3
- **Total Records Available**: 48,429
- **Unique Fields**: 38
- **Migration Complexity**: low

## API Endpoints Overview

### Available Endpoints by Category


#### Accounts (1 endpoints)

- **accounts**: 10,114 records

#### Operations (1 endpoints)

- **tickets**: 38,285 records

#### Users (1 endpoints)

- **users**: 30 records

## High-Value Endpoints (Top Data Sources)


### tickets

- **Records**: 38,285
- **Fields**: 20

**Fields**:

- `assignee`: `str` - Examples: "accounts"
- `assignee_id`: `int` - Examples: "62825", "100937", "107141"
- `category_ids`: `list` - Examples: "[]", "[1]"
- `child_ticket_ids`: `list` - Examples: "[]"
- `closed_at`: `str` (nullable) - Examples: "2025-09-12 02:25:06"
- `closed_by_user_id`: `int` (nullable) - Examples: "14"
- `created_at`: `str` - Examples: "2025-09-11 23:01:18", "2025-09-11 23:58:29", "2025-09-12 02:25:05"
- `due_date`: `NoneType` (nullable)
- `email_address`: `NoneType` (nullable) - Examples: "jecbr28@feedback.alamobroadband.com", "jonathan@govyvora.com"
- `id`: `int` - Examples: "40356", "40357", "40358"
- `inbound_email_account_id`: `NoneType` (nullable) - Examples: "3", "1"
- `last_reply_incoming`: `bool` - Examples: "False", "True"
- `open`: `bool` - Examples: "False", "True"
- `parent_ticket_id`: `NoneType` (nullable)
- `priority`: `int` - Examples: "4"
- `spam`: `bool` - Examples: "False"
- `subject`: `str` - Examples: "Fixed Wireless - Cannot connect with any devices", "Job 16069 Service Call With Maintenance completed successfully", "Billing - Make a payment"
- `ticket_group_id`: `int` - Examples: "10", "3", "1"
- `type`: `str` - Examples: "internal", "public"
- `user_id`: `NoneType` (nullable)

**Sample Record**:
```json
{
  "id": 40358,
  "subject": "Billing - Make a payment",
  "type": "internal",
  "ticket_group_id": 3,
  "user_id": null,
  "assignee": "accounts",
  "assignee_id": 100937,
  "due_date": null,
  "priority": 4,
  "category_ids": [
    1
  ],
  "open": false,
  "parent_ticket_id": null,
  "child_ticket_ids": [],
  "inbound_email_account_id": null,
  "spam": false,
  "last_reply_incoming": false,
  "email_address": null,
  "closed_at": "2025-09-12 02:25:06",
  "closed_by_user_id": 14,
  "created_at": "2025-09-12 02:25:05"
}
```

---

### accounts

- **Records**: 10,114
- **Fields**: 14

**Fields**:

- `account_groups`: `list` - Examples: "[1, 3]", "[]", "[1]"
- `account_status_id`: `int` - Examples: "5", "2", "3"
- `account_type_id`: `int` - Examples: "1"
- `available_funds`: `str` - Examples: "0.00"
- `balance_due`: `str` - Examples: "0.00"
- `balance_total`: `str` - Examples: "0.00"
- `company_id`: `int` - Examples: "1"
- `delinquent`: `bool` - Examples: "False"
- `id`: `int` - Examples: "9263", "10174", "10178"
- `name`: `str` - Examples: "Steve Whittley", "Margie Vega", "Clint Christian"
- `next_bill_date`: `str` (nullable) - Examples: "2025-09-01", "2025-10-01", "2025-02-16"
- `next_recurring_charge_amount`: `str` - Examples: "76.95", "46.95", "0.00"
- `sub_accounts`: `list` - Examples: "[105467]", "[106328]", "[]"
- `total_balance`: `str` - Examples: "0.00"

**Sample Record**:
```json
{
  "id": 9263,
  "name": "Margie Vega",
  "account_type_id": 1,
  "account_status_id": 5,
  "account_groups": [
    1
  ],
  "balance_due": "0.00",
  "balance_total": "0.00",
  "total_balance": "0.00",
  "sub_accounts": [
    105467
  ],
  "next_bill_date": "2025-09-01",
  "delinquent": false,
  "company_id": 1,
  "next_recurring_charge_amount": "46.95",
  "available_funds": "0.00"
}
```

---

### users

- **Records**: 30
- **Fields**: 8

**Fields**:

- `email_address`: `str` - Examples: "sonya@portman.net", "baron@baron.com", "support@sonar.software"
- `id`: `int` - Examples: "3", "2", "1"
- `locale`: `str` - Examples: "en"
- `mobile_number`: `int` (nullable) - Examples: "5195746696", "2103162300"
- `name`: `str` - Examples: "Sonya", "sonar", "Joe Portman"
- `public_name`: `str` - Examples: "Sonya Portman", "Sonar", "Joe Portman"
- `role_id`: `NoneType` (nullable) - Examples: "4", "2", "6"
- `username`: `str` - Examples: "sonya", "sonar", "admin"

**Sample Record**:
```json
{
  "id": 1,
  "username": "admin",
  "name": "Joe Portman",
  "public_name": "Joe Portman",
  "locale": "en",
  "role_id": null,
  "email_address": "baron@baron.com",
  "mobile_number": 2103162300
}
```

---

## Migration Planning Insights

### Recommended Migration Order

1. **Accounts**: 1 endpoints, 10,114 records
6. **Operations**: 1 endpoints, 38,285 records
7. **Users**: 1 endpoints, 30 records

### Priority Endpoints for Migration

- **accounts**: 10,114 records

### Complex Endpoints (>10 fields)

- **tickets**: 20 fields
- **accounts**: 14 fields

## Common Fields Analysis

Fields that appear across multiple endpoints:

- **id**: 3 endpoints, types: int
- **name**: 2 endpoints, types: str
- **email_address**: 2 endpoints, types: NoneType, str
