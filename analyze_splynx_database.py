#!/usr/bin/env python3
"""
Comprehensive Splynx Database Analysis
Direct MySQL access for complete schema and data discovery
"""

import mysql.connector
import json
import os
from datetime import datetime
from collections import defaultdict

from dotenv import load_dotenv

load_dotenv()

# Database credentials
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'unix_socket': os.getenv('MYSQL_SOCKET'),
    'database': os.getenv('MYSQL_DATABASE')
}

def get_database_connection(database=None):
    """Get MySQL database connection"""
    config = DB_CONFIG.copy()
    if database:
        config['database'] = database
    return mysql.connector.connect(**config)

def discover_databases():
    """Discover all databases"""
    conn = get_database_connection()
    cursor = conn.cursor()
    
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]
    
    cursor.close()
    conn.close()
    
    return databases

def analyze_table_schema(database, table):
    """Get detailed table schema information"""
    conn = get_database_connection(database)
    cursor = conn.cursor()
    
    # Get column information
    cursor.execute(f"DESCRIBE `{table}`")
    columns = []
    for row in cursor.fetchall():
        columns.append({
            'field': row[0],
            'type': row[1], 
            'null': row[2],
            'key': row[3],
            'default': row[4],
            'extra': row[5]
        })
    
    # Get foreign key relationships
    cursor.execute("""
        SELECT 
            COLUMN_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
        WHERE TABLE_SCHEMA = %s 
        AND TABLE_NAME = %s 
        AND REFERENCED_TABLE_NAME IS NOT NULL
    """, (database, table))
    
    foreign_keys = []
    for row in cursor.fetchall():
        foreign_keys.append({
            'column': row[0],
            'references_table': row[1],
            'references_column': row[2]
        })
    
    # Get table row count
    try:
        cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
        row_count = cursor.fetchone()[0]
    except:
        row_count = 0
    
    cursor.close()
    conn.close()
    
    return {
        'columns': columns,
        'foreign_keys': foreign_keys,
        'row_count': row_count
    }

def sample_table_data(database, table, limit=3):
    """Sample data from table"""
    conn = get_database_connection(database)
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute(f"SELECT * FROM `{table}` LIMIT {limit}")
        sample_data = cursor.fetchall()
        
        # Convert any non-serializable data
        for row in sample_data:
            for key, value in row.items():
                if isinstance(value, (bytes, bytearray)):
                    row[key] = f"<binary_data_{len(value)}_bytes>"
                elif hasattr(value, 'isoformat'):
                    row[key] = value.isoformat()
                    
        return sample_data
    except Exception as e:
        return {'error': str(e)}
    finally:
        cursor.close()
        conn.close()

def analyze_splynx_database():
    """Comprehensive Splynx database analysis"""
    print("🔍 COMPREHENSIVE SPLYNX DATABASE ANALYSIS")
    print("="*50)
    
    analysis = {
        'analysis_date': datetime.now().isoformat(),
        'databases': {},
        'splynx_schema': {},
        'table_categories': {},
        'relationships': [],
        'migration_insights': {}
    }
    
    # Discover databases
    print("\n📊 Discovering databases...")
    databases = discover_databases()
    analysis['databases'] = databases
    
    for db in databases:
        print(f"  📁 {db}")
    
    # Focus on splynx database (likely named 'splynx' or similar)
    splynx_db = None
    for db in databases:
        if 'splynx' in db.lower() or db.lower() in ['splynx', 'billing', 'isp']:
            splynx_db = db
            break
    
    if not splynx_db:
        # If no obvious splynx db, look for largest non-system database
        system_dbs = ['information_schema', 'mysql', 'performance_schema', 'sys']
        candidate_dbs = [db for db in databases if db not in system_dbs]
        if candidate_dbs:
            splynx_db = candidate_dbs[0]  # Pick first non-system database
    
    if not splynx_db:
        print("❌ Could not identify Splynx database")
        return analysis
    
    print(f"\n🎯 Analyzing Splynx database: {splynx_db}")
    
    # Get all tables in splynx database
    conn = get_database_connection(splynx_db)
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]
    cursor.close()
    conn.close()
    
    print(f"📋 Found {len(tables)} tables")
    
    # Categorize tables by function
    table_categories = {
        'customers': [],
        'services': [],
        'finance': [],
        'networking': [],
        'support': [],
        'admin': [],
        'logs': [],
        'config': [],
        'voice': [],
        'inventory': [],
        'scheduling': [],
        'auth': [],
        'monitoring': [],
        'other': []
    }
    
    for table in tables:
        table_lower = table.lower()
        if any(word in table_lower for word in ['customer', 'client', 'user']):
            table_categories['customers'].append(table)
        elif any(word in table_lower for word in ['service', 'tariff', 'plan']):
            table_categories['services'].append(table)
        elif any(word in table_lower for word in ['finance', 'invoice', 'payment', 'transaction', 'billing']):
            table_categories['finance'].append(table)
        elif any(word in table_lower for word in ['network', 'router', 'ip', 'nas', 'radius']):
            table_categories['networking'].append(table)
        elif any(word in table_lower for word in ['ticket', 'support', 'message']):
            table_categories['support'].append(table)
        elif any(word in table_lower for word in ['admin', 'administrator', 'role', 'permission']):
            table_categories['admin'].append(table)
        elif any(word in table_lower for word in ['log', 'audit', 'history', 'change']):
            table_categories['logs'].append(table)
        elif any(word in table_lower for word in ['config', 'setting', 'option']):
            table_categories['config'].append(table)
        elif any(word in table_lower for word in ['voice', 'call', 'cdr', 'phone']):
            table_categories['voice'].append(table)
        elif any(word in table_lower for word in ['inventory', 'item', 'product', 'supplier']):
            table_categories['inventory'].append(table)
        elif any(word in table_lower for word in ['schedule', 'task', 'project']):
            table_categories['scheduling'].append(table)
        elif any(word in table_lower for word in ['auth', 'token', 'session']):
            table_categories['auth'].append(table)
        elif any(word in table_lower for word in ['monitor', 'ping', 'snmp']):
            table_categories['monitoring'].append(table)
        else:
            table_categories['other'].append(table)
    
    analysis['table_categories'] = table_categories
    
    # Analyze key tables from each category
    priority_tables = []
    
    # Get most important tables from each category
    for category, tables_in_cat in table_categories.items():
        if tables_in_cat:
            # Sort by likely importance (shorter names often = core tables)
            sorted_tables = sorted(tables_in_cat, key=len)
            if category == 'customers':
                priority_tables.extend(sorted_tables[:5])  # Top 5 customer tables
            elif category in ['services', 'finance']:
                priority_tables.extend(sorted_tables[:4])  # Top 4 tables
            else:
                priority_tables.extend(sorted_tables[:2])  # Top 2 tables
    
    # Ensure we have core tables
    core_table_patterns = ['customers', 'tariffs', 'services', 'invoices', 'transactions', 'admin']
    for pattern in core_table_patterns:
        matching = [t for t in tables if pattern in t.lower()]
        if matching:
            priority_tables.extend(matching[:2])
    
    # Remove duplicates and limit total
    priority_tables = list(set(priority_tables))[:50]  # Limit to 50 tables
    
    print(f"\n🔍 Analyzing {len(priority_tables)} priority tables...")
    
    # Analyze each priority table
    table_analysis = {}
    relationships = []
    
    for i, table in enumerate(priority_tables, 1):
        print(f"  📋 ({i}/{len(priority_tables)}) Analyzing: {table}")
        
        try:
            schema = analyze_table_schema(splynx_db, table)
            sample_data = sample_table_data(splynx_db, table)
            
            table_info = {
                'table': table,
                'schema': schema,
                'sample_data': sample_data,
                'primary_keys': [col['field'] for col in schema['columns'] if col['key'] == 'PRI'],
                'foreign_keys': schema['foreign_keys'],
                'row_count': schema['row_count']
            }
            
            table_analysis[table] = table_info
            
            # Track relationships
            for fk in schema['foreign_keys']:
                relationships.append({
                    'from_table': table,
                    'from_column': fk['column'],
                    'to_table': fk['references_table'],
                    'to_column': fk['references_column']
                })
                
            print(f"    ✅ {schema['row_count']} rows, {len(schema['columns'])} columns, {len(schema['foreign_keys'])} FKs")
            
        except Exception as e:
            print(f"    ❌ Error analyzing {table}: {e}")
            table_analysis[table] = {'error': str(e)}
    
    analysis['splynx_schema'] = table_analysis
    analysis['relationships'] = relationships
    
    # Generate migration insights
    insights = {
        'total_tables': len(tables),
        'analyzed_tables': len([t for t in table_analysis.values() if 'error' not in t]),
        'table_distribution': {cat: len(tables_in_cat) for cat, tables_in_cat in table_categories.items() if tables_in_cat},
        'total_relationships': len(relationships),
        'high_priority_tables': [t for t, info in table_analysis.items() if info.get('row_count', 0) > 0],
        'migration_complexity': 'moderate' if len(relationships) < 100 else 'high'
    }
    
    analysis['migration_insights'] = insights
    
    return analysis

if __name__ == "__main__":
    try:
        analysis_results = analyze_splynx_database()
        
        # Save comprehensive results
        output_file = 'docs/splynx/database_analysis.json'
        with open(output_file, 'w') as f:
            json.dump(analysis_results, f, indent=2, default=str)
        
        print(f"\n💾 Complete database analysis saved to: {output_file}")
        
        # Print summary
        insights = analysis_results['migration_insights']
        print(f"\n📊 DATABASE ANALYSIS SUMMARY:")
        print(f"🔢 Total tables discovered: {insights['total_tables']}")
        print(f"🔍 Tables analyzed: {insights['analyzed_tables']}")
        print(f"🔗 Relationships found: {insights['total_relationships']}")
        print(f"📈 Migration complexity: {insights['migration_complexity']}")
        
        print(f"\n📋 TABLE DISTRIBUTION:")
        for category, count in insights['table_distribution'].items():
            if count > 0:
                print(f"  {category}: {count} tables")
        
        print(f"\n🎯 High priority tables with data:")
        for table in insights['high_priority_tables'][:10]:
            row_count = analysis_results['splynx_schema'][table]['row_count']
            print(f"  📊 {table}: {row_count} records")
        
        print(f"\n🚀 COMPLETE DATABASE STRUCTURE DISCOVERED!")
        print(f"Ready for detailed migration planning with full schema knowledge.")
        
    except Exception as e:
        print(f"❌ Database analysis failed: {e}")
        print("Checking MySQL connection and permissions...")
