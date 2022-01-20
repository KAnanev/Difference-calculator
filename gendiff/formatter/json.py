import json


def render_json(arr: dict):
    json_object = json.dumps(arr, indent=4)
    return json_object
