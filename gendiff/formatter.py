import itertools
from typing import List

from gendiff.differ import CHANGED, NESTED


def dict_to_str(data: dict or str, level) -> str:
    if not isinstance(data, dict):
        return data
    indent = '  ' * level
    lines = []
    for key, val in data.items():
        lines.append(f'{indent}   {key}: {dict_to_str(val, level + 1)}')
    result = itertools.chain("{", lines, [indent + " }"])
    return '\n'.join(result)


def render_string(key, value, level) -> str:
    operator = value['status'][1]
    indent = '  ' * level

    if value['status'] == CHANGED:
        result = f'{indent} {operator[0]} {key}: {dict_to_str(value["value"][0], level + 1)}\n' \
                 f'{indent} {operator[1]} {key}: {dict_to_str(value["value"][1], level + 1)}'
    elif value['status'] == NESTED:
        result = f'{indent} {operator} {key}: {render(value["value"], level + 1)}'
    else:
        result = f'{indent} {operator} {key}: {dict_to_str(value["value"], level + 1)}'
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
    indent = '     ' * level

    result = [render_string(key, value, level) for key, value in diff_dict.items()]
    result = itertools.chain("{", result, [indent + "}"])

    return '\n'.join(result)


def traverser_dict(data: dict, level=1):
    result = []
    for key, value in data.items():
        if isinstance(value, dict):
            return key, level, traverser_dict(value, level + 1)
        result.append([key, level, value])
    return result
