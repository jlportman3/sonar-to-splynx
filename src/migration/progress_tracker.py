"""Progress tracking and reporting for migration operations."""

from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import time

from src.migration.customer_selector import SonarCustomer
from src.utils.logger import get_logger

logger = get_logger(__name__)

class MigrationPhase(Enum):
    """Migration phases for progress tracking."""
    INITIALIZATION = "initialization"
    CUSTOMER_SELECTION = "customer_selection"
    FOUNDATION_MIGRATION = "foundation_migration"
    NETWORK_MIGRATION = "network_migration"
    INVENTORY_MIGRATION = "inventory_migration"
    CUSTOMER_MIGRATION = "customer_migration"
    VALIDATION = "validation"
    COMPLETION = "completion"

class ProgressStatus(Enum):
    """Progress status enumeration."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

@dataclass
class PhaseProgress:
    """Progress tracking for a migration phase."""
    phase: MigrationPhase
    status: ProgressStatus
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    total_items: int = 0
    completed_items: int = 0
    failed_items: int = 0
    error_messages: List[str] = None
    
    def __post_init__(self):
        if self.error_messages is None:
            self.error_messages = []
    
    @property
    def duration(self) -> Optional[timedelta]:
        """Get phase duration."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        elif self.start_time:
            return datetime.now() - self.start_time
        return None
    
    @property
    def progress_percentage(self) -> float:
        """Get progress percentage for this phase."""
        if self.total_items == 0:
            return 100.0 if self.status == ProgressStatus.COMPLETED else 0.0
        return (self.completed_items / self.total_items) * 100.0
    
    @property
    def success_rate(self) -> float:
        """Get success rate for this phase."""
        processed_items = self.completed_items + self.failed_items
        if processed_items == 0:
            return 100.0 if self.status == ProgressStatus.COMPLETED else 0.0
        return (self.completed_items / processed_items) * 100.0

@dataclass
class CustomerProgress:
    """Progress tracking for individual customer migration."""
    customer_id: int
    customer_name: str
    status: ProgressStatus
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    entities_migrated: Dict[str, int] = None
    error_message: Optional[str] = None
    
    def __post_init__(self):
        if self.entities_migrated is None:
            self.entities_migrated = {}
    
    @property
    def duration(self) -> Optional[timedelta]:
        """Get customer migration duration."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        elif self.start_time:
            return datetime.now() - self.start_time
        return None

class ProgressTracker:
    """Tracks detailed progress and provides reporting for migration operations."""
    
    def __init__(self):
        """Initialize progress tracker."""
        self._migration_id: Optional[str] = None
        self._migration_start_time: Optional[datetime] = None
        self._migration_end_time: Optional[datetime] = None
        self._phase_progress: Dict[MigrationPhase, PhaseProgress] = {}
        self._customer_progress: Dict[int, CustomerProgress] = {}
        self._overall_status = ProgressStatus.NOT_STARTED
        self._current_phase: Optional[MigrationPhase] = None
        
        # Statistics
        self._total_customers = 0
        self._completed_customers = 0
        self._failed_customers = 0
        self._total_entities = 0
        self._migrated_entities = 0
        
        # Performance metrics
        self._throughput_samples: List[Dict[str, Any]] = []
        self._last_update_time = datetime.now()
    
    def start_migration(self, request: Any) -> str:
        """Start tracking a new migration."""
        self._migration_id = f"MIG_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self._migration_start_time = datetime.now()
        self._overall_status = ProgressStatus.IN_PROGRESS
        self._current_phase = MigrationPhase.INITIALIZATION
        
        # Initialize phase progress
        self._initialize_phases()
        
        # Start initialization phase
        self.start_phase(MigrationPhase.INITIALIZATION)
        
        logger.info(f"Started migration tracking: {self._migration_id}")
        return self._migration_id
    
    def start_phase(self, phase: MigrationPhase, total_items: int = 0) -> None:
        """Start tracking a migration phase."""
        self._current_phase = phase
        
        if phase not in self._phase_progress:
            self._phase_progress[phase] = PhaseProgress(
                phase=phase,
                status=ProgressStatus.NOT_STARTED,
                total_items=total_items
            )
        
        phase_progress = self._phase_progress[phase]
        phase_progress.status = ProgressStatus.IN_PROGRESS
        phase_progress.start_time = datetime.now()
        phase_progress.total_items = total_items
        
        logger.info(f"Started phase: {phase.value} (total items: {total_items})")
    
    def complete_phase(self, phase: MigrationPhase, success: bool = True) -> None:
        """Complete a migration phase."""
        if phase not in self._phase_progress:
            logger.warning(f"Attempting to complete untracked phase: {phase.value}")
            return
        
        phase_progress = self._phase_progress[phase]
        phase_progress.end_time = datetime.now()
        phase_progress.status = ProgressStatus.COMPLETED if success else ProgressStatus.FAILED
        
        if phase == self._current_phase:
            self._current_phase = None
        
        logger.info(f"Completed phase: {phase.value} (success: {success})")
    
    def update_phase_progress(self, phase: MigrationPhase, completed_items: int, failed_items: int = 0) -> None:
        """Update progress for a specific phase."""
        if phase not in self._phase_progress:
            logger.warning(f"Attempting to update untracked phase: {phase.value}")
            return
        
        phase_progress = self._phase_progress[phase]
        phase_progress.completed_items = completed_items
        phase_progress.failed_items = failed_items
        
        # Update throughput metrics
        self._update_throughput_metrics(phase, completed_items)
    
    def start_customer_migration(self, customer: SonarCustomer) -> None:
        """Start tracking individual customer migration."""
        self._customer_progress[customer.id] = CustomerProgress(
            customer_id=customer.id,
            customer_name=customer.name,
            status=ProgressStatus.IN_PROGRESS,
            start_time=datetime.now()
        )
        
        logger.debug(f"Started customer migration tracking: {customer.name} (ID: {customer.id})")
    
    def update_customer_progress(self, customer_id: int, success: bool, 
                                entities_migrated: Optional[Dict[str, int]] = None,
                                error_message: Optional[str] = None) -> None:
        """Update progress for individual customer migration."""
        if customer_id not in self._customer_progress:
            logger.warning(f"Attempting to update untracked customer: {customer_id}")
            return
        
        customer_progress = self._customer_progress[customer_id]
        customer_progress.end_time = datetime.now()
        customer_progress.status = ProgressStatus.COMPLETED if success else ProgressStatus.FAILED
        
        if entities_migrated:
            customer_progress.entities_migrated = entities_migrated
            # Update total entity counts
            self._migrated_entities += sum(entities_migrated.values())
        
        if error_message:
            customer_progress.error_message = error_message
        
        # Update customer counts
        if success:
            self._completed_customers += 1
        else:
            self._failed_customers += 1
        
        logger.debug(f"Updated customer progress: {customer_id} (success: {success})")
    
    def complete_migration(self, result: Any) -> None:
        """Complete migration tracking."""
        self._migration_end_time = datetime.now()
        self._overall_status = ProgressStatus.COMPLETED
        
        # Update final statistics
        if hasattr(result, 'total_customers'):
            self._total_customers = result.total_customers
        if hasattr(result, 'successful_migrations'):
            self._completed_customers = result.successful_migrations
        if hasattr(result, 'failed_migrations'):
            self._failed_customers = result.failed_migrations
        
        # Complete current phase if any
        if self._current_phase:
            self.complete_phase(self._current_phase, True)
        
        logger.info(f"Completed migration tracking: {self._migration_id}")
    
    def get_overall_progress(self) -> Dict[str, Any]:
        """Get overall migration progress."""
        total_duration = None
        if self._migration_start_time:
            end_time = self._migration_end_time or datetime.now()
            total_duration = end_time - self._migration_start_time
        
        # Calculate overall progress percentage
        completed_phases = len([p for p in self._phase_progress.values() if p.status == ProgressStatus.COMPLETED])
        total_phases = len(self._phase_progress)
        phase_progress_percentage = (completed_phases / total_phases * 100) if total_phases > 0 else 0
        
        # Calculate customer progress percentage
        customer_progress_percentage = 0
        if self._total_customers > 0:
            processed_customers = self._completed_customers + self._failed_customers
            customer_progress_percentage = (processed_customers / self._total_customers) * 100
        
        # Use the more detailed progress indicator
        overall_percentage = max(phase_progress_percentage, customer_progress_percentage)
        
        return {
            'migration_id': self._migration_id,
            'status': self._overall_status.value,
            'current_phase': self._current_phase.value if self._current_phase else None,
            'start_time': self._migration_start_time.isoformat() if self._migration_start_time else None,
            'end_time': self._migration_end_time.isoformat() if self._migration_end_time else None,
            'duration_seconds': total_duration.total_seconds() if total_duration else None,
            'overall_progress_percentage': round(overall_percentage, 2),
            'customers': {
                'total': self._total_customers,
                'completed': self._completed_customers,
                'failed': self._failed_customers,
                'remaining': self._total_customers - self._completed_customers - self._failed_customers,
                'success_rate': round((self._completed_customers / self._total_customers * 100) if self._total_customers > 0 else 0, 2)
            },
            'entities': {
                'total': self._total_entities,
                'migrated': self._migrated_entities
            }
        }
    
    def get_phase_progress(self) -> Dict[str, Any]:
        """Get detailed phase progress."""
        phases = {}
        
        for phase, progress in self._phase_progress.items():
            phases[phase.value] = {
                'status': progress.status.value,
                'start_time': progress.start_time.isoformat() if progress.start_time else None,
                'end_time': progress.end_time.isoformat() if progress.end_time else None,
                'duration_seconds': progress.duration.total_seconds() if progress.duration else None,
                'total_items': progress.total_items,
                'completed_items': progress.completed_items,
                'failed_items': progress.failed_items,
                'progress_percentage': round(progress.progress_percentage, 2),
                'success_rate': round(progress.success_rate, 2),
                'error_messages': progress.error_messages
            }
        
        return phases
    
    def get_customer_progress(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get detailed customer progress."""
        customers = []
        
        customer_list = list(self._customer_progress.values())
        if limit:
            customer_list = customer_list[:limit]
        
        for progress in customer_list:
            customers.append({
                'customer_id': progress.customer_id,
                'customer_name': progress.customer_name,
                'status': progress.status.value,
                'start_time': progress.start_time.isoformat() if progress.start_time else None,
                'end_time': progress.end_time.isoformat() if progress.end_time else None,
                'duration_seconds': progress.duration.total_seconds() if progress.duration else None,
                'entities_migrated': progress.entities_migrated,
                'error_message': progress.error_message
            })
        
        return customers
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics and throughput analysis."""
        if not self._throughput_samples:
            return {
                'average_throughput': 0,
                'peak_throughput': 0,
                'current_throughput': 0,
                'estimated_completion': None
            }
        
        # Calculate throughput metrics
        throughputs = [sample['throughput'] for sample in self._throughput_samples]
        average_throughput = sum(throughputs) / len(throughputs)
        peak_throughput = max(throughputs)
        current_throughput = throughputs[-1] if throughputs else 0
        
        # Estimate completion time
        estimated_completion = None
        if current_throughput > 0 and self._total_customers > 0:
            remaining_customers = self._total_customers - self._completed_customers - self._failed_customers
            estimated_seconds = remaining_customers / current_throughput
            estimated_completion = (datetime.now() + timedelta(seconds=estimated_seconds)).isoformat()
        
        return {
            'average_throughput': round(average_throughput, 2),
            'peak_throughput': round(peak_throughput, 2),
            'current_throughput': round(current_throughput, 2),
            'estimated_completion': estimated_completion,
            'throughput_unit': 'customers_per_minute'
        }
    
    def get_comprehensive_report(self) -> Dict[str, Any]:
        """Get comprehensive migration progress report."""
        return {
            'overall_progress': self.get_overall_progress(),
            'phase_progress': self.get_phase_progress(),
            'customer_progress_summary': {
                'total_customers': len(self._customer_progress),
                'completed_customers': len([c for c in self._customer_progress.values() if c.status == ProgressStatus.COMPLETED]),
                'failed_customers': len([c for c in self._customer_progress.values() if c.status == ProgressStatus.FAILED]),
                'in_progress_customers': len([c for c in self._customer_progress.values() if c.status == ProgressStatus.IN_PROGRESS])
            },
            'performance_metrics': self.get_performance_metrics(),
            'recent_customer_progress': self.get_customer_progress(limit=10)
        }
    
    def export_progress_report(self, format: str = 'json') -> str:
        """Export progress report in specified format."""
        report = self.get_comprehensive_report()
        
        if format.lower() == 'json':
            import json
            return json.dumps(report, indent=2, default=str)
        elif format.lower() == 'csv':
            # Export customer progress as CSV
            import csv
            import io
            
            output = io.StringIO()
            writer = csv.writer(output)
            
            # Write header
            writer.writerow(['Customer ID', 'Customer Name', 'Status', 'Start Time', 'End Time', 'Duration (seconds)', 'Entities Migrated', 'Error Message'])
            
            # Write customer data
            for progress in self._customer_progress.values():
                writer.writerow([
                    progress.customer_id,
                    progress.customer_name,
                    progress.status.value,
                    progress.start_time.isoformat() if progress.start_time else '',
                    progress.end_time.isoformat() if progress.end_time else '',
                    progress.duration.total_seconds() if progress.duration else '',
                    str(progress.entities_migrated),
                    progress.error_message or ''
                ])
            
            return output.getvalue()
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def _initialize_phases(self) -> None:
        """Initialize all migration phases."""
        phases = [
            MigrationPhase.INITIALIZATION,
            MigrationPhase.CUSTOMER_SELECTION,
            MigrationPhase.FOUNDATION_MIGRATION,
            MigrationPhase.NETWORK_MIGRATION,
            MigrationPhase.INVENTORY_MIGRATION,
            MigrationPhase.CUSTOMER_MIGRATION,
            MigrationPhase.VALIDATION,
            MigrationPhase.COMPLETION
        ]
        
        for phase in phases:
            if phase not in self._phase_progress:
                self._phase_progress[phase] = PhaseProgress(
                    phase=phase,
                    status=ProgressStatus.NOT_STARTED
                )
    
    def _update_throughput_metrics(self, phase: MigrationPhase, completed_items: int) -> None:
        """Update throughput metrics for performance tracking."""
        current_time = datetime.now()
        time_diff = (current_time - self._last_update_time).total_seconds()
        
        if time_diff >= 60:  # Update every minute
            # Calculate throughput (items per minute)
            if hasattr(self, '_last_completed_items'):
                items_processed = completed_items - self._last_completed_items
                throughput = (items_processed / time_diff) * 60  # Convert to per minute
                
                self._throughput_samples.append({
                    'timestamp': current_time,
                    'phase': phase.value,
                    'throughput': throughput,
                    'completed_items': completed_items
                })
                
                # Keep only last 60 samples (1 hour of data)
                if len(self._throughput_samples) > 60:
                    self._throughput_samples = self._throughput_samples[-60:]
            
            self._last_completed_items = completed_items
            self._last_update_time = current_time
