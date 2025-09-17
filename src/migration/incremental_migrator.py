"""Incremental migration orchestrator for Sonar to Splynx data transfer."""

from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
import time

from src.migration.customer_selector import CustomerSelector, SonarCustomer, CustomerFilter, MigrationMode
from src.migration.priority_manager import PriorityManager, MigrationPriority
from src.migration.error_handler import MigrationErrorHandler, MigrationError
from src.migration.progress_tracker import ProgressTracker
from src.apis.sonar_client import SonarGraphQLClient
from src.apis.splynx_client import SplynxAPIClient
from src.config.settings import config
from src.utils.logger import get_logger

logger = get_logger(__name__)

@dataclass
class MigrationRequest:
    """Migration request configuration."""
    mode: MigrationMode
    customer_filter: CustomerFilter
    priority_phases: List[MigrationPriority]
    stop_on_error: bool = True
    validate_with_api: bool = True
    dry_run: bool = False

@dataclass
class MigrationResult:
    """Result of a customer migration."""
    customer_id: int
    customer_name: str
    success: bool
    error_message: Optional[str] = None
    entities_migrated: Dict[str, int] = None
    validation_results: Dict[str, bool] = None
    migration_time: float = 0.0
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    
    def __post_init__(self):
        if self.entities_migrated is None:
            self.entities_migrated = {}
        if self.validation_results is None:
            self.validation_results = {}

@dataclass
class BatchMigrationResult:
    """Result of a batch migration."""
    total_customers: int
    successful_migrations: int
    failed_migrations: int
    migration_results: List[MigrationResult]
    total_time: float
    start_time: datetime
    end_time: datetime
    phases_completed: List[MigrationPriority]
    error_summary: Dict[str, int]

class IncrementalMigrator:
    """Orchestrates incremental customer migration with priority phases."""
    
    def __init__(self, 
                 sonar_client: Optional[SonarGraphQLClient] = None,
                 splynx_client: Optional[SplynxAPIClient] = None):
        """Initialize incremental migrator."""
        self.sonar_client = sonar_client or SonarGraphQLClient(config)
        self.splynx_client = splynx_client or SplynxAPIClient(config)
        
        self.customer_selector = CustomerSelector(self.sonar_client)
        self.priority_manager = PriorityManager(self.sonar_client, self.splynx_client)
        self.error_handler = MigrationErrorHandler()
        self.progress_tracker = ProgressTracker()
        
        self._current_batch: List[SonarCustomer] = []
        self._migration_status = "idle"
        self._error_state = False
        
    @property
    def current_batch(self) -> List[SonarCustomer]:
        """Get current batch of customers being migrated."""
        return self._current_batch
    
    @property
    def migration_status(self) -> str:
        """Get current migration status."""
        return self._migration_status
    
    @property
    def error_state(self) -> bool:
        """Check if migration is in error state."""
        return self._error_state
    
    def migrate_single_customer(self, customer_id: int, 
                               priority_phases: Optional[List[MigrationPriority]] = None,
                               stop_on_error: bool = True,
                               validate_with_api: bool = True,
                               dry_run: bool = False) -> MigrationResult:
        """Migrate a single customer."""
        logger.info(f"Starting single customer migration for ID: {customer_id}")
        
        # Create migration request
        request = MigrationRequest(
            mode=MigrationMode.SINGLE_CUSTOMER,
            customer_filter=CustomerFilter(customer_ids=[customer_id]),
            priority_phases=priority_phases or [MigrationPriority.FOUNDATION, 
                                              MigrationPriority.NETWORK, 
                                              MigrationPriority.INVENTORY, 
                                              MigrationPriority.CUSTOMERS],
            stop_on_error=stop_on_error,
            validate_with_api=validate_with_api,
            dry_run=dry_run
        )
        
        # Execute migration
        batch_result = self.migrate_customers(request)
        
        if batch_result.migration_results:
            return batch_result.migration_results[0]
        else:
            return MigrationResult(
                customer_id=customer_id,
                customer_name="Unknown",
                success=False,
                error_message="Customer not found or could not be selected"
            )
    
    def migrate_customer_batch(self, customer_ids: List[int],
                              priority_phases: Optional[List[MigrationPriority]] = None,
                              stop_on_error: bool = True,
                              validate_with_api: bool = True,
                              dry_run: bool = False) -> BatchMigrationResult:
        """Migrate a batch of customers."""
        logger.info(f"Starting batch migration for {len(customer_ids)} customers")
        
        # Create migration request
        request = MigrationRequest(
            mode=MigrationMode.BATCH_CUSTOMERS,
            customer_filter=CustomerFilter(customer_ids=customer_ids),
            priority_phases=priority_phases or [MigrationPriority.FOUNDATION, 
                                              MigrationPriority.NETWORK, 
                                              MigrationPriority.INVENTORY, 
                                              MigrationPriority.CUSTOMERS],
            stop_on_error=stop_on_error,
            validate_with_api=validate_with_api,
            dry_run=dry_run
        )
        
        return self.migrate_customers(request)
    
    def migrate_all_customers(self, customer_filter: Optional[CustomerFilter] = None,
                             priority_phases: Optional[List[MigrationPriority]] = None,
                             stop_on_error: bool = True,
                             validate_with_api: bool = True,
                             dry_run: bool = False) -> BatchMigrationResult:
        """Migrate all customers matching filter criteria."""
        logger.info("Starting migration of all customers")
        
        # Create migration request
        request = MigrationRequest(
            mode=MigrationMode.ALL_CUSTOMERS,
            customer_filter=customer_filter or CustomerFilter(active_only=True),
            priority_phases=priority_phases or [MigrationPriority.FOUNDATION, 
                                              MigrationPriority.NETWORK, 
                                              MigrationPriority.INVENTORY, 
                                              MigrationPriority.CUSTOMERS],
            stop_on_error=stop_on_error,
            validate_with_api=validate_with_api,
            dry_run=dry_run
        )
        
        return self.migrate_customers(request)
    
    def migrate_customers(self, request: MigrationRequest) -> BatchMigrationResult:
        """Execute customer migration based on request configuration."""
        start_time = datetime.now()
        self._migration_status = "running"
        self._error_state = False
        
        logger.info(f"Starting migration with mode: {request.mode.value}")
        
        try:
            # Initialize progress tracking
            self.progress_tracker.start_migration(request)
            
            # Select customers based on filter
            customers = self.customer_selector.apply_filters(request.customer_filter)
            if not customers:
                logger.warning("No customers selected for migration")
                return self._create_empty_batch_result(start_time)
            
            # Order customers for migration
            ordered_customers = self.customer_selector.get_customer_migration_order(customers)
            self._current_batch = ordered_customers
            
            logger.info(f"Selected {len(ordered_customers)} customers for migration")
            
            # Execute priority phases first (if not dry run)
            phases_completed = []
            if not request.dry_run:
                phases_completed = self._execute_priority_phases(request.priority_phases, request)
            
            # Migrate individual customers
            migration_results = []
            for i, customer in enumerate(ordered_customers):
                logger.info(f"Migrating customer {i+1}/{len(ordered_customers)}: {customer.name} (ID: {customer.id})")
                
                try:
                    result = self._migrate_individual_customer(customer, request)
                    migration_results.append(result)
                    
                    # Update progress
                    self.progress_tracker.update_customer_progress(customer.id, result.success)
                    
                    # Handle errors
                    if not result.success:
                        self.error_handler.handle_error(
                            MigrationError(f"Customer migration failed: {result.error_message}"),
                            {"customer_id": customer.id, "customer_name": customer.name}
                        )
                        
                        if request.stop_on_error:
                            logger.error(f"Stopping migration due to error with customer {customer.id}")
                            self._error_state = True
                            break
                    
                except Exception as e:
                    error_result = MigrationResult(
                        customer_id=customer.id,
                        customer_name=customer.name,
                        success=False,
                        error_message=str(e)
                    )
                    migration_results.append(error_result)
                    
                    self.error_handler.handle_error(e, {"customer_id": customer.id})
                    
                    if request.stop_on_error:
                        logger.error(f"Stopping migration due to exception with customer {customer.id}: {e}")
                        self._error_state = True
                        break
            
            # Create batch result
            end_time = datetime.now()
            total_time = (end_time - start_time).total_seconds()
            
            successful_count = len([r for r in migration_results if r.success])
            failed_count = len([r for r in migration_results if not r.success])
            
            # Generate error summary
            error_summary = {}
            for result in migration_results:
                if not result.success and result.error_message:
                    error_type = result.error_message.split(':')[0] if ':' in result.error_message else result.error_message
                    error_summary[error_type] = error_summary.get(error_type, 0) + 1
            
            batch_result = BatchMigrationResult(
                total_customers=len(ordered_customers),
                successful_migrations=successful_count,
                failed_migrations=failed_count,
                migration_results=migration_results,
                total_time=total_time,
                start_time=start_time,
                end_time=end_time,
                phases_completed=phases_completed,
                error_summary=error_summary
            )
            
            # Complete progress tracking
            self.progress_tracker.complete_migration(batch_result)
            
            self._migration_status = "completed" if not self._error_state else "failed"
            
            logger.info(f"Migration completed: {successful_count} successful, {failed_count} failed")
            return batch_result
            
        except Exception as e:
            logger.error(f"Migration failed with exception: {e}")
            self._migration_status = "failed"
            self._error_state = True
            
            end_time = datetime.now()
            return BatchMigrationResult(
                total_customers=0,
                successful_migrations=0,
                failed_migrations=0,
                migration_results=[],
                total_time=(end_time - start_time).total_seconds(),
                start_time=start_time,
                end_time=end_time,
                phases_completed=[],
                error_summary={"system_error": 1}
            )
    
    def _execute_priority_phases(self, phases: List[MigrationPriority], 
                                request: MigrationRequest) -> List[MigrationPriority]:
        """Execute priority phases before customer migration."""
        completed_phases = []
        
        for phase in phases:
            if phase == MigrationPriority.CUSTOMERS:
                continue  # Skip customer phase as it's handled separately
            
            logger.info(f"Executing priority phase: {phase.name}")
            
            try:
                success = self.priority_manager.execute_phase(phase, request.validate_with_api)
                if success:
                    completed_phases.append(phase)
                    logger.info(f"Phase {phase.name} completed successfully")
                else:
                    logger.error(f"Phase {phase.name} failed")
                    if request.stop_on_error:
                        break
            except Exception as e:
                logger.error(f"Phase {phase.name} failed with exception: {e}")
                if request.stop_on_error:
                    break
        
        return completed_phases
    
    def _migrate_individual_customer(self, customer: SonarCustomer, 
                                   request: MigrationRequest) -> MigrationResult:
        """Migrate an individual customer."""
        start_time = datetime.now()
        
        try:
            if request.dry_run:
                # Simulate migration for dry run
                time.sleep(0.1)  # Simulate processing time
                return MigrationResult(
                    customer_id=customer.id,
                    customer_name=customer.name,
                    success=True,
                    entities_migrated={"customer": 1, "services": customer.services_count},
                    validation_results={"customer": True, "services": True},
                    migration_time=0.1,
                    start_time=start_time,
                    end_time=datetime.now()
                )
            
            # Execute actual customer migration
            result = self.priority_manager.migrate_customer_data(customer, request.validate_with_api)
            
            end_time = datetime.now()
            migration_time = (end_time - start_time).total_seconds()
            
            return MigrationResult(
                customer_id=customer.id,
                customer_name=customer.name,
                success=result.get("success", False),
                error_message=result.get("error_message"),
                entities_migrated=result.get("entities_migrated", {}),
                validation_results=result.get("validation_results", {}),
                migration_time=migration_time,
                start_time=start_time,
                end_time=end_time
            )
            
        except Exception as e:
            end_time = datetime.now()
            migration_time = (end_time - start_time).total_seconds()
            
            return MigrationResult(
                customer_id=customer.id,
                customer_name=customer.name,
                success=False,
                error_message=str(e),
                migration_time=migration_time,
                start_time=start_time,
                end_time=end_time
            )
    
    def _create_empty_batch_result(self, start_time: datetime) -> BatchMigrationResult:
        """Create empty batch result when no customers are selected."""
        end_time = datetime.now()
        return BatchMigrationResult(
            total_customers=0,
            successful_migrations=0,
            failed_migrations=0,
            migration_results=[],
            total_time=(end_time - start_time).total_seconds(),
            start_time=start_time,
            end_time=end_time,
            phases_completed=[],
            error_summary={}
        )
    
    def resume_failed_migration(self, migration_id: str) -> BatchMigrationResult:
        """Resume a failed migration after error fixes."""
        logger.info(f"Resuming failed migration: {migration_id}")
        
        # This would typically load the migration state from storage
        # For now, we'll return a placeholder implementation
        raise NotImplementedError("Migration resume functionality not yet implemented")
    
    def get_migration_summary(self, result: BatchMigrationResult) -> Dict[str, Any]:
        """Get detailed migration summary."""
        return {
            "overview": {
                "total_customers": result.total_customers,
                "successful": result.successful_migrations,
                "failed": result.failed_migrations,
                "success_rate": (result.successful_migrations / result.total_customers * 100) if result.total_customers > 0 else 0,
                "total_time": result.total_time,
                "average_time_per_customer": result.total_time / result.total_customers if result.total_customers > 0 else 0
            },
            "phases_completed": [phase.name for phase in result.phases_completed],
            "error_summary": result.error_summary,
            "timeline": {
                "start_time": result.start_time.isoformat(),
                "end_time": result.end_time.isoformat()
            },
            "customer_details": [
                {
                    "customer_id": r.customer_id,
                    "customer_name": r.customer_name,
                    "success": r.success,
                    "error_message": r.error_message,
                    "entities_migrated": r.entities_migrated,
                    "migration_time": r.migration_time
                }
                for r in result.migration_results
            ]
        }
