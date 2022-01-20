from gendiff.differ import check_string, get_diff_value, ADDED, \
    REMOVED, UNCHANGED, CHANGED, collect_diff_dicts, NESTED


def test_check_string():
    assert check_string(False) == 'false'
    assert check_string(True) == 'true'
    assert check_string(None) == 'null'
    assert check_string('') == ''
    assert check_string('value') == 'value'
    assert check_string(0) == 0
    assert check_string('empty') is None


def test_get_plain_diff_value():
    assert get_diff_value(
        'key', {}, {'key': 'value'}
    ) == {'status': ADDED, 'value': 'value'}
    assert get_diff_value(
        'key', {'key': 'value'}, {}
    ) == {'status': REMOVED, 'value': 'value'}
    assert get_diff_value(
        'key', {'key': 0}, {'key': 0}
    ) == {'status': UNCHANGED, 'value': 0}
    assert get_diff_value(
        'key', {'key': ''}, {'key': '0'}
    ) == {'status': CHANGED, 'value': ('', '0')}
    assert get_diff_value(
        'key', {'key': False}, {'key': True}
    ) == {'status': CHANGED, 'value': ('false', 'true')}


def test_get_nested_diff_value():
    assert get_diff_value(
        'key', {'key': {'key': 'value'}}, {'key': 'value'}
    ) == {'status': CHANGED, 'value': ({'key': 'value'}, 'value')}
    assert get_diff_value(
        'key', {'key': 'value'}, {'key': {'key': 'value'}}
    ) == {'status': CHANGED, 'value': ('value', {'key': 'value'})}
    assert get_diff_value(
        'key', {'key': {'key': 'value'}}, {'key': {'key': 'value'}}
    ) == {
        'status': NESTED, 'value': {
            'key': {
                'status': UNCHANGED, 'value': 'value'
            }
        }
    }
    assert get_diff_value(
        'key', {'key': {'key': 'value'}}, {'key': {'key': 'an_value'}}
    ) == {
        'status': NESTED, 'value': {
            'key': {
                'status': CHANGED, 'value': ('value', 'an_value')
            }
        }
    }


def test_collect_diff_dicts(diff_flat_dicts):
    assert collect_diff_dicts(
        {'key': None}, {'key': 'value'}
    ) == {'key': {'status': CHANGED, 'value': ('null', 'value')}}
    assert collect_diff_dicts(
        {'key': 'value'}, {'key': 'value'}
    ) == {'key': {'status': UNCHANGED, 'value': 'value'}}

    assert collect_diff_dicts(
        {
            'key_1': {
                'key_1_1': 'value_1_1'
            }
        },
        {
            'key_1': {
                'key_1_1': 'an_value_1_1'
            }
        }
    ) == {
        'key_1': {
            'status': ('nested', ' '), 'value': {
                'key_1_1': {
                    'status': ('changed', '-+'),
                    'value': ('value_1_1', 'an_value_1_1')
                }
            }
        }
    }


def test_nested_collect_diff_dicts(
        before_nested_dict, after_nested_dict, diff_nested_dicts
):
    assert collect_diff_dicts(
        before_nested_dict, after_nested_dict
    ) == diff_nested_dicts
