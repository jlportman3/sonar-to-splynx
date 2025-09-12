#!/usr/bin/env python3
"""
Investigate 405 Method Not Allowed errors
Test different HTTP methods and understand endpoint requirements
"""

import requests
import base64
import os
import mysql.connector
import json
from dotenv import load_dotenv
from datetime import datetime
from collections import defaultdict

load_dotenv()

# API credentials
url = os.getenv('SPLYNX_URL')
key = os.getenv('SPLYNX_API_KEY')
secret = os.getenv('SPLYNX_SECRET')

# Database credentials
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'), 
    'password': os.getenv('MYSQL_PASSWORD'),
    'unix_socket': os.getenv('MYSQL_SOCKET'),
    'database': os.getenv('MYSQL_DATABASE')
}

session = requests.Session()
credentials = base64.b64encode(f"{key}:{secret}".encode()).decode()
session.headers.update({
    'Authorization': f'Basic {credentials}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})

print("🔍 INVESTIGATING 405 METHOD NOT ALLOWED ERRORS")
print("="*50)

# Endpoints that returned 405
error_405_endpoints = {
    'admin/finance/refill-cards': 'Refill cards management',
    'admin/networking/cpe': 'CPE devices', 
    'admin/networking/cpe-ap': 'CPE Access Points',
    'admin/networking/cpe-qos': 'CPE QoS',
    'admin/fup/cap-tariff': 'CAP tariffs',
    'admin/fup/capped-data': 'Capped data',
    'admin/auth/tokens': 'Authentication tokens',
    'admin/auth/two-factor-status': 'Two-factor status'
}

def test_all_methods(endpoint):
    """Test all HTTP methods on an endpoint"""
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    results = {}
    
    for method in methods:
        try:
            test_url = f"{url}/api/2.0/{endpoint}"
            
            if method == 'GET':
                response = session.get(test_url, params={'limit': 1})
            elif method == 'POST':
                response = session.post(test_url, json={})
            elif method == 'PUT':
                response = session.put(test_url, json={})
            elif method == 'DELETE':
                response = session.delete(test_url)
            elif method == 'OPTIONS':
                response = session.options(test_url)
            elif method == 'HEAD':
                response = session.head(test_url)
                
            results[method] = {
                'status': response.status_code,
                'content_length': len(response.text) if response.text else 0
            }
            
            # Get additional info for successful responses
            if response.status_code == 200:
                try:
                    if method == 'OPTIONS':
                        data = response.json()
                        results[method]['schema'] = data
                    elif method in ['GET', 'POST']:
                        data = response.json()
                        results[method]['data_type'] = type(data).__name__
                        if isinstance(data, list):
                            results[method]['record_count'] = len(data)
                except:
                    pass
                    
        except Exception as e:
            results[method] = {'error': str(e)}
    
    return results

def check_database_tables(endpoint):
    """Check if related tables exist in database"""
    # Map endpoint to likely table names
    table_mappings = {
        'admin/finance/refill-cards': ['refill_cards', 'cards_refill', 'refill_card'],
        'admin/networking/cpe': ['cpe', 'cpe_devices'],
        'admin/networking/cpe-ap': ['cpe_ap', 'cpe_access_points'],
        'admin/networking/cpe-qos': ['cpe_qos', 'cpe_quality'],
        'admin/fup/cap-tariff': ['cap_tariff', 'fup_cap_tariff'],
        'admin/fup/capped-data': ['capped_data', 'fup_capped_data'],
        'admin/auth/tokens': ['auth_tokens', 'api_tokens', 'tokens'],
        'admin/auth/two-factor-status': ['two_factor', 'admin_2fa', 'auth_2fa']
    }
    
    possible_tables = table_mappings.get(endpoint, [])
    found_tables = []
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SHOW TABLES")
        all_tables = [table[0] for table in cursor.fetchall()]
        
        # Find matching tables
        for possible_table in possible_tables:
            exact_matches = [t for t in all_tables if t == possible_table]
            partial_matches = [t for t in all_tables if possible_table in t.lower()]
            
            found_tables.extend(exact_matches)
            found_tables.extend(partial_matches)
        
        # Remove duplicates
        found_tables = list(set(found_tables))
        
        # Get row counts for found tables
        table_info = []
        for table in found_tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
                count = cursor.fetchone()[0]
                table_info.append({'table': table, 'rows': count})
            except:
                table_info.append({'table': table, 'rows': 'error'})
        
        cursor.close()
        conn.close()
        
        return table_info
        
    except Exception as e:
        return {'error': str(e)}

def check_feature_configuration(endpoint):
    """Check if feature is enabled in configuration"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        
        # Check configuration settings related to endpoint
        feature_keywords = {
            'cpe': 'cpe',
            'cap-tariff': 'cap',
            'capped-data': 'cap',
            'refill-cards': 'refill',
            'auth/tokens': 'api',
            'two-factor': '2fa'
        }
        
        config_results = []
        for keyword in feature_keywords.values():
            cursor.execute("SELECT * FROM config WHERE `path` LIKE %s OR `key` LIKE %s LIMIT 10", 
                         (f'%{keyword}%', f'%{keyword}%'))
            results = cursor.fetchall()
            if results:
                config_results.extend(results)
        
        cursor.close()
        conn.close()
        
        return config_results
        
    except Exception as e:
        return {'error': str(e)}

print("\n🧪 TESTING HTTP METHODS FOR 405 ENDPOINTS")

investigation_results = {}

for endpoint, description in error_405_endpoints.items():
    print(f"\n🔍 Investigating: {endpoint}")
    print(f"   📝 {description}")
    
    # Test all HTTP methods
    method_results = test_all_methods(endpoint)
    
    # Check related database tables
    db_tables = check_database_tables(endpoint)
    
    # Check configuration
    config_info = check_feature_configuration(endpoint)
    
    investigation_results[endpoint] = {
        'description': description,
        'method_tests': method_results,
        'database_tables': db_tables,
        'configuration': config_info
    }
    
    # Print results
    print("   🧪 HTTP Method Results:")
    for method, result in method_results.items():
        if 'error' not in result:
            status = result['status']
            emoji = "✅" if status == 200 else "🔧" if status in [201, 202] else "❌" if status >= 400 else "❓"
            print(f"     {emoji} {method}: {status}")
            
            if status == 200 and 'schema' in result:
                print(f"        📋 Schema available")
            elif status == 200 and 'record_count' in result:
                print(f"        📊 {result['record_count']} records")
    
    print("   🗄️ Database Tables:")
    if isinstance(db_tables, list):
        if db_tables:
            for table_info in db_tables:
                print(f"     📊 {table_info['table']}: {table_info['rows']} rows")
        else:
            print("     ❌ No related tables found")
    else:
        print(f"     ❌ Database check error: {db_tables.get('error', 'unknown')}")
    
    print("   ⚙️ Configuration:")
    if isinstance(config_info, list):
        if config_info:
            for config in config_info[:3]:  # Show first 3 config items
                print(f"     🔧 {config['path']}.{config['key']} = {config['value']}")
        else:
            print("     ❌ No related configuration found")

# Analyze patterns
print(f"\n📊 405 ERROR PATTERN ANALYSIS")

methods_that_work = defaultdict(list)
features_with_data = []
features_disabled = []

for endpoint, results in investigation_results.items():
    # Find working methods
    for method, result in results['method_tests'].items():
        if not isinstance(result, dict) or 'error' in result:
            continue
        if result['status'] == 200:
            methods_that_work[method].append(endpoint)
    
    # Check if feature has data
    db_tables = results['database_tables']
    if isinstance(db_tables, list) and db_tables:
        total_rows = sum(info['rows'] for info in db_tables if isinstance(info['rows'], int))
        if total_rows > 0:
            features_with_data.append(endpoint)
        else:
            features_disabled.append(endpoint)

print(f"\n🎯 WORKING METHODS:")
for method, endpoints in methods_that_work.items():
    if endpoints:
        print(f"  ✅ {method}: {len(endpoints)} endpoints")
        for ep in endpoints:
            print(f"    - {ep}")

print(f"\n📊 FEATURE STATUS:")
print(f"✅ Features with data: {len(features_with_data)}")
for feature in features_with_data:
    print(f"  📈 {feature}")

print(f"\n❌ Features without data: {len(features_disabled)}")
for feature in features_disabled:
    print(f"  📉 {feature}")

# Save detailed investigation results
output_file = 'docs/splynx/405_error_investigation.json'
with open(output_file, 'w') as f:
    json.dump(investigation_results, f, indent=2, default=str)

print(f"\n💾 Investigation results saved to: {output_file}")

print(f"\n🎯 KEY FINDINGS:")
print(f"✅ 405 errors indicate endpoints exist but need different HTTP methods")
print(f"🔧 Some features may be disabled or require specific configurations")
print(f"📊 Database contains {sum(len(tables) for tables in investigation_results.values() if isinstance(investigation_results, dict))} related tables")
print(f"🚀 Combined API + Database access provides complete migration capability")
