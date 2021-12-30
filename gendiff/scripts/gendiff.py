import sys
from typing import Union

from gendiff.parser import get_data, parse_args

ADDED = ('added', '+',)
REMOVED = ('removed', '-',)
UNCHANGED = ('unchanged', ' ',)
CHANGED = ('changed', '-+',)


def bool_to_string(value: bool) -> not bool:
    """Функция преобразования булева значения в строку"""
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_diff_value(old_value: Union[str, None, dict],
                   new_value: Union[str, None, dict]) -> dict:
    """Функция разности двух значений"""
    if not old_value:
        return {
            'status': ADDED,
            'value': new_value,
        }

    elif not new_value:
        return {
            'status': REMOVED,
            'value': old_value,
        }

    elif old_value == new_value:
        return {
            'status': UNCHANGED,
            'value': old_value,
        }

    elif old_value != new_value:
        return {
            'status': CHANGED,
            'value': (old_value, new_value)
        }


def collect_diff_dicts(old_dict: dict, new_dict: dict) -> dict:
    """Функция разности двух словарей"""
    keys = list(old_dict.keys() | new_dict.keys())
    return {
        key: get_diff_value(
            bool_to_string(old_dict.get(key)), bool_to_string(new_dict.get(key))
        ) for key in sorted(keys)
    }


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
    before_dict = get_data(before_file)
    after_dict = get_data(after_file)
    diff_dict = collect_diff_dicts(before_dict, after_dict)

    return render(diff_dict)


def main():  # pragma: no cover
    parser = parse_args(sys.argv[1:])

    if parser.first_file and parser.second_file:
        print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':  # pragma: no cover
    main()
