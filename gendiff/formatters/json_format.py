import json


def format(diff):
    return json_formatter(diff)


def json_formatter(diff_d):
    result = json.dumps(diff_d, indent=2)
    return result
