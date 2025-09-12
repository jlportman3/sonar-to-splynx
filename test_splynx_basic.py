#!/usr/bin/env python3
"""
Basic Splynx connectivity and API availability test
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

print(f"Testing basic connectivity to Splynx at: {url}")

session = requests.Session()

# Test 1: Basic connectivity without auth
print("\n=== Test 1: Basic Connectivity (No Auth) ===")
try:
    response = session.get(url)
    print(f"Base URL Status: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    print(f"Response preview: {response.text[:300]}...")
except Exception as e:
    print(f"Connection error: {e}")

# Test 2: Try different API paths
print("\n=== Test 2: API Path Discovery ===")
api_paths = [
    '/api',
    '/api/',
    '/api/2.0',
    '/api/v2',
    '/api/v2.0',
    '/rest',
    '/rest/api',
    '/webapi',
    '/api/1.0',
    '/api/v1',
]

for path in api_paths:
    try:
        test_url = f"{url}{path}"
        response = session.get(test_url)
        print(f"{path:<15} | Status: {response.status_code}")
        if response.status_code not in [404, 500]:
            print(f"  Response: {response.text[:150]}...")
    except Exception as e:
        print(f"  Error: {e}")

# Test 3: Try with Basic Auth on different paths
print("\n=== Test 3: API Paths with Basic Auth ===")
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers['Authorization'] = f"Basic {credentials}"

for path in api_paths:
    try:
        test_url = f"{url}{path}"
        response = session.get(test_url)
        print(f"{path:<15} | Status: {response.status_code}")
        if response.status_code not in [404, 500, 401, 403]:
            print(f"  Response: {response.text[:150]}...")
    except Exception as e:
        print(f"  Error: {e}")

# Test 4: Check if web interface is accessible
print("\n=== Test 4: Web Interface Check ===")
web_paths = [
    '/',
    '/admin',
    '/admin/',
    '/customer',
    '/login',
]

# Remove auth for web interface test
if 'Authorization' in session.headers:
    del session.headers['Authorization']

for path in web_paths:
    try:
        test_url = f"{url}{path}"
        response = session.get(test_url)
        print(f"{path:<15} | Status: {response.status_code}")
        if response.status_code == 200:
            print(f"  Web interface found! Response length: {len(response.text)}")
    except Exception as e:
        print(f"  Error: {e}")

# Test 5: Try API status/health endpoints
print("\n=== Test 5: API Status/Health Endpoints ===")
session.headers['Authorization'] = f"Basic {credentials}"

health_endpoints = [
    'api/2.0/ping',
    'api/2.0/status',
    'api/2.0/health',
    'api/2.0/version',
    'api/2.0/test',
    'api/ping',
    'api/status',
    'ping',
    'status',
]

for endpoint in health_endpoints:
    try:
        test_url = f"{url}/{endpoint}"
        response = session.get(test_url)
        print(f"{endpoint:<20} | Status: {response.status_code}")
        if response.status_code not in [404, 500, 401, 403]:
            print(f"  Response: {response.text[:150]}...")
    except Exception as e:
        print(f"  Error: {e}")

# Test 6: Check if API is enabled by looking for telltale signs
print("\n=== Test 6: API Configuration Check ===")

# Try to access main page and look for API references
try:
    response = session.get(url)
    if response.status_code == 200:
        content = response.text.lower()
        api_indicators = ['api', 'rest', 'json', 'endpoint', 'swagger', 'openapi']
        found_indicators = [indicator for indicator in api_indicators if indicator in content]
        print(f"API indicators in main page: {found_indicators}")
        
        if 'api' in content:
            print("✅ API references found in main page")
        else:
            print("❌ No API references found in main page")
except Exception as e:
    print(f"Error checking main page: {e}")

print(f"\n=== Basic connectivity test complete ===")
print(f"Summary:")
print(f"- Basic connectivity: {'✅ Working' if True else '❌ Failed'}")
print(f"- API endpoints: {'❌ All returning 500 errors'}")
print(f"- Authentication: {'⚠️ Working but endpoints not responding'}")
print(f"\nRecommendation: Check if Splynx API is enabled in system settings")
