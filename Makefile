install:
	uv sync

run:
	uv run python -m src

debug:
	uv run python -m pdb -m src

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache

lint:
	uv run python3 -m flake8 . --exclude=.venv,data
	uv run python3 -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --exclude .venv --exclude data

lint-strict:
	uv run python3 -m flake8 . --exclude=.venv,data
	uv run python3 -m mypy . --strict --exclude .venv --exclude data

.PHONY: install run clean debug test lint lint-strict
