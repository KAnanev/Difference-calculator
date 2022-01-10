from gendiff.formatter.formatter import render
from gendiff.formatter.stylish import render_string, render_stylish
from tests.fixtures.output import output_plain, output_nested


def test_plain_render_string(collect_diff_dict):
    assert render_string('host', collect_diff_dict['host'], 0) == '    host: hexlet.io'
    assert render_string('host', collect_diff_dict['host'], 0) != '  - host: hexlet.io'
    assert render_string('timeout', collect_diff_dict['timeout'], 0) == '  - timeout: 50\n  + timeout: 20'


def test_plain_render(collect_diff_dict):
    assert render_stylish(collect_diff_dict) == output_plain


def test_nested_render(collect_nested_diff_dict):
    assert render_stylish(collect_nested_diff_dict) == output_nested


def test_plain_render_stylish(collect_diff_dict):
    render(collect_diff_dict, style='stylish')
    assert type(render(collect_diff_dict, style='stylish')) == str
