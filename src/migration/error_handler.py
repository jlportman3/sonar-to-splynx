"""Error handling and stop-on-error functionality for migration."""

from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
import traceback

from src.utils.logger import get_logger

logger = get_logger(__name__)

class ErrorSeverity(Enum):
    """Error severity levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ErrorCategory(Enum):
    """Error categories for classification."""
    NETWORK = "network"
    AUTHENTICATION = "authentication"
    VALIDATION = "validation"
    DATA_TRANSFORMATION = "data_transformation"
    API_ERROR = "api_error"
    SYSTEM_ERROR = "system_error"
    CUSTOMER_DATA = "customer_data"
    DEPENDENCY = "dependency"

@dataclass
class MigrationError(Exception):
    """Custom migration error with additional context."""
    message: str
    category: ErrorCategory = ErrorCategory.SYSTEM_ERROR
    severity: ErrorSeverity = ErrorSeverity.MEDIUM
    context: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.context is None:
            self.context = {}
        super().__init__(self.message)

@dataclass
class ErrorReport:
    """Detailed error report for analysis."""
    error_id: str
    error_message: str
    error_type: str
    category: ErrorCategory
    severity: ErrorSeverity
    context: Dict[str, Any]
    timestamp: datetime
    stack_trace: Optional[str] = None
    suggested_fixes: List[str] = None
    
    def __post_init__(self):
        if self.suggested_fixes is None:
            self.suggested_fixes = []

class MigrationErrorHandler:
    """Handles migration errors with stop-on-error behavior."""
    
    def __init__(self):
        """Initialize error handler."""
        self._error_count = 0
        self._last_error: Optional[ErrorReport] = None
        self._error_history: List[ErrorReport] = []
        self._recovery_suggestions: Dict[str, List[str]] = {}
        self._stop_on_error = True
        
        # Initialize recovery suggestions
        self._initialize_recovery_suggestions()
    
    @property
    def error_count(self) -> int:
        """Get total error count."""
        return self._error_count
    
    @property
    def last_error(self) -> Optional[ErrorReport]:
        """Get last error that occurred."""
        return self._last_error
    
    @property
    def recovery_suggestions(self) -> Dict[str, List[str]]:
        """Get recovery suggestions for error types."""
        return self._recovery_suggestions.copy()
    
    def handle_error(self, error: Exception, context: Dict[str, Any]) -> None:
        """Handle migration error with stop-on-error behavior."""
        self._error_count += 1
        
        # Create error report
        error_report = self._create_error_report(error, context)
        self._last_error = error_report
        self._error_history.append(error_report)
        
        # Log error with appropriate level
        self._log_error(error_report)
        
        # Generate suggestions
        suggestions = self.suggest_error_fixes(error_report.category.value)
        error_report.suggested_fixes = suggestions
        
        # Log suggestions
        if suggestions:
            logger.info(f"Suggested fixes for {error_report.category.value} error:")
            for i, suggestion in enumerate(suggestions, 1):
                logger.info(f"  {i}. {suggestion}")
        
        # Handle stop-on-error behavior
        if self._stop_on_error:
            logger.critical(f"Migration stopped due to error (stop_on_error=True)")
            logger.critical(f"Error ID: {error_report.error_id}")
            logger.critical(f"Fix the error and resume migration to continue")
            
            # In a real implementation, this might save state for resumption
            self._save_error_state(error_report)
    
    def create_error_report(self, migration_results: List[Any]) -> Dict[str, Any]:
        """Create comprehensive error report from migration results."""
        failed_results = [r for r in migration_results if hasattr(r, 'success') and not r.success]
        
        error_summary = {}
        error_details = []
        
        for result in failed_results:
            error_message = getattr(result, 'error_message', 'Unknown error')
            error_type = error_message.split(':')[0] if ':' in error_message else error_message
            
            error_summary[error_type] = error_summary.get(error_type, 0) + 1
            
            error_details.append({
                'customer_id': getattr(result, 'customer_id', None),
                'customer_name': getattr(result, 'customer_name', None),
                'error_message': error_message,
                'migration_time': getattr(result, 'migration_time', 0)
            })
        
        return {
            'total_errors': len(failed_results),
            'error_summary': error_summary,
            'error_details': error_details,
            'error_history': [self._error_report_to_dict(err) for err in self._error_history],
            'recovery_suggestions': self._recovery_suggestions
        }
    
    def suggest_error_fixes(self, error_type: str) -> List[str]:
        """Suggest fixes for specific error types."""
        suggestions = self._recovery_suggestions.get(error_type, [])
        
        # Add generic suggestions if no specific ones found
        if not suggestions:
            suggestions = [
                "Check network connectivity to both Sonar and Splynx instances",
                "Verify API credentials and permissions",
                "Review error logs for specific details",
                "Check if the issue is temporary and retry",
                "Contact system administrator if problem persists"
            ]
        
        return suggestions
    
    def enable_resume(self, error_id: str) -> bool:
        """Enable migration resume after error fix."""
        logger.info(f"Enabling resume for error ID: {error_id}")
        
        # Find the error in history
        error_report = None
        for err in self._error_history:
            if err.error_id == error_id:
                error_report = err
                break
        
        if not error_report:
            logger.error(f"Error ID {error_id} not found in history")
            return False
        
        # Mark error as resolved (placeholder implementation)
        logger.info(f"Error {error_id} marked as resolved, migration can resume")
        return True
    
    def clear_errors(self) -> None:
        """Clear error history and reset counters."""
        self._error_count = 0
        self._last_error = None
        self._error_history.clear()
        logger.info("Error history cleared")
    
    def set_stop_on_error(self, stop_on_error: bool) -> None:
        """Set stop-on-error behavior."""
        self._stop_on_error = stop_on_error
        logger.info(f"Stop-on-error set to: {stop_on_error}")
    
    def get_error_statistics(self) -> Dict[str, Any]:
        """Get error statistics and analysis."""
        if not self._error_history:
            return {
                'total_errors': 0,
                'error_categories': {},
                'error_severity': {},
                'most_common_errors': [],
                'error_timeline': []
            }
        
        # Categorize errors
        categories = {}
        severities = {}
        error_types = {}
        
        for error in self._error_history:
            # Count by category
            cat = error.category.value
            categories[cat] = categories.get(cat, 0) + 1
            
            # Count by severity
            sev = error.severity.value
            severities[sev] = severities.get(sev, 0) + 1
            
            # Count by error type
            err_type = error.error_type
            error_types[err_type] = error_types.get(err_type, 0) + 1
        
        # Get most common errors
        most_common = sorted(error_types.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Create timeline
        timeline = [
            {
                'timestamp': err.timestamp.isoformat(),
                'error_type': err.error_type,
                'category': err.category.value,
                'severity': err.severity.value
            }
            for err in self._error_history
        ]
        
        return {
            'total_errors': len(self._error_history),
            'error_categories': categories,
            'error_severity': severities,
            'most_common_errors': most_common,
            'error_timeline': timeline
        }
    
    def _create_error_report(self, error: Exception, context: Dict[str, Any]) -> ErrorReport:
        """Create detailed error report."""
        error_id = f"ERR_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{self._error_count:04d}"
        
        # Determine error category and severity
        category, severity = self._classify_error(error, context)
        
        # Get stack trace
        stack_trace = traceback.format_exc() if hasattr(error, '__traceback__') else None
        
        return ErrorReport(
            error_id=error_id,
            error_message=str(error),
            error_type=type(error).__name__,
            category=category,
            severity=severity,
            context=context.copy(),
            timestamp=datetime.now(),
            stack_trace=stack_trace
        )
    
    def _classify_error(self, error: Exception, context: Dict[str, Any]) -> tuple[ErrorCategory, ErrorSeverity]:
        """Classify error by category and severity."""
        error_message = str(error).lower()
        error_type = type(error).__name__
        
        # Check if it's a custom MigrationError
        if isinstance(error, MigrationError):
            return error.category, error.severity
        
        # Classify by error message content
        if any(keyword in error_message for keyword in ['connection', 'network', 'timeout', 'unreachable']):
            return ErrorCategory.NETWORK, ErrorSeverity.HIGH
        
        if any(keyword in error_message for keyword in ['authentication', 'unauthorized', 'forbidden', 'credentials']):
            return ErrorCategory.AUTHENTICATION, ErrorSeverity.CRITICAL
        
        if any(keyword in error_message for keyword in ['validation', 'invalid', 'required field', 'schema']):
            return ErrorCategory.VALIDATION, ErrorSeverity.MEDIUM
        
        if any(keyword in error_message for keyword in ['transform', 'mapping', 'conversion']):
            return ErrorCategory.DATA_TRANSFORMATION, ErrorSeverity.MEDIUM
        
        if any(keyword in error_message for keyword in ['api', 'endpoint', 'response', 'status code']):
            return ErrorCategory.API_ERROR, ErrorSeverity.HIGH
        
        if 'customer' in context.get('customer_name', '').lower() or 'customer_id' in context:
            return ErrorCategory.CUSTOMER_DATA, ErrorSeverity.MEDIUM
        
        # Default classification
        return ErrorCategory.SYSTEM_ERROR, ErrorSeverity.MEDIUM
    
    def _log_error(self, error_report: ErrorReport) -> None:
        """Log error with appropriate level based on severity."""
        log_message = f"Migration Error [{error_report.error_id}]: {error_report.error_message}"
        
        if error_report.context:
            context_str = ", ".join([f"{k}={v}" for k, v in error_report.context.items()])
            log_message += f" | Context: {context_str}"
        
        if error_report.severity == ErrorSeverity.CRITICAL:
            logger.critical(log_message)
        elif error_report.severity == ErrorSeverity.HIGH:
            logger.error(log_message)
        elif error_report.severity == ErrorSeverity.MEDIUM:
            logger.warning(log_message)
        else:
            logger.info(log_message)
        
        # Log stack trace for high severity errors
        if error_report.severity in [ErrorSeverity.HIGH, ErrorSeverity.CRITICAL] and error_report.stack_trace:
            logger.debug(f"Stack trace for {error_report.error_id}:\n{error_report.stack_trace}")
    
    def _save_error_state(self, error_report: ErrorReport) -> None:
        """Save error state for potential resumption."""
        # In a real implementation, this would save to a file or database
        logger.debug(f"Error state saved for {error_report.error_id}")
    
    def _error_report_to_dict(self, error_report: ErrorReport) -> Dict[str, Any]:
        """Convert error report to dictionary."""
        return {
            'error_id': error_report.error_id,
            'error_message': error_report.error_message,
            'error_type': error_report.error_type,
            'category': error_report.category.value,
            'severity': error_report.severity.value,
            'context': error_report.context,
            'timestamp': error_report.timestamp.isoformat(),
            'suggested_fixes': error_report.suggested_fixes
        }
    
    def _initialize_recovery_suggestions(self) -> None:
        """Initialize recovery suggestions for different error types."""
        self._recovery_suggestions = {
            'network': [
                "Check internet connectivity",
                "Verify Sonar and Splynx server URLs are accessible",
                "Check firewall settings and port access",
                "Test API endpoints manually with curl or Postman",
                "Verify DNS resolution for server hostnames"
            ],
            'authentication': [
                "Verify API credentials in .env file",
                "Check if API keys have expired",
                "Confirm user permissions for API access",
                "Test authentication with a simple API call",
                "Contact administrator to verify account status"
            ],
            'validation': [
                "Check required fields are present in data",
                "Verify data types match API schema requirements",
                "Review field length limits and constraints",
                "Check for special characters that might cause issues",
                "Validate data format (dates, emails, phone numbers)"
            ],
            'data_transformation': [
                "Review data mapping configuration",
                "Check for missing or null values in source data",
                "Verify field name mappings between systems",
                "Test transformation logic with sample data",
                "Check for data type conversion issues"
            ],
            'api_error': [
                "Check API endpoint URLs and methods",
                "Verify request payload format",
                "Review API rate limiting settings",
                "Check for API version compatibility",
                "Test with smaller data batches"
            ],
            'customer_data': [
                "Verify customer exists in Sonar",
                "Check customer data completeness",
                "Review customer status and permissions",
                "Validate customer contact information",
                "Check for duplicate customer records"
            ],
            'dependency': [
                "Ensure prerequisite data has been migrated",
                "Check foreign key relationships",
                "Verify required reference data exists",
                "Review migration phase order",
                "Check for circular dependencies"
            ],
            'system_error': [
                "Check system resources (memory, disk space)",
                "Review application logs for details",
                "Restart migration services if needed",
                "Check for software version compatibility",
                "Contact technical support if issue persists"
            ]
        }
