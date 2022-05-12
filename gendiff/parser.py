import json

import yaml


def parse(data, data_type):
    data_type_mapping = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load,
    }

    if data_type not in data_type_mapping:
        raise TypeError("Can't read this type of file")
    return data_type_mapping.get(data_type)(data)
