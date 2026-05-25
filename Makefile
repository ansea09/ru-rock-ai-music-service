PYTHON ?= python3
VENV ?= .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_PIP := $(VENV_PYTHON) -m pip
VENV_UVICORN := $(VENV)/bin/uvicorn
VENV_PYTEST := $(VENV)/bin/pytest
VENV_RUFF := $(VENV)/bin/ruff

.PHONY: install run test lint smoke openapi check

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)

install: $(VENV_PYTHON)
	$(VENV_PIP) install -e ".[dev]"

run:
	$(VENV_UVICORN) rock_music_generator.main:app --reload

test:
	$(VENV_PYTEST)

lint:
	$(VENV_RUFF) check .

smoke:
	$(VENV_PYTHON) scripts/run_mock_smoke.py

openapi:
	$(VENV_PYTHON) scripts/export_openapi.py docs/api/openapi.json

check: lint test
