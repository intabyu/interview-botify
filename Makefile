SHELL := /bin/bash
.PHONY : all

help:
	cat Makefile

##########
# DEV    #
##########

run_dev: lint
	poetry run python -m src

lint:
	poetry run python -m black src tests
	poetry run python -m isort --profile black src tests

test: test_static test_coverage

test_integration: test_static test_coverage_integration

test_static:
	poetry run python -m black --check src tests
	poetry run python -m isort --profile black --check src tests
	poetry run python -m flake8 src
	poetry run python -m mypy src --explicit-package-bases --namespace-packages --ignore-missing-imports --install-types
	poetry run python -m bandit -r src
	poetry run python -m safety check

test_coverage:
	poetry run python -m coverage run --source=src -m pytest --disable-pytest-warnings -x -s src tests --doctest-modules
	poetry run python -m coverage report -m
