from gendiff.scripts.gendiff import bool_to_string, get_diff_value, collect_diff_dicts, render, _string
from gendiff.parser import parse_args


def test_parser_args(path_before_file, path_after_file):
    parser = parse_args([path_before_file, path_after_file])
    assert parser.first_file
    assert parser.second_file
    assert parser.format


def test_bool_to_string():
    assert bool_to_string(False) == 'false'
    assert bool_to_string(True) == 'true'


def test_collect_diff_dicts():
    assert collect_diff_dicts({'key': 'value'}, {'key': 'value'}) == {'key': {'status': 'unchanged', 'value': 'value'}}
    assert collect_diff_dicts({'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22'},
                              {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}) == {
        'host': {'status': 'unchanged', 'value': 'hexlet.io'},
        'proxy': {'status': 'removed', 'value': '123.234.53.22'},
        'timeout': {'status': 'changed', 'value': (50, 20)},
        'verbose': {'status': 'added', 'value': 'true'}
    }


def test_collect_dicts_on_dict():
    assert get_diff_value(None, 'value') == {'status': 'added', 'value': 'value'}
    assert get_diff_value('value', None) == {'status': 'removed', 'value': 'value'}
    assert get_diff_value('value', 'value') == {'status': 'unchanged', 'value': 'value'}
    assert get_diff_value('value', 'an_value') == {'status': 'changed', 'value': ('value', 'an_value')}


def test__string():
    assert _string('+', 'key', 'value') == ' + key: value'


def test_render(diff_dict, answer_data):
    result = render(diff_dict)
    assert isinstance(result, str)
    assert result == answer_data
