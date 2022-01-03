import os
import argparse
import json
import yaml


def yaml_load(load_file):
    return yaml.load(load_file, yaml.SafeLoader)


MAPPING_LOAD = {
    '.json': json.load,
    '.yaml': yaml_load,
    '.yml': yaml_load,
}


def deserializer(file_path: str):
    _, file_extension = os.path.splitext(file_path)

    with open(file_path) as file:
        reads_from_file = MAPPING_LOAD.get(file_extension)
        return reads_from_file(file)


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
