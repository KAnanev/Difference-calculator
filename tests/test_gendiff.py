from gendiff.scripts.gendiff import bool_to_string, get_diff_value, collect_diff_dicts, \
    ADDED, CHANGED, UNCHANGED, REMOVED, render_string, render, generate_diff
from gendiff.parser import parse_args, get_data
from tests.fixtures.output import output_plain


def test_get_data():
    assert isinstance(get_data('data/before_plain.json'), dict)
    assert isinstance(get_data('data/before_plain.yaml'), dict)
    assert isinstance(get_data('data/after_plain.yml'), dict)


def test_parser_args():
    parser = parse_args(['file.json', 'file.json'])
    assert parser.first_file
    assert parser.second_file
    assert parser.format


def test_bool_to_string():
    assert bool_to_string(False) == 'false'
    assert bool_to_string(True) == 'true'
    assert bool_to_string('') == 'null'


def test_get_diff_value():
    assert get_diff_value(None, 'value') == {'status': ADDED, 'value': 'value'}
    assert get_diff_value('value', None) == {'status': REMOVED, 'value': 'value'}
    assert get_diff_value(True, None)
    assert get_diff_value('value', 'value') == {'status': UNCHANGED, 'value': 'value'}
    assert get_diff_value('value', 'an_value') == {'status': CHANGED, 'value': ('value', 'an_value')}

    assert get_diff_value({'key': 'value'}, 'value') == {'status': CHANGED, 'value': ({'key': 'value'}, 'value')}
    assert get_diff_value('value', {'key': 'value'}) == {'status': CHANGED, 'value': ('value', {'key': 'value'})}
    assert get_diff_value({'key': 'value'}, {'key': 'value'}) == {
        'status': 'nested', 'value': {
            'key': {
                'status': UNCHANGED, 'value': 'value'
            }
        }
    }

    assert get_diff_value({'key': 'value'}, {'key': 'an_value'}) == {
        'status': 'nested', 'value': {
            'key': {
                'status': CHANGED, 'value': ('value', 'an_value')
            }
        }
    }


def test_collect_diff_dicts(collect_diff_dict):
    assert collect_diff_dicts({'key': 'value'}, {'key': 'value'}) == {'key': {'status': UNCHANGED, 'value': 'value'}}

    assert collect_diff_dicts({'follow': False, 'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22'},
                              {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}) == collect_diff_dict


def test_render_string(collect_diff_dict):
    assert render_string('host', collect_diff_dict['host']) == '   host: hexlet.io'
    assert render_string('host', collect_diff_dict['host']) != ' - host: hexlet.io'
    assert render_string('timeout', collect_diff_dict['timeout']) == ' - timeout: 50\n + timeout: 20'


def test_render(collect_diff_dict):
    assert render(collect_diff_dict) == output_plain


def test_generate_diff(path_before_file, path_after_file):
    assert generate_diff(path_before_file, path_after_file) == output_plain
