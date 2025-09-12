#!/usr/bin/env python3
"""
Test Splynx API with different endpoints to find working permissions
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

print(f"Testing Splynx API permissions at: {url}")

session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

# Set up Basic Auth
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers['Authorization'] = f"Basic {credentials}"

# Test different endpoints with different permission levels
test_endpoints = [
    # System/General endpoints (usually lower permissions)
    'admin/administration/config',
    'admin/administration/locations', 
    'admin/administration/roles',
    
    # Customer related (might need customer permissions)
    'admin/customers/customer',
    'admin/customers/location',
    'admin/customers/contact',
    
    # Services (might need service permissions)  
    'admin/services/internet',
    'admin/services/voice',
    'admin/tariff-plans/internet',
    
    # Billing (might need billing permissions)
    'admin/billing/invoices',
    'admin/billing/payments',
    
    # Network (might need network permissions)
    'admin/networking/routers',
    'admin/networking/ip-pools',
    
    # Tickets (might need support permissions)
    'admin/tickets/tickets',
    
    # Reports (usually read-only, lower permissions)
    'admin/reports/customers',
    'admin/reports/financial',
    
    # RADIUS (network permissions)
    'admin/radius/accounts',
    
    # Try some simpler endpoints
    'admin/customers',  # Maybe without the subpath
    'admin/administration',
    'admin/billing',
    'admin/services',
]

successful_endpoints = []
failed_endpoints = []

print(f"\nTesting {len(test_endpoints)} endpoints with Basic Auth...")

for endpoint in test_endpoints:
    try:
        test_url = f"{url}/api/2.0/{endpoint}"
        response = session.get(test_url, params={'limit': 1})
        
        print(f"{endpoint:<35} | Status: {response.status_code}")
        
        if response.status_code == 200:
            successful_endpoints.append(endpoint)
            print(f"  SUCCESS! Response preview: {response.text[:100]}...")
        elif response.status_code == 403:
            failed_endpoints.append((endpoint, "FORBIDDEN - No permission"))
        elif response.status_code == 401:
            failed_endpoints.append((endpoint, "UNAUTHORIZED - Auth failed"))
        elif response.status_code == 404:
            failed_endpoints.append((endpoint, "NOT FOUND - Endpoint doesn't exist"))
        elif response.status_code == 405:
            # Method not allowed might mean endpoint exists but needs different method
            print(f"  Endpoint exists but needs different HTTP method")
            # Try POST
            post_response = session.post(test_url, json={})
            if post_response.status_code != 405:
                print(f"  POST Status: {post_response.status_code}")
        else:
            failed_endpoints.append((endpoint, f"OTHER - Status {response.status_code}"))
            print(f"  Response: {response.text[:100]}...")
            
    except Exception as e:
        failed_endpoints.append((endpoint, f"ERROR - {e}"))
        print(f"  Error: {e}")

print(f"\n=== SUMMARY ===")
print(f"Successful endpoints: {len(successful_endpoints)}")
for endpoint in successful_endpoints:
    print(f"  ✅ {endpoint}")

print(f"\nFailed endpoints: {len(failed_endpoints)}")
for endpoint, reason in failed_endpoints[:10]:  # Show first 10
    print(f"  ❌ {endpoint}: {reason}")

if len(failed_endpoints) > 10:
    print(f"  ... and {len(failed_endpoints) - 10} more")

# If we found successful endpoints, try to get more detailed schema
if successful_endpoints:
    print(f"\n=== DETAILED ANALYSIS OF SUCCESSFUL ENDPOINTS ===")
    for endpoint in successful_endpoints[:3]:  # Analyze first 3 successful
        try:
            test_url = f"{url}/api/2.0/{endpoint}"
            response = session.get(test_url, params={'limit': 5})  # Get more records
            data = response.json()
            
            print(f"\n--- {endpoint} ---")
            print(f"Response type: {type(data)}")
            
            if isinstance(data, list) and len(data) > 0:
                print(f"Records returned: {len(data)}")
                print(f"Sample record fields: {list(data[0].keys())}")
                print(f"Sample record: {data[0]}")
                
            elif isinstance(data, dict):
                print(f"Response keys: {list(data.keys())}")
                if 'data' in data:
                    print(f"Data type: {type(data['data'])}")
                    if isinstance(data['data'], list) and len(data['data']) > 0:
                        print(f"Records in data: {len(data['data'])}")
                        print(f"Sample record fields: {list(data['data'][0].keys())}")
                        print(f"Sample record: {data['data'][0]}")
                print(f"Full response: {data}")
                
        except Exception as e:
            print(f"Error analyzing {endpoint}: {e}")

print(f"\n=== Tests complete ===")
