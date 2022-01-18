from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.output import output_flat, output_nested_stylish


def test_plain_json_generate_diff(
        path_to_plain_before_json_file, path_to_plain_after_json_file
):
    assert generate_diff(
        path_to_plain_before_json_file,
        path_to_plain_after_json_file,
        style='stylish'
    ) == output_flat


def test_plain_yaml_generate_diff(
        path_to_plain_before_yaml_file, path_to_plain_after_yml_file
):
    assert generate_diff(
        path_to_plain_before_yaml_file,
        path_to_plain_after_yml_file,
        style='stylish'
    ) == output_flat


def test_nested_json_generate_diff(
        path_to_nested_before_json_file,
        path_to_nested_after_json_file
):
    assert generate_diff(
        path_to_nested_before_json_file, path_to_nested_after_json_file,
        style='stylish'
    ) == output_nested_stylish


def test_nested_yaml_generate_diff(
        path_to_nested_before_yaml_file, path_to_nested_after_yaml_file
):
    assert generate_diff(
        path_to_nested_before_yaml_file,
        path_to_nested_after_yaml_file,
        style='stylish'
    ) == output_nested_stylish
