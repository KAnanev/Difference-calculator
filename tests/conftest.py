import pytest
import json


@pytest.fixture
def path_before_file():
    return 'data/before_plain.json'


@pytest.fixture()
def path_after_file():
    return 'data/after_plain.json'


@pytest.fixture()
def collect_diff_dict():
    return {
        'follow': {'status': ('removed', '-'), 'value': 'false'},
        'host': {'status': ('unchanged', ' '), 'value': 'hexlet.io'},
        'proxy': {'status': ('removed', '-'), 'value': '123.234.53.22'},
        'timeout': {'status': ('changed', '-+'), 'value': (50, 20)},
        'verbose': {'status': ('added', '+'), 'value': 'true'},
    }

