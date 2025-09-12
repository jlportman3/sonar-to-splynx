#!/usr/bin/env python3
"""
Discover actual Splynx API endpoint structure
"""

import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# Get credentials
url = os.getenv('SPLYNX_URL')
key = os.getenv('SPLYNX_API_KEY')
secret = os.getenv('SPLYNX_SECRET')

print(f"Discovering Splynx API structure at: {url}")

session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

# Set up Basic Auth
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers['Authorization'] = f"Basic {credentials}"

# Try to discover the base API structure
print("\n=== API Discovery ===")

# Test base API endpoints
base_tests = [
    'api/2.0',
    'api/2.0/',
    'api/2.0/admin',
    'api/2.0/admin/',
    'api/2.0/customer',
    'api/2.0/reseller',
]

for base_test in base_tests:
    try:
        test_url = f"{url}/{base_test}"
        response = session.get(test_url)
        print(f"{base_test:<20} | Status: {response.status_code}")
        if response.status_code not in [401, 500]:
            print(f"  Response: {response.text[:200]}...")
    except Exception as e:
        print(f"  Error: {e}")

# Try some different endpoint structures
print("\n=== Testing Different Endpoint Structures ===")

endpoint_variants = [
    # Different admin paths
    'admin/customers',
    'admin/customer',
    'admin/billing',
    'admin/services',
    'admin/tariffs',
    'admin/tariff',
    'admin/locations',
    'admin/location',
    'admin/administrators',
    'admin/administrator',
    'admin/roles',
    'admin/role',
    
    # Try without admin prefix
    'customers',
    'customer',
    'billing',
    'services',
    'tariffs',
    'invoices',
    'payments',
    
    # Try customer portal endpoints
    'customer/info',
    'customer/services',
    'customer/billing',
    
    # Try different API versions
    '../1.0/admin/customers',
    '../1.0/customers',
]

successful_endpoints = []
permission_denied = []
not_found = []

for endpoint in endpoint_variants:
    try:
        test_url = f"{url}/api/2.0/{endpoint}"
        response = session.get(test_url, params={'limit': 1})
        
        status_symbol = "❓"
        if response.status_code == 200:
            status_symbol = "✅"
            successful_endpoints.append(endpoint)
        elif response.status_code == 403:
            status_symbol = "🔒"
            permission_denied.append(endpoint)
        elif response.status_code == 404:
            status_symbol = "❌"
            not_found.append(endpoint)
        
        print(f"{status_symbol} {endpoint:<30} | {response.status_code}")
        
        if response.status_code == 200:
            print(f"  SUCCESS! Response: {response.text[:150]}...")
        elif response.status_code not in [403, 404, 401, 500]:
            print(f"  Interesting response: {response.text[:100]}...")
            
    except Exception as e:
        print(f"❌ {endpoint:<30} | Error: {e}")

print(f"\n=== DISCOVERY RESULTS ===")
print(f"✅ Successful (200): {len(successful_endpoints)}")
for endpoint in successful_endpoints:
    print(f"   {endpoint}")

print(f"\n🔒 Permission Denied (403): {len(permission_denied)}")
for endpoint in permission_denied[:5]:  # Show first 5
    print(f"   {endpoint}")
if len(permission_denied) > 5:
    print(f"   ... and {len(permission_denied) - 5} more")

print(f"\n❌ Not Found (404): {len(not_found)}")
for endpoint in not_found[:5]:  # Show first 5
    print(f"   {endpoint}")
if len(not_found) > 5:
    print(f"   ... and {len(not_found) - 5} more")

# Try to get API documentation or help
print(f"\n=== API Documentation Discovery ===")
doc_endpoints = [
    'help',
    'docs',
    'documentation',
    'schema',
    'endpoints',
    'admin/help',
    'admin/docs',
    'admin/api',
    'info',
    'version',
    'status',
]

for doc_endpoint in doc_endpoints:
    try:
        test_url = f"{url}/api/2.0/{doc_endpoint}"
        response = session.get(test_url)
        print(f"{doc_endpoint:<20} | Status: {response.status_code}")
        if response.status_code == 200:
            print(f"  Documentation found: {response.text[:200]}...")
    except Exception as e:
        print(f"  Error: {e}")

# If we have working endpoints, analyze them
if successful_endpoints:
    print(f"\n=== ANALYZING SUCCESSFUL ENDPOINTS ===")
    for endpoint in successful_endpoints:
        try:
            test_url = f"{url}/api/2.0/{endpoint}"
            
            # Try different approaches to get more data
            for params in [{'limit': 10}, {}, {'page': 1}, {'per_page': 5}]:
                response = session.get(test_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    print(f"\n--- {endpoint} (params: {params}) ---")
                    print(f"Response type: {type(data)}")
                    print(f"Response: {data}")
                    break
                    
        except Exception as e:
            print(f"Error analyzing {endpoint}: {e}")

print(f"\n=== Discovery complete ===")
