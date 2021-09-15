import json
import os
import yaml
import argparse


def open_file(path: str):
    """ Открывает файл и десериализует его"""
    _, file_extension = os.path.splitext(path)
    with open(path) as file:
        if file_extension == '.json':
            return json.load(file)
        elif file_extension in ('.yaml', 'yml'):
            return yaml.load(file, yaml.SafeLoader)


def generate_diff(file_path1, file_path2):
    """ Получает путь к двум файлам,
    сравнивает их и возвращает строку разности файлов"""

    result = []
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)

    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    set_ = set1.union(set2)

    for key in sorted(list(set_)):
        if key in dict1:
            if key in dict2:
                if dict1[key] == dict2[key]:
                    result.append(f'  {key}: {dict1[key]}')
                else:
                    result.append(f'- {key}: {dict1[key]}')
                    result.append(f'+ {key}: {dict2[key]}')
            else:
                result.append(f'- {key}: {dict1[key]}')
        else:
            result.append(f'+ {key}: {dict2[key]}')

    return '{\n ' + '\n '.join(result) + '\n}'


def main():
    parser = argparse.ArgumentParser(
        description='Generate diff'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str, )
    parser.add_argument(
        '-f', '--format',
        type=str, default='FORMAT',
        help='set format of output',
    )

    args = parser.parse_args()
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
