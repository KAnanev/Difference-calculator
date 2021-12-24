from gendiff.scripts.gendiff import diff_dict, generate_diff, collect_diff_dict
from gendiff.parser import get_data, parse_args


def test_get_data(path_before_file, yaml_path_before_file, yml_path_after_file):
    assert isinstance(get_data(path_before_file), dict)
    assert isinstance(get_data(yaml_path_before_file), dict)
    assert isinstance(get_data(yml_path_after_file), dict)


def test_diff_dict(answer_data, json_before_dict, json_after_dict):
    assert diff_dict(json_before_dict, json_after_dict) == answer_data


def test_generate_diff(answer_data, path_before_file, path_after_file):
    assert generate_diff(path_before_file, path_after_file) == answer_data


def test_parser_args(path_before_file, path_after_file):
    parser = parse_args([path_before_file, path_after_file])
    assert parser.first_file
    assert parser.second_file
    assert parser.format

def test_collect_diff_dict():
    assert True
