"""Customer selection and filtering logic for incremental migration."""

from typing import List, Optional, Tuple, Dict, Any
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
import logging

from src.apis.sonar_client import SonarGraphQLClient
from src.config.settings import config
from src.utils.logger import get_logger

logger = get_logger(__name__)

class CustomerStatus(Enum):
    """Customer status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"

class MigrationMode(Enum):
    """Migration mode enumeration."""
    SINGLE_CUSTOMER = "single"
    BATCH_CUSTOMERS = "batch"
    ALL_CUSTOMERS = "all"

@dataclass
class CustomerFilter:
    """Customer filtering criteria."""
    customer_ids: Optional[List[int]] = None
    status_filter: Optional[List[CustomerStatus]] = None
    date_range: Optional[Tuple[datetime, datetime]] = None
    limit: Optional[int] = None
    active_only: bool = True

@dataclass
class SonarCustomer:
    """Sonar customer data model."""
    id: int
    name: str
    status: CustomerStatus
    account_type: str
    created_date: datetime
    last_activity: Optional[datetime]
    email: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True
    services_count: int = 0
    billing_balance: float = 0.0

class CustomerSelector:
    """Handles customer filtering and selection logic."""
    
    def __init__(self, sonar_client: Optional[SonarGraphQLClient] = None):
        """Initialize customer selector with Sonar client."""
        self.sonar_client = sonar_client or SonarGraphQLClient(config)
        self._customers_cache: Optional[List[SonarCustomer]] = None
        self._cache_timestamp: Optional[datetime] = None
        self._cache_ttl_minutes = 30
        
    @property
    def total_customers(self) -> int:
        """Get total number of customers."""
        customers = self._get_all_customers()
        return len(customers)
    
    @property
    def active_count(self) -> int:
        """Get count of active customers."""
        customers = self._get_all_customers()
        return len([c for c in customers if c.is_active])
    
    def select_by_ids(self, customer_ids: List[int]) -> List[SonarCustomer]:
        """Select customers by specific IDs."""
        logger.info(f"Selecting customers by IDs: {customer_ids}")
        
        if not customer_ids:
            return []
        
        # Use GraphQL query to get specific customers
        query = """
        query GetCustomersByIds($ids: [ID!]!) {
            accounts(ids: $ids) {
                entities {
                    id
                    name
                    account_status {
                        name
                    }
                    account_type {
                        name
                    }
                    created_at
                    updated_at
                    contacts {
                        entities {
                            email_address
                            phone_number
                        }
                    }
                    services {
                        entities {
                            id
                            status
                        }
                    }
                    account_billing_parameters {
                        entities {
                            current_balance
                        }
                    }
                }
            }
        }
        """
        
        try:
            response = self.sonar_client.execute_query(query, {"ids": customer_ids})
            if response.success and response.data:
                customers = self._parse_sonar_customers(response.data.get("accounts", {}).get("entities", []))
                logger.info(f"Successfully selected {len(customers)} customers by IDs")
                return customers
            else:
                logger.error(f"Failed to select customers by IDs: {response.errors}")
                return []
        except Exception as e:
            logger.error(f"Error selecting customers by IDs: {e}")
            return []
    
    def select_active_customers(self, limit: Optional[int] = None) -> List[SonarCustomer]:
        """Get active customers with optional limit."""
        logger.info(f"Selecting active customers (limit: {limit})")
        
        filter_criteria = CustomerFilter(
            status_filter=[CustomerStatus.ACTIVE],
            active_only=True,
            limit=limit
        )
        
        return self.apply_filters(filter_criteria)
    
    def filter_by_status(self, status: CustomerStatus) -> List[SonarCustomer]:
        """Filter customers by status."""
        logger.info(f"Filtering customers by status: {status.value}")
        
        filter_criteria = CustomerFilter(status_filter=[status])
        return self.apply_filters(filter_criteria)
    
    def apply_filters(self, filter_criteria: CustomerFilter) -> List[SonarCustomer]:
        """Apply comprehensive filtering criteria."""
        logger.info(f"Applying customer filters: {filter_criteria}")
        
        # Get all customers if specific IDs not provided
        if filter_criteria.customer_ids:
            customers = self.select_by_ids(filter_criteria.customer_ids)
        else:
            customers = self._get_all_customers()
        
        # Apply status filter
        if filter_criteria.status_filter:
            status_values = [s.value for s in filter_criteria.status_filter]
            customers = [c for c in customers if c.status.value in status_values]
        
        # Apply active only filter
        if filter_criteria.active_only:
            customers = [c for c in customers if c.is_active]
        
        # Apply date range filter
        if filter_criteria.date_range:
            start_date, end_date = filter_criteria.date_range
            customers = [c for c in customers if start_date <= c.created_date <= end_date]
        
        # Apply limit
        if filter_criteria.limit:
            customers = customers[:filter_criteria.limit]
        
        logger.info(f"Filtered to {len(customers)} customers")
        return customers
    
    def get_customer_migration_order(self, customers: List[SonarCustomer]) -> List[SonarCustomer]:
        """Get customers in priority order for migration (active first, then by creation date)."""
        logger.info(f"Ordering {len(customers)} customers for migration")
        
        # Sort by: active status (True first), then by creation date (newest first)
        ordered_customers = sorted(
            customers,
            key=lambda c: (not c.is_active, -c.created_date.timestamp())
        )
        
        logger.info(f"Ordered customers: {len([c for c in ordered_customers if c.is_active])} active, "
                   f"{len([c for c in ordered_customers if not c.is_active])} inactive")
        
        return ordered_customers
    
    def _get_all_customers(self) -> List[SonarCustomer]:
        """Get all customers with caching."""
        # Check cache validity
        if (self._customers_cache and self._cache_timestamp and 
            (datetime.now() - self._cache_timestamp).total_seconds() < self._cache_ttl_minutes * 60):
            logger.debug("Using cached customer data")
            return self._customers_cache
        
        logger.info("Fetching all customers from Sonar")
        
        # GraphQL query to get all customers
        query = """
        query GetAllCustomers($limit: Int, $offset: Int) {
            accounts(limit: $limit, offset: $offset) {
                entities {
                    id
                    name
                    account_status {
                        name
                    }
                    account_type {
                        name
                    }
                    created_at
                    updated_at
                    contacts {
                        entities {
                            email_address
                            phone_number
                        }
                    }
                    services {
                        entities {
                            id
                            status
                        }
                    }
                    account_billing_parameters {
                        entities {
                            current_balance
                        }
                    }
                }
                page_info {
                    has_next_page
                    end_cursor
                }
            }
        }
        """
        
        all_customers = []
        offset = 0
        limit = 100
        has_more = True
        
        try:
            while has_more:
                response = self.sonar_client.execute_query(query, {"limit": limit, "offset": offset})
                
                if response.success and response.data:
                    accounts_data = response.data.get("accounts", {})
                    entities = accounts_data.get("entities", [])
                    page_info = accounts_data.get("page_info", {})
                    
                    customers = self._parse_sonar_customers(entities)
                    all_customers.extend(customers)
                    
                    has_more = page_info.get("has_next_page", False)
                    offset += limit
                    
                    logger.debug(f"Fetched {len(customers)} customers (total: {len(all_customers)})")
                else:
                    logger.error(f"Failed to fetch customers: {response.errors}")
                    break
            
            # Cache the results
            self._customers_cache = all_customers
            self._cache_timestamp = datetime.now()
            
            logger.info(f"Successfully fetched {len(all_customers)} total customers")
            return all_customers
            
        except Exception as e:
            logger.error(f"Error fetching all customers: {e}")
            return []
    
    def _parse_sonar_customers(self, entities: List[Dict[str, Any]]) -> List[SonarCustomer]:
        """Parse Sonar customer entities into SonarCustomer objects."""
        customers = []
        
        for entity in entities:
            try:
                # Parse status
                status_name = entity.get("account_status", {}).get("name", "").lower()
                if "active" in status_name:
                    status = CustomerStatus.ACTIVE
                elif "suspended" in status_name:
                    status = CustomerStatus.SUSPENDED
                elif "terminated" in status_name:
                    status = CustomerStatus.TERMINATED
                else:
                    status = CustomerStatus.INACTIVE
                
                # Parse contact info
                contacts = entity.get("contacts", {}).get("entities", [])
                email = None
                phone = None
                if contacts:
                    email = contacts[0].get("email_address")
                    phone = contacts[0].get("phone_number")
                
                # Parse services
                services = entity.get("services", {}).get("entities", [])
                services_count = len(services)
                is_active = any(s.get("status") == "active" for s in services) if services else status == CustomerStatus.ACTIVE
                
                # Parse billing
                billing_params = entity.get("account_billing_parameters", {}).get("entities", [])
                billing_balance = 0.0
                if billing_params:
                    billing_balance = float(billing_params[0].get("current_balance", 0))
                
                customer = SonarCustomer(
                    id=int(entity["id"]),
                    name=entity.get("name", ""),
                    status=status,
                    account_type=entity.get("account_type", {}).get("name", ""),
                    created_date=datetime.fromisoformat(entity["created_at"].replace("Z", "+00:00")),
                    last_activity=datetime.fromisoformat(entity["updated_at"].replace("Z", "+00:00")) if entity.get("updated_at") else None,
                    email=email,
                    phone=phone,
                    is_active=is_active,
                    services_count=services_count,
                    billing_balance=billing_balance
                )
                
                customers.append(customer)
                
            except Exception as e:
                logger.warning(f"Failed to parse customer entity {entity.get('id', 'unknown')}: {e}")
                continue
        
        return customers
    
    def clear_cache(self):
        """Clear the customer cache."""
        self._customers_cache = None
        self._cache_timestamp = None
        logger.info("Customer cache cleared")
    
    def get_customer_summary(self, customers: List[SonarCustomer]) -> Dict[str, Any]:
        """Get summary statistics for a list of customers."""
        if not customers:
            return {
                "total": 0,
                "active": 0,
                "inactive": 0,
                "suspended": 0,
                "terminated": 0,
                "with_services": 0,
                "total_services": 0,
                "total_balance": 0.0
            }
        
        summary = {
            "total": len(customers),
            "active": len([c for c in customers if c.status == CustomerStatus.ACTIVE]),
            "inactive": len([c for c in customers if c.status == CustomerStatus.INACTIVE]),
            "suspended": len([c for c in customers if c.status == CustomerStatus.SUSPENDED]),
            "terminated": len([c for c in customers if c.status == CustomerStatus.TERMINATED]),
            "with_services": len([c for c in customers if c.services_count > 0]),
            "total_services": sum(c.services_count for c in customers),
            "total_balance": sum(c.billing_balance for c in customers)
        }
        
        return summary
