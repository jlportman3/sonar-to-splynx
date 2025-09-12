"""Schema analyzer for Sonar GraphQL API."""

import json
import os
from typing import Dict, Any, List
from datetime import datetime

from src.apis.sonar_client import SonarGraphQLClient
from src.config.settings import config
from src.utils.logger import setup_logger, get_logger

# Setup logging
setup_logger(config.log_level)
logger = get_logger("schema_analyzer")

class SonarSchemaAnalyzer:
    """Analyzes and documents Sonar GraphQL schema."""
    
    def __init__(self):
        self.client = None
        self.schema_data = None
    
    def connect(self) -> bool:
        """Connect to Sonar API and test connection."""
        try:
            logger.info("Initializing Sonar GraphQL client...")
            self.client = SonarGraphQLClient(config)
            
            # Test connection
            if self.client.test_connection():
                logger.info("Successfully connected to Sonar API")
                return True
            else:
                logger.error("Failed to connect to Sonar API")
                return False
                
        except Exception as e:
            logger.error(f"Failed to initialize Sonar client: {e}")
            return False
    
    def analyze_schema(self) -> Dict[str, Any]:
        """Perform comprehensive schema analysis."""
        if not self.client:
            raise RuntimeError("Client not connected. Call connect() first.")
        
        logger.info("Starting comprehensive schema analysis...")
        
        # Get full schema
        schema_info = self.client.get_schema_info()
        self.schema_data = schema_info
        
        # Analyze different aspects
        analysis = {
            "metadata": self._get_metadata(),
            "queries": self._analyze_queries(),
            "mutations": self._analyze_mutations(),
            "types": self._analyze_types(),
            "entities": self._identify_entities(),
            "relationships": self._analyze_relationships(),
            "summary": self._generate_summary()
        }
        
        logger.info("Schema analysis completed")
        return analysis
    
    def _get_metadata(self) -> Dict[str, Any]:
        """Extract schema metadata."""
        if not self.schema_data:
            return {}
        
        schema = self.schema_data["__schema"]
        
        return {
            "analyzed_at": datetime.now().isoformat(),
            "query_type": schema.get("queryType", {}).get("name") if schema.get("queryType") else None,
            "mutation_type": schema.get("mutationType", {}).get("name") if schema.get("mutationType") else None,
            "subscription_type": schema.get("subscriptionType", {}).get("name") if schema.get("subscriptionType") else None,
            "total_types": len(schema.get("types", [])),
            "total_directives": len(schema.get("directives", []))
        }
    
    def _analyze_queries(self) -> Dict[str, Any]:
        """Analyze available queries."""
        if not self.client:
            return {}
        
        queries = self.client.get_available_queries()
        categorized = self.client.explore_entity_queries()
        
        # Get detailed query information
        query_details = []
        schema = self.schema_data["__schema"]
        
        # Find Query type
        query_type = None
        for type_info in schema["types"]:
            if type_info["name"] == schema["queryType"]["name"]:
                query_type = type_info
                break
        
        if query_type and query_type.get("fields"):
            for field in query_type["fields"]:
                query_details.append({
                    "name": field["name"],
                    "description": field.get("description"),
                    "return_type": self._extract_type_name(field["type"]),
                    "arguments": [
                        {
                            "name": arg["name"],
                            "type": self._extract_type_name(arg["type"]),
                            "description": arg.get("description")
                        }
                        for arg in field.get("args", [])
                    ]
                })
        
        return {
            "total_queries": len(queries),
            "categorized": categorized,
            "query_details": query_details
        }
    
    def _analyze_mutations(self) -> Dict[str, Any]:
        """Analyze available mutations."""
        schema = self.schema_data["__schema"]
        
        if not schema.get("mutationType"):
            return {"total_mutations": 0, "mutations": []}
        
        # Find Mutation type
        mutation_type = None
        for type_info in schema["types"]:
            if type_info["name"] == schema["mutationType"]["name"]:
                mutation_type = type_info
                break
        
        mutations = []
        if mutation_type and mutation_type.get("fields"):
            for field in mutation_type["fields"]:
                mutations.append({
                    "name": field["name"],
                    "description": field.get("description"),
                    "return_type": self._extract_type_name(field["type"]),
                    "arguments": [
                        {
                            "name": arg["name"],
                            "type": self._extract_type_name(arg["type"]),
                            "description": arg.get("description")
                        }
                        for arg in field.get("args", [])
                    ]
                })
        
        return {
            "total_mutations": len(mutations),
            "mutations": mutations
        }
    
    def _analyze_types(self) -> Dict[str, Any]:
        """Analyze GraphQL types."""
        schema = self.schema_data["__schema"]
        types = schema.get("types", [])
        
        type_analysis = {
            "scalars": [],
            "objects": [],
            "enums": [],
            "interfaces": [],
            "unions": [],
            "input_objects": []
        }
        
        for type_info in types:
            kind = type_info.get("kind", "").lower()
            type_name = type_info.get("name", "")
            
            # Skip introspection types
            if type_name.startswith("__"):
                continue
            
            type_summary = {
                "name": type_name,
                "description": type_info.get("description"),
                "fields_count": len(type_info.get("fields", [])) if type_info.get("fields") else 0
            }
            
            if kind == "scalar":
                type_analysis["scalars"].append(type_summary)
            elif kind == "object":
                type_analysis["objects"].append(type_summary)
            elif kind == "enum":
                type_summary["values"] = [
                    enum_val["name"] for enum_val in type_info.get("enumValues", [])
                ]
                type_analysis["enums"].append(type_summary)
            elif kind == "interface":
                type_analysis["interfaces"].append(type_summary)
            elif kind == "union":
                type_analysis["unions"].append(type_summary)
            elif kind == "input_object":
                type_analysis["input_objects"].append(type_summary)
        
        return type_analysis
    
    def _identify_entities(self) -> List[Dict[str, Any]]:
        """Identify ALL business entities with comprehensive analysis."""
        schema = self.schema_data["__schema"]
        types = schema.get("types", [])
        
        entities = []
        
        # Comprehensive entity indicators (expanded)
        primary_indicators = ["id", "created_at", "updated_at", "name", "status"]
        secondary_indicators = ["type", "date", "time", "enabled", "active", "deleted", "description"]
        operational_indicators = ["job", "log", "event", "history", "audit", "queue", "worker"]
        
        for type_info in types:
            if (type_info.get("kind") == "OBJECT" and 
                not type_info.get("name", "").startswith("__") and
                type_info.get("fields")):
                
                fields = type_info["fields"]
                field_names = [field["name"].lower() for field in fields]
                type_name = type_info["name"]
                
                # Score based on different entity patterns
                primary_score = sum(1 for indicator in primary_indicators if indicator in field_names)
                secondary_score = sum(1 for indicator in secondary_indicators if indicator in field_names)
                operational_score = sum(1 for indicator in operational_indicators if indicator in field_names or indicator in type_name.lower())
                
                # Include more entities with lower thresholds for comprehensive analysis
                total_score = primary_score * 3 + secondary_score * 2 + operational_score
                
                if (primary_score >= 1 or secondary_score >= 2 or operational_score >= 1 or 
                    len(fields) >= 3):  # Much more inclusive
                    
                    # Categorize entity type
                    entity_category = self._categorize_entity(type_name, field_names)
                    
                    # Get ALL fields for deep analysis
                    all_fields = []
                    for field in fields:
                        field_type = self._extract_type_name(field["type"])
                        field_info = {
                            "name": field["name"],
                            "type": field_type,
                            "description": field.get("description"),
                            "is_list": self._is_list_type(field["type"]),
                            "is_required": self._is_required_type(field["type"]),
                            "is_connection": field_type.endswith("Connection"),
                            "is_enum": self._is_enum_type(field_type, schema)
                        }
                        all_fields.append(field_info)
                    
                    entity_info = {
                        "name": type_name,
                        "description": type_info.get("description"),
                        "category": entity_category,
                        "primary_score": primary_score,
                        "secondary_score": secondary_score,
                        "operational_score": operational_score,
                        "total_score": total_score,
                        "fields": all_fields,
                        "total_fields": len(fields),
                        "key_fields": self._identify_key_fields(all_fields),
                        "relationship_fields": [f for f in all_fields if f["is_connection"] or not f["type"].lower() in ["string", "int", "boolean", "float", "id", "datetime", "date", "time"]],
                        "enum_fields": [f for f in all_fields if f["is_enum"]]
                    }
                    entities.append(entity_info)
        
        # Sort by total score and name
        entities.sort(key=lambda x: (x["total_score"], x["name"]), reverse=True)
        
        return entities
    
    def _analyze_relationships(self) -> Dict[str, Any]:
        """Analyze relationships between entities."""
        schema = self.schema_data["__schema"]
        types = schema.get("types", [])
        
        relationships = []
        
        for type_info in types:
            if (type_info.get("kind") == "OBJECT" and 
                not type_info.get("name", "").startswith("__") and
                type_info.get("fields")):
                
                for field in type_info["fields"]:
                    field_type = self._extract_type_name(field["type"])
                    
                    # Look for references to other types
                    if field_type and not field_type.lower() in ["string", "int", "boolean", "float", "id"]:
                        relationships.append({
                            "from_type": type_info["name"],
                            "to_type": field_type,
                            "field_name": field["name"],
                            "relationship_type": "has_one" if not field_type.endswith("Connection") else "has_many"
                        })
        
        return {
            "total_relationships": len(relationships),
            "relationships": relationships[:50]  # Limit for readability
        }
    
    def _generate_summary(self) -> Dict[str, Any]:
        """Generate a summary of the schema analysis."""
        if not self.schema_data:
            return {}
        
        schema = self.schema_data["__schema"]
        
        return {
            "schema_complexity": "high" if len(schema.get("types", [])) > 100 else "medium" if len(schema.get("types", [])) > 50 else "low",
            "has_mutations": bool(schema.get("mutationType")),
            "has_subscriptions": bool(schema.get("subscriptionType")),
            "custom_scalars": len([t for t in schema.get("types", []) if t.get("kind") == "SCALAR" and not t.get("name", "").startswith("__")]),
            "business_objects": len([t for t in schema.get("types", []) if t.get("kind") == "OBJECT" and not t.get("name", "").startswith("__")])
        }
    
    def _extract_type_name(self, type_ref: Dict[str, Any]) -> str:
        """Extract the actual type name from a type reference."""
        if not type_ref:
            return ""
        
        if type_ref.get("name"):
            return type_ref["name"]
        
        if type_ref.get("ofType"):
            return self._extract_type_name(type_ref["ofType"])
        
        return ""
    
    def _categorize_entity(self, type_name: str, field_names: List[str]) -> str:
        """Categorize entity based on name and fields."""
        type_lower = type_name.lower()
        field_set = set(field_names)
        
        # COMPREHENSIVE category patterns matching the expanded client patterns
        categories = {
            "accounts": ["account", "customer", "subscriber", "client"],
            "services": ["service", "plan", "package", "subscription", "rate", "tariff", "pricing"],
            "billing": ["bill", "invoice", "payment", "credit", "debit", "transaction", "charge", "fee", "tax", "recurring"],
            
            # Network Infrastructure
            "network_equipment": ["router", "switch", "access_point", "ap", "cpe", "modem", "gateway", "bridge", "repeater", "concentrator"],
            "network_interfaces": ["interface", "port", "ethernet", "wifi", "wireless", "fiber", "coax", "cable"],
            "ip_management": ["ip", "subnet", "vlan", "dhcp", "dns", "arp", "mac", "lease", "pool", "range", "assignment"],
            "network_protocols": ["radius", "pppoe", "snmp", "ospf", "bgp", "vrrp", "hsrp", "stp", "lacp", "lldp"],
            
            # Physical Infrastructure
            "sites": ["site", "location", "building", "premises", "facility", "datacenter", "pop", "node"],
            "towers": ["tower", "antenna", "mast", "pole", "cellular", "radio", "microwave", "backhaul"],
            "geographic": ["address", "geographic", "gps", "coordinate", "latitude", "longitude", "zone", "region"],
            "physical_assets": ["rack", "cabinet", "enclosure", "shelter", "power", "cooling", "generator", "ups"],
            
            # Equipment & Inventory
            "inventory": ["inventory", "item", "model", "vendor", "equipment", "asset", "serial", "part", "component"],
            "devices": ["device", "hardware", "firmware", "software", "version", "revision", "patch"],
            "cables": ["cable", "fiber", "copper", "patch", "trunk", "drop", "splice", "termination"],
            
            # Users & Access Management
            "users": ["user", "employee", "technician", "admin", "operator", "manager", "staff"],
            "roles": ["role", "permission", "privilege", "group", "team", "department", "access", "authorization"],
            "authentication": ["auth", "login", "password", "token", "session", "certificate", "key", "credential"],
            
            # Tickets & Operations
            "tickets": ["ticket", "task", "work_order", "trouble", "incident", "request", "comment", "priority", "category"],
            "maintenance": ["maintenance", "repair", "upgrade", "installation", "outage", "downtime", "scheduled"],
            
            # Monitoring & Performance
            "monitoring": ["monitor", "alert", "notification", "threshold", "metric", "status", "health", "performance"],
            "statistics": ["statistic", "graph", "chart", "measurement", "reading", "sample", "data_point"],
            "availability": ["uptime", "downtime", "sla", "availability", "reliability", "quality"],
            
            # Business Operations
            "contacts": ["contact", "phone", "email", "communication", "correspondence"],
            "financial": ["ledger", "balance", "deposit", "refund", "adjustment", "write_off", "accounting"],
            "contracts": ["contract", "agreement", "terms", "conditions", "sla", "warranty"],
            
            # System Operations
            "jobs": ["job", "scheduled", "cron", "queue", "worker", "background", "batch", "process"],
            "logs": ["log", "audit", "history", "event", "activity", "change", "trace", "debug"],
            "configuration": ["setting", "config", "preference", "option", "parameter", "policy", "rule"],
            "backup": ["backup", "restore", "snapshot", "archive", "recovery", "replication"],
            
            # Integration & APIs
            "integration": ["webhook", "api", "sync", "import", "export", "third_party", "external", "feed"],
            "provisioning": ["provision", "activate", "suspend", "terminate", "deploy", "configure", "setup"],
            
            # Usage & Analytics
            "usage": ["usage", "data", "bandwidth", "consumption", "quota", "overage", "traffic", "volume"],
            "reports": ["report", "dashboard", "analytic", "summary", "export", "statement"],
            
            # Documentation & Files
            "documents": ["document", "file", "attachment", "template", "manual", "diagram", "drawing"],
            "scheduling": ["schedule", "appointment", "calendar", "time_slot", "availability", "booking"],
            
            # Specialized Network Services
            "voip": ["voip", "sip", "voice", "phone", "call", "pbx", "trunk", "extension"],
            "video": ["video", "streaming", "iptv", "multicast", "codec", "bitrate"],
            "wireless": ["wireless", "wifi", "radio", "frequency", "channel", "ssid", "signal", "spectrum"],
            "security": ["firewall", "vpn", "ipsec", "acl", "nat", "qos", "traffic_shaping", "encryption"]
        }
        
        # Check type name first
        for category, patterns in categories.items():
            if any(pattern in type_lower for pattern in patterns):
                return category
        
        # Check field names
        for category, patterns in categories.items():
            if any(pattern in field_name for field_name in field_names for pattern in patterns):
                return category
        
        return "other"
    
    def _is_list_type(self, type_ref: Dict[str, Any]) -> bool:
        """Check if the type is a list/array."""
        if not type_ref:
            return False
        
        if type_ref.get("kind") == "LIST":
            return True
        
        if type_ref.get("ofType"):
            return self._is_list_type(type_ref["ofType"])
        
        return False
    
    def _is_required_type(self, type_ref: Dict[str, Any]) -> bool:
        """Check if the type is required (non-null)."""
        if not type_ref:
            return False
        
        return type_ref.get("kind") == "NON_NULL"
    
    def _is_enum_type(self, type_name: str, schema: Dict[str, Any]) -> bool:
        """Check if the type is an enum."""
        if not type_name or not schema:
            return False
        
        for type_info in schema.get("types", []):
            if type_info.get("name") == type_name and type_info.get("kind") == "ENUM":
                return True
        
        return False
    
    def _identify_key_fields(self, fields: List[Dict[str, Any]]) -> List[str]:
        """Identify key fields that are important for entity identification."""
        key_patterns = ["id", "name", "email", "username", "slug", "code", "number", "key"]
        key_fields = []
        
        for field in fields:
            field_name = field["name"].lower()
            if any(pattern in field_name for pattern in key_patterns):
                key_fields.append(field["name"])
        
        return key_fields
    
    def save_analysis(self, analysis: Dict[str, Any], output_dir: str = "docs/sonar") -> None:
        """Save analysis results to files."""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save full analysis as JSON
        with open(f"{output_dir}/schema_analysis.json", "w") as f:
            json.dump(analysis, f, indent=2)
        
        # Generate markdown documentation
        self._generate_markdown_docs(analysis, output_dir)
        
        logger.info(f"Analysis saved to {output_dir}")
    
    def _generate_markdown_docs(self, analysis: Dict[str, Any], output_dir: str) -> None:
        """Generate comprehensive markdown documentation from analysis."""
        
        # Main schema documentation
        md_content = f"""# Sonar GraphQL API Deep Schema Analysis

Generated on: {analysis['metadata']['analyzed_at']}

## Executive Summary

- **Query Type**: {analysis['metadata']['query_type']}
- **Mutation Type**: {analysis['metadata']['mutation_type']}
- **Total Types**: {analysis['metadata']['total_types']}
- **Schema Complexity**: {analysis['summary']['schema_complexity']}
- **Total Entities Found**: {len(analysis['entities'])}
- **Business Objects**: {analysis['summary']['business_objects']}
- **Custom Scalars**: {analysis['summary']['custom_scalars']}

## API Capabilities Overview

### Queries ({analysis['queries']['total_queries']} total)

This Sonar instance exposes {analysis['queries']['total_queries']} different query endpoints categorized as follows:

"""
        
        # Show query categories with counts
        for category, queries in analysis['queries']['categorized'].items():
            if queries:
                md_content += f"- **{category.title()}**: {len(queries)} queries\n"
        
        md_content += "\n### Detailed Query Breakdown\n\n"
        
        for category, queries in analysis['queries']['categorized'].items():
            if queries:
                md_content += f"\n#### {category.title()} Queries ({len(queries)} total)\n\n"
                for query in queries:
                    md_content += f"- `{query}`\n"
        
        # Comprehensive entity analysis
        md_content += f"\n## Complete Entity Catalog ({len(analysis['entities'])} entities)\n\n"
        
        # Group entities by category
        entities_by_category = {}
        for entity in analysis['entities']:
            category = entity['category']
            if category not in entities_by_category:
                entities_by_category[category] = []
            entities_by_category[category].append(entity)
        
        # Show category overview
        md_content += "### Entity Distribution by Category\n\n"
        for category, entities in sorted(entities_by_category.items()):
            md_content += f"- **{category.title()}**: {len(entities)} entities\n"
        
        md_content += "\n### Detailed Entity Analysis\n\n"
        
        # Show ALL entities grouped by category
        for category, entities in sorted(entities_by_category.items()):
            md_content += f"\n## {category.title()} Entities ({len(entities)} total)\n\n"
            
            for entity in sorted(entities, key=lambda x: x['total_score'], reverse=True):
                md_content += f"\n### {entity['name']}\n\n"
                
                if entity['description']:
                    md_content += f"**Description**: {entity['description']}\n\n"
                
                md_content += f"**Category**: {entity['category']}\n"
                md_content += f"**Relevance Score**: {entity['total_score']} (Primary: {entity['primary_score']}, Secondary: {entity['secondary_score']}, Operational: {entity['operational_score']})\n"
                md_content += f"**Total Fields**: {entity['total_fields']}\n\n"
                
                if entity['key_fields']:
                    md_content += f"**Key Fields**: {', '.join(f'`{field}`' for field in entity['key_fields'])}\n\n"
                
                if entity['enum_fields']:
                    enum_field_names = ', '.join(f"`{field['name']}`" for field in entity['enum_fields'])
                    md_content += f"**Enum Fields**: {len(entity['enum_fields'])} ({enum_field_names})\n\n"
                
                if entity['relationship_fields']:
                    rel_field_names = ', '.join(f"`{field['name']}`" for field in entity['relationship_fields'][:5])
                    more_indicator = '...' if len(entity['relationship_fields']) > 5 else ''
                    md_content += f"**Relationship Fields**: {len(entity['relationship_fields'])} ({rel_field_names}{more_indicator})\n\n"
                
                md_content += "**All Fields**:\n\n"
                
                for field in entity['fields']:
                    field_desc = ""
                    if field['is_required']:
                        field_desc += " (required)"
                    if field['is_list']:
                        field_desc += " (list)"
                    if field['is_connection']:
                        field_desc += " (connection)"
                    if field['is_enum']:
                        field_desc += " (enum)"
                    
                    md_content += f"- `{field['name']}`: `{field['type']}`{field_desc}"
                    if field['description']:
                        md_content += f" - {field['description']}"
                    md_content += "\n"
                
                md_content += "\n---\n"
        
        # Mutations analysis
        if analysis['mutations']['total_mutations'] > 0:
            md_content += f"\n## Mutations ({analysis['mutations']['total_mutations']} total)\n\n"
            
            for mutation in analysis['mutations']['mutations'][:20]:  # Show first 20 mutations
                md_content += f"\n### {mutation['name']}\n\n"
                if mutation['description']:
                    md_content += f"{mutation['description']}\n\n"
                
                md_content += f"**Returns**: `{mutation['return_type']}`\n\n"
                
                if mutation['arguments']:
                    md_content += "**Arguments**:\n\n"
                    for arg in mutation['arguments']:
                        md_content += f"- `{arg['name']}`: `{arg['type']}`"
                        if arg['description']:
                            md_content += f" - {arg['description']}"
                        md_content += "\n"
                md_content += "\n"
        
        # Type summary
        md_content += "\n## Schema Type Analysis\n\n"
        
        type_summary = analysis['types']
        md_content += f"- **Object Types**: {len(type_summary['objects'])} (business entities, API types)\n"
        md_content += f"- **Scalar Types**: {len(type_summary['scalars'])} (custom data types)\n"
        md_content += f"- **Enum Types**: {len(type_summary['enums'])} (predefined value sets)\n"
        md_content += f"- **Interface Types**: {len(type_summary['interfaces'])} (contracts)\n"
        md_content += f"- **Union Types**: {len(type_summary['unions'])} (polymorphic types)\n"
        md_content += f"- **Input Object Types**: {len(type_summary['input_objects'])} (mutation inputs)\n"
        
        # Relationships
        if analysis['relationships']['total_relationships'] > 0:
            md_content += f"\n## Entity Relationships\n\n"
            md_content += f"**Total Relationships Identified**: {analysis['relationships']['total_relationships']}\n\n"
            
            # Group relationships by type
            has_one_rels = [r for r in analysis['relationships']['relationships'] if r['relationship_type'] == 'has_one']
            has_many_rels = [r for r in analysis['relationships']['relationships'] if r['relationship_type'] == 'has_many']
            
            if has_one_rels:
                md_content += f"\n### Has-One Relationships ({len(has_one_rels)})\n\n"
                for rel in has_one_rels[:10]:
                    md_content += f"- `{rel['from_type']}` → `{rel['to_type']}` (via `{rel['field_name']}`)\n"
            
            if has_many_rels:
                md_content += f"\n### Has-Many Relationships ({len(has_many_rels)})\n\n"
                for rel in has_many_rels[:10]:
                    md_content += f"- `{rel['from_type']}` → `{rel['to_type']}` (via `{rel['field_name']}`)\n"
        
        # Migration recommendations
        md_content += f"\n## Migration Insights\n\n"
        md_content += "### High-Priority Entities for Migration\n\n"
        
        high_priority = [e for e in analysis['entities'] if e['total_score'] >= 5]
        md_content += f"**{len(high_priority)} entities** identified as high-priority for migration:\n\n"
        
        for entity in high_priority[:10]:
            md_content += f"- **{entity['name']}** ({entity['category']}) - Score: {entity['total_score']}, Fields: {entity['total_fields']}\n"
        
        md_content += "\n### Entity Categories Summary\n\n"
        for category, entities in sorted(entities_by_category.items()):
            total_fields = sum(e['total_fields'] for e in entities)
            avg_score = sum(e['total_score'] for e in entities) / len(entities) if entities else 0
            md_content += f"- **{category.title()}**: {len(entities)} entities, {total_fields} total fields, avg score: {avg_score:.1f}\n"
        
        # Save comprehensive markdown
        with open(f"{output_dir}/api_schema.md", "w") as f:
            f.write(md_content)
        
        # Also create a summary file
        summary_content = f"""# Sonar Schema Migration Summary

**Total Entities**: {len(analysis['entities'])}
**Total Queries**: {analysis['queries']['total_queries']}
**Total Mutations**: {analysis['mutations']['total_mutations']}

## Entity Categories:
"""
        for category, entities in sorted(entities_by_category.items()):
            summary_content += f"- {category.title()}: {len(entities)} entities\n"
        
        with open(f"{output_dir}/migration_summary.md", "w") as f:
            f.write(summary_content)


def main():
    """Main function to run schema analysis."""
    analyzer = SonarSchemaAnalyzer()
    
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
            logger.error("Failed to connect to Sonar API")
            return
        
        # Analyze schema
        analysis = analyzer.analyze_schema()
        
        # Save results
        analyzer.save_analysis(analysis)
        
        logger.info("Schema analysis completed successfully!")
        logger.info("Check docs/sonar/ for generated documentation")
        
    except Exception as e:
        logger.error(f"Schema analysis failed: {e}")
        raise

if __name__ == "__main__":
    main()
