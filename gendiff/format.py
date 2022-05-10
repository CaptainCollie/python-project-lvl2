from gendiff.formatters import stylish, plain, json_format


def format(diff_dict, format):
    formats_mapping = {
        'stylish': stylish.do_format,
        'plain': plain.do_format,
        'json': json_format.do_format
    }
    return formats_mapping.get(format, stylish.do_format)(diff_dict)
