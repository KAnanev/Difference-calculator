import sys

from gendiff.parser import get_data, parse_args


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


def generate_diff(before_file, after_file):
    before_dict = get_data(before_file)
    after_dict = get_data(after_file)

    return diff_dict(before_dict, after_dict)


def main():  # pragma: no cover
    parser = parse_args(sys.argv[1:])

    if parser.first_file and parser.second_file:
        print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':  # pragma: no cover
    main()
