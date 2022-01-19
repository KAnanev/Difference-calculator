def removed(*args):
    string_ = f"Property '{args[0]}' was removed"
    return string_


def changed(key, value):
    string_ = f"Property '{key}' was updated. From {value[0]} to {value[1]}"
    return string_


def added(key, value):
    string_ = f"Property '{key}' was added with value: '{value}'"
    return string_


mapping = {
    'removed': removed,
    'changed': changed,
    'added': added,
}


def render_plain(arr: dict) -> str:
    re = [render_plain_string(k, v) for k, v in arr.items()]
    return '\n'.join(filter(None, re))


def render_plain_string(key: str, value: dict) -> str:
    status = value['status'][0]
    value = value['value']
    f = mapping.get(status)
    if f:
        return f(key, value)
