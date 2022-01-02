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


@pytest.fixture()
def collect_nested_diff_dict():
    return {
        'common': {
            'status': 'nested','value': {
                'follow': {'status': ('added', '+'), 'value': 'false'},
                'setting1': {'status': ('unchanged', ' '),'value': 'Value 1'},
                'setting2': {'status': ('removed', '-'), 'value': 200},
                'setting3': {'status': ('removed', '-'), 'value': 'true'},
                'setting4': {'status': ('added', '+'), 'value': 'blah blah'},
                'setting5': {'status': ('added', '+'), 'value': {'key5': 'value5'}},
                'setting6': {'status': 'nested', 'value': {
                    'doge': {'status': 'nested', 'value': {
                        'wow': {'status': ('added', '+'), 'value': 'so ' 'much'}
                    }
                             },
                    'key': {'status': ('unchanged',' '), 'value': 'value'},
                    'ops': {'status': ('added', '+'), 'value': 'vops'}
                }
                             }
            }
        }
    }
