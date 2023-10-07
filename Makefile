install:
		poetry install

lint:
		poetry run flake8

build:
		poetry build

test:
		poetry run pytest

self_check:
	poetry check

check: self_check test lint

coverage:
	poetry run pytest --cov=gendiff --cov-report xml