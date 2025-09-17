# 💻 TECHNICAL CONTEXT
**Technology Stack & Technical Decisions**  
**Last Updated:** September 12, 2025  
**Tech Stack:** Python 3.8+, GraphQL, Splynx REST API, MySQL

---

## 🛠️ **CORE TECHNOLOGY STACK**

### **Backend Framework**
```python
# Python 3.8+ (Primary Language)
Language: Python 3.8+
Reason: Excellent API client libraries, data processing capabilities
Status: ✅ Production ready

# Key Libraries
requests==2.31.0      # REST API communication (Splynx)
gql==3.4.1           # GraphQL client (Sonar)
pydantic==2.4.2      # Data modeling and validation
python-dotenv==1.0.0 # Environment configuration
mysql-connector-python==9.0.0  # MySQL database access
loguru==0.7.2        # Advanced logging
pytest==7.4.2       # Testing framework
```

### **API Integration Technologies**
```yaml
# Sonar System
API Type: GraphQL (primary data interface)
Client: gql library with authentication
Authentication: API tokens via headers
Data Format: JSON with complex nested structures

# Splynx System  
API Type: REST API (comprehensive)
Client: requests library with session management
Authentication: Basic Auth (base64 encoded)
Database: Direct MySQL access via mysql-connector
```

### **Data Processing Stack**
```python
# Data Modeling
pydantic: Input validation and data structures
typing: Type hints for better code quality
dataclasses: Simple data containers

# Database Access
mysql-connector-python: Direct MySQL connections
Raw SQL: For performance-critical operations
ORM Alternative: Direct SQL for migration precision
```

---

## 🔧 **TECHNICAL DECISIONS**

### **Database Access Strategy**
```python
# Decision: Direct MySQL + API Hybrid Approach
APPROACH = "hybrid_database_api"

Reasoning:
✅ Performance: Direct DB access faster than API rate limits
✅ Reliability: Database transactions more reliable
✅ Completeness: Access to all data, not just API-exposed fields
✅ Validation: API provides business logic compliance

Implementation:
database.insert(data)  # Primary data insertion
api.validate(data.id)  # Business logic validation
```

**Alternative Considered:** API-only approach  
**Rejected Because:** Rate limits, incomplete data access, performance issues

### **Authentication Patterns**
```python
# Splynx: Basic Auth (chosen for reliability)
auth_header = {
    'Authorization': f'Basic {base64.b64encode(f"{key}:{secret}".encode()).decode()}'
}

# Alternative Considered: Session tokens
# Rejected: More complex, session management overhead

# Sonar: Token-based (required by system)
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
```

### **Error Handling Strategy**
```python
# Decision: Classify and handle errors by type
ERROR_CLASSIFICATION = {
    401: "authentication_issue",      # Retry with fresh credentials
    403: "permissions_issue",         # Check access rights  
    404: "endpoint_not_found",        # Endpoint missing/deprecated
    405: "method_not_allowed",        # Feature disabled (NOT error)
    422: "validation_error",          # Data format issues
    500: "server_error"               # System issues
}
```

**Key Insight:** 405 errors indicate disabled features, not broken endpoints

---

## 📊 **DEVELOPMENT TOOLS**

### **Code Quality Tools**
```bash
# Formatting & Style
black: Code formatting
mypy: Static type checking  
pytest: Unit and integration testing

# Development Environment
venv: Virtual environment isolation
python-dotenv: Environment variable management
loguru: Structured logging with rotation
```

### **Analysis & Documentation Tools**
```python
# Schema Analysis
gql: GraphQL introspection and query building
mysql-connector: Database schema analysis
json: Schema serialization and documentation

# Custom Analysis Scripts
analyze_sonar_schema.py: GraphQL schema documentation  
analyze_splynx_database.py: Database structure analysis
investigate_405_errors.py: HTTP error investigation
backup_sonar_graphql.py: GraphQL-only full data backup into SQLite for pre-migration snapshots
docs/sonar/schema.md: High-level GraphQL domain map for quick reference
```

### **Configuration Management**
```ini
# .env Configuration Pattern
SONAR_URL=https://sonar.domain.com
SONAR_TOKEN=secret_token_here
SPLYNX_URL=https://splynx.domain.com  
SPLYNX_API_KEY=api_key_here
SPLYNX_SECRET=secret_here

# Database Access
MYSQL_HOST=localhost
MYSQL_USER=debian-sys-maint
MYSQL_PASSWORD=secure_password
MYSQL_SOCKET=/var/run/mysqld/mysqld.sock
```

---

## 🔍 **TECHNICAL DISCOVERIES**

### **GraphQL Best Practices**
```python
# Sonar GraphQL Patterns
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Introspection for schema discovery
introspection_query = gql("""
    query IntrospectionQuery {
        __schema {
            types {
                name
                fields {
                    name
                    type { name }
                }
            }
        }
    }
""")

# Pagination for large datasets
accounts_query = gql("""
    query GetAccounts($first: Int, $after: String) {
        accounts(first: $first, after: $after) {
            edges { node { id name } }
            pageInfo { hasNextPage endCursor }
        }
    }
""")
```

### **MySQL Connection Optimization**
```python
# Unix Socket > TCP for local connections
config = {
    'host': 'localhost',
    'user': 'debian-sys-maint',
    'password': password,
    'unix_socket': '/var/run/mysqld/mysqld.sock',  # Key optimization
    'database': 'splynx'
}

# Connection pattern for migration scripts
with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
```

### **REST API Optimization**
```python
# Session reuse for performance
session = requests.Session()
session.headers.update(auth_headers)

# Batch operations where possible
def batch_api_calls(items, batch_size=100):
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        yield process_batch(batch)
```

---

## 🚀 **PERFORMANCE OPTIMIZATIONS**

### **Database Operations**
```sql
-- Use bulk insertions for migration
INSERT INTO customers (name, email, status) VALUES 
    ('Customer 1', 'email1@example.com', 'active'),
    ('Customer 2', 'email2@example.com', 'active'),
    ('Customer 3', 'email3@example.com', 'active');

-- Index optimization for lookups
CREATE INDEX idx_customer_lookup ON customers(email, status);
```

### **API Rate Limiting**
```python
# Rate limiting pattern
import time
from functools import wraps

def rate_limit(calls_per_second=10):
    def decorator(func):
        last_called = [0.0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = 1.0 / calls_per_second - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.time()
            return ret
        return wrapper
    return decorator
```

---

## 🔄 **TECHNOLOGY EVOLUTION**

### **Current State**
```
Analysis Phase Technologies:
├── Python scripts for discovery
├── Direct database connections  
├── Manual API testing
└── JSON documentation output

Production Migration Technologies (Planned):
├── Automated data processing pipelines
├── Batch processing with progress tracking
├── Error recovery and retry mechanisms
└── Performance monitoring and optimization
```

### **Future Technology Considerations**
```python
# Potential Additions for Phase 3+
- asyncio: For concurrent API operations
- pandas: For complex data transformations
- SQLAlchemy: If ORM becomes beneficial
- Redis: For caching and session management
- Docker: For deployment consistency
```

---

## 📋 **TECHNICAL STANDARDS**

### **Code Style Standards**
```python
# Type hints required
def process_customer(customer: Dict[str, Any]) -> CustomerResult:
    pass

# Docstrings for public functions
def migrate_data(source: SonarData, target: SplynxDB) -> MigrationResult:
    """
    Migrate data from Sonar to Splynx system.
    
    Args:
        source: Sonar data source
        target: Splynx database target
        
    Returns:
        Migration result with status and metrics
    """
    pass

# Error handling with specific exceptions
try:
    result = api_call()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 405:
        logger.info("Feature disabled, skipping")
    else:
        raise
```

### **Configuration Standards**
```python
# Use environment variables for all secrets
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SONAR_URL = os.getenv('SONAR_URL')
    SPLYNX_API_KEY = os.getenv('SPLYNX_API_KEY')
    
    @classmethod
    def validate(cls):
        required = ['SONAR_URL', 'SPLYNX_API_KEY']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing environment variables: {missing}")
```

---

**Technology Status: 🟢 STABLE - PROVEN STACK**  
**Next Evolution: Production migration engine with performance optimization**
