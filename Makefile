.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: lint
lint:  ## Linter the code.
	@echo "🚨 Linting code"
	poetry run isort rsort tests --check
	poetry run flake8 rsort tests
	poetry run mypy rsort
	poetry run black rsort tests --check --diff
	poetry run bandit -r rsort/
	poetry run safety check -i 39462


.PHONY: format
format:
	@echo "🎨 Formatting code"
	poetry run isort rsort tests
	poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place rsort tests --exclude=__init__.py
	poetry run black rsort tests


.PHONY: test
test:  ## Test your code.
	@echo "🍜 Running pytest"
	poetry run pytest tests/ --cov=rsort --cov-report=term-missing:skip-covered --cov-report=xml --cov-fail-under 100
