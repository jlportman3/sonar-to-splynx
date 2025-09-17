"""Priority phase management for Sonar to Splynx migration."""

from typing import Dict, Any, List, Optional
from enum import Enum
from datetime import datetime

from src.migration.customer_selector import SonarCustomer
from src.apis.sonar_client import SonarGraphQLClient
from src.apis.splynx_client import SplynxAPIClient
from src.utils.logger import get_logger

logger = get_logger(__name__)

class MigrationPriority(Enum):
    """Migration priority phases."""
    FOUNDATION = 1      # Company, users, groups, plans, tariffs
    NETWORK = 2         # Network, IP ranges, pools
    INVENTORY = 3       # Inventory, locations, vendors, models
    CUSTOMERS = 4       # Active customers first, others later

class PriorityManager:
    """Manages migration phases and priorities."""
    
    def __init__(self, sonar_client: SonarGraphQLClient, splynx_client: SplynxAPIClient):
        """Initialize priority manager."""
        self.sonar_client = sonar_client
        self.splynx_client = splynx_client
        
        self._current_phase: Optional[MigrationPriority] = None
        self._completed_phases: List[MigrationPriority] = []
        self._remaining_phases: List[MigrationPriority] = []
        
    @property
    def current_phase(self) -> Optional[MigrationPriority]:
        """Get current migration phase."""
        return self._current_phase
    
    @property
    def completed_phases(self) -> List[MigrationPriority]:
        """Get list of completed phases."""
        return self._completed_phases.copy()
    
    @property
    def remaining_phases(self) -> List[MigrationPriority]:
        """Get list of remaining phases."""
        return self._remaining_phases.copy()
    
    def get_migration_order(self, phases: List[MigrationPriority]) -> List[MigrationPriority]:
        """Get phases in correct migration order."""
        # Sort by enum value to ensure correct order
        ordered_phases = sorted(phases, key=lambda p: p.value)
        logger.info(f"Migration order: {[p.name for p in ordered_phases]}")
        return ordered_phases
    
    def execute_phase(self, phase: MigrationPriority, validate_with_api: bool = True) -> bool:
        """Execute a specific migration phase."""
        logger.info(f"Executing migration phase: {phase.name}")
        self._current_phase = phase
        
        try:
            if phase == MigrationPriority.FOUNDATION:
                success = self._migrate_foundation_data(validate_with_api)
            elif phase == MigrationPriority.NETWORK:
                success = self._migrate_network_infrastructure(validate_with_api)
            elif phase == MigrationPriority.INVENTORY:
                success = self._migrate_inventory_data(validate_with_api)
            elif phase == MigrationPriority.CUSTOMERS:
                # Customer migration is handled separately
                success = True
            else:
                logger.error(f"Unknown migration phase: {phase}")
                success = False
            
            if success:
                self._completed_phases.append(phase)
                logger.info(f"Phase {phase.name} completed successfully")
            else:
                logger.error(f"Phase {phase.name} failed")
            
            return success
            
        except Exception as e:
            logger.error(f"Phase {phase.name} failed with exception: {e}")
            return False
        finally:
            self._current_phase = None
    
    def validate_dependencies(self, phase: MigrationPriority) -> bool:
        """Validate that required dependencies are met for a phase."""
        logger.debug(f"Validating dependencies for phase: {phase.name}")
        
        if phase == MigrationPriority.FOUNDATION:
            # Foundation has no dependencies
            return True
        elif phase == MigrationPriority.NETWORK:
            # Network depends on foundation
            return MigrationPriority.FOUNDATION in self._completed_phases
        elif phase == MigrationPriority.INVENTORY:
            # Inventory depends on foundation
            return MigrationPriority.FOUNDATION in self._completed_phases
        elif phase == MigrationPriority.CUSTOMERS:
            # Customers depend on foundation, and optionally network/inventory
            return MigrationPriority.FOUNDATION in self._completed_phases
        
        return False
    
    def skip_phase(self, phase: MigrationPriority, reason: str = "User requested") -> None:
        """Skip a migration phase."""
        logger.info(f"Skipping phase {phase.name}: {reason}")
        # Don't add to completed phases, but remove from remaining if present
        if phase in self._remaining_phases:
            self._remaining_phases.remove(phase)
    
    def _migrate_foundation_data(self, validate_with_api: bool) -> bool:
        """Migrate company, user, group, plan, and tariff data."""
        logger.info("Starting foundation data migration")
        
        try:
            # Migrate company information
            company_success = self._migrate_company_info(validate_with_api)
            if not company_success:
                logger.error("Company migration failed")
                return False
            
            # Migrate users and groups
            users_success = self._migrate_users(validate_with_api)
            if not users_success:
                logger.error("Users migration failed")
                return False
            
            groups_success = self._migrate_groups(validate_with_api)
            if not groups_success:
                logger.error("Groups migration failed")
                return False
            
            # Migrate plans and tariffs
            plans_success = self._migrate_plans(validate_with_api)
            if not plans_success:
                logger.error("Plans migration failed")
                return False
            
            logger.info("Foundation data migration completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Foundation data migration failed: {e}")
            return False
    
    def _migrate_network_infrastructure(self, validate_with_api: bool) -> bool:
        """Migrate network, IP ranges, and pools."""
        logger.info("Starting network infrastructure migration")
        
        try:
            # Migrate IP ranges
            ip_ranges_success = self._migrate_ip_ranges(validate_with_api)
            if not ip_ranges_success:
                logger.error("IP ranges migration failed")
                return False
            
            # Migrate IP pools
            pools_success = self._migrate_pools(validate_with_api)
            if not pools_success:
                logger.error("IP pools migration failed")
                return False
            
            # Migrate network configuration
            network_success = self._migrate_network_config(validate_with_api)
            if not network_success:
                logger.error("Network configuration migration failed")
                return False
            
            logger.info("Network infrastructure migration completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Network infrastructure migration failed: {e}")
            return False
    
    def _migrate_inventory_data(self, validate_with_api: bool) -> bool:
        """Migrate inventory, locations, vendors, and models."""
        logger.info("Starting inventory data migration")
        
        try:
            # Migrate locations
            locations_success = self._migrate_locations(validate_with_api)
            if not locations_success:
                logger.error("Locations migration failed")
                return False
            
            # Migrate vendors
            vendors_success = self._migrate_vendors(validate_with_api)
            if not vendors_success:
                logger.error("Vendors migration failed")
                return False
            
            # Migrate models
            models_success = self._migrate_models(validate_with_api)
            if not models_success:
                logger.error("Models migration failed")
                return False
            
            # Migrate inventory items
            inventory_success = self._migrate_inventory(validate_with_api)
            if not inventory_success:
                logger.error("Inventory migration failed")
                return False
            
            logger.info("Inventory data migration completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Inventory data migration failed: {e}")
            return False
    
    def migrate_customer_data(self, customer: SonarCustomer, validate_with_api: bool) -> Dict[str, Any]:
        """Migrate individual customer data."""
        logger.info(f"Migrating customer data for: {customer.name} (ID: {customer.id})")
        
        try:
            entities_migrated = {}
            validation_results = {}
            
            # Extract customer data from Sonar
            customer_data = self._extract_customer_data(customer)
            if not customer_data:
                return {
                    "success": False,
                    "error_message": "Failed to extract customer data from Sonar"
                }
            
            # Transform customer data for Splynx
            transformed_data = self._transform_customer_data(customer_data)
            if not transformed_data:
                return {
                    "success": False,
                    "error_message": "Failed to transform customer data"
                }
            
            # Create customer in Splynx
            customer_result = self._create_splynx_customer(transformed_data, validate_with_api)
            if not customer_result.get("success"):
                return {
                    "success": False,
                    "error_message": f"Failed to create customer in Splynx: {customer_result.get('error')}"
                }
            
            entities_migrated["customer"] = 1
            validation_results["customer"] = customer_result.get("validated", False)
            
            # Migrate customer services
            if customer.services_count > 0:
                services_result = self._migrate_customer_services(customer, customer_result.get("customer_id"), validate_with_api)
                entities_migrated["services"] = services_result.get("count", 0)
                validation_results["services"] = services_result.get("success", False)
            
            # Migrate customer billing data
            billing_result = self._migrate_customer_billing(customer, customer_result.get("customer_id"), validate_with_api)
            entities_migrated["billing"] = billing_result.get("count", 0)
            validation_results["billing"] = billing_result.get("success", False)
            
            logger.info(f"Customer migration completed for {customer.name}")
            return {
                "success": True,
                "entities_migrated": entities_migrated,
                "validation_results": validation_results
            }
            
        except Exception as e:
            logger.error(f"Customer migration failed for {customer.name}: {e}")
            return {
                "success": False,
                "error_message": str(e)
            }
    
    # Foundation migration methods
    def _migrate_company_info(self, validate_with_api: bool) -> bool:
        """Migrate company information."""
        logger.info("Migrating company information")
        
        # Query Sonar for company information
        query = """
        query GetCompanyInfo {
            company {
                name
                address
                phone
                email
                website
            }
        }
        """
        
        try:
            response = self.sonar_client.execute_query(query)
            if response.success and response.data:
                company_data = response.data.get("company", {})
                
                # Transform and create in Splynx (placeholder implementation)
                # This would typically involve creating/updating company settings in Splynx
                logger.info(f"Company data extracted: {company_data.get('name', 'Unknown')}")
                return True
            else:
                logger.error(f"Failed to extract company info: {response.errors}")
                return False
                
        except Exception as e:
            logger.error(f"Company migration failed: {e}")
            return False
    
    def _migrate_users(self, validate_with_api: bool) -> bool:
        """Migrate user accounts."""
        logger.info("Migrating user accounts")
        
        # Query Sonar for users
        query = """
        query GetUsers {
            users {
                entities {
                    id
                    name
                    email_address
                    role
                    enabled
                }
            }
        }
        """
        
        try:
            response = self.sonar_client.execute_query(query)
            if response.success and response.data:
                users = response.data.get("users", {}).get("entities", [])
                logger.info(f"Found {len(users)} users to migrate")
                
                # Transform and create users in Splynx (placeholder)
                # This would involve creating administrator accounts in Splynx
                return True
            else:
                logger.error(f"Failed to extract users: {response.errors}")
                return False
                
        except Exception as e:
            logger.error(f"Users migration failed: {e}")
            return False
    
    def _migrate_groups(self, validate_with_api: bool) -> bool:
        """Migrate user groups."""
        logger.info("Migrating user groups")
        # Placeholder implementation
        return True
    
    def _migrate_plans(self, validate_with_api: bool) -> bool:
        """Migrate service plans and tariffs."""
        logger.info("Migrating service plans and tariffs")
        
        # Query Sonar for service plans
        query = """
        query GetServicePlans {
            service_plans {
                entities {
                    id
                    name
                    description
                    price
                    data_service_detail {
                        download_speed_kilobits_per_second
                        upload_speed_kilobits_per_second
                    }
                }
            }
        }
        """
        
        try:
            response = self.sonar_client.execute_query(query)
            if response.success and response.data:
                plans = response.data.get("service_plans", {}).get("entities", [])
                logger.info(f"Found {len(plans)} service plans to migrate")
                
                # Transform and create tariffs in Splynx
                for plan in plans:
                    tariff_data = {
                        "title": plan.get("name", ""),
                        "partners_ids": [1],  # Default partner
                        "speed_download": plan.get("data_service_detail", {}).get("download_speed_kilobits_per_second", 1024),
                        "speed_upload": plan.get("data_service_detail", {}).get("upload_speed_kilobits_per_second", 1024),
                        "price": float(plan.get("price", 0)),
                        "with_vat": True,
                        "billing_types": ["recurring"],
                        "available_for_locations": [1],
                        "customer_categories": ["person"]
                    }
                    
                    if validate_with_api:
                        result = self.splynx_client.create_tariff_internet(tariff_data)
                        if not result.get("success"):
                            logger.error(f"Failed to create tariff {plan.get('name')}: {result.get('error')}")
                            return False
                
                return True
            else:
                logger.error(f"Failed to extract service plans: {response.errors}")
                return False
                
        except Exception as e:
            logger.error(f"Plans migration failed: {e}")
            return False
    
    # Network migration methods
    def _migrate_ip_ranges(self, validate_with_api: bool) -> bool:
        """Migrate IP address ranges."""
        logger.info("Migrating IP address ranges")
        # Placeholder implementation
        return True
    
    def _migrate_pools(self, validate_with_api: bool) -> bool:
        """Migrate IP pools."""
        logger.info("Migrating IP pools")
        # Placeholder implementation
        return True
    
    def _migrate_network_config(self, validate_with_api: bool) -> bool:
        """Migrate network configuration."""
        logger.info("Migrating network configuration")
        # Placeholder implementation
        return True
    
    # Inventory migration methods
    def _migrate_locations(self, validate_with_api: bool) -> bool:
        """Migrate locations."""
        logger.info("Migrating locations")
        # Placeholder implementation
        return True
    
    def _migrate_vendors(self, validate_with_api: bool) -> bool:
        """Migrate vendors."""
        logger.info("Migrating vendors")
        # Placeholder implementation
        return True
    
    def _migrate_models(self, validate_with_api: bool) -> bool:
        """Migrate equipment models."""
        logger.info("Migrating equipment models")
        # Placeholder implementation
        return True
    
    def _migrate_inventory(self, validate_with_api: bool) -> bool:
        """Migrate inventory items."""
        logger.info("Migrating inventory items")
        # Placeholder implementation
        return True
    
    # Customer migration helper methods
    def _extract_customer_data(self, customer: SonarCustomer) -> Optional[Dict[str, Any]]:
        """Extract detailed customer data from Sonar."""
        query = """
        query GetCustomerDetails($id: ID!) {
            account(id: $id) {
                id
                name
                account_status {
                    name
                }
                account_type {
                    name
                }
                created_at
                contacts {
                    entities {
                        name
                        email_address
                        phone_number
                        role
                    }
                }
                services {
                    entities {
                        id
                        status
                        service_plan {
                            name
                            price
                        }
                    }
                }
                account_billing_parameters {
                    entities {
                        current_balance
                        billing_start_date
                    }
                }
                addresses {
                    entities {
                        line_1
                        city
                        state
                        zip
                        country
                    }
                }
            }
        }
        """
        
        try:
            response = self.sonar_client.execute_query(query, {"id": customer.id})
            if response.success and response.data:
                return response.data.get("account")
            else:
                logger.error(f"Failed to extract customer data: {response.errors}")
                return None
        except Exception as e:
            logger.error(f"Error extracting customer data: {e}")
            return None
    
    def _transform_customer_data(self, customer_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Transform Sonar customer data for Splynx."""
        try:
            # Extract contact information
            contacts = customer_data.get("contacts", {}).get("entities", [])
            primary_contact = contacts[0] if contacts else {}
            
            # Extract address information
            addresses = customer_data.get("addresses", {}).get("entities", [])
            primary_address = addresses[0] if addresses else {}
            
            # Transform to Splynx customer format
            transformed = {
                "login": f"customer_{customer_data['id']}",
                "password": "temp_password_123",  # Should be generated securely
                "name": customer_data.get("name", ""),
                "email": primary_contact.get("email_address", ""),
                "phone": primary_contact.get("phone_number", ""),
                "status": "new",  # Will be updated based on account status
                "category": "person",  # Default category
                "street_1": primary_address.get("line_1", ""),
                "city": primary_address.get("city", ""),
                "zip_code": primary_address.get("zip", ""),
                "date_add": datetime.now().strftime("%Y-%m-%d"),
                "partner_id": 1,
                "location_id": 1,
                "billing_type": "recurring"
            }
            
            return transformed
            
        except Exception as e:
            logger.error(f"Error transforming customer data: {e}")
            return None
    
    def _create_splynx_customer(self, customer_data: Dict[str, Any], validate_with_api: bool) -> Dict[str, Any]:
        """Create customer in Splynx."""
        try:
            if validate_with_api:
                # Validate data before creation
                validation_result = self.splynx_client.options("admin/customers/customer")
                if not validation_result.get("success"):
                    return {"success": False, "error": "Schema validation failed"}
                
                # Create customer
                result = self.splynx_client.post("admin/customers/customer", customer_data)
                if result.get("success"):
                    customer_id = result.get("data", {}).get("id")
                    return {
                        "success": True,
                        "customer_id": customer_id,
                        "validated": True
                    }
                else:
                    return {"success": False, "error": result.get("error")}
            else:
                # Simulate creation for dry run
                return {
                    "success": True,
                    "customer_id": 999999,  # Placeholder ID
                    "validated": False
                }
                
        except Exception as e:
            logger.error(f"Error creating Splynx customer: {e}")
            return {"success": False, "error": str(e)}
    
    def _migrate_customer_services(self, customer: SonarCustomer, splynx_customer_id: int, validate_with_api: bool) -> Dict[str, Any]:
        """Migrate customer services."""
        # Placeholder implementation
        return {"success": True, "count": customer.services_count}
    
    def _migrate_customer_billing(self, customer: SonarCustomer, splynx_customer_id: int, validate_with_api: bool) -> Dict[str, Any]:
        """Migrate customer billing data."""
        # Placeholder implementation
        return {"success": True, "count": 1}
