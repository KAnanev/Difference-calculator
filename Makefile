install:
		poetry install

lint:
		poetry run flake8

build:
		poetry build

test:
		poetry run pytest

coverage:
		poetry run coverage run -m pytest

coverage_xml:
		poetry run coverage xml