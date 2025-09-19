VENV_PYTHON := venv/bin/python
PYTHON ?= $(if $(wildcard $(VENV_PYTHON)),$(VENV_PYTHON),python3)
BACKUP_ARGS ?=

COMPOSE ?= docker compose
COMPOSE_FILE ?= docker-compose.yml

.PHONY: backup backup-test backup-clean backup-splynx docker-up docker-down docker-logs docker-status

backup:
	$(PYTHON) backup_sonar_graphql.py $(BACKUP_ARGS)

backup-test:
	$(PYTHON) backup_sonar_graphql.py --sample-size 100 --page-size 100 $(BACKUP_ARGS)

backup-clean:
	$(PYTHON) scripts/clean_backup_db.py

backup-splynx:
	$(PYTHON) scripts/dump_splynx_db.py

docker-up:
	$(COMPOSE) -f $(COMPOSE_FILE) up -d postgres

docker-down:
	$(COMPOSE) -f $(COMPOSE_FILE) down

docker-logs:
	$(COMPOSE) -f $(COMPOSE_FILE) logs -f postgres

docker-status:
	$(COMPOSE) -f $(COMPOSE_FILE) ps
