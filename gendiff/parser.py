import json

import yaml


def parser(data, data_type):
    data_type_mapping = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    return data_type_mapping.get(data_type)(data)
