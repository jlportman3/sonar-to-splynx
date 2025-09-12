
"""Main script to run the Sonar data extraction."""

from src.extractors.sonar_extractor import SonarExtractor
from src.utils.logger import setup_logger

if __name__ == "__main__":
    setup_logger()
    extractor = SonarExtractor()
    extractor.extract_all_data()
