import pytest
import json


@pytest.fixture
def cli_answer_data():
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


@pytest.fixture
def answer_data():
    with open(f'tests/fixtures/answer.txt') as file:
        return file.read()


@pytest.fixture
def path_before_file():
    return 'tests/fixtures/before_plain.json'


@pytest.fixture()
def path_after_file():
    return 'tests/fixtures/after_plain.json'


@pytest.fixture()
def yaml_path_before_file():
    return 'tests/fixtures/before_plain.yaml'


@pytest.fixture()
def yml_path_after_file():
    return 'tests/fixtures/after_plain.yml'


@pytest.fixture()
def json_before_dict(path_before_file):
    with open(path_before_file) as file:
        return json.load(file)


@pytest.fixture()
def json_after_dict(path_after_file):
    with open(path_after_file) as file:
        return json.load(file)


@pytest.fixture()
def collect_diff_dict():
    return {
        'follow': {'status': ('removed', '-'), 'value': 'false'},
        'host': {'status': ('unchanged', ' '), 'value': 'hexlet.io'},
        'proxy': {'status': ('removed', '-'), 'value': '123.234.53.22'},
        'timeout': {'status': ('changed', '-+'), 'value': (50, 20)},
        'verbose': {'status': ('added', '+'), 'value': 'true'},
    }

