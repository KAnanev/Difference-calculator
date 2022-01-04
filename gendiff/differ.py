ADDED = ('added', '+',)
REMOVED = ('removed', '-',)
UNCHANGED = ('unchanged', ' ',)
CHANGED = ('changed', '-+',)
NESTED = ('nested', ' ')


def collect_dict(status, value):
    """Собирает значение словаря разностей"""
    return {
        'status': status,
        'value': value,
    }


def add_(*args):
    return collect_dict(ADDED, args[1])


def rm_(*args):
    return collect_dict(REMOVED, args[0])


def un_change_(*args):
    return collect_dict(UNCHANGED, args[1])


def change_(*args):
    return collect_dict(CHANGED, args)


def diff_dicts_(*args):
    return collect_dict(NESTED[0], collect_diff_dicts(*args))


ACTION_STATUS = {
    (True, False): rm_,
    (False, True): add_,
    True: un_change_,
    False: change_,
    (True, True): diff_dicts_,

}


def check_string(value):
    """Проверка значения и приведение к строке"""
    mapping = {
        None: 'null',
        True: 'true',
        False: 'false',
        'empty': None,
    }
    if type(value) in (float, int):
        return value
    return mapping.get(value, value)


def get_value(data, key):
    """Нормализует значение"""
    value = data.get(key, 'empty')
    return check_string(value)


def get_diff_value(old_value, new_value):
    """Получает разность двух значений"""

    if old_value and new_value:
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            diff_values = ACTION_STATUS.get((bool(old_value), bool(new_value)))
        else:
            diff_values = ACTION_STATUS.get(old_value == new_value)
    else:
        diff_values = ACTION_STATUS.get((bool(old_value), bool(new_value)))

    return diff_values(old_value, new_value)


def collect_diff_dicts(old_dict: dict, new_dict: dict) -> dict:
    """Собирает разность двух словарей"""
    sorted_keys = sorted(list(old_dict.keys() | new_dict.keys()))
    return {
        key: get_diff_value(
            get_value(old_dict, key), get_value(new_dict, key)
        ) for key in sorted_keys
    }
