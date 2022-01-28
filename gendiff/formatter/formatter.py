from gendiff.formatter.json import render_json
from gendiff.formatter.plain import render_plain
from gendiff.formatter.stylish import render_stylish

STYLE_MAP = {
    'stylish': render_stylish,
    'plain': render_plain,
    'json': render_json,
}


def render(diff_dict, style):
    """Рендерит выходные данные"""
    return STYLE_MAP.get(style)(diff_dict)
