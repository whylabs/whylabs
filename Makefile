NAME=
PY_SOURCE=$(shell find src/ -type f -name "*.py") 
SHA=$(shell git rev-parse HEAD)
VERSION=$(SHA)
REQUIREMENTS=requirements.txt

.PHONY: default 
.PHONY: lint format format-fix test setup help requirements

default:help

requirements: requirements.txt

requirements.txt: pyproject.toml
	poetry export -f requirements.txt > requirements.txt

lint:
	poetry run mypy src/

format:
	poetry run black --check --line-length 120 src

format-fix:
	poetry run black --line-length 120 src

setup:
	poetry install

test:
	poetry run pytest

help: ## Show this help message.
	@echo 'usage: make [target] ...'
	@echo
	@echo 'targets:'
	@egrep '^(.+)\:(.*) ##\ (.+)' ${MAKEFILE_LIST} | sed -s 's/:\(.*\)##/: ##/' | column -t -c 2 -s ':#'
