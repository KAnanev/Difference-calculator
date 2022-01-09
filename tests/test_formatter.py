from gendiff.formatter import render_string, render
from tests.fixtures.output import output_plain, output_nested


def test_render_string(collect_diff_dict):
    assert render_string('host', collect_diff_dict['host'], 0) == '   host: hexlet.io'
    assert render_string('host', collect_diff_dict['host'], 0) != ' - host: hexlet.io'
    assert render_string('timeout', collect_diff_dict['timeout'], 0) == ' - timeout: 50\n + timeout: 20'
    assert render_string(
        'common', {'status': ('nested', ' '), 'value': {'follow': {'status': ('added', '+'), 'value': 'false'}}}
        , 0) == "   common: ['   + follow: false']"


def test_plain_render(collect_diff_dict):
    assert render(collect_diff_dict) == output_plain




def test_nested_render(collect_nested_diff_dict):
    assert render(
        {'setting5': {'status': ('added', '+'), 'value': {'key5': 'value5'}}}
    ) == '{\n + setting5: {\n        key5: value5\n    }\n}'
    # assert render(collect_nested_diff_dict) == output_nested
