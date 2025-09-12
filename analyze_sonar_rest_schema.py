#!/usr/bin/env python3
"""
Analyze Sonar REST API schema and generate comprehensive documentation.
This script discovers all available endpoints and creates detailed schema documentation.
"""

import sys
import os
import json
from datetime import datetime
from typing import Dict, Any, List

# Add src to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.apis.sonar_rest_client import SonarRestClient
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger

# Setup logging
setup_logger(config.log_level)
logger = get_logger("rest_schema_analyzer")

class SonarRestSchemaAnalyzer:
    """Analyzes Sonar REST API schema and generates documentation."""
    
    def __init__(self):
        self.client = None
        self.discovered_endpoints = []
        self.endpoint_schemas = {}
    
    def connect(self) -> bool:
        """Connect to Sonar REST API and test connection."""
        try:
            logger.info("Initializing Sonar REST API client...")
            self.client = SonarRestClient(config)
            
            # Test connection
            if self.client.test_connection():
                logger.info("Successfully connected to Sonar REST API")
                return True
            else:
                logger.error("Failed to connect to Sonar REST API")
                return False
                
        except Exception as e:
            logger.error(f"Failed to initialize Sonar REST client: {e}")
            return False
    
    def discover_all_endpoints(self) -> List[str]:
        """Discover all available REST API endpoints."""
        if not self.client:
            raise RuntimeError("Client not connected. Call connect() first.")
        
        logger.info("Starting endpoint discovery...")
        self.discovered_endpoints = self.client.discover_endpoints()
        
        logger.info(f"Discovered {len(self.discovered_endpoints)} endpoints")
        return self.discovered_endpoints
    
    def analyze_all_schemas(self) -> Dict[str, Any]:
        """Analyze schemas for all discovered endpoints."""
        if not self.discovered_endpoints:
            raise RuntimeError("No endpoints discovered. Call discover_all_endpoints() first.")
        
        logger.info("Starting comprehensive schema analysis...")
        
        for endpoint in self.discovered_endpoints:
            try:
                schema = self.client.analyze_endpoint_schema(endpoint, sample_size=10)
                self.endpoint_schemas[endpoint] = schema
                logger.info(f"Analyzed schema for {endpoint}: {schema.get('total_records', 0)} records")
            except Exception as e:
                logger.error(f"Failed to analyze {endpoint}: {e}")
                self.endpoint_schemas[endpoint] = {
                    "endpoint": endpoint,
                    "available": False,
                    "error": str(e)
                }
        
        return self.endpoint_schemas
    
    def categorize_endpoints(self) -> Dict[str, List[str]]:
        """Categorize discovered endpoints by business function."""
        categories = {
            "accounts": ["account", "customer", "subscriber"],
            "billing": ["invoice", "payment", "transaction", "charge", "credit", "debit", "billing"],
            "services": ["service", "plan", "package", "subscription"],
            "network": ["network", "ip", "vlan", "router", "switch", "access_point", "radius", "dhcp"],
            "infrastructure": ["tower", "site", "facility", "address", "geographic", "inventory", "equipment"],
            "operations": ["ticket", "task", "work_order", "maintenance", "outage", "schedule"],
            "monitoring": ["monitor", "alert", "notification", "statistic", "performance", "availability"],
            "users": ["user", "role", "permission", "group", "authentication"],
            "system": ["company", "setting", "configuration", "log", "audit", "job"],
            "integration": ["webhook", "api", "integration", "provisioning"],
            "usage": ["usage", "bandwidth", "data", "quota", "overage", "traffic"],
            "documents": ["document", "file", "attachment", "template"],
            "voip": ["voip", "sip", "phone", "call"],
            "financial": ["balance", "adjustment", "refund", "deposit"],
            "reporting": ["report", "dashboard", "analytic", "export"]
        }
        
        categorized = {category: [] for category in categories.keys()}
        categorized["other"] = []
        
        for endpoint in self.discovered_endpoints:
            categorized_flag = False
            for category, patterns in categories.items():
                if any(pattern in endpoint.lower() for pattern in patterns):
                    categorized[category].append(endpoint)
                    categorized_flag = True
                    break
            
            if not categorized_flag:
                categorized["other"].append(endpoint)
        
        return categorized
    
    def generate_comprehensive_analysis(self) -> Dict[str, Any]:
        """Generate comprehensive analysis of the REST API."""
        categorized_endpoints = self.categorize_endpoints()
        
        # Calculate statistics
        total_endpoints = len(self.discovered_endpoints)
        total_records = sum(
            schema.get("total_records", 0) 
            for schema in self.endpoint_schemas.values() 
            if schema.get("available", False)
        )
        
        # Identify high-value endpoints (lots of data)
        high_value_endpoints = []
        for endpoint, schema in self.endpoint_schemas.items():
            if schema.get("available") and schema.get("total_records", 0) > 10:
                high_value_endpoints.append({
                    "endpoint": endpoint,
                    "record_count": schema["total_records"],
                    "field_count": len(schema.get("fields", {}))
                })
        
        high_value_endpoints.sort(key=lambda x: x["record_count"], reverse=True)
        
        # Generate field statistics
        all_fields = {}
        for endpoint, schema in self.endpoint_schemas.items():
            if schema.get("available") and schema.get("fields"):
                for field_name, field_info in schema["fields"].items():
                    if field_name not in all_fields:
                        all_fields[field_name] = {
                            "endpoints": [],
                            "types": set(),
                            "nullable_count": 0
                        }
                    
                    all_fields[field_name]["endpoints"].append(endpoint)
                    all_fields[field_name]["types"].add(field_info.get("type", "unknown"))
                    if field_info.get("nullable", False):
                        all_fields[field_name]["nullable_count"] += 1
        
        # Convert sets to lists for JSON serialization
        for field_info in all_fields.values():
            field_info["types"] = list(field_info["types"])
        
        return {
            "metadata": {
                "analyzed_at": datetime.now().isoformat(),
                "total_endpoints": total_endpoints,
                "total_records": total_records,
                "api_base_url": self.client.base_url
            },
            "discovery": {
                "discovered_endpoints": self.discovered_endpoints,
                "categorized_endpoints": categorized_endpoints,
                "high_value_endpoints": high_value_endpoints[:20]  # Top 20
            },
            "schemas": self.endpoint_schemas,
            "field_analysis": {
                "common_fields": {
                    field: info for field, info in all_fields.items() 
                    if len(info["endpoints"]) > 1  # Fields that appear in multiple endpoints
                },
                "total_unique_fields": len(all_fields)
            },
            "migration_insights": self._generate_migration_insights(categorized_endpoints, high_value_endpoints)
        }
    
    def _generate_migration_insights(self, categorized_endpoints: Dict[str, List[str]], 
                                   high_value_endpoints: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate insights for migration planning."""
        
        # Priority endpoints for migration
        priority_categories = ["accounts", "billing", "services", "network"]
        priority_endpoints = []
        
        for category in priority_categories:
            priority_endpoints.extend(categorized_endpoints.get(category, []))
        
        # Data volume analysis
        total_priority_records = sum(
            endpoint["record_count"] for endpoint in high_value_endpoints 
            if endpoint["endpoint"] in priority_endpoints
        )
        
        # Complexity analysis
        complex_endpoints = [
            endpoint for endpoint in high_value_endpoints
            if endpoint["field_count"] > 10  # More than 10 fields = complex
        ]
        
        return {
            "priority_endpoints": priority_endpoints,
            "high_priority_record_count": total_priority_records,
            "complex_endpoints": [e["endpoint"] for e in complex_endpoints],
            "recommended_migration_order": [
                "accounts",
                "services", 
                "billing",
                "network",
                "infrastructure",
                "operations",
                "users",
                "system"
            ],
            "estimated_complexity": "high" if len(complex_endpoints) > 10 else "medium" if len(complex_endpoints) > 5 else "low"
        }
    
    def save_analysis(self, analysis: Dict[str, Any], output_dir: str = "docs/sonar") -> None:
        """Save comprehensive analysis to files."""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save full analysis as JSON
        with open(f"{output_dir}/rest_api_analysis.json", "w") as f:
            json.dump(analysis, f, indent=2)
        
        # Generate markdown documentation
        self._generate_markdown_docs(analysis, output_dir)
        
        # Generate programming-friendly schema files
        self._generate_programming_schemas(analysis, output_dir)
        
        logger.info(f"Analysis saved to {output_dir}")
    
    def _generate_markdown_docs(self, analysis: Dict[str, Any], output_dir: str) -> None:
        """Generate comprehensive markdown documentation."""
        
        md_content = f"""# Sonar REST API Complete Schema Analysis

Generated on: {analysis['metadata']['analyzed_at']}
API Base URL: {analysis['metadata']['api_base_url']}

## Executive Summary

- **Total Endpoints Discovered**: {analysis['metadata']['total_endpoints']}
- **Total Records Available**: {analysis['metadata']['total_records']:,}
- **Unique Fields**: {analysis['field_analysis']['total_unique_fields']}
- **Migration Complexity**: {analysis['migration_insights']['estimated_complexity']}

## API Endpoints Overview

### Available Endpoints by Category

"""
        
        # Show endpoint categories
        categorized = analysis['discovery']['categorized_endpoints']
        for category, endpoints in categorized.items():
            if endpoints:
                md_content += f"\n#### {category.title()} ({len(endpoints)} endpoints)\n\n"
                for endpoint in sorted(endpoints):
                    schema = analysis['schemas'].get(endpoint, {})
                    record_count = schema.get('total_records', 0)
                    md_content += f"- **{endpoint}**: {record_count:,} records\n"
        
        # High-value endpoints
        md_content += f"\n## High-Value Endpoints (Top Data Sources)\n\n"
        
        for endpoint_info in analysis['discovery']['high_value_endpoints']:
            endpoint = endpoint_info['endpoint']
            record_count = endpoint_info['record_count']
            field_count = endpoint_info['field_count']
            
            md_content += f"\n### {endpoint}\n\n"
            md_content += f"- **Records**: {record_count:,}\n"
            md_content += f"- **Fields**: {field_count}\n"
            
            # Add field details
            schema = analysis['schemas'].get(endpoint, {})
            if schema.get('fields'):
                md_content += f"\n**Fields**:\n\n"
                for field_name, field_info in sorted(schema['fields'].items()):
                    field_type = field_info.get('type', 'unknown')
                    nullable = " (nullable)" if field_info.get('nullable', False) else ""
                    sample_values = field_info.get('sample_values', [])
                    
                    md_content += f"- `{field_name}`: `{field_type}`{nullable}"
                    if sample_values:
                        sample_str = ", ".join(f'"{v}"' for v in sample_values[:3])
                        md_content += f" - Examples: {sample_str}"
                    md_content += "\n"
                
                # Add sample records
                if schema.get('sample_records'):
                    md_content += f"\n**Sample Record**:\n```json\n{json.dumps(schema['sample_records'][0], indent=2)}\n```\n"
            
            md_content += "\n---\n"
        
        # Migration insights
        md_content += f"\n## Migration Planning Insights\n\n"
        
        insights = analysis['migration_insights']
        
        md_content += f"### Recommended Migration Order\n\n"
        for i, category in enumerate(insights['recommended_migration_order'], 1):
            endpoints = categorized.get(category, [])
            if endpoints:
                total_records = sum(
                    analysis['schemas'].get(ep, {}).get('total_records', 0) 
                    for ep in endpoints
                )
                md_content += f"{i}. **{category.title()}**: {len(endpoints)} endpoints, {total_records:,} records\n"
        
        md_content += f"\n### Priority Endpoints for Migration\n\n"
        for endpoint in insights['priority_endpoints'][:10]:
            record_count = analysis['schemas'].get(endpoint, {}).get('total_records', 0)
            md_content += f"- **{endpoint}**: {record_count:,} records\n"
        
        md_content += f"\n### Complex Endpoints (>10 fields)\n\n"
        for endpoint in insights['complex_endpoints']:
            field_count = len(analysis['schemas'].get(endpoint, {}).get('fields', {}))
            md_content += f"- **{endpoint}**: {field_count} fields\n"
        
        # Common fields analysis
        md_content += f"\n## Common Fields Analysis\n\n"
        md_content += "Fields that appear across multiple endpoints:\n\n"
        
        common_fields = analysis['field_analysis']['common_fields']
        for field_name, field_info in sorted(common_fields.items(), key=lambda x: len(x[1]['endpoints']), reverse=True)[:20]:
            endpoint_count = len(field_info['endpoints'])
            types = ", ".join(field_info['types'])
            md_content += f"- **{field_name}**: {endpoint_count} endpoints, types: {types}\n"
        
        # Save markdown documentation
        with open(f"{output_dir}/rest_api_schema.md", "w") as f:
            f.write(md_content)
    
    def _generate_programming_schemas(self, analysis: Dict[str, Any], output_dir: str) -> None:
        """Generate programming-friendly schema files."""
        
        # Generate Python dataclass definitions
        python_models = self._generate_python_models(analysis)
        with open(f"{output_dir}/sonar_models.py", "w") as f:
            f.write(python_models)
        
        # Generate endpoint mapping for programming
        endpoint_mapping = {
            "endpoints": {
                endpoint: {
                    "url": f"/api/v1/{endpoint}",
                    "method": "GET",
                    "pagination": bool(schema.get('pagination')),
                    "total_records": schema.get('total_records', 0),
                    "fields": list(schema.get('fields', {}).keys())
                }
                for endpoint, schema in analysis['schemas'].items()
                if schema.get('available', False)
            },
            "categories": analysis['discovery']['categorized_endpoints'],
            "migration_order": analysis['migration_insights']['recommended_migration_order']
        }
        
        with open(f"{output_dir}/endpoint_mapping.json", "w") as f:
            json.dump(endpoint_mapping, f, indent=2)
        
        # Generate simple endpoint list for quick reference
        with open(f"{output_dir}/available_endpoints.txt", "w") as f:
            f.write("# Available Sonar REST API Endpoints\n\n")
            for endpoint in sorted(analysis['discovery']['discovered_endpoints']):
                record_count = analysis['schemas'].get(endpoint, {}).get('total_records', 0)
                f.write(f"{endpoint}: {record_count:,} records\n")
    
    def _generate_python_models(self, analysis: Dict[str, Any]) -> str:
        """Generate Python dataclass models for major endpoints."""
        
        models_code = '''"""
Auto-generated Python models for Sonar REST API.
Generated from live API schema analysis.
"""

from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime

'''
        
        # Generate models for high-value endpoints
        high_value_endpoints = analysis['discovery']['high_value_endpoints'][:10]
        
        for endpoint_info in high_value_endpoints:
            endpoint = endpoint_info['endpoint']
            schema = analysis['schemas'].get(endpoint, {})
            
            if not schema.get('fields'):
                continue
            
            # Convert endpoint name to class name
            class_name = ''.join(word.capitalize() for word in endpoint.split('_'))
            if not class_name.endswith('s'):
                class_name += 'Item'
            else:
                class_name = class_name[:-1]  # Remove trailing 's'
            
            models_code += f"\n@dataclass\nclass {class_name}:\n"
            models_code += f'    """Model for {endpoint} endpoint."""\n'
            
            # Generate fields
            for field_name, field_info in schema['fields'].items():
                field_type = field_info.get('type', 'str')
                nullable = field_info.get('nullable', False)
                
                # Map Python types
                if field_type == 'int':
                    python_type = 'int'
                elif field_type == 'float':
                    python_type = 'float'
                elif field_type == 'bool':
                    python_type = 'bool'
                elif field_type == 'list':
                    python_type = 'List[Any]'
                elif field_type == 'dict':
                    python_type = 'dict'
                else:
                    python_type = 'str'
                
                if nullable:
                    python_type = f"Optional[{python_type}]"
                    default_value = " = None"
                else:
                    default_value = ""
                
                models_code += f"    {field_name}: {python_type}{default_value}\n"
            
            models_code += "\n"
        
        return models_code


def main():
    """Main function to run REST API schema analysis."""
    analyzer = SonarRestSchemaAnalyzer()
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        logger.error("No .env file found. Please create one with your Sonar credentials.")
        logger.info("Copy .env.example to .env and fill in your credentials.")
        return
    
    try:
        # Validate configuration
        config.validate()
        
        # Connect to Sonar
        if not analyzer.connect():
            logger.error("Failed to connect to Sonar REST API")
            return
        
        # Discover endpoints
        endpoints = analyzer.discover_all_endpoints()
        logger.info(f"Discovered {len(endpoints)} endpoints")
        
        # Analyze schemas
        analyzer.analyze_all_schemas()
        
        # Generate comprehensive analysis
        analysis = analyzer.generate_comprehensive_analysis()
        
        # Save results
        analyzer.save_analysis(analysis)
        
        logger.info("REST API schema analysis completed successfully!")
        logger.info("Check docs/sonar/ for generated documentation")
        
        # Print summary
        print(f"\n🎉 Analysis Complete!")
        print(f"📊 Discovered {len(endpoints)} endpoints")
        print(f"💾 Total records: {analysis['metadata']['total_records']:,}")
        print(f"🔧 Migration complexity: {analysis['migration_insights']['estimated_complexity']}")
        print(f"📁 Documentation saved to docs/sonar/")
        
    except Exception as e:
        logger.error(f"REST API schema analysis failed: {e}")
        raise

if __name__ == "__main__":
    main()
