import json
import os
import sys

import yaml
import argparse


def differ(key, first_value, second_value):
    if first_value and second_value:
        if first_value == second_value:
            return f'   {key}: {first_value}'
        else:
            return f' - {key}: {first_value}\n + {key}: {second_value}'
    elif first_value:
        return f' - {key}: {first_value}'
    elif second_value:
        return f' + {key}: {second_value}'


def diff_dict(before_dict: dict, after_dict: dict) -> str:
    keys = sorted(list(before_dict.keys() | after_dict.keys()))
    result = '{\n'

    for key in keys:
        first_value = str(before_dict.get(key, ''))
        second_value = str(after_dict.get(key, ''))
        result += f'{differ(key, first_value, second_value)}\n'
    result += '}'

    return result


def get_data(file_path: str):
    _, file_extension = os.path.splitext(file_path)

    with open(file_path) as file:
        if file_extension == '.json':
            return json.load(file)
        elif file_extension in ('.yaml', 'yml'):
            return yaml.load(file, yaml.SafeLoader)


def generate_diff(before_file, after_file):
    before_dict = get_data(before_file)
    after_dict = get_data(after_file)

    return diff_dict(before_dict, after_dict)


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Generate diff'
    )
    parser.add_argument('first_file', type=str, )
    parser.add_argument('second_file', type=str, )
    parser.add_argument(
        '-f', '--format',
        type=str, default='FORMAT',
        help='set format of output',
    )

    return parser.parse_args(args)


def main():  # pragma: no cover
    parser = parse_args(sys.argv[1:])

    if parser.first_file and parser.second_file:
        print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':  # pragma: no cover
    main()
