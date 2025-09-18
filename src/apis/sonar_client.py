"""Sonar GraphQL API client for data extraction and schema analysis."""

from typing import Dict, Any, Optional, List
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from tenacity import retry, stop_after_attempt, wait_exponential
from dataclasses import dataclass

from src.config.settings import MigrationConfig
from src.utils.logger import get_logger

logger = get_logger("sonar_client")

@dataclass
class GraphQLResponse:
    """Response from GraphQL query."""
    data: Optional[Dict[str, Any]]
    errors: Optional[List[Dict[str, str]]]
    success: bool

class SonarGraphQLClient:
    """GraphQL client for Sonar API interactions."""

    def __init__(self, config: MigrationConfig, request_timeout: float = 30.0):
        self.config = config
        self.request_timeout = request_timeout
        self.client: Optional[Client] = None
        self.transport: Optional[RequestsHTTPTransport] = None
        self._setup_client()
    
    def _setup_client(self) -> None:
        """Setup GraphQL client with authentication."""
        try:
            # Build GraphQL endpoint URL
            graphql_url = f"{self.config.sonar_url.rstrip('/')}/api/graphql"
            
            # Setup headers
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Sonar-Migration-Tool/1.0"
            }
            
            # Add authentication
            if self.config.sonar_token:
                headers["Authorization"] = f"Bearer {self.config.sonar_token}"
                logger.info("Using token authentication for Sonar")
            elif self.config.sonar_api_key:
                headers["Authorization"] = f"Bearer {self.config.sonar_api_key}"
                logger.info("Using API key authentication for Sonar")
            elif self.config.sonar_username and self.config.sonar_password:
                # Basic auth will be handled by requests
                auth = (self.config.sonar_username, self.config.sonar_password)
                logger.info("Using username/password authentication for Sonar")
            else:
                raise ValueError("No authentication method configured for Sonar")
            
            # Create transport
            if self.config.sonar_username and self.config.sonar_password and not self.config.sonar_token and not self.config.sonar_api_key:
                self.transport = RequestsHTTPTransport(
                    url=graphql_url,
                    headers=headers,
                    auth=(self.config.sonar_username, self.config.sonar_password)
                )
            else:
                self.transport = RequestsHTTPTransport(
                    url=graphql_url,
                    headers=headers
                )
            
            # Create GraphQL client
            self.client = Client(transport=self.transport, fetch_schema_from_transport=True)
            
            logger.info(f"Sonar GraphQL client initialized for {graphql_url}")
            
        except Exception as e:
            logger.error(f"Failed to setup Sonar GraphQL client: {e}")
            raise
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def execute_query(self, query: str, variables: Optional[Dict[str, Any]] = None) -> GraphQLResponse:
        """Execute a GraphQL query with retry logic using direct requests."""
        try:
            url = f"{self.config.sonar_url.rstrip('/')}/api/graphql"
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Sonar-Migration-Tool/1.0"
            }
            
            # Add authentication
            if self.config.sonar_token:
                headers["Authorization"] = f"Bearer {self.config.sonar_token}"
            elif self.config.sonar_api_key:
                headers["Authorization"] = f"Bearer {self.config.sonar_api_key}"
            
            payload = {
                "query": query,
                "variables": variables or {}
            }
            
            request_kwargs = {
                "headers": headers,
                "json": payload,
                "timeout": self.request_timeout,
            }

            if self.config.sonar_username and self.config.sonar_password and not self.config.sonar_token and not self.config.sonar_api_key:
                auth = (self.config.sonar_username, self.config.sonar_password)
                request_kwargs["auth"] = auth

            response = requests.post(url, **request_kwargs)
            
            response.raise_for_status()
            result = response.json()
            
            if "errors" in result:
                logger.error(f"GraphQL errors: {result['errors']}")
                return GraphQLResponse(
                    data=result.get("data"),
                    errors=result["errors"],
                    success=False
                )
            
            logger.debug(f"Query executed successfully: {query[:100]}...")
            
            return GraphQLResponse(
                data=result.get("data"),
                errors=None,
                success=True
            )
            
        except Exception as e:
            logger.error(f"GraphQL query failed: {e}")
            return GraphQLResponse(
                data=None,
                errors=[{"message": str(e)}],
                success=False
            )
    
    def get_schema_info(self) -> Dict[str, Any]:
        """Get GraphQL schema information using introspection."""
        introspection_query = """
        query IntrospectionQuery {
          __schema {
            queryType { name }
            mutationType { name }
            subscriptionType { name }
            types {
              ...FullType
            }
            directives {
              name
              description
              locations
              args {
                ...InputValue
              }
            }
          }
        }

        fragment FullType on __Type {
          kind
          name
          description
          fields(includeDeprecated: true) {
            name
            description
            args {
              ...InputValue
            }
            type {
              ...TypeRef
            }
            isDeprecated
            deprecationReason
          }
          inputFields {
            ...InputValue
          }
          interfaces {
            ...TypeRef
          }
          enumValues(includeDeprecated: true) {
            name
            description
            isDeprecated
            deprecationReason
          }
          possibleTypes {
            ...TypeRef
          }
        }

        fragment InputValue on __InputValue {
          name
          description
          type { ...TypeRef }
          defaultValue
        }

        fragment TypeRef on __Type {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                  ofType {
                    kind
                    name
                    ofType {
                      kind
                      name
                      ofType {
                        kind
                        name
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """
        
        logger.info("Fetching Sonar GraphQL schema...")
        response = self.execute_query(introspection_query)
        
        if response.success and response.data:
            logger.info("Schema introspection successful")
            return response.data
        else:
            logger.error("Failed to fetch schema")
            raise RuntimeError(f"Schema introspection failed: {response.errors}")
    
    def test_connection(self) -> bool:
        """Test the connection to Sonar API."""
        simple_query = """
        query {
          __typename
        }
        """
        
        logger.info("Testing Sonar API connection...")
        response = self.execute_query(simple_query)
        
        if response.success:
            logger.info("Sonar API connection successful")
            return True
        else:
            logger.error(f"Sonar API connection failed: {response.errors}")
            return False
    
    def get_available_queries(self) -> List[str]:
        """Get list of available root queries."""
        try:
            schema = self.get_schema_info()
            query_type = None
            
            # Find the Query type
            for type_info in schema["__schema"]["types"]:
                if type_info["name"] == schema["__schema"]["queryType"]["name"]:
                    query_type = type_info
                    break
            
            if query_type and query_type["fields"]:
                queries = [field["name"] for field in query_type["fields"]]
                logger.info(f"Found {len(queries)} available queries")
                return queries
            else:
                logger.warning("No queries found in schema")
                return []
                
        except Exception as e:
            logger.error(f"Failed to get available queries: {e}")
            return []
    
    def explore_entity_queries(self) -> Dict[str, Any]:
        """Explore and categorize entity-related queries."""
        queries = self.get_available_queries()
        
        # COMPREHENSIVE entity patterns for COMPLETE Sonar analysis
        entity_patterns = {
            "accounts": ["account", "customer", "subscriber", "client"],
            "services": ["service", "plan", "package", "subscription", "rate", "tariff", "pricing"],
            "billing": ["bill", "invoice", "payment", "credit", "debit", "transaction", "charge", "fee", "tax", "recurring"],
            
            # Network Infrastructure
            "network_equipment": ["router", "switch", "access_point", "ap", "cpe", "modem", "gateway", "bridge", "repeater", "concentrator"],
            "network_interfaces": ["interface", "port", "ethernet", "wifi", "wireless", "fiber", "coax", "cable"],
            "ip_management": ["ip", "subnet", "vlan", "dhcp", "dns", "arp", "mac", "lease", "pool", "range", "assignment"],
            "network_protocols": ["radius", "pppoe", "snmp", "ospf", "bgp", "vrrp", "hsrp", "stp", "lacp", "lldp"],
            
            # Physical Infrastructure
            "sites": ["site", "location", "building", "premises", "facility", "datacenter", "pop", "node"],
            "towers": ["tower", "antenna", "mast", "pole", "cellular", "radio", "microwave", "backhaul"],
            "geographic": ["address", "geographic", "gps", "coordinate", "latitude", "longitude", "zone", "region"],
            "physical_assets": ["rack", "cabinet", "enclosure", "shelter", "power", "cooling", "generator", "ups"],
            
            # Equipment & Inventory
            "inventory": ["inventory", "item", "model", "vendor", "equipment", "asset", "serial", "part", "component"],
            "devices": ["device", "hardware", "firmware", "software", "version", "revision", "patch"],
            "cables": ["cable", "fiber", "copper", "patch", "trunk", "drop", "splice", "termination"],
            
            # Users & Access Management
            "users": ["user", "employee", "technician", "admin", "operator", "manager", "staff"],
            "roles": ["role", "permission", "privilege", "group", "team", "department", "access", "authorization"],
            "authentication": ["auth", "login", "password", "token", "session", "certificate", "key", "credential"],
            
            # Tickets & Operations
            "tickets": ["ticket", "task", "work_order", "trouble", "incident", "request", "comment", "priority", "category"],
            "maintenance": ["maintenance", "repair", "upgrade", "installation", "outage", "downtime", "scheduled"],
            
            # Monitoring & Performance
            "monitoring": ["monitor", "alert", "notification", "threshold", "metric", "status", "health", "performance"],
            "statistics": ["statistic", "graph", "chart", "measurement", "reading", "sample", "data_point"],
            "availability": ["uptime", "downtime", "sla", "availability", "reliability", "quality"],
            
            # Business Operations
            "contacts": ["contact", "phone", "email", "communication", "correspondence"],
            "financial": ["ledger", "balance", "deposit", "refund", "adjustment", "write_off", "accounting"],
            "contracts": ["contract", "agreement", "terms", "conditions", "sla", "warranty"],
            
            # System Operations
            "jobs": ["job", "scheduled", "cron", "queue", "worker", "background", "batch", "process"],
            "logs": ["log", "audit", "history", "event", "activity", "change", "trace", "debug"],
            "configuration": ["setting", "config", "preference", "option", "parameter", "policy", "rule"],
            "backup": ["backup", "restore", "snapshot", "archive", "recovery", "replication"],
            
            # Integration & APIs
            "integration": ["webhook", "api", "sync", "import", "export", "third_party", "external", "feed"],
            "provisioning": ["provision", "activate", "suspend", "terminate", "deploy", "configure", "setup"],
            
            # Usage & Analytics
            "usage": ["usage", "data", "bandwidth", "consumption", "quota", "overage", "traffic", "volume"],
            "reports": ["report", "dashboard", "analytic", "summary", "export", "statement"],
            
            # Documentation & Files
            "documents": ["document", "file", "attachment", "template", "manual", "diagram", "drawing"],
            "scheduling": ["schedule", "appointment", "calendar", "time_slot", "availability", "booking"],
            
            # Specialized Network Services
            "voip": ["voip", "sip", "voice", "phone", "call", "pbx", "trunk", "extension"],
            "video": ["video", "streaming", "iptv", "multicast", "codec", "bitrate"],
            "wireless": ["wireless", "wifi", "radio", "frequency", "channel", "ssid", "signal", "spectrum"],
            "security": ["firewall", "vpn", "ipsec", "acl", "nat", "qos", "traffic_shaping", "encryption"]
        }
        
        categorized = {category: [] for category in entity_patterns.keys()}
        categorized["other"] = []
        
        for query in queries:
            categorized_flag = False
            for category, patterns in entity_patterns.items():
                if any(pattern in query.lower() for pattern in patterns):
                    categorized[category].append(query)
                    categorized_flag = True
                    break
            
            if not categorized_flag:
                categorized["other"].append(query)
        
        logger.info("Entity queries categorized")
        return categorized
