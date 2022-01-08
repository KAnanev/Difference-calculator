import itertools
from typing import List

from gendiff.differ import CHANGED, NESTED


def render_string(key, value, level) -> str:
    operator = value['status'][1]
    indent = '  ' * level
    # result = []
    status = value['status']
    if value['status'] == CHANGED:
        result = f'{indent} {operator[0]} {key}: {value["value"][0]}\n' \
                 f'{indent} {operator[1]} {key}: {value["value"][1]}'
    elif value['status'] == NESTED:
        result = f'{indent} {operator} {key}: {render(value["value"], level + 1)}'
    else:
        result = f'{indent} {operator} {key}: {value["value"]}'
    return result


def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):

        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def render(diff_dict: dict, level=0) -> str:
    """Функция форматирования словаря в строку"""
    # result = []
    result = [render_string(key, value, level) for key, value in diff_dict.items()]

    # for key, value in diff_dict.items():
    #     result.append(render_string(key, value, level))

    return '\n'.join(result)


def traverser_dict(data: dict, level=1):
    result = []
    for key, value in data.items():
        if isinstance(value, dict):
            return key, level, traverser_dict(value, level + 1)
        result.append([key, level, value])
    return result
