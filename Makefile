install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

check:
	test lint

build:
	uv build

setup:
	python3 -m pip install --force-reinstall dist/*.whl
