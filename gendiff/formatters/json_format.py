import json


def do_format(diff_dict):
    result = json.dumps(diff_dict, indent=2)
    return result
