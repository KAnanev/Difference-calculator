from gendiff.scripts.gendiff import diff_dict, get_data, generate_diff


def test_get_data():
    assert isinstance(get_data('tests/fixtures/before_plain.json'), dict)


def test_diff_dict(answer_data, json_before_dict, json_after_dict):
    assert diff_dict(json_before_dict, json_after_dict) == answer_data


def test_generate_diff(answer_data, path_before_file, path_after_file):
    assert generate_diff(path_before_file, path_after_file) == answer_data
