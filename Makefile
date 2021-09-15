install:
		poetry install

lint:
		poetry run flake8 gendiff

build:
		poetry build

test:
		poetry run pytest

coverage:
		poetry run coverage run --omit '.venv/*' -m pytest tests/*.py && coverage report -m

coverage_xml:
		poetry run coverage xml