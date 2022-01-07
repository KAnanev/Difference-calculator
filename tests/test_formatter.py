from gendiff.formatter import render_string, render
from tests.fixtures.output import output_plain


def test_render_string(collect_diff_dict):
    assert render_string('host', collect_diff_dict['host']) == '   host: hexlet.io'
    assert render_string('host', collect_diff_dict['host']) != ' - host: hexlet.io'
    assert render_string('timeout', collect_diff_dict['timeout']) == ' - timeout: 50\n + timeout: 20'
    assert render_string(
        'common', {'status': ('nested', ' '), 'value': {'follow': {'status': ('added', '+'), 'value': 'false'}}}
    ) == '{\n   common: {\n + follow: false\n}\n)'


def test_render(collect_diff_dict):
    assert render(collect_diff_dict) == output_plain
