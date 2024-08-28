.PHONY: build \
	install \
	check_format \
	format \
	check_lint \
	lint \
	check_types \
	tests \
	check_all \
	prepare_env_pyenv

REPOSITORY = bpmn-parser
SOURCE = bpmn_parser
TESTS = tests


build:
	@docker build -t $(REPOSITORY):latest .

install:
	@echo "\nInstalling project..."
	@poetry install --no-root
	@echo "\nProject installed!"

check_format:
	@poetry run ruff format $(SOURCE) --check
	@poetry run ruff format $(TESTS) --check

format:
	@poetry run ruff format $(SOURCE)
	@poetry run ruff format $(TESTS)

check_lint:
	@poetry run ruff check $(SOURCE)
	@poetry run ruff check $(TESTS)

lint:
	@poetry run ruff check $(SOURCE) --fix
	@poetry run ruff check $(TESTS) --fix

check_types:
	@poetry run mypy $(SOURCE)
	@poetry run mypy $(TESTS)

tests:
	@echo "\nRunning Tests"
	@poetry run pytest -s $(TESTS) --cov=$(SOURCE)
	@poetry run coverage-badge -o assets/coverage-badge.svg -f -q

check_all: check_format check_lint check_types tests
	@echo "\nAll checks have been passed!"

prepare_env_pyenv:
	@echo "\nPreparing virtualenv using pyenv..."
	@pyenv update
	@pyenv install 3.11 -s
	@pyenv virtualenv -f 3.11 bpmn_parser-env
	@pyenv local bpmn_parser-env

	@echo "\nInstalling poetry..."
	@pip install poetry
	@poetry config virtualenvs.create false --local
	@poetry config virtualenvs.prefer-active-python true --local

	@echo "\nProject prepared to install!"
