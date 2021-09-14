import json
import argparse


def open_file(path):
    """ Открывает файл десериализует JSON"""
    with open(path) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    """ Получает путь к двум файлам,
    сравнивает их и возвращает строку разности"""

    result = []
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)

    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    set_ = set1.union(set2)

    for key in sorted(list(set_)):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result.append(f'  {key}: {dict1[key]}')
            else:
                result.append(f'- {key}: {dict1[key]}')
                result.append(f'+ {key}: {dict2[key]}')
        if key not in dict2:
            result.append(f'- {key}: {dict1[key]}')
        if key not in dict1:
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
