#!/usr/bin/env python3
"""
Examine actual data in working Splynx endpoints
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

session = requests.Session()
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers.update({
    'Authorization': f'Basic {credentials}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

print(f"🔍 EXAMINING ACTUAL DATA IN SPLYNX")
print(f"URL: {url}")

# Endpoints that had data in our analysis
data_endpoints = [
    'admin/finance/payment-methods',
    'admin/finance/transaction-categories', 
    'admin/administration/locations',
    'admin/administration/administrators',
    'admin/administration/partners'
]

print(f"\n=== EXAMINING ENDPOINTS WITH ACTUAL DATA ===")

for endpoint in data_endpoints:
    try:
        print(f"\n--- {endpoint} ---")
        response = session.get(f"{url}/api/2.0/{endpoint}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"📊 Records: {len(data)}")
            
            if len(data) > 0:
                print(f"🔍 Sample record:")
                sample = data[0]
                for key, value in sample.items():
                    print(f"  {key}: {value}")
                
                print(f"\n📋 All records:")
                for i, record in enumerate(data):
                    if 'name' in record:
                        print(f"  {i+1}. {record['name']} (ID: {record.get('id', 'N/A')})")
                    elif 'title' in record:
                        print(f"  {i+1}. {record['title']} (ID: {record.get('id', 'N/A')})")
                    elif 'login' in record:
                        print(f"  {i+1}. {record['login']} - {record.get('name', 'N/A')} (ID: {record.get('id', 'N/A')})")
                    else:
                        print(f"  {i+1}. {record}")
        else:
            print(f"❌ Status: {response.status_code}")
            
    except Exception as e:
        print(f"💥 Error: {e}")

# Try alternative customer endpoints
print(f"\n=== TRYING ALTERNATIVE CUSTOMER ENDPOINTS ===")

alternative_customer_endpoints = [
    'admin/customers',  # Without /customer suffix
    'customers/customer',  # Without admin prefix
    'admin/customer',  # Singular
    'customer',  # Simple
    'admin/customers/list',  # Alternative path
    'admin/customers/search',  # Search endpoint
    'admin/customers/get',  # Get endpoint
]

for endpoint in alternative_customer_endpoints:
    try:
        response = session.get(f"{url}/api/2.0/{endpoint}", params={'limit': 1})
        status_emoji = "✅" if response.status_code == 200 else "🚫" if response.status_code == 403 else "❓"
        print(f"{status_emoji} {endpoint}: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"  🎉 FOUND WORKING CUSTOMER ENDPOINT!")
            print(f"  📊 Data type: {type(data)}")
            if isinstance(data, list):
                print(f"  📊 Records: {len(data)}")
            elif isinstance(data, dict):
                print(f"  🔑 Keys: {list(data.keys())}")
                
    except Exception as e:
        print(f"💥 {endpoint}: Error - {e}")

# Check what services we can access for the existing customers
print(f"\n=== CHECKING SERVICE-RELATED ENDPOINTS ===")

service_endpoints = [
    'admin/services',
    'admin/services/list', 
    'admin/customer-services',
    'admin/internet-services',
    'admin/voice-services',
    'admin/custom-services',
    'services/internet',
    'services/voice',
    'services/custom'
]

for endpoint in service_endpoints:
    try:
        response = session.get(f"{url}/api/2.0/{endpoint}", params={'limit': 1})
        status_emoji = "✅" if response.status_code == 200 else "🚫" if response.status_code == 403 else "❓"
        print(f"{status_emoji} {endpoint}: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
