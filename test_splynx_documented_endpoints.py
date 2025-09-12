#!/usr/bin/env python3
"""
Test Splynx API using exact endpoints from documentation
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

print(f"Testing documented Splynx API endpoints at: {url}")

session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

# Set up Basic Auth
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers['Authorization'] = f"Basic {credentials}"

# Test endpoints exactly as documented
documented_endpoints = [
    # Authentication and tokens
    'admin/auth/tokens',
    'admin/api/check',
    
    # Administration (from docs)
    'admin/administration/locations',
    'admin/administration/administrators', 
    'admin/administration/partners',
    
    # Customers (from docs)
    'admin/customers/customer',
    'admin/customers/customer-info/1',
    'admin/customers/customer-billing/1',
    'admin/customers/customer-statistics',
    
    # Tariffs (from docs) 
    'admin/tariffs/internet',
    'admin/tariffs/voice',
    'admin/tariffs/recurring',
    'admin/tariffs/bundle',
    'admin/tariffs/one-time',
    
    # Services (from docs)
    'admin/customers/customer/1/internet-services',
    'admin/customers/customer/1/voice-services',
    'admin/customers/customer/1/recurring-services',
    
    # Finance (from docs)
    'admin/finance/transactions',
    'admin/finance/invoices',
    'admin/finance/payments',
    'admin/finance/payment-methods',
    'admin/finance/transaction-categories',
    
    # Networking (from docs)
    'admin/networking/routers',
    'admin/networking/routers-sectors',
    'admin/networking/voice-devices',
    'admin/networking/ipv4',
    'admin/networking/ipv6',
    'admin/networking/monitoring',
    
    # Support (from docs)
    'admin/support/tickets',
    'admin/support/ticket-messages',
    'admin/support/tickets-statuses',
    
    # Dashboard
    'admin/dashboard/dashboard',
    'portal/dashboard/dashboard',
    
    # Config
    'admin/config/additional-fields/customers',
    'admin/config/company-info',
    'admin/config/config?module=main&path=portal',
]

successful_endpoints = []
forbidden_endpoints = []
not_found_endpoints = []
server_error_endpoints = []
other_endpoints = []

print(f"\nTesting {len(documented_endpoints)} documented endpoints...")

for endpoint in documented_endpoints:
    try:
        test_url = f"{url}/api/2.0/{endpoint}"
        response = session.get(test_url, params={'limit': 1})
        
        status_symbol = "❓"
        if response.status_code == 200:
            status_symbol = "✅"
            successful_endpoints.append(endpoint)
        elif response.status_code == 403:
            status_symbol = "🔒"
            forbidden_endpoints.append(endpoint)
        elif response.status_code == 404:
            status_symbol = "❌"
            not_found_endpoints.append(endpoint)
        elif response.status_code == 500:
            status_symbol = "💥"
            server_error_endpoints.append(endpoint)
        else:
            status_symbol = "❓"
            other_endpoints.append((endpoint, response.status_code))
        
        print(f"{status_symbol} {endpoint:<45} | {response.status_code}")
        
        if response.status_code == 200:
            print(f"  ✅ SUCCESS! Response: {response.text[:100]}...")
        elif response.status_code == 401:
            print(f"  🔑 AUTH FAILED: {response.text[:100]}...")
        elif response.status_code not in [403, 404, 500]:
            print(f"  ❓ UNEXPECTED: {response.text[:100]}...")
            
    except Exception as e:
        print(f"💥 {endpoint:<45} | ERROR: {e}")

print(f"\n=== DETAILED RESULTS ===")
print(f"✅ Successful (200): {len(successful_endpoints)}")
for endpoint in successful_endpoints:
    print(f"   {endpoint}")

print(f"\n🔒 Forbidden (403): {len(forbidden_endpoints)}")
for endpoint in forbidden_endpoints:
    print(f"   {endpoint}")

print(f"\n❌ Not Found (404): {len(not_found_endpoints)}")
for endpoint in not_found_endpoints[:10]:
    print(f"   {endpoint}")
if len(not_found_endpoints) > 10:
    print(f"   ... and {len(not_found_endpoints) - 10} more")

print(f"\n💥 Server Error (500): {len(server_error_endpoints)}")
for endpoint in server_error_endpoints:
    print(f"   {endpoint}")

print(f"\n❓ Other Status: {len(other_endpoints)}")
for endpoint, status in other_endpoints:
    print(f"   {endpoint}: {status}")

# If any endpoints work, get detailed schema info
if successful_endpoints:
    print(f"\n=== ANALYZING SUCCESSFUL ENDPOINTS ===")
    for endpoint in successful_endpoints[:3]:  # First 3 successful
        try:
            test_url = f"{url}/api/2.0/{endpoint}"
            
            # Try to get more detailed information
            response = session.get(test_url, params={'limit': 5})
            if response.status_code == 200:
                data = response.json()
                print(f"\n--- {endpoint} ---")
                print(f"Response type: {type(data)}")
                
                if isinstance(data, list):
                    print(f"Array with {len(data)} items")
                    if len(data) > 0:
                        print(f"First item keys: {list(data[0].keys())}")
                        print(f"Sample: {data[0]}")
                elif isinstance(data, dict):
                    print(f"Object keys: {list(data.keys())}")
                    print(f"Full response: {data}")
                
                # Try OPTIONS to get field info
                options_response = session.options(test_url)
                if options_response.status_code == 200:
                    print(f"OPTIONS available - schema info may be available")
                    
        except Exception as e:
            print(f"Error analyzing {endpoint}: {e}")

print(f"\n=== API Test Complete ===")
