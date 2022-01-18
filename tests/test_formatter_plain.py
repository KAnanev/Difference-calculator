from tests.fixtures.output import output_nested_plain
from gendiff.formatter.plain import render_plain, render_plain_string


def test_render_plain_flat(diff_flat_dicts):
    assert render_plain(
        diff_flat_dicts
    ) == "Property 'follow' was removed\n" \
         "Property 'proxy' was removed\n" \
         "Property 'timeout' was updated. From 50 to 20\n" \
         "Property 'verbose' was added with value: 'true'"


def test_render_plain_string_flat(diff_flat_dicts):
    assert render_plain_string(
        diff_flat_dicts['follow']
    ) == "Property 'follow' was removed"
    assert render_plain_string(
        diff_flat_dicts['timeout']
    ) == "Property 'timeout' was updated. From 50 to 20"
    assert render_plain_string(
        diff_flat_dicts['verbose']
    ) == "Property 'verbose' was added with value: 'true'"


def test_render_plain_nested(diff_nested_dicts):
    assert render_plain(
        diff_nested_dicts
    ) == output_nested_plain


def test_render_plain_string_nested(diff_nested_dicts):
    pass
