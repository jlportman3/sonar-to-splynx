# Implementation Plan

## Overview
Create a comprehensive incremental migration system to transfer pertinent data from Sonar instance to Splynx instance with selective customer migration capabilities.

This migration application will handle incremental data transfer with the ability to migrate one customer, a hundred customers, or all customers from Sonar to Splynx. The system prioritizes company/user/group information, plans, and tariffs first, followed by network infrastructure, then inventory management, with active customers taking priority over inactive ones. The implementation uses API-first validation, stops on any error for immediate resolution, and provides detailed progress tracking throughout the migration process.

## Types
Define comprehensive data models for incremental migration with customer selection capabilities.

**Migration Priority Enums:**
```python
class MigrationPriority(Enum):
    FOUNDATION = 1      # Company, users, groups, plans, tariffs
    NETWORK = 2         # Network, IP ranges, pools
    INVENTORY = 3       # Inventory, locations, vendors, models
    CUSTOMERS = 4       # Active customers first, others later

class CustomerStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"

class MigrationMode(Enum):
    SINGLE_CUSTOMER = "single"
    BATCH_CUSTOMERS = "batch"
    ALL_CUSTOMERS = "all"
```

**Customer Selection Models:**
```python
@dataclass
class CustomerFilter:
    customer_ids: Optional[List[int]] = None
    status_filter: Optional[List[CustomerStatus]] = None
    date_range: Optional[Tuple[datetime, datetime]] = None
    limit: Optional[int] = None
    active_only: bool = True

@dataclass
class MigrationRequest:
    mode: MigrationMode
    customer_filter: CustomerFilter
    priority_phases: List[MigrationPriority]
    stop_on_error: bool = True
    validate_with_api: bool = True
```

**Enhanced Entity Models:**
```python
@dataclass
class SonarCustomer:
    id: int
    name: str
    status: CustomerStatus
    account_type: str
    created_date: datetime
    last_activity: Optional[datetime]
    services: List['SonarService']
    billing_info: 'SonarBillingInfo'
    is_active: bool

@dataclass
class MigrationResult:
    customer_id: int
    success: bool
    error_message: Optional[str]
    entities_migrated: Dict[str, int]
    validation_results: Dict[str, bool]
    migration_time: float
```

## Files
Organize migration system with customer selection and incremental processing capabilities.

**New Core Migration Files:**
- `src/migration/customer_selector.py` - Customer filtering and selection logic
- `src/migration/incremental_migrator.py` - Incremental migration orchestration
- `src/migration/priority_manager.py` - Migration priority and phase management
- `src/migration/error_handler.py` - Stop-on-error handling and recovery
- `src/migration/progress_tracker.py` - Detailed progress tracking and reporting

**Enhanced Extractor Files:**
- `src/extractors/foundation_extractor.py` - Company, users, groups, plans, tariffs
- `src/extractors/network_extractor.py` - Network infrastructure, IP ranges, pools
- `src/extractors/inventory_extractor.py` - Inventory, locations, vendors, models
- `src/extractors/customer_extractor.py` - Customer data with status filtering

**Validation and API Files:**
- `src/validators/api_validator.py` - API-first validation for all entities
- `src/validators/relationship_validator.py` - Cross-entity relationship validation
- `src/apis/enhanced_splynx_client.py` - Extended Splynx client with validation endpoints

**Customer Management Files:**
- `src/models/customer_models.py` - Customer-specific data models
- `src/transformers/customer_transformer.py` - Customer data transformation
- `src/loaders/customer_loader.py` - Customer data loading with validation

**Configuration and CLI:**
- `src/cli/migration_cli.py` - Command-line interface for customer selection
- `src/config/migration_settings.py` - Migration-specific configuration
- `migration_runner.py` - Main entry point for migration execution

## Functions
Implement customer-centric migration functions with incremental processing capabilities.

**Customer Selection Functions:**
- `select_customers_by_ids(customer_ids: List[int]) -> List[SonarCustomer]` - Select specific customers
- `select_active_customers(limit: Optional[int] = None) -> List[SonarCustomer]` - Get active customers
- `filter_customers_by_status(status: CustomerStatus) -> List[SonarCustomer]` - Filter by status
- `get_customer_migration_order(customers: List[SonarCustomer]) -> List[SonarCustomer]` - Priority ordering

**Incremental Migration Functions:**
- `migrate_single_customer(customer_id: int) -> MigrationResult` - Migrate one customer
- `migrate_customer_batch(customer_ids: List[int]) -> List[MigrationResult]` - Migrate customer batch
- `migrate_all_customers(filter: CustomerFilter) -> List[MigrationResult]` - Migrate all matching customers
- `resume_failed_migration(migration_id: str) -> MigrationResult` - Resume after error fix

**Priority Phase Functions:**
- `migrate_foundation_data() -> MigrationResult` - Company, users, groups, plans, tariffs
- `migrate_network_infrastructure() -> MigrationResult` - Network, IP ranges, pools
- `migrate_inventory_data() -> MigrationResult` - Inventory, locations, vendors, models
- `migrate_customer_data(customer: SonarCustomer) -> MigrationResult` - Individual customer migration

**API Validation Functions:**
- `validate_customer_creation(customer_data: Dict) -> ValidationResult` - Pre-creation validation
- `validate_service_assignment(service_data: Dict) -> ValidationResult` - Service validation
- `validate_billing_setup(billing_data: Dict) -> ValidationResult` - Billing validation
- `post_migration_validation(customer_id: int) -> ValidationResult` - Post-migration checks

**Error Handling Functions:**
- `handle_migration_error(error: Exception, context: Dict) -> None` - Stop and log error
- `create_error_report(migration_results: List[MigrationResult]) -> Dict` - Error reporting
- `suggest_error_fixes(error_type: str) -> List[str]` - Error resolution suggestions

## Classes
Design customer-focused migration classes with incremental processing capabilities.

**Customer Management Classes:**
- `CustomerSelector` - Handles customer filtering and selection logic
  - Methods: `select_by_ids()`, `filter_by_status()`, `get_active_customers()`, `apply_filters()`
  - Properties: `total_customers`, `active_count`, `selected_customers`

- `IncrementalMigrator` - Orchestrates incremental customer migration
  - Methods: `migrate_customers()`, `process_batch()`, `handle_dependencies()`, `track_progress()`
  - Properties: `current_batch`, `migration_status`, `error_state`

**Priority Management Classes:**
- `PriorityManager` - Manages migration phases and priorities
  - Methods: `get_migration_order()`, `execute_phase()`, `validate_dependencies()`, `skip_phase()`
  - Properties: `current_phase`, `completed_phases`, `remaining_phases`

- `FoundationMigrator` - Handles company, user, group, plan, and tariff migration
  - Methods: `migrate_company_info()`, `migrate_users()`, `migrate_groups()`, `migrate_plans()`

- `NetworkMigrator` - Handles network infrastructure migration
  - Methods: `migrate_ip_ranges()`, `migrate_pools()`, `migrate_network_config()`

- `InventoryMigrator` - Handles inventory and location migration
  - Methods: `migrate_locations()`, `migrate_vendors()`, `migrate_models()`, `migrate_inventory()`

**Enhanced API Classes:**
- `EnhancedSplynxClient` - Extended Splynx client with validation capabilities
  - Methods: `validate_before_create()`, `create_with_validation()`, `verify_creation()`
  - Properties: `validation_enabled`, `last_validation_result`

**Error Management Classes:**
- `MigrationErrorHandler` - Handles stop-on-error behavior
  - Methods: `handle_error()`, `create_error_context()`, `suggest_fixes()`, `enable_resume()`
  - Properties: `error_count`, `last_error`, `recovery_suggestions`

## Dependencies
Enhanced dependencies for customer management and incremental migration.

**Core Migration Dependencies:**
```
requests>=2.31.0          # HTTP client for REST API calls
gql>=3.4.1                # GraphQL client for Sonar
aiohttp>=3.8.5            # Async HTTP for concurrent processing
pydantic>=2.4.2           # Data validation and serialization
python-dotenv>=1.0.0      # Environment configuration
tenacity>=8.2.3           # Retry mechanisms
click>=8.1.7              # CLI interface for customer selection
rich>=13.6.0              # Enhanced progress display
loguru>=0.7.2             # Detailed logging
```

**Customer Management Dependencies:**
```
pandas>=2.1.1             # Customer data analysis and filtering
sqlalchemy>=2.0.0         # Database ORM for migration tracking
alembic>=1.12.0           # Database migrations
psycopg2-binary>=2.9.7    # PostgreSQL adapter for Splynx database
```

**Validation and Testing:**
```
pytest>=7.4.2            # Testing framework
pytest-asyncio>=0.21.1   # Async testing support
factory-boy>=3.3.0       # Test data factories
responses>=0.23.3        # HTTP request mocking
```

## Testing
Comprehensive testing strategy for customer migration and incremental processing.

**Customer Migration Testing:**
- `tests/test_customer_selector.py` - Customer filtering and selection logic
- `tests/test_incremental_migration.py` - Incremental migration workflows
- `tests/test_priority_phases.py` - Migration phase execution
- `tests/test_error_handling.py` - Stop-on-error behavior

**Integration Testing:**
- `tests/integration/test_single_customer.py` - Single customer migration end-to-end
- `tests/integration/test_batch_migration.py` - Batch customer migration
- `tests/integration/test_api_validation.py` - API validation workflows
- `tests/integration/test_error_recovery.py` - Error handling and recovery

**Performance Testing:**
- `tests/performance/test_large_batch.py` - Large customer batch performance
- `tests/performance/test_concurrent_migration.py` - Concurrent processing limits
- `tests/performance/test_memory_usage.py` - Memory usage during migration

**Validation Testing:**
- Mock Splynx API responses for validation testing
- Test customer data integrity across migration
- Verify relationship preservation between entities
- Test rollback capabilities for failed migrations

## Implementation Order
Phased implementation focusing on customer migration capabilities and incremental processing.

**Phase 1: Customer Selection Foundation (Week 1)**
1. Implement customer filtering and selection logic
2. Create customer status management and priority ordering
3. Build CLI interface for customer selection
4. Develop migration request and configuration management

**Phase 2: Incremental Migration Core (Week 2)**
5. Implement incremental migration orchestrator
6. Build priority phase management system
7. Create stop-on-error handling with detailed logging
8. Develop progress tracking and reporting

**Phase 3: Priority Data Migration (Week 3)**
9. Implement foundation data migration (company, users, groups, plans, tariffs)
10. Build network infrastructure migration (IP ranges, pools)
11. Create inventory migration (locations, vendors, models)
12. Develop customer data migration with dependency handling

**Phase 4: API Validation Integration (Week 4)**
13. Enhance Splynx client with validation capabilities
14. Implement pre-migration validation for all entity types
15. Build post-migration verification and integrity checks
16. Create validation reporting and error suggestion system

**Phase 5: Testing and Production Readiness (Week 5)**
17. Implement comprehensive test suite for customer migration
18. Performance testing with various customer batch sizes
19. Error handling testing and recovery procedures
20. Documentation and production deployment preparation

**Phase 6: Advanced Features (Week 6)**
21. Implement migration resume capabilities after error fixes
22. Add concurrent customer processing with rate limiting
23. Create detailed migration analytics and reporting
24. Build migration rollback and cleanup procedures
