import json


def render_json(arr: dict):
    """Рендерит JSON"""
    json_object = json.dumps(arr, indent=4)
    return json_object
