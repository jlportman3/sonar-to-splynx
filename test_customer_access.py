#!/usr/bin/env python3
"""
Test customer endpoint access after permissions update
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

print(f"🧪 TESTING CUSTOMER ACCESS WITH UPDATED PERMISSIONS")
print(f"URL: {url}")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Test primary customer endpoint
print(f"\n=== TESTING CUSTOMER ENDPOINTS ===")

customer_endpoints = [
    'admin/customers/customer',
    'admin/customers/customer-statistics',
    'admin/customers/customers-online'
]

for endpoint in customer_endpoints:
    try:
        test_url = f"{url}/api/2.0/{endpoint}"
        response = session.get(test_url, params={'limit': 5})
        
        status_emoji = "✅" if response.status_code == 200 else "🚫" if response.status_code == 403 else "❓"
        print(f"{status_emoji} {endpoint}: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"  🎉 SUCCESS! Customer endpoint is now accessible!")
            print(f"  📊 Records found: {len(data) if isinstance(data, list) else 'Object response'}")
            
            if isinstance(data, list) and len(data) > 0:
                sample_customer = data[0]
                print(f"  🔑 Customer fields: {', '.join(sample_customer.keys())}")
                print(f"  👤 Sample customer:")
                for key, value in sample_customer.items():
                    if key in ['id', 'name', 'email', 'status', 'category', 'partner_id', 'location_id']:
                        print(f"    {key}: {value}")
                
                # Get schema for customer endpoint
                try:
                    options_response = session.options(test_url)
                    if options_response.status_code == 200:
                        schema = options_response.json()
                        if 'attributes' in schema:
                            required_fields = [attr['name'] for attr in schema['attributes'] if attr.get('required')]
                            print(f"  🔧 Schema: {len(schema['attributes'])} fields, {len(required_fields)} required")
                            print(f"  📋 Required fields: {', '.join(required_fields[:5])}{'...' if len(required_fields) > 5 else ''}")
                except Exception as e:
                    print(f"  ⚠️ Schema fetch failed: {e}")
                    
            elif isinstance(data, list) and len(data) == 0:
                print(f"  📝 No customers in database yet")
                
                # Still get schema even if no data
                try:
                    options_response = session.options(test_url)
                    if options_response.status_code == 200:
                        schema = options_response.json()
                        if 'attributes' in schema:
                            required_fields = [attr['name'] for attr in schema['attributes'] if attr.get('required')]
                            print(f"  🔧 Schema available: {len(schema['attributes'])} fields, {len(required_fields)} required")
                            print(f"  📋 Required fields: {', '.join(required_fields)}")
                except Exception as e:
                    print(f"  ⚠️ Schema fetch failed: {e}")
                    
        elif response.status_code == 403:
            print(f"  🔒 Still restricted - permissions may need more time to propagate")
        else:
            print(f"  ❓ Unexpected response: {response.text[:100]}")
            
    except Exception as e:
        print(f"  💥 Error: {e}")

# Test customer creation
print(f"\n=== TESTING CUSTOMER CREATION ===")

try:
    customer_url = f"{url}/api/2.0/admin/customers/customer"
    
    # First, get schema to see required fields
    schema_response = session.options(customer_url)
    if schema_response.status_code == 200:
        schema = schema_response.json()
        if 'attributes' in schema:
            required_fields = [attr['name'] for attr in schema['attributes'] if attr.get('required')]
            print(f"✅ Customer schema available - Required fields: {', '.join(required_fields)}")
            
            # Show some key fields
            print(f"\n📋 Key customer fields:")
            for attr in schema['attributes'][:10]:  # First 10 fields
                req_mark = "⚠️ REQUIRED" if attr.get('required') else ""
                print(f"  - {attr['name']} ({attr['type']}): {attr.get('title', 'No description')} {req_mark}")
        
        # Create minimal test customer
        test_customer = {
            'name': f'Test Customer {int(datetime.now().timestamp())}',
            'email': f'test{int(datetime.now().timestamp())}@example.com'
        }
        
        # Add required fields if we know them
        if 'partner_id' in required_fields:
            test_customer['partner_id'] = 1
        if 'location_id' in required_fields:
            test_customer['location_id'] = 1
        if 'category' in required_fields:
            test_customer['category'] = 'person'
        if 'status' in required_fields:
            test_customer['status'] = 'active'
            
        print(f"\n👤 Creating test customer: {test_customer}")
        
        create_response = session.post(customer_url, json=test_customer)
        print(f"📤 Creation status: {create_response.status_code}")
        
        if create_response.status_code == 201:
            created_data = create_response.json()
            customer_id = created_data.get('id')
            print(f"🎉 SUCCESS! Customer created with ID: {customer_id}")
            
            # Try to get the created customer
            if customer_id:
                get_response = session.get(f"{customer_url}/{customer_id}")
                if get_response.status_code == 200:
                    customer_data = get_response.json()
                    print(f"✅ Can retrieve customer: {customer_data.get('name', 'Unknown')}")
                
                # Test deletion
                delete_response = session.delete(f"{customer_url}/{customer_id}")
                print(f"🗑️ Deletion status: {delete_response.status_code}")
                if delete_response.status_code == 204:
                    print(f"✅ Customer successfully deleted")
        else:
            print(f"❌ Creation failed: {create_response.text}")
            
    else:
        print(f"❌ Cannot get customer schema: {schema_response.status_code}")
        
except Exception as e:
    print(f"💥 Customer creation test error: {e}")

# Check for any existing customers in a fresh call
print(f"\n=== FINAL CUSTOMER ACCESS TEST ===")
try:
    customer_response = session.get(f"{url}/api/2.0/admin/customers/customer", params={'limit': 10})
    print(f"📞 Final customer list call: {customer_response.status_code}")
    
    if customer_response.status_code == 200:
        customers = customer_response.json()
        print(f"🎉 CUSTOMER ACCESS CONFIRMED!")
        print(f"📊 Found {len(customers)} customers in system")
        
        if len(customers) > 0:
            print(f"👥 Customer list:")
            for customer in customers:
                name = customer.get('name', 'Unknown')
                email = customer.get('email', 'No email')
                status = customer.get('status', 'Unknown')
                print(f"  - {name} ({email}) - Status: {status}")
        else:
            print(f"📝 No customers in system yet (fresh installation)")
            
    elif customer_response.status_code == 403:
        print(f"🔒 Customer access still restricted")
        print(f"💡 May need to check specific customer permissions in Splynx admin")
    else:
        print(f"❓ Unexpected status: {customer_response.status_code}")
        print(f"Response: {customer_response.text}")
        
except Exception as e:
    print(f"💥 Final test error: {e}")

print(f"\n🏁 Customer access test complete!")
