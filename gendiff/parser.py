import argparse
import json
import os

import yaml


def get_data(file_path: str):
    _, file_extension = os.path.splitext(file_path)

    with open(file_path) as file:
        if file_extension == '.json':
            return json.load(file)
        elif file_extension in ('.yaml', '.yml'):
            return yaml.load(file, yaml.SafeLoader)


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
