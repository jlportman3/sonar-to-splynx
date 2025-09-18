# Sonar to Splynx Migration Tool

A comprehensive Python application for migrating data from Sonar software instances to Splynx instances using their respective APIs. This tool provides incremental migration capabilities with the ability to migrate one customer, a hundred customers, or all customers with detailed progress tracking and error handling.

## 🚀 Features

- **Incremental Migration**: Migrate one customer, a batch of customers, or all customers
- **Priority-Based Migration**: Foundation → Network → Inventory → Customers
- **Stop-on-Error Handling**: Immediate error detection and resolution guidance
- **API-First Validation**: Comprehensive validation using Splynx REST API
- **Progress Tracking**: Detailed progress reporting and performance metrics
- **Customer Selection**: Advanced filtering by status, date range, and custom criteria
- **Dry Run Support**: Test migrations without actual data transfer
- **Comprehensive Logging**: Detailed logging with multiple levels and error categorization

## 📋 Prerequisites

- Python 3.8+
- Access to a Sonar instance with API credentials
- Access to a Splynx instance with API credentials
- Network connectivity between migration host and both systems

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd sonar-to-splynx
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env
```

5. **Edit `.env` with your credentials:**
```bash
# Sonar API Configuration
SONAR_URL=https://your-sonar-instance.com
SONAR_API_KEY=your_sonar_api_key
# OR use username/password
SONAR_USERNAME=your_sonar_username
SONAR_PASSWORD=your_sonar_password

# Splynx API Configuration  
SPLYNX_URL=https://your-splynx-instance.com
SPLYNX_API_KEY=your_splynx_api_key
SPLYNX_PASSWORD=your_splynx_api_secret

# Migration Settings
BATCH_SIZE=100
RETRY_ATTEMPTS=3
PARALLEL_WORKERS=4
LOG_LEVEL=INFO
```

## 🎯 Quick Start

### Test Connection
```bash
python migration_runner.py all --dry-run --limit 1
```

### Migrate a Single Customer
```bash
python migration_runner.py single --customer-id 123
```

### Migrate a Batch of Customers
```bash
python migration_runner.py batch --customer-ids "123,456,789"
```

### Migrate All Active Customers
```bash
python migration_runner.py all --active-only
```

## 📖 Usage Guide

### Command Structure
```bash
python migration_runner.py [COMMAND] [OPTIONS]
```

### Available Commands

#### 1. Single Customer Migration
```bash
python migration_runner.py single --customer-id <ID> [OPTIONS]
```

**Options:**
- `--customer-id`: Customer ID to migrate (required)

#### 2. Batch Customer Migration
```bash
python migration_runner.py batch --customer-ids "<ID1,ID2,ID3>" [OPTIONS]
```

**Options:**
- `--customer-ids`: Comma-separated list of customer IDs (required)

#### 3. All Customers Migration
```bash
python migration_runner.py all [OPTIONS]
```

**Options:**
- `--status`: Filter by status (active, inactive, suspended, terminated)
- `--active-only`: Migrate only active customers (default: True)
- `--include-inactive`: Include inactive customers
- `--limit`: Limit number of customers to migrate

### Global Options

#### Migration Control
- `--dry-run`: Perform a dry run without actual migration
- `--stop-on-error`: Stop migration on first error (default: True)
- `--no-stop-on-error`: Continue migration even if errors occur
- `--validate-api`: Use API validation (default: True)
- `--no-validate-api`: Skip API validation

#### Migration Phases
- `--phases`: Comma-separated list of phases
  - `foundation`: Company, users, groups, plans, tariffs
  - `network`: Network, IP ranges, pools
  - `inventory`: Inventory, locations, vendors, models
  - `customers`: Customer data migration

#### Logging and Output
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `--verbose`, `-v`: Verbose output with detailed results

### Back Up Sonar Data with GraphQL Only

Use the dedicated backup utility to snapshot every accessible Sonar GraphQL collection into PostgreSQL before running any migrations:

```bash
# start the storage container (runs Postgres on localhost:5433)
make docker-up

# direct invocation (defaults to scalar-only field selection)
BACKUP_DATABASE_URL="postgresql://sonar:sonar_pass@localhost:5433/sonar_backup" \
python backup_sonar_graphql.py --page-size 200

# or via Makefile with additional arguments
make backup BACKUP_ARGS="--include accounts,services --page-size 100"

# smoke-test only ~100 rows per collection
make backup-test

# clear previously cached backup data (metadata + per-collection tables)
make backup-clean
```

- Set `SONAR_URL` and either `SONAR_API_KEY` or `SONAR_USERNAME`/`SONAR_PASSWORD` in your `.env` file.
- Export `BACKUP_DATABASE_URL` (or pass `--database-url`) so the backup process knows where to write data.
- Activate the local virtual environment first (`source venv/bin/activate`) or let the Makefile auto-detect `venv/bin/python`.
- Adjust `--include`/`--exclude` to target specific root queries (e.g. `--include accounts,services`).
- Increase `--max-depth` if you need nested relationships in the backup (default `0` captures top-level scalar fields only).
- The tool introspects the schema, paginates through each list-style query using the GraphQL API only, and stores JSON payloads per query in Postgres tables (one table per root query) along with run metadata. Use `--sample-size` (as in `make backup-test`) when you only need a limited sample per collection.
- Use `--request-timeout` to fail fast if Sonar stops responding (defaults to 30 seconds per HTTP request).
- Use `--rate-limit-delay` / `--rate-limit-retries` to automatically pause when Sonar signals rate limiting (defaults: 5 s delay, 5 attempts).

## 📊 Migration Phases

The migration follows a priority-based approach:

### 1. Foundation Phase
- Company information
- User accounts and groups
- Service plans and tariffs
- Basic configuration

### 2. Network Phase
- IP address ranges
- IP pools
- Network configuration
- Router and equipment setup

### 3. Inventory Phase
- Locations and sites
- Vendors and suppliers
- Equipment models
- Inventory items

### 4. Customer Phase
- Customer accounts
- Contact information
- Service assignments
- Billing data

## 🔍 Examples

### Basic Migration Examples

**Dry run for a single customer:**
```bash
python migration_runner.py single --customer-id 123 --dry-run
```

**Migrate specific customers with detailed logging:**
```bash
python migration_runner.py batch --customer-ids "123,456,789" --verbose --log-level DEBUG
```

**Migrate all active customers with foundation and customer phases only:**
```bash
python migration_runner.py all --active-only --phases "foundation,customers"
```

### Advanced Migration Examples

**Continue on errors with API validation:**
```bash
python migration_runner.py all --no-stop-on-error --validate-api --limit 50
```

**Migrate suspended customers only:**
```bash
python migration_runner.py all --status suspended --include-inactive
```

**Full migration with all phases:**
```bash
python migration_runner.py all --phases "foundation,network,inventory,customers" --verbose
```

## 📈 Progress Tracking

The migration tool provides comprehensive progress tracking:

### Real-time Progress
- Overall migration percentage
- Current phase and status
- Customer processing rate
- Estimated completion time

### Detailed Reporting
- Phase-by-phase progress
- Individual customer results
- Error categorization and suggestions
- Performance metrics

### Export Options
- JSON format for programmatic access
- CSV format for spreadsheet analysis

## ⚠️ Error Handling

### Error Categories
- **Network**: Connection and timeout issues
- **Authentication**: API credential problems
- **Validation**: Data format and schema issues
- **Data Transformation**: Mapping and conversion errors
- **API Error**: Splynx API response issues
- **Customer Data**: Customer-specific problems

### Error Resolution
Each error includes:
- Detailed error message
- Error category and severity
- Suggested fixes
- Context information

### Stop-on-Error Behavior
When enabled (default), migration stops on the first error and provides:
- Error ID for tracking
- Specific error details
- Resolution suggestions
- Resume instructions

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SONAR_URL` | Sonar instance URL | Yes |
| `SONAR_API_KEY` | Sonar API key | Yes* |
| `SONAR_USERNAME` | Sonar username | Yes* |
| `SONAR_PASSWORD` | Sonar password | Yes* |
| `SPLYNX_URL` | Splynx instance URL | Yes |
| `SPLYNX_API_KEY` | Splynx API key | Yes |
| `SPLYNX_PASSWORD` | Splynx API secret | Yes |
| `BATCH_SIZE` | Batch processing size | No |
| `RETRY_ATTEMPTS` | Number of retry attempts | No |
| `LOG_LEVEL` | Logging level | No |

*Either API key or username/password required

### Migration Settings

```python
# Default settings in .env
BATCH_SIZE=100          # Items per batch
RETRY_ATTEMPTS=3        # Retry failed operations
PARALLEL_WORKERS=4      # Concurrent workers
LOG_LEVEL=INFO          # Logging verbosity
```

## 🧪 Testing

### Dry Run Testing
Always test with dry run first:
```bash
python migration_runner.py all --dry-run --limit 5
```

### Connection Testing
Test API connections:
```bash
python -c "
from src.apis.sonar_client import SonarGraphQLClient
from src.apis.splynx_client import SplynxAPIClient, SplynxConfig
from src.config.settings import config

# Test Sonar
sonar = SonarGraphQLClient(config)
print('Sonar:', sonar.test_connection())

# Test Splynx
splynx_config = SplynxConfig(config.splynx_url, config.splynx_api_key, config.splynx_password)
splynx = SplynxAPIClient(splynx_config)
print('Splynx:', splynx.test_connection())
"
```

### Validation Testing
Test with API validation:
```bash
python migration_runner.py single --customer-id 123 --validate-api --dry-run
```

## 📝 Logging

### Log Levels
- **DEBUG**: Detailed debugging information
- **INFO**: General information messages
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical error messages

### Log Files
Logs are written to:
- Console output (formatted)
- Log files (if configured)
- Error reports (JSON format)

### Log Analysis
```bash
# View recent logs
tail -f logs/migration.log

# Search for errors
grep "ERROR" logs/migration.log

# Filter by customer
grep "customer_id:123" logs/migration.log
```

## 🔒 Security Considerations

### API Credentials
- Store credentials in `.env` file (not in code)
- Use API keys when possible (preferred over passwords)
- Rotate credentials regularly
- Limit API permissions to minimum required

### Network Security
- Use HTTPS for all API connections
- Verify SSL certificates
- Consider VPN for sensitive environments
- Monitor API access logs

### Data Protection
- Test with non-production data first
- Backup target system before migration
- Validate data integrity after migration
- Implement rollback procedures

## 🚨 Troubleshooting

### Common Issues

#### Connection Problems
```bash
# Test network connectivity
curl -I https://your-sonar-instance.com
curl -I https://your-splynx-instance.com

# Test API endpoints
curl -H "Authorization: Bearer YOUR_API_KEY" https://your-sonar-instance.com/api/graphql
curl -u "API_KEY:API_SECRET" https://your-splynx-instance.com/api/2.0/admin/api/check
```

#### Authentication Issues
```bash
# Verify credentials
python -c "
from src.config.settings import config
config.validate()
print('Configuration valid')
"
```

#### Data Issues
```bash
# Check customer data
python migration_runner.py single --customer-id 123 --dry-run --verbose
```

### Error Recovery

#### Resume After Error Fix
1. Note the error ID from the log
2. Fix the underlying issue
3. Resume migration (feature in development)

#### Manual Cleanup
If migration fails partway through:
1. Check Splynx for partially created records
2. Clean up incomplete data
3. Restart migration with corrected configuration

## 📚 API Documentation

### Sonar GraphQL API
- Schema introspection supported
- Comprehensive entity coverage
- Relationship mapping
- Pagination support

### Splynx REST API
- Version 2.0 supported
- Schema validation via OPTIONS
- CRUD operations
- Batch processing

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Install development dependencies
4. Run tests
5. Submit pull request

### Code Standards
- Follow PEP 8 style guide
- Add type hints
- Write comprehensive tests
- Update documentation

### Testing
```bash
# Run unit tests
python -m pytest tests/

# Run integration tests
python -m pytest tests/integration/

# Run with coverage
python -m pytest --cov=src tests/
```

## 📄 License

[License information to be added]

## 🆘 Support

### Getting Help
1. Check this documentation
2. Review error messages and suggestions
3. Check the troubleshooting section
4. Contact system administrator

### Reporting Issues
When reporting issues, include:
- Migration command used
- Error messages and IDs
- Log excerpts
- System configuration
- Steps to reproduce

### Feature Requests
Submit feature requests with:
- Use case description
- Expected behavior
- Current limitations
- Priority level

---

## 📋 Migration Checklist

### Pre-Migration
- [ ] Backup Splynx database
- [ ] Verify API credentials
- [ ] Test connections
- [ ] Run dry run migration
- [ ] Review migration plan

### During Migration
- [ ] Monitor progress
- [ ] Watch for errors
- [ ] Check system resources
- [ ] Validate sample data

### Post-Migration
- [ ] Verify data integrity
- [ ] Test system functionality
- [ ] Update configurations
- [ ] Document any issues
- [ ] Plan follow-up actions

---

**Ready to migrate? Start with a dry run to test your configuration!**

```bash
python migration_runner.py all --dry-run --limit 1 --verbose
