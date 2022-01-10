from gendiff.formatter import render_string, render
from tests.fixtures.output import output_plain, output_nested


def test_plain_render_string(collect_diff_dict):
    assert render_string('host', collect_diff_dict['host'], 0) == '   host: hexlet.io'
    assert render_string('host', collect_diff_dict['host'], 0) != ' - host: hexlet.io'
    assert render_string('timeout', collect_diff_dict['timeout'], 0) == ' - timeout: 50\n + timeout: 20'
    assert render_string('setting5', collect_diff_dict['setting5'], 0) == ' + setting5: {\n     key5: value5\n   }'
    assert render_string('nest', collect_diff_dict['nest'], 0) == ' - nest: {\n     key: value\n   }\n + nest: str'

    assert render_string('group3', collect_diff_dict['group3'], 0) == ''


def test_plain_render(collect_diff_dict):
    assert render(collect_diff_dict) == output_plain


def test_nested_render(collect_nested_diff_dict):
    assert render(collect_nested_diff_dict) == output_nested


