from tests.fixtures.output import output_nested_plain
from gendiff.formatter.plain import render_plain, render_plain_string


def test_render_plain_flat(diff_flat_dicts):
    assert render_plain(
        diff_flat_dicts
    ) == "Property 'follow' was removed\n" \
         "Property 'proxy' was removed\n" \
         "Property 'timeout' was updated. From '50' to '20'\n" \
         "Property 'verbose' was added with value: true"


def test_render_plain_string_flat(diff_flat_dicts):
    assert render_plain_string(
        'follow', diff_flat_dicts['follow'], None
    ) == "Property 'follow' was removed"
    assert render_plain_string(
        'timeout', diff_flat_dicts['timeout'], None
    ) == "Property 'timeout' was updated. From '50' to '20'"
    assert render_plain_string(
        'verbose', diff_flat_dicts['verbose'], None
    ) == "Property 'verbose' was added with value: true"


def test_render_plain_nested(diff_nested_dicts):
    assert render_plain(
        diff_nested_dicts
    ) == output_nested_plain


def test_render_plain_string_nested(diff_nested_dicts):
    assert render_plain_string(
        'common',
        {
            'status': ('nested', ' '),
            'value': {
                'follow': {
                    'status': ('added', '+'),
                    'value': 'false'
                }
            }
        }, None
    ) == "Property 'common.follow' was added with value: false"

    assert render_plain_string(
        'common',
        {
            'status': ('nested', ' '),
            'value': {
                'setting5': {
                    'status': ('added', '+'),
                    'value': {'key5': 'value5'}
                }
            }
        }, None
    ) == "Property 'common.setting5' was added with value: [complex value]"

    assert render_plain_string(
        'group1', {
            'status': ('nested', ' '), 'value': {
                'baz': {
                    'status': ('changed', '-+'),
                    'value': ('bas', 'bars')
                },
                'nest': {
                    'status': ('changed', '-+'),
                    'value': ({'key': 'value'}, 'str')
                }
            }
        }, None
    ) == """Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'"""
