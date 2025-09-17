# AGENTS GUIDE

This repository is maintained with AI assistance. Use this guide as the canonical reference for how automation agents should operate inside the project.

## Mission
- Focus on **Sonar → Splynx** migration tooling.
- Interact with **Sonar via GraphQL only** (REST endpoints were intentionally removed).
- Use **Splynx REST** or direct DB access for target operations.

## Core Scripts & Entry Points
| Purpose | Command | Notes |
| --- | --- | --- |
| GraphQL backup (preferred) | `make backup BACKUP_ARGS="--include accounts --page-size 100"` | Runs `backup_sonar_graphql.py` through the venv-aware Makefile. Creates/updates `backups/sonar_graphql.sqlite`. |
| GraphQL smoke test | `venv/bin/python test_graphql_major_entities.py` | Verifies Sonar API access for major collections. Update query shapes if Sonar schema changes. |
| Migration CLI | `python migration_runner.py ...` | Supports `single`, `batch`, `all` commands. Relies on the incremental migration stack under `src/migration/`. |

## Environment Expectations
- Virtual environment located at `venv/`. Use `source venv/bin/activate` or rely on the Makefile’s auto-detection of `venv/bin/python`.
- `.env` must define Sonar and Splynx credentials (`SONAR_URL`, `SONAR_API_KEY` or username/password, `SPLYNX_URL`, `SPLYNX_API_KEY`, etc.).

## Code Boundaries
- **Do not reintroduce Sonar REST clients or documentation.** All Sonar data extraction must be GraphQL-based.
- Splynx REST client lives at `src/apis/splynx_client.py`. Expand it as needed for migration phases.
- GraphQL backup internals live under `src/backup/`. Reuse the helper classes when building new Sonar data flows.

## Logging & Testing
- Logging is powered by `loguru` via `src/utils/logger.py`. Ensure new scripts call `setup_logger()` before emitting output.
- Prefer targeted smoke tests (e.g., `test_graphql_major_entities.py`) over broad migrations when validating connectivity.
- Python files should compile under `python -m compileall` as a quick syntax check.

## Documentation Touchpoints
- Keep `docs/sonar/schema.md` aligned with schema changes or new GraphQL discoveries.
- Update memory-bank files (`memory-bank/*.md`) whenever major context, progress, or patterns change.
- Record new automation workflows here if agents gain new responsibilities.

## Operational Tips
- Batch GraphQL requests conservatively to respect Sonar rate guidance.
- When crafting new queries, prefer depth-limited selections and paginate with the connection pattern (`page_info.has_next_page` / `end_cursor`).
- For migrations, stage transformations inside `src/migration/` modules; avoid embedding ad-hoc logic in CLI wrappers.

Stay within these guidelines to keep automated assistance predictable and aligned with project conventions.
