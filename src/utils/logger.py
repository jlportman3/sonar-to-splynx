"""Logging configuration and utilities."""

import sys
from loguru import logger
from typing import Optional

def setup_logger(log_level: str = "INFO", log_file: Optional[str] = None) -> None:
    """Setup logging configuration with loguru."""
    
    # Remove default logger
    logger.remove()
    
    # Add console handler with formatting
    logger.add(
        sys.stderr,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True
    )
    
    # Add file handler if specified
    if log_file:
        logger.add(
            log_file,
            level=log_level,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            rotation="10 MB",
            retention="10 days"
        )
    
    logger.info(f"Logger initialized with level: {log_level}")

def get_logger(name: str):
    """Get a logger instance for a specific module."""
    return logger.bind(name=name)
