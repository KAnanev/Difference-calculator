from gendiff.formatter.plain import render_plain
from gendiff.formatter.stylish import render_stylish

STYLE_MAP = {
    'stylish': render_stylish,
    'plain': render_plain
}


def render(diff_dict, style):
    return STYLE_MAP.get(style)(diff_dict)
