import sys

from gendiff.formatter.formatter import render
from gendiff.parser import deserializer, parse_args
from gendiff.differ import collect_diff_dicts


def generate_diff(before_file, after_file, style='stylish'):
    """Генерирует разность двух файлов"""
    before_dict = deserializer(before_file)
    after_dict = deserializer(after_file)
    diff_dict = collect_diff_dicts(before_dict, after_dict)

    return render(diff_dict, style)


def main():  # pragma: no cover
    parser = parse_args(sys.argv[1:])

    if parser.first_file and parser.second_file:
        print(
            generate_diff(parser.first_file, parser.second_file, parser.format)
        )


if __name__ == '__main__':  # pragma: no cover
    main()
