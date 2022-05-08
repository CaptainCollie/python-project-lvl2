from gendiff.formatters import stylish, plain, json_format


def format(diff_d, formatter):
    formats_mapping = {
        'stylish': stylish.format,
        'plain': plain.format,
        'json': json_format.format
    }
    return formats_mapping.get(formatter)(diff_d)
