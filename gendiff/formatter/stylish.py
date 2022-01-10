import itertools

from gendiff.differ import CHANGED, NESTED


def dict_to_str(data: dict or str, level) -> str:
    """Форматирует вложенные словари в значениях"""
    if not isinstance(data, dict):
        return data
    indent = '    ' * level
    lines = []
    for key, val in data.items():
        lines.append(f'{indent}    {key}: {dict_to_str(val, level + 1)}')
    result = itertools.chain("{", lines, [indent + "}"])
    return '\n'.join(result)


def render_string(key, value, level) -> str:
    """Форматирует AST словари в строки"""
    operator = value['status'][1]
    indent = '    ' * level

    if value['status'] == CHANGED:
        result = f'{indent}  {operator[0]} {key}: ' \
                 f'{dict_to_str(value["value"][0], level + 1)}\n' \
                 f'{indent}  {operator[1]} {key}: ' \
                 f'{dict_to_str(value["value"][1], level + 1)}'
    elif value['status'] == NESTED:
        result = f'{indent}  {operator} {key}: ' \
                 f'{render_stylish(value["value"], level + 1)}'
    else:
        result = f'{indent}  {operator} {key}: ' \
                 f'{dict_to_str(value["value"], level + 1)}'
    return result


def render_stylish(diff_dict: dict, level=0) -> str:
    """Форматирует AST в текст"""
    indent = '    ' * level

    result = [
        render_string(key, value, level) for key, value in diff_dict.items()
    ]
    result = itertools.chain("{", result, [indent + "}"])

    return '\n'.join(result)
