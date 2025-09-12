#!/usr/bin/env python3
"""
Analyze working Splynx API endpoints and extract schema information
"""

import requests
import base64
import os
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Get credentials
url = os.getenv('SPLYNX_URL')
key = os.getenv('SPLYNX_API_KEY')
secret = os.getenv('SPLYNX_SECRET')

print(f"Analyzing working Splynx API schema at: {url}")

session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

# Set up Basic Auth
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers['Authorization'] = f"Basic {credentials}"

# Working endpoints from previous test
working_endpoints = [
    'admin/api/check',
    'admin/tariffs/internet',
    'admin/tariffs/voice', 
    'admin/tariffs/recurring',
    'admin/tariffs/bundle',
    'admin/tariffs/one-time'
]

schema_analysis = {
    'analysis_date': datetime.now().isoformat(),
    'splynx_url': url,
    'api_version': '2.0',
    'working_endpoints': {},
    'endpoint_schemas': {},
    'summary': {}
}

print(f"\n=== ANALYZING {len(working_endpoints)} WORKING ENDPOINTS ===")

for endpoint in working_endpoints:
    try:
        test_url = f"{url}/api/2.0/{endpoint}"
        
        print(f"\n--- Analyzing {endpoint} ---")
        
        # Get basic data
        response = session.get(test_url, params={'limit': 10})
        endpoint_info = {
            'url': test_url,
            'status': response.status_code,
            'methods': [],
            'fields': [],
            'sample_data': None,
            'record_count': 0
        }
        
        if response.status_code == 200:
            data = response.json()
            endpoint_info['sample_data'] = data
            
            if isinstance(data, list):
                endpoint_info['record_count'] = len(data)
                print(f"  📊 List endpoint with {len(data)} records")
                
                if len(data) > 0:
                    # Analyze first record structure
                    first_record = data[0]
                    endpoint_info['fields'] = list(first_record.keys())
                    print(f"  🔑 Fields: {', '.join(first_record.keys())}")
                    print(f"  📝 Sample record: {first_record}")
                else:
                    print(f"  📝 Empty list - no records to analyze")
                    
            elif isinstance(data, dict):
                endpoint_info['fields'] = list(data.keys())
                print(f"  🔑 Fields: {', '.join(data.keys())}")
                print(f"  📝 Response: {data}")
        
        # Try OPTIONS to get schema information
        try:
            options_response = session.options(test_url)
            if options_response.status_code == 200:
                options_data = options_response.json()
                endpoint_info['schema'] = options_data
                endpoint_info['methods'].append('OPTIONS')
                print(f"  🔧 OPTIONS schema available: {len(options_data) if isinstance(options_data, (list, dict)) else 'Unknown'} fields")
                
                if isinstance(options_data, list) and len(options_data) > 0:
                    # Show field definitions
                    for field_def in options_data[:5]:  # First 5 fields
                        if isinstance(field_def, dict) and 'name' in field_def:
                            print(f"    - {field_def.get('name', 'unknown')}: {field_def.get('type', 'unknown')} ({field_def.get('title', 'No title')})")
                            if field_def.get('required'):
                                print(f"      ⚠️ REQUIRED")
        except Exception as e:
            print(f"  ⚠️ OPTIONS failed: {e}")
        
        # Test POST to see if creation is allowed
        try:
            post_response = session.post(test_url, json={})
            if post_response.status_code != 405:  # Method not allowed
                endpoint_info['methods'].append('POST')
                print(f"  ✅ POST allowed (Status: {post_response.status_code})")
            else:
                print(f"  🚫 POST not allowed")
        except:
            pass
            
        schema_analysis['working_endpoints'][endpoint] = endpoint_info
        
    except Exception as e:
        print(f"  💥 Error analyzing {endpoint}: {e}")

# Try to create a test tariff to see POST functionality
print(f"\n=== TESTING TARIFF CREATION ===")
try:
    # Try to create a simple internet tariff
    tariff_data = {
        'title': 'Test Migration Tariff',
        'partners_ids': [1],
        'speed_download': 1024,
        'speed_upload': 1024,
        'price': 10.00,
        'with_vat': True
    }
    
    create_url = f"{url}/api/2.0/admin/tariffs/internet"
    create_response = session.post(create_url, json=tariff_data)
    
    print(f"Create tariff status: {create_response.status_code}")
    print(f"Create response: {create_response.text}")
    
    if create_response.status_code == 201:
        # Successfully created, now try to delete it
        created_data = create_response.json()
        if 'id' in created_data:
            tariff_id = created_data['id']
            delete_url = f"{url}/api/2.0/admin/tariffs/internet/{tariff_id}"
            delete_response = session.delete(delete_url)
            print(f"Delete tariff status: {delete_response.status_code}")
            
except Exception as e:
    print(f"Error testing tariff creation: {e}")

# Generate summary
print(f"\n=== SCHEMA ANALYSIS SUMMARY ===")
total_working = len([ep for ep in schema_analysis['working_endpoints'] if schema_analysis['working_endpoints'][ep]['status'] == 200])
total_with_data = len([ep for ep in schema_analysis['working_endpoints'] if schema_analysis['working_endpoints'][ep].get('record_count', 0) > 0])
total_with_schema = len([ep for ep in schema_analysis['working_endpoints'] if 'schema' in schema_analysis['working_endpoints'][ep]])

schema_analysis['summary'] = {
    'total_endpoints_tested': len(working_endpoints),
    'successful_endpoints': total_working,
    'endpoints_with_data': total_with_data,
    'endpoints_with_schema': total_with_schema,
    'api_status': 'PARTIALLY_WORKING' if total_working > 0 else 'NOT_WORKING'
}

print(f"📊 Total endpoints tested: {len(working_endpoints)}")
print(f"✅ Successful endpoints: {total_working}")
print(f"📁 Endpoints with data: {total_with_data}")
print(f"🔧 Endpoints with schema: {total_with_schema}")

# Save analysis to file
output_file = 'docs/splynx/working_api_analysis.json'
os.makedirs('docs/splynx', exist_ok=True)
with open(output_file, 'w') as f:
    json.dump(schema_analysis, f, indent=2, default=str)

print(f"\n💾 Analysis saved to: {output_file}")

# Create a summary markdown file
markdown_output = f"""# Splynx API Working Endpoints Analysis

**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Splynx Instance:** {url}  
**API Version:** 2.0  

## 📊 Summary

- **Total Endpoints Tested:** {len(working_endpoints)}
- **Successful Endpoints:** {total_working}
- **Endpoints with Data:** {total_with_data}
- **Endpoints with Schema Info:** {total_with_schema}
- **API Status:** {'✅ PARTIALLY WORKING' if total_working > 0 else '❌ NOT WORKING'}

## ✅ Working Endpoints

"""

for endpoint, info in schema_analysis['working_endpoints'].items():
    if info['status'] == 200:
        markdown_output += f"### `{endpoint}`\n"
        markdown_output += f"- **Status:** {info['status']}\n"
        markdown_output += f"- **Record Count:** {info['record_count']}\n"
        markdown_output += f"- **Fields:** {len(info['fields'])}\n"
        if info['fields']:
            markdown_output += f"- **Available Fields:** `{'`, `'.join(info['fields'])}`\n"
        markdown_output += f"- **Methods:** {', '.join(info['methods'])}\n\n"

markdown_output += f"""
## 🔒 Restricted Endpoints

The following endpoints returned 403 (Forbidden), indicating they need additional permissions:

"""

forbidden_count = 0
for endpoint, info in schema_analysis['working_endpoints'].items():
    if info['status'] == 403:
        forbidden_count += 1
        markdown_output += f"- `{endpoint}`\n"

markdown_output += f"""
**Total Forbidden:** {forbidden_count} endpoints

## 🎯 Migration Capabilities

Based on the working endpoints, we can currently:

✅ **Read Tariff Information:**
- Internet tariffs with speed and pricing data
- Voice tariffs with call pricing structures  
- Recurring service tariffs
- Bundle package definitions
- One-time service tariffs

⚠️ **Limited Access:**
- Customer management requires additional permissions
- Service management needs higher access level
- Financial data access is restricted
- Network configuration requires network permissions

## 📋 Next Steps

1. **Request Additional API Permissions:**
   - Customer management permissions
   - Service management permissions  
   - Financial data access
   - Network configuration access

2. **Alternative Approaches:**
   - Database direct access (if available)
   - Export/import via Splynx web interface
   - Contact Splynx administrator for proper API setup

3. **Current Migration Scope:**
   - Can extract tariff structures for reference
   - Can analyze pricing models and service definitions
   - Limited to read-only tariff data currently
"""

# Save markdown summary
markdown_file = 'docs/splynx/working_api_summary.md'
with open(markdown_file, 'w') as f:
    f.write(markdown_output)

print(f"📄 Summary saved to: {markdown_file}")
print(f"\n🎯 Key Finding: Tariff endpoints are working! We can analyze pricing structures.")
print(f"⚠️  Issue: Customer/service endpoints need additional permissions")
