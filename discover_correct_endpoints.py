#!/usr/bin/env python3
"""
Intelligent Splynx API Endpoint Discovery
Try to find the correct paths for endpoints that returned 404
"""

import requests
import base64
import os
import json
from dotenv import load_dotenv
from datetime import datetime
import time

load_dotenv()

# Get credentials
url = os.getenv('SPLYNX_URL')
key = os.getenv('SPLYNX_API_KEY')
secret = os.getenv('SPLYNX_SECRET')

session = requests.Session()
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers.update({
    'Authorization': f'Basic {credentials}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

print(f"🔍 INTELLIGENT Splynx API Endpoint Discovery")
print(f"URL: {url}")
print(f"Analysis started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def test_endpoint_variations(base_endpoint):
    """Test different variations of an endpoint path"""
    variations = []
    
    # Original
    variations.append(base_endpoint)
    
    # Without admin prefix
    if base_endpoint.startswith('admin/'):
        variations.append(base_endpoint[6:])
    
    # With v1/v2 prefixes
    variations.append(f"v1/{base_endpoint}")
    variations.append(f"v2/{base_endpoint}")
    
    # Plural/singular variations
    if base_endpoint.endswith('s'):
        variations.append(base_endpoint[:-1])  # Remove 's'
    else:
        variations.append(f"{base_endpoint}s")  # Add 's'
    
    # Replace dashes with underscores
    if '-' in base_endpoint:
        variations.append(base_endpoint.replace('-', '_'))
    
    # Replace underscores with dashes  
    if '_' in base_endpoint:
        variations.append(base_endpoint.replace('_', '-'))
    
    # Different common path patterns
    parts = base_endpoint.split('/')
    if len(parts) >= 3:
        # Try different ordering
        variations.append(f"{parts[0]}/{parts[2]}/{parts[1]}")
        
        # Try without middle part
        variations.append(f"{parts[0]}/{parts[2]}")
        
        # Try with different patterns
        if parts[1] == 'customers':
            variations.append(f"{parts[0]}/customer/{parts[2]}")
            variations.append(f"{parts[0]}/customer-{parts[2]}")
        
        if parts[1] == 'services':
            variations.append(f"{parts[0]}/service/{parts[2]}")
            variations.append(f"{parts[0]}/customer-services/{parts[2]}")
    
    return list(set(variations))  # Remove duplicates

def discover_endpoint(endpoint_name, expected_functionality):
    """Try to discover the correct path for a given endpoint"""
    print(f"\n🔍 Discovering: {endpoint_name} ({expected_functionality})")
    
    variations = test_endpoint_variations(endpoint_name)
    found_endpoints = []
    
    for variation in variations:
        try:
            test_url = f"{url}/api/2.0/{variation}"
            response = session.get(test_url, params={'limit': 1})
            
            if response.status_code == 200:
                print(f"  ✅ FOUND: {variation} (Status: 200)")
                found_endpoints.append({
                    'endpoint': variation,
                    'status': 200,
                    'url': test_url
                })
                
                # Get sample data
                try:
                    data = response.json()
                    if isinstance(data, list):
                        print(f"    📊 Records: {len(data)}")
                        if len(data) > 0:
                            print(f"    🔑 Fields: {', '.join(data[0].keys()[:5])}...")
                    elif isinstance(data, dict):
                        print(f"    🔑 Response keys: {', '.join(data.keys())}")
                except:
                    pass
                    
            elif response.status_code in [403, 405]:
                print(f"  ⚠️ EXISTS but restricted: {variation} (Status: {response.status_code})")
                found_endpoints.append({
                    'endpoint': variation,
                    'status': response.status_code,
                    'url': test_url,
                    'note': 'Exists but restricted/not allowed'
                })
            
            time.sleep(0.1)  # Rate limiting
            
        except Exception as e:
            continue
    
    if not found_endpoints:
        print(f"  ❌ No working variations found for {endpoint_name}")
    
    return found_endpoints

# Endpoints that returned 404 in our analysis
unfound_endpoints = {
    'admin/customers/location': 'Customer location management',
    'admin/customers/contact': 'Customer contact information',
    'admin/customers/lead': 'Lead management',
    'admin/services/internet': 'Internet service management',
    'admin/services/voice': 'Voice service management', 
    'admin/services/custom': 'Custom service management',
    'admin/services/ipv4': 'IPv4 service management',
    'admin/services/ipv6': 'IPv6 service management',
    'admin/finance/bank-accounts': 'Bank account management',
    'admin/administration/roles': 'Role management',
    'admin/administration/config': 'Configuration management',
    'admin/administration/main': 'Main administration',
    'admin/networking/nas-types': 'NAS type management',
    'admin/networking/vlans': 'VLAN management',
    'admin/networking/ip-pools': 'IP pool management',
    'admin/support/canned-responses': 'Canned response management',
    'admin/inventory/categories': 'Inventory category management',
    'admin/crm/tasks': 'CRM task management',
    'admin/crm/deals': 'CRM deal management',
    'admin/crm/pipeline': 'CRM pipeline management',
    'admin/reports/customers': 'Customer reports',
    'admin/reports/financial': 'Financial reports',
    'admin/reports/custom': 'Custom reports',
    'admin/dashboard/widgets': 'Dashboard widgets',
    'admin/radius/accounts': 'RADIUS account management',
    'admin/radius/sessions': 'RADIUS session management',
    'admin/radius/nas': 'RADIUS NAS management',
    'admin/radius/settings': 'RADIUS settings',
    'admin/monitoring/maps': 'Network monitoring maps',
    'admin/monitoring/ping': 'Ping monitoring',
    'admin/monitoring/traceroute': 'Traceroute monitoring'
}

discovered_endpoints = {}

print(f"\n=== DISCOVERING {len(unfound_endpoints)} UNFOUND ENDPOINTS ===")

for endpoint, description in unfound_endpoints.items():
    found = discover_endpoint(endpoint, description)
    if found:
        discovered_endpoints[endpoint] = found

# Try some additional systematic discovery patterns
print(f"\n=== SYSTEMATIC ENDPOINT PATTERN DISCOVERY ===")

# Test common Splynx patterns based on working endpoints
base_patterns = [
    'admin/customers',
    'admin/tariffs', 
    'admin/finance',
    'admin/administration',
    'admin/networking',
    'admin/support',
    'admin/inventory',
    'admin/radius',
    'admin/monitoring',
    'admin/reports',
    'admin/dashboard',
    'admin/crm'
]

# Test if these base patterns give us directory listings or other info
for pattern in base_patterns:
    try:
        response = session.get(f"{url}/api/2.0/{pattern}")
        if response.status_code in [200, 403]:
            print(f"✅ Base pattern exists: {pattern} (Status: {response.status_code})")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"  📋 Response: {data}")
                except:
                    print(f"  📋 Response: {response.text[:100]}")
                    
    except:
        continue

# Try to get API documentation or endpoint listing
print(f"\n=== LOOKING FOR API DOCUMENTATION ENDPOINTS ===")

doc_endpoints = [
    'admin/api',
    'admin/api/docs',
    'admin/api/endpoints',
    'admin/api/routes',
    'admin/help',
    'admin/documentation',
    'api/documentation',
    'api/help',
    'docs',
    'help',
    'api'
]

for doc_endpoint in doc_endpoints:
    try:
        response = session.get(f"{url}/api/2.0/{doc_endpoint}")
        if response.status_code == 200:
            print(f"✅ Documentation endpoint found: {doc_endpoint}")
            try:
                data = response.json()
                print(f"  📋 Contains: {type(data)} with {len(data) if isinstance(data, (list, dict)) else 'unknown'} items")
                if isinstance(data, dict) and 'endpoints' in data:
                    print(f"  🎯 Endpoint list found!")
                elif isinstance(data, list) and len(data) > 0:
                    print(f"  📝 Sample item: {data[0]}")
            except:
                print(f"  📄 HTML/Text response: {response.text[:100]}")
    except:
        continue

# Test alternative service endpoint patterns
print(f"\n=== TESTING ALTERNATIVE SERVICE PATTERNS ===")

service_patterns = [
    'admin/customer-services/internet',
    'admin/customer-services/voice',
    'admin/customer-services/custom',
    'admin/customer/services/internet', 
    'admin/customer/services/voice',
    'admin/customer/services/custom',
    'admin/customers/services',
    'admin/customers/internet-services',
    'admin/customers/voice-services',
    'admin/customers/custom-services',
    'admin/internet-services',
    'admin/voice-services',
    'admin/custom-services'
]

working_service_endpoints = []

for pattern in service_patterns:
    try:
        response = session.get(f"{url}/api/2.0/{pattern}", params={'limit': 1})
        if response.status_code in [200, 403]:
            status_emoji = "✅" if response.status_code == 200 else "🔒"
            print(f"{status_emoji} {pattern}: {response.status_code}")
            
            if response.status_code == 200:
                working_service_endpoints.append(pattern)
                try:
                    data = response.json()
                    if isinstance(data, list):
                        print(f"  📊 Records: {len(data)}")
                        if len(data) > 0:
                            print(f"  🔑 Fields: {', '.join(data[0].keys()[:5])}...")
                except:
                    pass
                    
    except:
        continue

# Save discovered endpoints
discovery_results = {
    'analysis_date': datetime.now().isoformat(),
    'original_unfound_count': len(unfound_endpoints),
    'discovered_alternatives': discovered_endpoints,
    'working_service_patterns': working_service_endpoints,
    'total_discovered': len(discovered_endpoints) + len(working_service_endpoints),
    'notes': 'Systematic discovery of alternative endpoint paths'
}

# Save results
output_file = 'docs/splynx/endpoint_discovery_results.json'
with open(output_file, 'w') as f:
    json.dump(discovery_results, f, indent=2, default=str)

print(f"\n📊 DISCOVERY SUMMARY:")
print(f"🔍 Original unfound endpoints: {len(unfound_endpoints)}")
print(f"✅ Alternative paths discovered: {len(discovered_endpoints)}")
print(f"🛠️ Service patterns found: {len(working_service_endpoints)}")
print(f"💾 Results saved to: {output_file}")

if working_service_endpoints:
    print(f"\n🎉 FOUND WORKING SERVICE ENDPOINTS:")
    for service_ep in working_service_endpoints:
        print(f"  ✅ {service_ep}")

if discovered_endpoints:
    print(f"\n🎯 ALTERNATIVE PATHS DISCOVERED:")
    for original, alternatives in discovered_endpoints.items():
        print(f"  🔄 {original}:")
        for alt in alternatives:
            print(f"    → {alt['endpoint']} (Status: {alt['status']})")

print(f"\n🏁 Endpoint discovery complete!")
