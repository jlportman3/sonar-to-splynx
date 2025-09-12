# Sonar to Splynx Migration Tool

A comprehensive Python application to migrate data from Sonar software instances to Splynx instances using their respective APIs.

## Project Status

🚧 **Currently implementing**: Sonar GraphQL schema analysis and documentation

## Features

- ✅ Sonar GraphQL API client with authentication support
- ✅ Comprehensive schema analysis and documentation generation
- 🚧 Splynx REST API client (planned)
- 🚧 Data extraction and transformation (planned)
- 🚧 Migration orchestration (planned)

## Setup

### Prerequisites

- Python 3.8+
- Access to a Sonar instance with API credentials
- Access to a Splynx instance with API credentials

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sonar-to-splynx
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create your environment configuration:
```bash
cp .env.example .env
```

5. Edit `.env` with your actual credentials:
```bash
# Sonar API Configuration
SONAR_URL=https://your-sonar-instance.com
SONAR_API_KEY=your_sonar_api_key
# OR use username/password
SONAR_USERNAME=your_sonar_username
SONAR_PASSWORD=your_sonar_password

# Splynx API Configuration  
SPLYNX_URL=https://your-splynx-instance.com
SPLYNX_API_KEY=your_splynx_api_key
# OR use username/password
SPLYNX_USERNAME=your_splynx_username
SPLYNX_PASSWORD=your_splynx_password
```

## Current Usage

### Analyze Sonar Schema

To analyze your Sonar GraphQL schema and generate documentation:

```bash
python analyze_sonar_schema.py
```

This will:
1. Connect to your Sonar instance using the credentials in `.env`
2. Perform GraphQL schema introspection
3. Analyze the schema structure and identify business entities
4. Generate comprehensive documentation in `docs/sonar/`

### Generated Documentation

The schema analysis creates:

- `docs/sonar/schema_analysis.json` - Complete raw analysis data
- `docs/sonar/api_schema.md` - Human-readable schema documentation

The documentation includes:
- Overview of available queries and mutations
- Business entity identification and relationships
- Type definitions and categorizations
- Query categorization by business domain

## Authentication Methods

### Sonar API
- **API Key**: Preferred method using Bearer token authentication
- **Username/Password**: Basic authentication fallback

### Splynx API
- **API Key**: Standard API key authentication
- **Username/Password**: HTTP Basic authentication

## Project Structure

```
├── src/                          # Main application code
│   ├── config/                   # Configuration management
│   ├── apis/                     # API clients
│   ├── models/                   # Data models
│   ├── utils/                    # Utilities and helpers
│   └── schema_analyzer.py        # Schema analysis tool
├── docs/                         # Generated documentation
│   ├── sonar/                    # Sonar API documentation
│   └── splynx/                   # Splynx API documentation (planned)
├── tests/                        # Test suite
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
└── analyze_sonar_schema.py       # Schema analysis runner
```

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Formatting

```bash
black src/
```

### Type Checking

```bash
mypy src/
```

## Roadmap

### Phase 1: Foundation ✅
- [x] Project structure and configuration
- [x] Sonar GraphQL client
- [x] Schema analysis and documentation

### Phase 2: API Documentation (In Progress)
- [ ] Splynx REST API client  
- [ ] Splynx API documentation scraper
- [ ] Data mapping strategy documentation

### Phase 3: Data Processing (Planned)
- [ ] Data extraction from Sonar
- [ ] Data transformation and normalization
- [ ] Data loading into Splynx

### Phase 4: Migration Orchestration (Planned)
- [ ] Migration workflow orchestration
- [ ] Progress tracking and reporting
- [ ] Error handling and recovery

### Phase 5: Testing and Optimization (Planned)
- [ ] Comprehensive test suite
- [ ] Performance optimization
- [ ] Production deployment guide

## Troubleshooting

### Connection Issues

1. **Verify credentials**: Ensure your `.env` file has correct credentials
2. **Check network access**: Ensure you can reach both Sonar and Splynx instances
3. **Verify API endpoints**: Confirm your URLs are correct and include protocol (https://)

### Schema Analysis Issues

1. **Authentication failures**: Check that your API key or username/password are correct
2. **Permission errors**: Ensure your account has API access permissions
3. **Network timeouts**: Check your network connection and API server status

## Contributing

1. Follow the implementation plan in `implementation_plan.md`
2. Write tests for new functionality
3. Update documentation for any API changes
4. Follow Python best practices and type hints

## License

[License information to be added]
