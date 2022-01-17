from gendiff.formatter.formatter import render
from gendiff.formatter.stylish import render_string, render_stylish
from tests.fixtures.output import output_plain, output_nested


def test_plain_render_string(diff_flat_dicts):
    assert render_string(
        'host', diff_flat_dicts['host'], 0
    ) == '    host: hexlet.io'
    assert render_string(
        'host', diff_flat_dicts['host'], 0
    ) != '  - host: hexlet.io'
    assert render_string(
        'timeout', diff_flat_dicts['timeout'], 0
    ) == '  - timeout: 50\n  + timeout: 20'


def test_plain_render(diff_flat_dicts):
    assert render_stylish(diff_flat_dicts) == output_plain


def test_nested_render(diff_nested_dicts):
    assert render_stylish(diff_nested_dicts) == output_nested


def test_plain_render_stylish(diff_flat_dicts):
    render(diff_flat_dicts, style='stylish')
    assert type(render(diff_flat_dicts, style='stylish')) == str
