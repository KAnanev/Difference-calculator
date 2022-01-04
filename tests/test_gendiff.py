from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.output import output_plain


def test_generate_diff(path_before_file, path_after_file):
    assert generate_diff(path_before_file, path_after_file) == output_plain
