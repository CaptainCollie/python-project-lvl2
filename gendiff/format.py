from gendiff.formatters import stylish, plain, json_format


def format(diff_dict, format):
    formats_mapping = {
        'stylish': stylish.format,
        'plain': plain.format,
        'json': json_format.format
    }
    return formats_mapping.get(format, stylish.format)(diff_dict)
