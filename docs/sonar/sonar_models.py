"""
Auto-generated Python models for Sonar REST API.
Generated from live API schema analysis.
"""

from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime


@dataclass
class Ticket:
    """Model for tickets endpoint."""
    id: int
    subject: str
    type: str
    ticket_group_id: int
    user_id: Optional[str] = None
    assignee: str
    assignee_id: int
    due_date: Optional[str] = None
    priority: int
    category_ids: List[Any]
    open: bool
    parent_ticket_id: Optional[str] = None
    child_ticket_ids: List[Any]
    inbound_email_account_id: Optional[str] = None
    spam: bool
    last_reply_incoming: bool
    email_address: Optional[str] = None
    closed_at: Optional[str] = None
    closed_by_user_id: Optional[int] = None
    created_at: str


@dataclass
class Account:
    """Model for accounts endpoint."""
    id: int
    name: str
    account_type_id: int
    account_status_id: int
    account_groups: List[Any]
    balance_due: str
    balance_total: str
    total_balance: str
    sub_accounts: List[Any]
    next_bill_date: Optional[str] = None
    delinquent: bool
    company_id: int
    next_recurring_charge_amount: str
    available_funds: str


@dataclass
class User:
    """Model for users endpoint."""
    id: int
    username: str
    name: str
    public_name: str
    locale: str
    role_id: Optional[str] = None
    email_address: str
    mobile_number: Optional[int] = None

