from gendiff.differ import CHANGED, NESTED


def render_string(key, value) -> str:
    operator = value['status'][1]
    if value['status'] == CHANGED:
        return f' {operator[0]} {key}: {value["value"][0]}\n' \
               f' {operator[1]} {key}: {value["value"][1]}'
    elif value['status'] == NESTED:
        return f' {operator} {key}: {render(value)}'
    else:
        return f' {operator} {key}: {value["value"]}'


def render(diff_dict: dict) -> str:
    """Функция форматирования словаря в строку"""
    result = [render_string(key, value) for key, value in diff_dict.items()]
    result = ['{'] + result + ['}']
    return '\n'.join(result)


def traverser_dict(data: dict, level=1):
    if not isinstance(data, dict):
        return data, level
    for key, value in data.items():
        return key, level, traverser_dict(value, level + 1)
