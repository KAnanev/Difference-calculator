from gendiff.scripts.gendiff import render_string, render, generate_diff
from tests.fixtures.output import output_plain


def test_render_string(collect_diff_dict):
    assert render_string('host', collect_diff_dict['host']) == '   host: hexlet.io'
    assert render_string('host', collect_diff_dict['host']) != ' - host: hexlet.io'
    assert render_string('timeout', collect_diff_dict['timeout']) == ' - timeout: 50\n + timeout: 20'


def test_render(collect_diff_dict):
    assert render(collect_diff_dict) == output_plain


def test_generate_diff(path_before_file, path_after_file):
    assert generate_diff(path_before_file, path_after_file) == output_plain
