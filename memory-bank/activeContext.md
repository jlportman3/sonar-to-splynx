# 🎯 ACTIVE CONTEXT
**Current Working Focus:** Sonar GraphQL Data Backup  
**Last Updated:** September 13, 2025  
**Status:** Backup tooling implemented – ready for baseline snapshot

---

## 🔍 **CURRENT WORK ITEMS**

### **Focus Area: Sonar GraphQL Backup Tooling**
- **Objective:** Capture a complete, API-only snapshot of Sonar data prior to migration
- **Deliverable:** `backup_sonar_graphql.py` CLI with supporting backup engine
- **Storage:** PostgreSQL database (`sonar_backup` on localhost:5433) holding JSON payloads per query
- **Usage Notes:** Supports include/exclude filters, configurable pagination, depth-limited field selection, request timeouts (`--request-timeout`), automatic rate-limit handling (`--rate-limit-delay` / `--rate-limit-retries`), and `--sample-size` for capped snapshots (`make backup-test` grabs 100 rows per collection)

### **Sessions & Progress**
```
Session A: Schema-driven design
├── Reviewed existing GraphQL client utilities
├── Planned introspection + auto-selection strategy
└── Defined PostgreSQL layout for per-query JSON storage

Session B: Implementation
├── Added src/backup/sonar_graphql_backup.py (introspection + pagination)
├── Created CLI entry point backup_sonar_graphql.py
├── Wired logging/metadata tables for repeatable runs
└── Updated README + techContext with backup guidance

Session C: Verification
├── python -m compileall to sanity check syntax
├── Documented usage and configuration prerequisites
└── Ready for live execution once Sonar credentials confirmed
```

### **Key Decisions Made**
- **GraphQL Only:** No REST fallback—ensures parity with customer request
- **JSON Storage:** Preserve raw entity payloads for replay/reference
- **Auto Discovery:** Introspection-driven query discovery avoids manual query lists
- **Depth Limit Defaults:** Cap nested selection at depth 2 to prevent runaway recursion while capturing core fields

### **Next Steps**
- Execute initial backup (ensure `BACKUP_DATABASE_URL` points to Postgres instance)
- Use `make backup-test` to capture a 100-row sample set for schema/transform design before full exports
- Run `make backup-clean` when you need to clear prior runs (drops all per-collection tables and resets metadata)
- Review resulting tables and adjust include/exclude filters if needed
- Integrate backup artifacts into broader migration validation workflow

---

## 🗂️ **PREVIOUS CONTEXT (ARCHIVED)**

### **405 HTTP Error Investigation & Splynx System Analysis**
- **Outcome:** Feature modules disabled triggered 405 responses; no blockers for migration
- **Artifacts:** `splynx_system_analysis_report.md`, `docs/splynx/405_error_investigation.json`, `analyze_splynx_database.py`, `investigate_405_errors.py`
- **Status:** Complete – informed current backup and migration planning phases
