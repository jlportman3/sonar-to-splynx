VENV_PYTHON := venv/bin/python
PYTHON ?= $(if $(wildcard $(VENV_PYTHON)),$(VENV_PYTHON),python3)
BACKUP_DIR ?= backups
BACKUP_DB ?= $(BACKUP_DIR)/sonar_graphql.sqlite
BACKUP_ARGS ?=

.PHONY: backup backup-dir

backup: backup-dir
	$(PYTHON) backup_sonar_graphql.py --output $(BACKUP_DB) $(BACKUP_ARGS)

backup-dir:
	mkdir -p $(BACKUP_DIR)
