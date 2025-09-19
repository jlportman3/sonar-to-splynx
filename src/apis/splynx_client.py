#!/usr/bin/env python3
"""
Splynx REST API Client

This module provides a client for interacting with Splynx's REST API.
Updated to work with actual Splynx v2.0 API endpoints and authentication.
"""

import requests
import base64
import json
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
import time

logger = logging.getLogger(__name__)

@dataclass
class SplynxConfig:
    base_url: str
    api_key: str
    api_secret: str
    timeout: int = 30

class SplynxAPIClient:
    """Splynx REST API client for data migration operations."""
    
    def __init__(self, config: SplynxConfig):
        self.config = config
        self.session = requests.Session()
        self.base_url = config.base_url.rstrip('/')
        self.api_key = config.api_key
        self.api_secret = config.api_secret
        self.session.timeout = config.timeout
        
        # Set up Basic Auth (working method from our tests)
        credentials = base64.b64encode(f"{config.api_key}:{config.api_secret}".encode()).decode()
        self.session.headers.update({
            'Authorization': f'Basic {credentials}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        logger.info(f"Initialized Splynx client for {self.base_url}")
    
    def test_connection(self) -> Dict[str, Any]:
        """Test API connection using the working check endpoint."""
        try:
            response = self._make_request('GET', 'admin/api/check')
            if response.status_code == 200:
                data = response.json()
                logger.info(f"Splynx API connection successful: {data.get('message', 'Unknown')}")
                return {'success': True, 'data': data}
            else:
                logger.error(f"Connection test failed: {response.status_code} - {response.text}")
                return {'success': False, 'error': f"Status {response.status_code}", 'message': response.text}
        except Exception as e:
            logger.error(f"Connection test error: {e}")
            return {'success': False, 'error': str(e)}
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make a request to the Splynx API."""
        url = f"{self.base_url}/api/2.0/{endpoint}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            logger.debug(f"{method} {url} -> {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Request failed: {method} {url} - {e}")
            raise
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and return standardized result."""
        try:
            if response.status_code in [200, 201, 202, 204]:
                if response.content:
                    return {
                        'success': True,
                        'status_code': response.status_code,
                        'data': response.json()
                    }
                else:
                    return {
                        'success': True,
                        'status_code': response.status_code,
                        'data': None
                    }
            else:
                try:
                    error_data = response.json()
                except:
                    error_data = {'message': response.text}
                    
                return {
                    'success': False,
                    'status_code': response.status_code,
                    'error': error_data
                }
        except Exception as e:
            return {
                'success': False,
                'status_code': response.status_code,
                'error': f"Response parsing failed: {e}",
                'raw_response': response.text[:500]
            }
    
    # =================================================================
    # WORKING ENDPOINTS - Based on actual API testing
    # =================================================================
    
    def get_tariffs_internet(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get internet tariffs - CONFIRMED WORKING"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/tariffs/internet', params=params)
        return self._handle_response(response)
    
    def create_tariff_internet(self, tariff_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create internet tariff - CONFIRMED WORKING"""
        response = self._make_request('POST', 'admin/tariffs/internet', json=tariff_data)
        return self._handle_response(response)
    
    def get_tariff_internet_schema(self) -> Dict[str, Any]:
        """Get internet tariff schema via OPTIONS - CONFIRMED WORKING"""
        response = self._make_request('OPTIONS', 'admin/tariffs/internet')
        return self._handle_response(response)
    
    def get_tariffs_voice(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get voice tariffs - CONFIRMED WORKING"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/tariffs/voice', params=params)
        return self._handle_response(response)
    
    def create_tariff_voice(self, tariff_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create voice tariff - CONFIRMED WORKING"""
        response = self._make_request('POST', 'admin/tariffs/voice', json=tariff_data)
        return self._handle_response(response)
    
    def get_tariff_voice_schema(self) -> Dict[str, Any]:
        """Get voice tariff schema via OPTIONS - CONFIRMED WORKING"""
        response = self._make_request('OPTIONS', 'admin/tariffs/voice')
        return self._handle_response(response)
    
    def get_tariffs_recurring(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get recurring tariffs - CONFIRMED WORKING"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/tariffs/recurring', params=params)
        return self._handle_response(response)
    
    def create_tariff_recurring(self, tariff_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create recurring tariff - CONFIRMED WORKING"""
        response = self._make_request('POST', 'admin/tariffs/recurring', json=tariff_data)
        return self._handle_response(response)
    
    def get_tariffs_bundle(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get bundle tariffs - CONFIRMED WORKING"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/tariffs/bundle', params=params)
        return self._handle_response(response)
    
    def create_tariff_bundle(self, tariff_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create bundle tariff - CONFIRMED WORKING"""
        response = self._make_request('POST', 'admin/tariffs/bundle', json=tariff_data)
        return self._handle_response(response)
    
    def get_tariff_bundle_schema(self) -> Dict[str, Any]:
        """Get bundle tariff schema via OPTIONS - CONFIRMED WORKING"""
        response = self._make_request('OPTIONS', 'admin/tariffs/bundle')
        return self._handle_response(response)
    
    def get_tariffs_onetime(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get one-time tariffs - CONFIRMED WORKING"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/tariffs/one-time', params=params)
        return self._handle_response(response)
    
    def create_tariff_onetime(self, tariff_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create one-time tariff - CONFIRMED WORKING"""
        response = self._make_request('POST', 'admin/tariffs/one-time', json=tariff_data)
        return self._handle_response(response)

    def list_administrators(self) -> Dict[str, Any]:
        """List existing Splynx administrators."""
        response = self._make_request('GET', 'admin/administration/administrators')
        return self._handle_response(response)

    def create_administrator(self, admin_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a Splynx administrator."""
        response = self._make_request('POST', 'admin/administration/administrators', json=admin_data)
        return self._handle_response(response)

    def get_tariff_onetime_schema(self) -> Dict[str, Any]:
        """Get one-time tariff schema via OPTIONS - CONFIRMED WORKING"""
        response = self._make_request('OPTIONS', 'admin/tariffs/one-time')
        return self._handle_response(response)
    
    # =================================================================
    # RESTRICTED ENDPOINTS - Need additional permissions
    # =================================================================
    
    def get_customers(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get customers - REQUIRES ADDITIONAL PERMISSIONS"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/customers/customer', params=params)
        return self._handle_response(response)
    
    def create_customer(self, customer_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create customer - REQUIRES ADDITIONAL PERMISSIONS"""
        response = self._make_request('POST', 'admin/customers/customer', json=customer_data)
        return self._handle_response(response)
    
    def get_services_internet(self, customer_id: int) -> Dict[str, Any]:
        """Get internet services for customer - REQUIRES ADDITIONAL PERMISSIONS"""
        response = self._make_request('GET', f'admin/customers/customer/{customer_id}/internet-services')
        return self._handle_response(response)
    
    def get_invoices(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get invoices - REQUIRES ADDITIONAL PERMISSIONS"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/finance/invoices', params=params)
        return self._handle_response(response)
    
    def get_payments(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get payments - REQUIRES ADDITIONAL PERMISSIONS"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/finance/payments', params=params)
        return self._handle_response(response)
    
    def get_transactions(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get transactions - REQUIRES ADDITIONAL PERMISSIONS"""
        params = {'limit': limit, 'offset': offset}
        response = self._make_request('GET', 'admin/finance/transactions', params=params)
        return self._handle_response(response)
    
    # =================================================================
    # SCHEMA ANALYSIS METHODS
    # =================================================================
    
    def get_all_working_schemas(self) -> Dict[str, Any]:
        """Get schemas for all working endpoints."""
        schemas = {}
        
        working_endpoints = [
            'admin/tariffs/internet',
            'admin/tariffs/voice', 
            'admin/tariffs/recurring',
            'admin/tariffs/bundle',
            'admin/tariffs/one-time'
        ]
        
        for endpoint in working_endpoints:
            try:
                # Get data
                data_response = self._make_request('GET', endpoint, params={'limit': 10})
                
                # Get schema via OPTIONS if available
                schema_response = self._make_request('OPTIONS', endpoint)
                
                endpoint_info = {
                    'endpoint': endpoint,
                    'data_status': data_response.status_code,
                    'schema_status': schema_response.status_code,
                    'data': None,
                    'schema': None
                }
                
                if data_response.status_code == 200:
                    endpoint_info['data'] = data_response.json()
                
                if schema_response.status_code == 200:
                    endpoint_info['schema'] = schema_response.json()
                
                schemas[endpoint] = endpoint_info
                
            except Exception as e:
                logger.error(f"Error getting schema for {endpoint}: {e}")
                schemas[endpoint] = {'error': str(e)}
        
        return schemas
    
    def test_tariff_creation(self) -> Dict[str, Any]:
        """Test tariff creation and deletion to validate write permissions."""
        try:
            # Create a test internet tariff
            test_tariff = {
                'title': f'Test Migration Tariff {int(time.time())}',
                'partners_ids': [1],
                'speed_download': 1024,
                'speed_upload': 1024,
                'price': 10.00,
                'with_vat': True,
                'billing_types': ['recurring'],
                'available_for_locations': [1],
                'customer_categories': ['person']
            }
            
            # Create tariff
            create_result = self.create_tariff_internet(test_tariff)
            
            if create_result['success'] and 'data' in create_result and 'id' in create_result['data']:
                tariff_id = create_result['data']['id']
                
                # Try to delete the test tariff
                delete_response = self._make_request('DELETE', f'admin/tariffs/internet/{tariff_id}')
                delete_success = delete_response.status_code == 204
                
                return {
                    'success': True,
                    'create_status': create_result['status_code'],
                    'delete_status': delete_response.status_code,
                    'delete_success': delete_success,
                    'tariff_id': tariff_id,
                    'message': 'Successfully created and deleted test tariff'
                }
            else:
                return {
                    'success': False,
                    'error': 'Failed to create test tariff',
                    'details': create_result
                }
                
        except Exception as e:
            logger.error(f"Error testing tariff creation: {e}")
            return {'success': False, 'error': str(e)}
    
    # =================================================================
    # GENERIC API METHODS
    # =================================================================
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make GET request to Splynx API."""
        response = self._make_request('GET', endpoint, params=params or {})
        return self._handle_response(response)
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make POST request to Splynx API."""
        response = self._make_request('POST', endpoint, json=data)
        return self._handle_response(response)
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make PUT request to Splynx API."""
        response = self._make_request('PUT', endpoint, json=data)
        return self._handle_response(response)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make DELETE request to Splynx API."""
        response = self._make_request('DELETE', endpoint)
        return self._handle_response(response)
    
    def options(self, endpoint: str) -> Dict[str, Any]:
        """Make OPTIONS request to get schema information."""
        response = self._make_request('OPTIONS', endpoint)
        return self._handle_response(response)
    
    # =================================================================
    # SCHEMA DISCOVERY AND ANALYSIS
    # =================================================================
    
    def analyze_api_capabilities(self) -> Dict[str, Any]:
        """Comprehensive analysis of API capabilities and permissions."""
        logger.info("Starting comprehensive Splynx API analysis...")
        
        # Test connection first
        connection_test = self.test_connection()
        if not connection_test['success']:
            return {'error': 'Connection test failed', 'details': connection_test}
        
        # Test endpoints from documentation
        documented_endpoints = [
            # Working endpoints (confirmed)
            'admin/api/check',
            'admin/tariffs/internet',
            'admin/tariffs/voice',
            'admin/tariffs/recurring', 
            'admin/tariffs/bundle',
            'admin/tariffs/one-time',
            
            # Customer endpoints (likely restricted)
            'admin/customers/customer',
            'admin/customers/customer-statistics',
            'admin/customers/customers-online',
            
            # Finance endpoints (likely restricted)
            'admin/finance/transactions',
            'admin/finance/invoices',
            'admin/finance/payments',
            'admin/finance/payment-methods',
            'admin/finance/transaction-categories',
            
            # Administration endpoints
            'admin/administration/locations',
            'admin/administration/administrators',
            'admin/administration/partners',
            
            # Networking endpoints
            'admin/networking/routers',
            'admin/networking/ipv4',
            'admin/networking/ipv6',
            'admin/networking/monitoring',
            
            # Support endpoints
            'admin/support/tickets',
            'admin/support/ticket-messages',
            
            # Dashboard
            'admin/dashboard/dashboard',
            
            # Config
            'admin/config/company-info',
            'admin/config/additional-fields/customers'
        ]
        
        endpoint_results = {}
        working_endpoints = []
        restricted_endpoints = []
        
        for endpoint in documented_endpoints:
            try:
                response = self._make_request('GET', endpoint, params={'limit': 1})
                
                result = {
                    'status_code': response.status_code,
                    'accessible': response.status_code == 200,
                    'restricted': response.status_code == 403,
                    'not_found': response.status_code == 404,
                    'method_not_allowed': response.status_code == 405,
                    'server_error': response.status_code == 500
                }
                
                if response.status_code == 200:
                    working_endpoints.append(endpoint)
                    try:
                        result['sample_data'] = response.json()
                    except:
                        result['sample_data'] = None
                        
                    # Try to get schema via OPTIONS
                    try:
                        options_response = self._make_request('OPTIONS', endpoint)
                        if options_response.status_code == 200:
                            result['schema'] = options_response.json()
                    except:
                        pass
                        
                elif response.status_code == 403:
                    restricted_endpoints.append(endpoint)
                
                endpoint_results[endpoint] = result
                
            except Exception as e:
                endpoint_results[endpoint] = {'error': str(e)}
        
        # Test creation capabilities on working endpoints
        creation_tests = {}
        for endpoint in working_endpoints:
            if 'tariffs' in endpoint:
                try:
                    # Test POST with empty data to see if it's allowed
                    response = self._make_request('POST', endpoint, json={})
                    creation_tests[endpoint] = {
                        'post_allowed': response.status_code != 405,
                        'status_code': response.status_code
                    }
                except:
                    creation_tests[endpoint] = {'post_allowed': False}
        
        analysis_result = {
            'connection_test': connection_test,
            'endpoint_analysis': endpoint_results,
            'working_endpoints': working_endpoints,
            'restricted_endpoints': restricted_endpoints,
            'creation_capabilities': creation_tests,
            'summary': {
                'total_tested': len(documented_endpoints),
                'working': len(working_endpoints),
                'restricted': len(restricted_endpoints),
                'api_functional': len(working_endpoints) > 0
            },
            'analysis_timestamp': time.time()
        }
        
        logger.info(f"API analysis complete: {len(working_endpoints)} working, {len(restricted_endpoints)} restricted")
        return analysis_result
    
    def get_working_endpoint_schemas(self) -> Dict[str, Any]:
        """Get detailed schemas for all working endpoints."""
        schemas = {}
        
        working_endpoints = [
            'admin/tariffs/internet',
            'admin/tariffs/voice',
            'admin/tariffs/recurring',
            'admin/tariffs/bundle', 
            'admin/tariffs/one-time'
        ]
        
        for endpoint in working_endpoints:
            try:
                # Get current data
                data_result = self.get(endpoint, {'limit': 5})
                
                # Get schema
                schema_result = self.options(endpoint)
                
                schemas[endpoint] = {
                    'data_response': data_result,
                    'schema_response': schema_result,
                    'endpoint_url': f"{self.base_url}/api/2.0/{endpoint}"
                }
                
            except Exception as e:
                schemas[endpoint] = {'error': str(e)}
        
        return schemas
