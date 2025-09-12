# Gemini Code Assistant Context

## Project Overview

This project is a Python-based data migration tool designed to transfer data from Sonar ISP billing software to the Splynx ISP management platform. The tool leverages the Sonar GraphQL API for data extraction and the Splynx REST API for data ingestion. In addition to the API, the tool also has direct access to the Splynx MySQL database, which allows for more efficient and reliable data migration.

The project is in the early stages of development. Key implemented features include a Sonar GraphQL client with robust schema analysis capabilities. The Splynx client is partially implemented, with a focus on discovering and documenting the available API endpoints. The core data mapping and migration logic is planned but not yet implemented.

**Key Technologies:**

*   **Backend:** Python 3.8+
*   **API Interaction:**
    *   `requests` for REST API communication (Splynx)
    *   `gql` for GraphQL API communication (Sonar)
*   **Data Modeling:** `pydantic`
*   **Configuration:** `python-dotenv` for managing environment variables.
*   **Testing:** `pytest`

## Project Status

According to the `migration_status_summary.md` file, the project is **ready for full migration**. The analysis of both Sonar and Splynx APIs is complete, and full read/write access has been confirmed. The schema mapping between the two systems is also complete.

### Implementation Plan

The `implementation_plan.md` outlines a five-phase implementation plan:

1.  **Foundation Setup:** Complete
2.  **API Documentation and Schema Analysis:** Complete
3.  **Core Data Processing Components:** Ready to Start
4.  **Migration Orchestration:** Ready to Start
5.  **Testing and Optimization:** Ready to Start

### Sonar System Analysis

A detailed analysis of the Sonar API is available in the `docs/sonar/` directory.

**Key Findings:**

*   **GraphQL API:** The Sonar GraphQL API is extensive, with 318 queries and 591 entities. The full schema is documented in `docs/sonar/api_schema.md`.
*   **REST API:** The Sonar REST API has three identified endpoints: `accounts`, `tickets`, and `users`. The `accounts` endpoint is a high priority for migration.
*   **Data Availability:** The Sonar system contains a significant amount of data, including over 10,000 accounts and 38,000 tickets.

### Splynx System Analysis

A comprehensive analysis of the Splynx system has been completed and is documented in the `splynx_system_analysis_report.md` and `docs/splynx/comprehensive_api_report.md` files.

**Key Findings:**

*   **Full Access:** The migration tool has full access to the Splynx system via both the API and direct MySQL database access.
*   **API Status:** The Splynx API is fully functional, with 26 working endpoints confirmed.
*   **Database Status:** The Splynx database is a fresh installation with 462 tables.
*   **405 Errors:** The 405 "Method Not Allowed" errors are not a concern and simply indicate that certain features are not enabled in the fresh Splynx installation.
*   **Migration Readiness:** The Splynx system is ready for migration.

## Building and Running

### Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    *   Copy `.env.example` to `.env`.
    *   Fill in the required Sonar and Splynx API credentials in the `.env` file.

### Running the Application

The primary entry point for the current functionality is the `analyze_sonar_schema.py` script:

```bash
python analyze_sonar_schema.py
```

This script connects to the Sonar instance, introspects the GraphQL schema, and generates documentation in the `docs/sonar/` directory.

### Running Tests

The project uses `pytest` for testing. To run the test suite:

```bash
python -m pytest tests/
```

## Development Conventions

*   **Code Style:** The project uses `black` for code formatting.
*   **Type Checking:** `mypy` is used for static type checking.
*   **Modularity:** The code is organized into modules by functionality (e.g., `apis`, `config`, `models`).
*   **API Clients:** Separate clients are implemented for the Sonar and Splynx APIs (`src/apis/sonar_client.py` and `src/apis/splynx_client.py`).
*   **Configuration:** Application settings are centralized in `src/config/settings.py` and loaded from a `.env` file. The `MigrationConfig` dataclass in this file holds all the configuration for the migration tool.
*   **Logging:** The project uses the `loguru` library for logging. The `setup_logger` function in `src/utils/logger.py` configures a console logger and an optional file logger.
*   **Data Modeling:** The project uses a normalized schema to represent data in an intermediate format during migration. The normalized data structures are defined in `src/models/normalized_schema.py`.
*   **Schema Analysis:** The `SonarSchemaAnalyzer` class in `src/schema_analyzer.py` is used to analyze the Sonar GraphQL schema and generate documentation.