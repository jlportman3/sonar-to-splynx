# 🏗️ SYSTEM PATTERNS
**Architecture & Design Patterns**  
**Last Updated:** September 12, 2025  
**Current Architecture:** Hybrid API + Database Migration System

---

## 🎯 **CORE ARCHITECTURE PATTERNS**

### **Hybrid Data Access Pattern** ⭐
```python
# Primary Pattern: Database-First with API Validation
class HybridMigrationPattern:
    """
    Use direct database access for data migration performance,
    API calls for business logic validation and compliance
    """
    def migrate_data(self, data):
        # 1. Insert directly to database for speed/reliability
        self.database.insert(transformed_data)
        
        # 2. Validate via API for business logic compliance
        validation_result = self.api.validate(data.id)
        
        # 3. Handle any discrepancies
        if not validation_result.valid:
            self.reconcile(data, validation_result)
```

**When to Use:** Large-scale data migrations where API rate limits would be problematic  
**Benefits:** Maximum performance + business logic compliance  
**Trade-offs:** More complex error handling, dual validation required

### **Progressive Analysis Pattern**
```python
# Pattern: Analyze systems incrementally, build understanding
class ProgressiveAnalysisPattern:
    """
    Start with API discovery, progress to schema analysis,
    end with deep database understanding
    """
    def analyze_system(self):
        # Phase 1: API surface discovery
        endpoints = self.discover_api_endpoints()
        
        # Phase 2: Schema structure analysis  
        schema = self.analyze_database_schema()
        
        # Phase 3: Data relationship mapping
        relationships = self.map_relationships(schema)
        
        # Phase 4: Business logic understanding
        patterns = self.identify_business_patterns(relationships)
```

**When to Use:** Complex system integration where understanding must be built incrementally  
**Benefits:** Reduces risk, builds confidence, comprehensive understanding  
**Application:** Used successfully for both Sonar and Splynx analysis

---

## 🔧 **DATA ACCESS PATTERNS**

### **Database Connection Pattern**
```python
# Successful Pattern for MySQL Access
import mysql.connector

def get_database_connection(config):
    """Reliable connection pattern for Splynx MySQL"""
    return mysql.connector.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        unix_socket=config.socket,  # Key: Use unix socket
        database=config.database
    )
```

**Key Insights:**
- Unix socket more reliable than TCP for local connections
- debian-sys-maint user provides admin access
- Connection pooling not needed for migration scripts

### **API Authentication Pattern**
```python
# REST API Basic Auth Pattern
import base64

def authenticate_api(key, secret):
    """Splynx API authentication pattern"""
    credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
```

**Key Insights:**
- Basic auth more reliable than session tokens for scripts
- Include Accept header to ensure JSON responses
- Store credentials securely in environment variables

---

## 🔍 **ERROR HANDLING PATTERNS**

### **HTTP Error Classification Pattern**
```python
# Pattern: Classify HTTP errors by type and action
class HTTPErrorClassifier:
    """
    Different HTTP error codes require different responses
    """
    ERROR_ACTIONS = {
        401: "authentication_retry",     # Bad credentials
        403: "permissions_check",        # Access denied  
        404: "endpoint_missing",         # Not found
        405: "method_not_allowed",       # ⭐ Feature disabled
        422: "validation_error",         # Bad data
        500: "server_error"              # System issue
    }
```

**Key Pattern:** 405 errors indicate feature modules disabled, NOT permissions  
**Application:** Critical for understanding Splynx system capabilities

### **Progressive Error Investigation Pattern**
```python
# Pattern: Systematic error analysis
def investigate_http_error(endpoint, error_code):
    """
    Systematic approach to understanding HTTP errors
    """
    # 1. Test all HTTP methods
    methods_results = test_all_methods(endpoint)
    
    # 2. Check database for related tables
    db_status = check_database_tables(endpoint)
    
    # 3. Examine configuration settings
    config_status = check_feature_configuration(endpoint)
    
    # 4. Classify and document
    return classify_error_cause(methods_results, db_status, config_status)
```

---

## 📊 **DATA TRANSFORMATION PATTERNS**

### **Schema Mapping Pattern**
```python
# Pattern: Flexible field mapping with transformation
class SchemaMapper:
    """
    Map fields between systems with transformation support
    """
    FIELD_MAPPINGS = {
        'sonar_field': {
            'splynx_field': 'target_column',
            'transformer': lambda x: transform_function(x),
            'validator': lambda x: validate_function(x)
        }
    }
```

**Benefits:** Maintainable, testable, extensible  
**Usage:** Core pattern for Sonar → Splynx field mapping

### **Relationship Preservation Pattern**
```python
# Pattern: Maintain foreign key relationships during migration
class RelationshipPreserver:
    """
    Ensure data integrity during migration by preserving relationships
    """
    def migrate_with_relationships(self, source_data):
        # 1. Create dependency graph
        dependencies = self.build_dependency_graph(source_data)
        
        # 2. Sort by dependency order  
        ordered_data = self.topological_sort(dependencies)
        
        # 3. Migrate in dependency order
        for table_data in ordered_data:
            self.migrate_table(table_data)
```

---

## 🔄 **WORKFLOW PATTERNS**

### **Phase-Based Development Pattern**
```
Phase 1: Foundation → Phase 2: Analysis → Phase 3: Implementation
    ↓                    ↓                     ↓
Environment Setup → Schema Discovery → Core Migration Engine
Dependencies     → API Testing       → Data Processing  
Configuration    → Error Analysis    → Validation Logic
```

**Benefits:** Clear progress tracking, risk reduction, manageable complexity  
**Application:** Successfully used for this migration project

### **Documentation-Driven Development Pattern**
```python
# Pattern: Document understanding before implementation
def analyze_system():
    # 1. Discover and document
    findings = investigate_system()
    create_documentation(findings)
    
    # 2. Validate understanding  
    validate_findings(findings)
    
    # 3. Plan implementation
    plan = create_implementation_plan(findings)
    
    # 4. Implement with confidence
    implement(plan)
```

**Key Insight:** Time spent on analysis/documentation pays dividends in implementation  
**Evidence:** 405 error investigation prevented potential migration blocks

---

## 🚀 **ARCHITECTURAL EVOLUTION**

### **Current Architecture State**
```
┌─── Sonar System ────┐    ┌─── Migration Engine ────┐    ┌─── Splynx System ────┐
│ ┌─ GraphQL API ──┐  │    │ ┌─ Data Extraction ──┐  │    │ ┌─ REST API ───────┐ │
│ ├─ REST API ─────┤  │ ←→ │ ├─ Field Mapping ────┤  │ ←→ │ ├─ MySQL Database ─┤ │
│ └─ Data Sources ─┘  │    │ └─ Validation ───────┘  │    │ └─ Feature Modules ─┘ │
└─────────────────────┘    └─────────────────────────┘    └─────────────────────┘
```

### **Planned Evolution**
```
Current: Manual analysis scripts
    ↓
Phase 3: Automated data processing
    ↓  
Phase 4: Production migration engine
    ↓
Phase 5: Monitoring and optimization
```

---

**Architecture Status: 🟢 STABLE - PATTERNS PROVEN**  
**Next Evolution: Core migration engine implementation**
