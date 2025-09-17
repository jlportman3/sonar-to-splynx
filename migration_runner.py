#!/usr/bin/env python3
"""Main entry point for Sonar to Splynx migration."""

import sys
import os
import argparse
from typing import List, Optional
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.migration.incremental_migrator import IncrementalMigrator, MigrationRequest
from src.migration.customer_selector import CustomerFilter, CustomerStatus, MigrationMode
from src.migration.priority_manager import MigrationPriority
from src.apis.sonar_client import SonarGraphQLClient
from src.apis.splynx_client import SplynxAPIClient, SplynxConfig
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger

def setup_logging(log_level: str = "INFO"):
    """Setup logging configuration."""
    setup_logger(log_level)
    return get_logger("migration_runner")

def create_api_clients():
    """Create and test API clients."""
    logger = get_logger("migration_runner")
    
    # Create Sonar client
    logger.info("Initializing Sonar GraphQL client...")
    sonar_client = SonarGraphQLClient(config)
    
    # Test Sonar connection
    if not sonar_client.test_connection():
        logger.error("Failed to connect to Sonar API")
        sys.exit(1)
    
    # Create Splynx client
    logger.info("Initializing Splynx REST client...")
    splynx_config = SplynxConfig(
        base_url=config.splynx_url,
        api_key=config.splynx_api_key,
        api_secret=config.splynx_password or config.splynx_api_key
    )
    splynx_client = SplynxAPIClient(splynx_config)
    
    # Test Splynx connection
    connection_test = splynx_client.test_connection()
    if not connection_test.get('success'):
        logger.error(f"Failed to connect to Splynx API: {connection_test.get('error')}")
        sys.exit(1)
    
    logger.info("API clients initialized successfully")
    return sonar_client, splynx_client

def parse_customer_ids(customer_ids_str: str) -> List[int]:
    """Parse customer IDs from string."""
    if not customer_ids_str:
        return []
    
    try:
        # Handle comma-separated values
        ids = [int(id_str.strip()) for id_str in customer_ids_str.split(',')]
        return ids
    except ValueError as e:
        raise ValueError(f"Invalid customer ID format: {e}")

def parse_priority_phases(phases_str: str) -> List[MigrationPriority]:
    """Parse priority phases from string."""
    if not phases_str:
        return [MigrationPriority.FOUNDATION, MigrationPriority.NETWORK, 
                MigrationPriority.INVENTORY, MigrationPriority.CUSTOMERS]
    
    phase_map = {
        'foundation': MigrationPriority.FOUNDATION,
        'network': MigrationPriority.NETWORK,
        'inventory': MigrationPriority.INVENTORY,
        'customers': MigrationPriority.CUSTOMERS
    }
    
    phases = []
    for phase_str in phases_str.split(','):
        phase_name = phase_str.strip().lower()
        if phase_name in phase_map:
            phases.append(phase_map[phase_name])
        else:
            raise ValueError(f"Unknown phase: {phase_name}")
    
    return phases

def migrate_single_customer(args, migrator: IncrementalMigrator):
    """Migrate a single customer."""
    logger = get_logger("migration_runner")
    
    logger.info(f"Starting single customer migration for ID: {args.customer_id}")
    
    priority_phases = parse_priority_phases(args.phases)
    
    result = migrator.migrate_single_customer(
        customer_id=args.customer_id,
        priority_phases=priority_phases,
        stop_on_error=args.stop_on_error,
        validate_with_api=args.validate_api,
        dry_run=args.dry_run
    )
    
    # Print results
    print(f"\n{'='*60}")
    print(f"SINGLE CUSTOMER MIGRATION RESULTS")
    print(f"{'='*60}")
    print(f"Customer ID: {result.customer_id}")
    print(f"Customer Name: {result.customer_name}")
    print(f"Success: {result.success}")
    print(f"Migration Time: {result.migration_time:.2f} seconds")
    
    if result.entities_migrated:
        print(f"Entities Migrated: {result.entities_migrated}")
    
    if result.validation_results:
        print(f"Validation Results: {result.validation_results}")
    
    if not result.success and result.error_message:
        print(f"Error: {result.error_message}")
    
    return result.success

def migrate_customer_batch(args, migrator: IncrementalMigrator):
    """Migrate a batch of customers."""
    logger = get_logger("migration_runner")
    
    customer_ids = parse_customer_ids(args.customer_ids)
    logger.info(f"Starting batch migration for {len(customer_ids)} customers")
    
    priority_phases = parse_priority_phases(args.phases)
    
    result = migrator.migrate_customer_batch(
        customer_ids=customer_ids,
        priority_phases=priority_phases,
        stop_on_error=args.stop_on_error,
        validate_with_api=args.validate_api,
        dry_run=args.dry_run
    )
    
    # Print results
    print(f"\n{'='*60}")
    print(f"BATCH MIGRATION RESULTS")
    print(f"{'='*60}")
    print(f"Total Customers: {result.total_customers}")
    print(f"Successful: {result.successful_migrations}")
    print(f"Failed: {result.failed_migrations}")
    print(f"Success Rate: {(result.successful_migrations / result.total_customers * 100):.1f}%")
    print(f"Total Time: {result.total_time:.2f} seconds")
    print(f"Average Time per Customer: {(result.total_time / result.total_customers):.2f} seconds")
    
    if result.phases_completed:
        print(f"Phases Completed: {[p.name for p in result.phases_completed]}")
    
    if result.error_summary:
        print(f"\nError Summary:")
        for error_type, count in result.error_summary.items():
            print(f"  {error_type}: {count}")
    
    # Show detailed results if requested
    if args.verbose:
        print(f"\nDetailed Customer Results:")
        for customer_result in result.migration_results:
            status = "✓" if customer_result.success else "✗"
            print(f"  {status} {customer_result.customer_name} (ID: {customer_result.customer_id})")
            if not customer_result.success and customer_result.error_message:
                print(f"    Error: {customer_result.error_message}")
    
    return result.successful_migrations == result.total_customers

def migrate_all_customers(args, migrator: IncrementalMigrator):
    """Migrate all customers matching filter criteria."""
    logger = get_logger("migration_runner")
    
    # Create customer filter
    status_filter = None
    if args.status:
        status_map = {
            'active': CustomerStatus.ACTIVE,
            'inactive': CustomerStatus.INACTIVE,
            'suspended': CustomerStatus.SUSPENDED,
            'terminated': CustomerStatus.TERMINATED
        }
        status_filter = [status_map[args.status.lower()]]
    
    customer_filter = CustomerFilter(
        status_filter=status_filter,
        limit=args.limit,
        active_only=args.active_only
    )
    
    priority_phases = parse_priority_phases(args.phases)
    
    logger.info("Starting migration of all customers matching filter criteria")
    
    result = migrator.migrate_all_customers(
        customer_filter=customer_filter,
        priority_phases=priority_phases,
        stop_on_error=args.stop_on_error,
        validate_with_api=args.validate_api,
        dry_run=args.dry_run
    )
    
    # Print results
    print(f"\n{'='*60}")
    print(f"ALL CUSTOMERS MIGRATION RESULTS")
    print(f"{'='*60}")
    print(f"Total Customers: {result.total_customers}")
    print(f"Successful: {result.successful_migrations}")
    print(f"Failed: {result.failed_migrations}")
    print(f"Success Rate: {(result.successful_migrations / result.total_customers * 100):.1f}%")
    print(f"Total Time: {result.total_time:.2f} seconds")
    
    if result.total_customers > 0:
        print(f"Average Time per Customer: {(result.total_time / result.total_customers):.2f} seconds")
    
    if result.phases_completed:
        print(f"Phases Completed: {[p.name for p in result.phases_completed]}")
    
    if result.error_summary:
        print(f"\nError Summary:")
        for error_type, count in result.error_summary.items():
            print(f"  {error_type}: {count}")
    
    return result.successful_migrations == result.total_customers

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Sonar to Splynx Migration Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Migrate a single customer
  python migration_runner.py single --customer-id 123

  # Migrate a batch of customers
  python migration_runner.py batch --customer-ids "123,456,789"

  # Migrate all active customers (dry run)
  python migration_runner.py all --active-only --dry-run

  # Migrate all customers with specific phases
  python migration_runner.py all --phases "foundation,customers"

  # Migrate with detailed logging and continue on errors
  python migration_runner.py batch --customer-ids "123,456" --verbose --no-stop-on-error
        """
    )
    
    # Global arguments
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], 
                       default='INFO', help='Logging level')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Perform a dry run without actual migration')
    parser.add_argument('--stop-on-error', action='store_true', default=True,
                       help='Stop migration on first error (default: True)')
    parser.add_argument('--no-stop-on-error', dest='stop_on_error', action='store_false',
                       help='Continue migration even if errors occur')
    parser.add_argument('--validate-api', action='store_true', default=True,
                       help='Use API validation (default: True)')
    parser.add_argument('--no-validate-api', dest='validate_api', action='store_false',
                       help='Skip API validation')
    parser.add_argument('--phases', type=str, 
                       help='Comma-separated list of phases: foundation,network,inventory,customers')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output with detailed results')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Migration commands')
    
    # Single customer migration
    single_parser = subparsers.add_parser('single', help='Migrate a single customer')
    single_parser.add_argument('--customer-id', type=int, required=True,
                              help='Customer ID to migrate')
    
    # Batch customer migration
    batch_parser = subparsers.add_parser('batch', help='Migrate a batch of customers')
    batch_parser.add_argument('--customer-ids', type=str, required=True,
                             help='Comma-separated list of customer IDs')
    
    # All customers migration
    all_parser = subparsers.add_parser('all', help='Migrate all customers')
    all_parser.add_argument('--status', choices=['active', 'inactive', 'suspended', 'terminated'],
                           help='Filter customers by status')
    all_parser.add_argument('--active-only', action='store_true', default=True,
                           help='Migrate only active customers (default: True)')
    all_parser.add_argument('--include-inactive', dest='active_only', action='store_false',
                           help='Include inactive customers')
    all_parser.add_argument('--limit', type=int,
                           help='Limit number of customers to migrate')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Setup logging
    logger = setup_logging(args.log_level)
    
    try:
        # Validate configuration
        config.validate()
        logger.info("Configuration validated successfully")
        
        # Create API clients
        sonar_client, splynx_client = create_api_clients()
        
        # Create migrator
        migrator = IncrementalMigrator(sonar_client, splynx_client)
        
        # Execute migration based on command
        success = False
        start_time = datetime.now()
        
        if args.command == 'single':
            success = migrate_single_customer(args, migrator)
        elif args.command == 'batch':
            success = migrate_customer_batch(args, migrator)
        elif args.command == 'all':
            success = migrate_all_customers(args, migrator)
        
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        
        # Print final summary
        print(f"\n{'='*60}")
        print(f"MIGRATION SUMMARY")
        print(f"{'='*60}")
        print(f"Command: {args.command}")
        print(f"Total Execution Time: {total_time:.2f} seconds")
        print(f"Dry Run: {args.dry_run}")
        print(f"Stop on Error: {args.stop_on_error}")
        print(f"API Validation: {args.validate_api}")
        print(f"Overall Success: {success}")
        
        if args.dry_run:
            print(f"\nNote: This was a dry run. No actual data was migrated.")
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        logger.info("Migration interrupted by user")
        print("\nMigration interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Migration failed with error: {e}")
        print(f"\nMigration failed: {e}")
        if args.log_level == 'DEBUG':
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
