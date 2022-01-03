import sys

from gendiff.parser import deserializer, parse_args
from gendiff.differ import CHANGED, collect_diff_dicts


def render_string(key, value) -> str:
    operator = value['status'][1]
    if value['status'] == CHANGED:
        return f' {operator[0]} {key}: {value["value"][0]}\n' \
               f' {operator[1]} {key}: {value["value"][1]}'
    else:
        return f' {operator} {key}: {value["value"]}'


def render(diff_dict: dict) -> str:
    """Функция форматирования словаря в строку"""
    result = [render_string(key, value) for key, value in diff_dict.items()]
    result = ['{'] + result + ['}']
    return '\n'.join(result)


def generate_diff(before_file, after_file):
    before_dict = deserializer(before_file)
    after_dict = deserializer(after_file)
    diff_dict = collect_diff_dicts(before_dict, after_dict)

    return render(diff_dict)


def main():  # pragma: no cover
    parser = parse_args(sys.argv[1:])

    if parser.first_file and parser.second_file:
        print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':  # pragma: no cover
    main()
