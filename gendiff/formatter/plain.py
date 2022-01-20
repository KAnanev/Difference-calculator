def removed(*args):
    string_ = f"Property '{args[0]}' was removed"
    return string_


def changed(path, value):
    string_ = f"Property '{path}' was updated. " \
              f"From {validated_value(value[0])} to {validated_value(value[1])}"
    return string_


def added(path, value):
    string_ = f"Property '{path}' was added " \
              f"with value: {validated_value(value)}"
    return string_


def nested(path, value):
    return render_plain(value, path)


mapping = {
    'removed': removed,
    'changed': changed,
    'added': added,
    'nested': nested,
}


def render_plain(arr: dict, path=None) -> str:
    re = [render_plain_string(k, v, path) for k, v in arr.items()]
    return '\n'.join(filter(None, re))


def render_plain_string(key: str, value: dict, path) -> str:
    status = value['status'][0]
    value = value['value']
    path = '.'.join(filter(None, [path, key]))
    f = mapping.get(status)
    if f:
        return f(path, value)


def validated_value(value: dict or str) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    if value in ['true', 'false', 'null']:
        return value
    if isinstance(value, str):
        return f"'{value}'"
    return value
