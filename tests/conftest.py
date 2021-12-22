import pytest


@pytest.fixture
def answer_data():
    with open(f'tests/fixtures/answer.txt', 'rb') as file:
        return file.read()


@pytest.fixture
def cli_data():
    with open(f'tests/fixtures/cli.txt', 'rb') as file:
        return file.read()


@pytest.fixture
def error_cli_data():
    with open(f'tests/fixtures/error_cli.txt', 'rb') as file:
        return file.read()
