#!/usr/bin/env python3
"""
Normalized Schema for Sonar to Splynx Migration

This module defines the normalized data structures used as an intermediate
format during the migration process. It provides a common schema that can
accommodate data from both Sonar and Splynx systems.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
from enum import Enum
import json

class EntityType(Enum):
    """Supported entity types for migration."""
    CUSTOMER = "customer"
    CONTACT = "contact"
    SERVICE_INTERNET = "service_internet"
    SERVICE_VOICE = "service_voice"
    SERVICE_CUSTOM = "service_custom"
    INVOICE = "invoice"
    PAYMENT = "payment"
    TRANSACTION = "transaction"
    DEVICE = "device"
    TICKET = "ticket"
    LOCATION = "location"
    TARIFF = "tariff"
    NETWORK = "network"
    IP_ADDRESS = "ip_address"

class MigrationStatus(Enum):
    """Migration status for entities."""
    PENDING = "pending"
    EXTRACTED = "extracted"
    TRANSFORMED = "transformed"
    LOADED = "loaded"
    FAILED = "failed"
    SKIPPED = "skipped"

@dataclass
class NormalizedEntity:
    """Base class for all normalized entities."""
    source_id: str                          # Original ID from source system
    entity_type: EntityType                 # Type of entity
    source_system: str                      # "sonar" or "splynx"
    target_id: Optional[str] = None        # ID in target system after migration
    data: Dict[str, Any] = field(default_factory=dict)  # Normalized data
    metadata: Dict[str, Any] = field(default_factory=dict)  # Migration metadata
    relationships: List[str] = field(default_factory=list)  # Related entity IDs
    validation_errors: List[str] = field(default_factory=list)  # Validation issues
    migration_status: MigrationStatus = MigrationStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def add_relationship(self, related_id: str, relationship_type: str):
        """Add a relationship to another entity."""
        relationship = f"{relationship_type}:{related_id}"
        if relationship not in self.relationships:
            self.relationships.append(relationship)

    def set_validation_error(self, error: str):
        """Add a validation error."""
        if error not in self.validation_errors:
            self.validation_errors.append(error)

    def is_valid(self) -> bool:
        """Check if entity is valid for migration."""
        return len(self.validation_errors) == 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'source_id': self.source_id,
            'entity_type': self.entity_type.value,
            'source_system': self.source_system,
            'target_id': self.target_id,
            'data': self.data,
            'metadata': self.metadata,
            'relationships': self.relationships,
            'validation_errors': self.validation_errors,
            'migration_status': self.migration_status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

@dataclass
class NormalizedCustomer(NormalizedEntity):
    """Normalized customer/account data."""
    
    def __post_init__(self):
        self.entity_type = EntityType.CUSTOMER
        # Set default data structure
        if not self.data:
            self.data = {
                'login': '',
                'name': '',
                'email': '',
                'phone': '',
                'status': 'new',
                'category': 'person',  # person or company
                'street_1': '',
                'city': '',
                'zip_code': '',
                'date_add': '',
                'partner_id': 1,
                'location_id': 1,
                'billing_type': 'recurring',
                'additional_attributes': {}
            }

@dataclass
class NormalizedContact(NormalizedEntity):
    """Normalized contact data."""
    
    def __post_init__(self):
        self.entity_type = EntityType.CONTACT
        if not self.data:
            self.data = {
                'customer_id': '',
                'name': '',
                'email': '',
                'phone': '',
                'type': 'primary',  # primary, billing, technical
                'additional_attributes': {}
            }

@dataclass
class NormalizedService(NormalizedEntity):
    """Normalized service data."""
    
    def __post_init__(self):
        # Will be set by specific service type
        if not self.data:
            self.data = {
                'customer_id': '',
                'tariff_id': '',
                'status': 'active',
                'description': '',
                'start_date': '',
                'end_date': '0000-00-00',
                'quantity': 1,
                'unit_price': 0.0,
                'additional_attributes': {}
            }

@dataclass
class NormalizedInternetService(NormalizedService):
    """Normalized internet service data."""
    
    def __post_init__(self):
        super().__post_init__()
        self.entity_type = EntityType.SERVICE_INTERNET
        self.data.update({
            'login': '',
            'password': '',
            'router_id': 0,
            'taking_ipv4': 0,  # 0=None, 1=Permanent, 2=Dynamic
            'ipv4': '',
            'ipv4_pool_id': 0,
            'mac': '',
