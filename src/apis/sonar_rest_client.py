"""Sonar REST API client for data extraction and schema analysis."""

from typing import Dict, Any, Optional, List
import requests
from dataclasses import dataclass
import time
from urllib.parse import urljoin

from src.config.settings import MigrationConfig
from src.utils.logger import get_logger

logger = get_logger("sonar_rest_client")

@dataclass
class RestResponse:
    """Response from REST API call."""
    data: Optional[Dict[str, Any]]
    status_code: int
    success: bool
    error: Optional[str] = None

class SonarRestClient:
    """REST API client for Sonar API interactions."""
    
    def __init__(self, config: MigrationConfig):
        self.config = config
        self.session = requests.Session()
        self.base_url = f"{config.sonar_url.rstrip('/')}/api/v1"
        self._setup_authentication()
    
    def _setup_authentication(self) -> None:
        """Setup authentication for REST API."""
        if self.config.sonar_username and self.config.sonar_password:
            self.session.auth = (self.config.sonar_username, self.config.sonar_password)
            logger.info("Using Basic authentication for Sonar REST API")
        elif self.config.sonar_api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {self.config.sonar_api_key}'
            })
            logger.info("Using Bearer token authentication for Sonar REST API")
        else:
            raise ValueError("No authentication method configured for Sonar")
        
        # Set common headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Sonar-Migration-Tool/1.0'
        })
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> RestResponse:
        """Make GET request to Sonar REST API."""
        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))
        
        try:
            logger.debug(f"GET request to: {url}")
            response = self.session.get(url, params=params or {})
            
            if response.status_code == 200:
                data = response.json()
                return RestResponse(
                    data=data,
                    status_code=response.status_code,
                    success=True
                )
            else:
                logger.error(f"API request failed: {response.status_code} - {response.text}")
                return RestResponse(
                    data=None,
                    status_code=response.status_code,
                    success=False,
                    error=f"HTTP {response.status_code}: {response.text}"
                )
                
        except Exception as e:
            logger.error(f"Request failed: {e}")
            return RestResponse(
                data=None,
                status_code=0,
                success=False,
                error=str(e)
            )
    
    def test_connection(self) -> bool:
        """Test connection to Sonar REST API."""
        logger.info("Testing Sonar REST API connection...")
        response = self.get("accounts", {"limit": 1})
        
        if response.success:
            logger.info("Sonar REST API connection successful")
            return True
        else:
            logger.error(f"Sonar REST API connection failed: {response.error}")
            return False
    
    def discover_endpoints(self) -> List[str]:
        """Discover available REST API endpoints."""
        # Common Sonar REST API endpoints based on typical ISP management patterns
        potential_endpoints = [
            # Core entities
            "accounts", "customers", "services", "plans", "packages",
            
            # Billing
            "invoices", "payments", "transactions", "charges", "credits", "debits",
            "payment_methods", "billing_cycles", "recurring_charges",
            
            # Network infrastructure
            "network_sites", "towers", "access_points", "routers", "switches",
            "network_monitoring_templates", "network_interfaces", "vlans",
            "ip_pools", "ip_assignments", "dhcp_servers", "dhcp_leases",
            "radius_accounts", "radius_groups", "pppoe_accounts",
            
            # Physical infrastructure
            "addresses", "geographic_coordinates", "buildings", "facilities",
            "inventory_items", "models", "vendors", "equipment",
            "cables", "fiber_cables", "copper_cables",
            
            # Operations
            "tickets", "tasks", "work_orders", "ticket_categories", "ticket_priorities",
            "scheduled_events", "maintenance_windows", "outages",
            
            # Monitoring & Performance
            "monitoring_templates", "alerts", "notifications", "graphs",
            "statistics", "performance_metrics", "availability_reports",
            
            # Users & Access
            "users", "user_roles", "permissions", "groups", "departments",
            "authentication_logs", "api_keys", "sessions",
            
            # System & Configuration
            "companies", "settings", "configuration", "system_logs",
            "audit_logs", "scheduled_jobs", "cron_jobs", "background_jobs",
            
            # Integration & Provisioning
            "webhooks", "api_logs", "integrations", "external_systems",
            "provisioning_templates", "device_configurations",
            
            # Usage & Analytics
            "usage_records", "bandwidth_reports", "data_usage", "quotas",
            "overage_charges", "usage_analytics", "traffic_reports",
            
            # Documents & Files
            "documents", "files", "attachments", "templates", "contracts",
            
            # Scheduling
            "appointments", "calendar_events", "availability_windows",
            "technician_schedules", "service_appointments",
            
            # Specialized services
            "voip_accounts", "sip_accounts", "phone_numbers", "call_logs",
            "video_services", "iptv_channels", "streaming_packages",
            "wireless_networks", "wifi_networks", "ssids", "frequencies",
            
            # Financial
            "account_balances", "financial_transactions", "adjustments",
            "refunds", "write_offs", "deposits", "account_credits",
            
            # Reporting
            "reports", "dashboards", "analytics", "export_templates",
            "custom_reports", "scheduled_reports"
        ]
        
        available_endpoints = []
        
        for endpoint in potential_endpoints:
            logger.info(f"Testing endpoint: {endpoint}")
            response = self.get(endpoint, {"limit": 1})
            
            if response.success:
                available_endpoints.append(endpoint)
                logger.info(f"✓ Found endpoint: {endpoint}")
            else:
                logger.debug(f"✗ Endpoint not available: {endpoint}")
            
            # Add small delay to be respectful to the API
            time.sleep(0.1)
        
        logger.info(f"Discovered {len(available_endpoints)} available endpoints")
        return available_endpoints
    
    def analyze_endpoint_schema(self, endpoint: str, sample_size: int = 5) -> Dict[str, Any]:
        """Analyze the data structure of a specific endpoint."""
        logger.info(f"Analyzing schema for endpoint: {endpoint}")
        
        # Get sample data
        response = self.get(endpoint, {"limit": sample_size})
        
        if not response.success:
            return {
                "endpoint": endpoint,
                "available": False,
                "error": response.error
            }
        
        data = response.data
        
        # Extract pagination info if available
        pagination_info = None
        if isinstance(data, dict) and "paginator" in data:
            pagination_info = {
                "total_count": data["paginator"].get("total_count"),
                "total_pages": data["paginator"].get("total_pages"),
                "current_page": data["paginator"].get("current_page"),
                "limit": data["paginator"].get("limit")
            }
        
        # Extract sample records
        records = []
        if isinstance(data, dict) and "data" in data:
            records = data["data"]
        elif isinstance(data, list):
            records = data
        
        # Analyze field structure from sample records
        field_analysis = {}
        if records:
            sample_record = records[0] if records else {}
            
            for field, value in sample_record.items():
                field_type = type(value).__name__
                field_info = {
                    "type": field_type,
                    "nullable": any(record.get(field) is None for record in records[:3]),
                    "sample_values": []
                }
                
                # Collect sample values (first 3 unique values)
                unique_values = set()
                for record in records[:sample_size]:
                    if field in record and record[field] is not None:
                        unique_values.add(str(record[field])[:100])  # Limit string length
                        if len(unique_values) >= 3:
                            break
                
                field_info["sample_values"] = list(unique_values)
                field_analysis[field] = field_info
        
        return {
            "endpoint": endpoint,
            "available": True,
            "total_records": pagination_info["total_count"] if pagination_info else len(records),
            "pagination": pagination_info,
            "sample_record_count": len(records),
            "fields": field_analysis,
            "sample_records": records[:2] if records else []  # Include 2 sample records
        }
    
    def get_all_paginated_data(self, endpoint: str, max_pages: int = 100) -> List[Dict[str, Any]]:
        """Get all data from a paginated endpoint."""
        all_data = []
        page = 1
        
        while page <= max_pages:
            response = self.get(endpoint, {"page": page, "limit": 100})
            
            if not response.success:
                logger.error(f"Failed to fetch page {page} from {endpoint}")
                break
            
            data = response.data
            
            if isinstance(data, dict) and "data" in data:
                records = data["data"]
                all_data.extend(records)
                
                # Check if we have more pages
                paginator = data.get("paginator", {})
                if page >= paginator.get("total_pages", 1):
                    break
            else:
                # Non-paginated response
                if isinstance(data, list):
                    all_data.extend(data)
                break
            
            page += 1
            time.sleep(0.1)  # Be respectful to the API
        
        logger.info(f"Retrieved {len(all_data)} total records from {endpoint}")
        return all_data
