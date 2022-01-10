import pytest


@pytest.fixture()
def path_to_plain_before_json_file():
    return 'data/before_plain.json'


@pytest.fixture()
def path_to_plain_after_json_file():
    return 'data/after_plain.json'


@pytest.fixture()
def path_to_plain_before_yaml_file():
    return 'data/before_plain.yaml'


@pytest.fixture()
def path_to_plain_after_yml_file():
    return 'data/after_plain.yml'


@pytest.fixture
def path_to_nested_before_json_file():
    return 'data/before_nested.json'


@pytest.fixture()
def path_to_nested_after_json_file():
    return 'data/after_nested.json'


@pytest.fixture
def path_to_nested_before_yaml_file():
    return 'data/before_nested.yaml'


@pytest.fixture()
def path_to_nested_after_yaml_file():
    return 'data/after_nested.yaml'


@pytest.fixture()
def collect_diff_dict():
    return {
        'follow': {'status': ('removed', '-'), 'value': 'false'},
        'host': {'status': ('unchanged', ' '), 'value': 'hexlet.io'},
        'proxy': {'status': ('removed', '-'), 'value': '123.234.53.22'},
        'timeout': {'status': ('changed', '-+'), 'value': (50, 20)},
        'verbose': {'status': ('added', '+'), 'value': 'true'},
        'setting5': {'status': ('added', '+'), 'value': {'key5': 'value5'}},
        'nest': {'status': ('changed', '-+'), 'value': ({'key': 'value'}, 'str')},
        'group3': {'status': ('added', '+'), 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
    }


@pytest.fixture()
def before_dict():
    return {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True,
                       'setting6': {'key': 'value', 'doge': {'wow': ''}}},
            'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
            'group2': {'abc': 12345, 'deep': {'id': 45}}}


@pytest.fixture()
def after_dict():
    return {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah',
                       'setting5': {'key5': 'value5'},
                       'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}},
            'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'},
            'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}


@pytest.fixture()
def collect_nested_diff_dict():
    return {
        'common': {
            'status': ('nested', ' '), 'value': {
                'follow': {
                    'status': ('added', '+'), 'value': 'false'
                },
                'setting1': {
                    'status': ('unchanged', ' '), 'value': 'Value 1'
                },
                'setting2': {
                    'status': ('removed', '-'), 'value': 200
                },
                'setting3': {
                    'status': ('changed', '-+'), 'value': ('true', 'null')
                },
                'setting4': {
                    'status': ('added', '+'), 'value': 'blah blah'
                },
                'setting5': {
                    'status': ('added', '+'), 'value': {'key5': 'value5'}
                },
                'setting6': {
                    'status': ('nested', ' '), 'value': {
                        'doge': {
                            'status': ('nested', ' '), 'value': {
                                'wow': {
                                    'status': ('changed', '-+'), 'value': ('', 'so much')
                                }
                            }
                        },
                        'key': {
                            'status': ('unchanged', ' '), 'value': 'value'
                        },
                        'ops': {
                            'status': ('added', '+'), 'value': 'vops'
                        }
                    }
                }
            }
        },
        'group1': {
            'status': ('nested', ' '), 'value': {
                'baz': {
                    'status': ('changed', '-+'), 'value': ('bas', 'bars')
                },
                'foo': {
                    'status': ('unchanged', ' '), 'value': 'bar'
                },
                'nest': {
                    'status': ('changed', '-+'), 'value': ({'key': 'value'}, 'str')
                }
            }
        },
        'group2': {
            'status': ('removed', '-'), 'value': {
                'abc': 12345, 'deep': {'id': 45}
            }
        },
        'group3': {
            'status': ('added', '+'), 'value': {
                'deep': {
                    'id': {
                        'number': 45
                    }
                },
                'fee': 100500
            }
        }
    }
