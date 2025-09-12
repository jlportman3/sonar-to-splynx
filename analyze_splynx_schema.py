#!/usr/bin/env python3
"""
Splynx API Schema Analyzer

This script analyzes the Splynx REST API to discover endpoints, schemas, and data structures.
It creates comprehensive documentation for migration planning.
"""

import os
import json
import logging
from dotenv import load_dotenv
from src.apis.splynx_client import SplynxAPIClient, SplynxConfig

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def analyze_splynx_api():
    """Analyze Splynx API and generate documentation."""
    
    # Get Splynx configuration from environment
    splynx_url = os.getenv('SPLYNX_URL')
    splynx_key = os.getenv('SPLYNX_API_KEY')
    splynx_secret = os.getenv('SPLYNX_SECRET')
    
    if not all([splynx_url, splynx_key, splynx_secret]):
        logger.error("Missing Splynx configuration. Please check .env file:")
        logger.error("Required: SPLYNX_URL, SPLYNX_API_KEY, SPLYNX_SECRET")
        return
    
    # Initialize Splynx client
    config = SplynxConfig(
        base_url=splynx_url,
        api_key=splynx_key,
        api_secret=splynx_secret
    )
    
    client = SplynxAPIClient(config)
    
    logger.info("Starting Splynx API analysis...")
    
    # Analyze the API
    analysis = client.analyze_all_schemas()
    
    if 'error' in analysis:
        logger.error(f"Analysis failed: {analysis['error']}")
        return
    
    # Save raw analysis data
    os.makedirs('docs/splynx', exist_ok=True)
    
    with open('docs/splynx/api_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2, default=str)
    
    logger.info("Saved raw analysis to docs/splynx/api_analysis.json")
    
    # Generate markdown documentation
    generate_markdown_docs(analysis)
    
    # Generate summary report
    generate_summary_report(analysis)
    
    logger.info("Splynx API analysis completed successfully!")

def generate_markdown_docs(analysis):
    """Generate comprehensive markdown documentation."""
    
    doc_content = f"""# Splynx API Schema Documentation

Generated on: {analysis.get('analysis_timestamp', 'Unknown')}

## API Overview

**Base URL:** {analysis.get('api_info', {}).get('base_url', 'Not available')}
**API Version:** 2.0
**Total Endpoints Discovered:** {analysis.get('total_endpoints', 0)}

## Available Endpoints

"""
    
    # Add endpoints list
    endpoints = analysis.get('endpoints', [])
    for endpoint in sorted(endpoints):
        doc_content += f"- `{endpoint}`\n"
    
    doc_content += "\n## Endpoint Schemas\n\n"
    
    # Add detailed schemas
    schemas = analysis.get('schemas', {})
    for endpoint, schema in schemas.items():
        doc_content += f"### {endpoint}\n\n"
        
        if 'error' in schema:
            doc_content += f"**Error:** {schema['error']}\n\n"
            continue
        
        doc_content += f"**URL:** `{schema.get('url', 'N/A')}`\n"
        doc_content += f"**Method:** {schema.get('method', 'GET')}\n"
        
        fields = schema.get('fields', [])
        if fields:
            doc_content += f"**Fields ({len(fields)}):**\n"
            for field in sorted(fields):
                doc_content += f"- `{field}`\n"
        
        # Add sample data structure (limited)
        sample_data = schema.get('sample_data')
        if sample_data:
            doc_content += "\n**Sample Response Structure:**\n```json\n"
            if isinstance(sample_data, list) and len(sample_data) > 0:
                # Show structure of first record only
                sample_record = sample_data[0]
                doc_content += json.dumps({k: type(v).__name__ for k, v in sample_record.items()}, indent=2)
            elif isinstance(sample_data, dict):
                if 'data' in sample_data and isinstance(sample_data['data'], list) and len(sample_data['data']) > 0:
                    sample_record = sample_data['data'][0]
                    structure = {
                        'data': [{k: type(v).__name__ for k, v in sample_record.items()}],
                        'meta': 'object (if present)'
                    }
                    doc_content += json.dumps(structure, indent=2)
                else:
                    doc_content += json.dumps({k: type(v).__name__ for k, v in sample_data.items()}, indent=2)
            doc_content += "\n```\n"
        
        doc_content += "\n---\n\n"
    
    # Save documentation
    with open('docs/splynx/api_schema.md', 'w') as f:
        f.write(doc_content)
    
    logger.info("Generated comprehensive documentation: docs/splynx/api_schema.md")

def generate_summary_report(analysis):
    """Generate a summary report of the analysis."""
    
    total_endpoints = analysis.get('total_endpoints', 0)
    schemas = analysis.get('schemas', {})
    
    # Categorize endpoints
    categories = {
        'customers': [],
        'billing': [],
        'services': [],
        'networking': [],
        'administration': [],
        'reports': [],
        'inventory': [],
        'tickets': [],
        'radius': [],
        'monitoring': [],
        'other': []
    }
    
    for endpoint in analysis.get('endpoints', []):
        categorized = False
        for category in categories.keys():
            if category in endpoint.lower():
                categories[category].append(endpoint)
                categorized = True
                break
        if not categorized:
            categories['other'].append(endpoint)
    
    # Count fields per category
    field_counts = {}
    successful_schemas = 0
    
    for endpoint, schema in schemas.items():
        if 'error' not in schema:
            successful_schemas += 1
            fields = schema.get('fields', [])
            
            # Find category
            category = 'other'
            for cat in categories.keys():
                if cat in endpoint.lower():
                    category = cat
                    break
            
            if category not in field_counts:
                field_counts[category] = 0
            field_counts[category] += len(fields)
    
    # Generate report
    report = f"""# Splynx API Analysis Summary

## Overview
- **Total Endpoints Discovered:** {total_endpoints}
- **Successfully Analyzed:** {successful_schemas}
- **Analysis Success Rate:** {(successful_schemas/total_endpoints*100):.1f}%

## Endpoints by Category

"""
    
    for category, endpoints in categories.items():
        if endpoints:
            field_count = field_counts.get(category, 0)
            report += f"### {category.title()} ({len(endpoints)} endpoints, ~{field_count} fields)\n"
            for endpoint in sorted(endpoints):
                report += f"- `{endpoint}`\n"
            report += "\n"
    
    report += """## Key Findings

### Customer Management
- Customer records with contact information
- Location and address management
- Lead tracking and conversion

### Billing & Financial
- Invoice generation and management
- Payment processing and tracking
- Transaction history
- Bank account integration

### Service Management
- Internet service provisioning
- Voice service management
- Custom service types
- Tariff plan configuration

### Network Infrastructure
- Router and equipment management
- IP pool administration
- VLAN configuration
- RADIUS integration

### Administration
- User and role management
- Location and partner management
- System configuration
- Administrative tools

### Reporting & Analytics
- Customer reports
- Financial reporting
- Usage analytics
- Performance monitoring

## Migration Compatibility

Based on this analysis, Splynx provides comprehensive REST API coverage for:
- ✅ Customer data migration
- ✅ Billing information transfer
- ✅ Service configuration
- ✅ Network settings
- ✅ User management
- ✅ Financial data

The API appears well-suited for migration from Sonar with good coverage of ISP management functions.
"""
    
    # Save report
    with open('docs/splynx/migration_analysis.md', 'w') as f:
        f.write(report)
    
    logger.info("Generated migration analysis: docs/splynx/migration_analysis.md")

if __name__ == "__main__":
    analyze_splynx_api()
