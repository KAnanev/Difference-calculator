import sys

from gendiff.parser import get_data, parse_args

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
CHANGED = 'changed'


def collect_diff_dict(key, old_value=None, new_value=None, status=UNCHANGED, parent=None):
    collect_dict = {
        key: {
            old_value,
            new_value,
            status,
            parent,
        }
    }
    return collect_dict


def collect_dicts_on_dict(key, first_value=None, second_value=None):

    if first_value and second_value:
        if first_value == second_value:
            return collect_diff_dict(key=key, old_value=first_value)
        else:
            return collect_diff_dict(key=key, old_value=first_value, new_value=second_value, status=CHANGED)
    elif second_value:
        return collect_diff_dict(key=key, new_value=second_value, status=ADDED)
    else:
        return collect_diff_dict(key=key, old_value=first_value, status=REMOVED)


# def diff_dict(before_dict: dict, after_dict: dict) -> str:
#     keys = sorted(list(before_dict.keys() | after_dict.keys()))
#     result = '{\n'
#
#     for key in keys:
#         first_value = str(before_dict.get(key, ''))
#         second_value = str(after_dict.get(key, ''))
#         result += f'{differ(key, first_value, second_value)}\n'
#     result += '}'
#
#     return result


def generate_diff(before_file, after_file):
    before_dict = get_data(before_file)
    after_dict = get_data(after_file)

    # return diff_dict(before_dict, after_dict)


def main():  # pragma: no cover
    parser = parse_args(sys.argv[1:])

    if parser.first_file and parser.second_file:
        print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':  # pragma: no cover
    main()
