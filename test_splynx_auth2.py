#!/usr/bin/env python3
"""
Advanced Splynx authentication test script
"""

import requests
import base64
import os
import hashlib
import hmac
import time
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

# Test 1: Splynx-EA with key:secret
print("\n=== Test 1: Splynx-EA key:secret ===")
try:
    session.headers['Authorization'] = f"Splynx-EA {key}:{secret}"
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    if 'Authorization' in session.headers:
        del session.headers['Authorization']
except Exception as e:
    print(f"Error: {e}")

# Test 2: Splynx-EA with base64
print("\n=== Test 2: Splynx-EA base64 ===")
try:
    credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
    session.headers['Authorization'] = f"Splynx-EA {credentials}"
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    if 'Authorization' in session.headers:
        del session.headers['Authorization']
except Exception as e:
    print(f"Error: {e}")

# Test 3: API-Key format
print("\n=== Test 3: API-Key format ===")
try:
    session.headers['Authorization'] = f"API-Key {key}"
    session.headers['X-API-Secret'] = secret
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    if 'Authorization' in session.headers:
        del session.headers['Authorization']
    if 'X-API-Secret' in session.headers:
        del session.headers['X-API-Secret']
except Exception as e:
    print(f"Error: {e}")

# Test 4: HMAC signature approach
print("\n=== Test 4: HMAC signature ===")
try:
    timestamp = str(int(time.time()))
    message = f"GET\n/api/2.0/admin/customers/customer\n{timestamp}"
    signature = base64.b64encode(hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest()).decode()
    session.headers['Authorization'] = f"Splynx-EA {key}:{signature}:{timestamp}"
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    if 'Authorization' in session.headers:
        del session.headers['Authorization']
except Exception as e:
    print(f"Error: {e}")

# Test 5: Bearer with concatenated key:secret
print("\n=== Test 5: Bearer concatenated ===")
try:
    token = f"{key}:{secret}"
    session.headers['Authorization'] = f"Bearer {token}"
    response = session.get(test_url, params={'limit': 1})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    if 'Authorization' in session.headers:
        del session.headers['Authorization']
except Exception as e:
    print(f"Error: {e}")

# Test 6: Check what exact Authorization header Splynx expects
print("\n=== Test 6: Different Splynx-EA formats ===")
formats = [
    f"Splynx-EA api_key={key} api_secret={secret}",
    f"Splynx-EA api_key={key};api_secret={secret}",
    f"Splynx-EA api_key={key}&api_secret={secret}",
    f"Splynx-EA {key};{secret}",
    f"Splynx-EA {key}|{secret}",
    f"Splynx-EA {key}/{secret}",
]

for i, auth_format in enumerate(formats, 1):
    try:
        session.headers['Authorization'] = auth_format
        response = session.get(test_url, params={'limit': 1})
        print(f"Format {i}: {response.status_code} - {auth_format[:50]}...")
        if response.status_code == 200:
            print(f"SUCCESS! Response: {response.text[:100]}...")
            break
        if 'Authorization' in session.headers:
            del session.headers['Authorization']
    except Exception as e:
        print(f"Format {i} Error: {e}")

# Test 7: Try session creation with different auth approaches
print("\n=== Test 7: Session creation attempts ===")
session_url = f"{url}/api/2.0/admin/auth/sessions"

# Try different auth data formats
auth_attempts = [
    {'auth_type': 'api_key', 'key': key, 'secret': secret},
    {'auth_type': 'api', 'api_key': key, 'api_secret': secret},
    {'type': 'api_key', 'key': key, 'secret': secret},
    {'api_key': key, 'api_secret': secret},
    {'username': key, 'password': secret, 'auth_type': 'api'},
]

for i, auth_data in enumerate(auth_attempts, 1):
    try:
        response = session.post(session_url, json=auth_data)
        print(f"Attempt {i}: {response.status_code} - {auth_data}")
        if response.status_code == 200:
            print(f"SUCCESS! Response: {response.text[:200]}...")
            break
        else:
            print(f"Response: {response.text[:100]}...")
    except Exception as e:
        print(f"Attempt {i} Error: {e}")

print("\n=== Tests complete ===")
