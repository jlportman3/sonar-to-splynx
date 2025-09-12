#!/usr/bin/env python3
"""
Simple script to analyze Sonar GraphQL schema.
Make sure to create a .env file with your Sonar credentials first.
"""

import sys
import os

# Add src to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from schema_analyzer import main

if __name__ == "__main__":
    main()
