"""Configuration management for the Sonar-to-Splynx migration application."""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@dataclass
class MigrationConfig:
    """Configuration class for migration settings."""
    
    # Required fields first
    sonar_url: str
    splynx_url: str
    
    # Optional fields
    sonar_api_key: Optional[str] = None
    sonar_token: Optional[str] = None
    sonar_username: Optional[str] = None
    sonar_password: Optional[str] = None
    splynx_api_key: Optional[str] = None
    splynx_username: Optional[str] = None
    splynx_password: Optional[str] = None
    
    # Migration Settings
    batch_size: int = 100
    retry_attempts: int = 3
    parallel_workers: int = 4
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "MigrationConfig":
        """Create configuration from environment variables."""
        return cls(
            # Sonar configuration
            sonar_url=os.getenv("SONAR_URL", ""),
            sonar_api_key=os.getenv("SONAR_API_KEY"),
            sonar_token=os.getenv("SONAR_TOKEN"),
            sonar_username=os.getenv("SONAR_USERNAME"),
            sonar_password=os.getenv("SONAR_PASSWORD"),
            
            # Splynx configuration
            splynx_url=os.getenv("SPLYNX_URL", ""),
            splynx_api_key=os.getenv("SPLYNX_API_KEY"),
            splynx_username=os.getenv("SPLYNX_USERNAME"),
            splynx_password=os.getenv("SPLYNX_PASSWORD"),
            
            # Migration settings
            batch_size=int(os.getenv("BATCH_SIZE", "100")),
            retry_attempts=int(os.getenv("RETRY_ATTEMPTS", "3")),
            parallel_workers=int(os.getenv("PARALLEL_WORKERS", "4")),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )

    def validate(self) -> bool:
        """Validate that required configuration is present."""
        if not self.sonar_url:
            raise ValueError("SONAR_URL is required")
        
        if not self.splynx_url:
            raise ValueError("SPLYNX_URL is required")
        
        # Check that at least one authentication method is provided for Sonar
        if not (self.sonar_api_key or (self.sonar_username and self.sonar_password)):
            raise ValueError("Either SONAR_API_KEY or SONAR_USERNAME/SONAR_PASSWORD is required")
        
        # Check that at least one authentication method is provided for Splynx
        if not (self.splynx_api_key or (self.splynx_username and self.splynx_password)):
            raise ValueError("Either SPLYNX_API_KEY or SPLYNX_USERNAME/SPLYNX_PASSWORD is required")
        
        return True

# Global configuration instance
config = MigrationConfig.from_env()
