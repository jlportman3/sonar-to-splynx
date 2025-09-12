#!/usr/bin/env python3
"""
Simple Splynx authentication test script
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

print(f"Testing Splynx API at: {url}")
print(f"API Key: {key[:10]}...")
print(f"Secret: {secret[:10]}...")

session = requests.Session()
session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

test_url = f"{url}/api/2.0/admin/customers/customer"

# Test 1: Query parameters
print("\n=== Test 1: Query parameters ===")
try:
    response = session.get(test_url, params={'key': key, 'secret': secret, 'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Headers: {dict(response.headers)}")
    print(f"Response: {response.text[:200]}...")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Different query param names
print("\n=== Test 2: Different query param names ===")
try:
    response = session.get(test_url, params={'api_key': key, 'api_secret': secret, 'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
except Exception as e:
    print(f"Error: {e}")

# Test 3: Basic auth
print("\n=== Test 3: Basic auth ===")
try:
    session.auth = (key, secret)
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    session.auth = None
except Exception as e:
    print(f"Error: {e}")

# Test 4: Basic auth header manually
print("\n=== Test 4: Basic auth header manually ===")
try:
    credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
    session.headers['Authorization'] = f"Basic {credentials}"
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    del session.headers['Authorization']
except Exception as e:
    print(f"Error: {e}")

# Test 5: X-API headers
print("\n=== Test 5: X-API headers ===")
try:
    session.headers['X-API-Key'] = key
    session.headers['X-API-Secret'] = secret
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    del session.headers['X-API-Key']
    del session.headers['X-API-Secret']
except Exception as e:
    print(f"Error: {e}")

# Test 6: Get API info
print("\n=== Test 6: API info endpoint ===")
try:
    response = session.get(f"{url}/api/2.0")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:500]}...")
except Exception as e:
    print(f"Error: {e}")

# Test 7: Session endpoint
print("\n=== Test 7: Session endpoint ===")
try:
    auth_data = {
        'auth_type': 'api_key',
        'key': key,
        'secret': secret
    }
    response = session.post(f"{url}/api/2.0/admin/auth/sessions", json=auth_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:300]}...")
except Exception as e:
    print(f"Error: {e}")

print("\n=== Tests complete ===")
