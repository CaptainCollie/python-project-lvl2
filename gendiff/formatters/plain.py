from typing import Dict, Union


def do_format(diff_dict: dict):
    result = '\n'.join(plain(diff_dict))
    return result


def plain(d: Dict[str, Union[str, dict]], prev_key: str = '') -> list:
    result = []
    processed_keys = set()
    prev_key += '.' if prev_key else ''
    for key, value in d.items():
        if key.startswith('  ') and isinstance(value, dict):
            key = key.replace('  ', '')
            result.extend(plain(value, f'{prev_key}{key}'))
        elif key.startswith('- ') and key.replace('- ', '+ ') in d:
            value = to_str(value)
            value_with_same_key_other_sign = d.get(key.replace('- ', '+ '))
            value_with_same_key_other_sign = to_str(
                value_with_same_key_other_sign)
            processed_keys.add(key.replace('- ', '+ '))
            key = key.replace('- ', '')
            result.append(
                f"Property '{prev_key}{key}' was updated. "
                f"From {value} to {value_with_same_key_other_sign}")
        elif key.startswith('+ ') and key not in processed_keys:
            value = to_str(value)
            key = key.replace('+ ', '')
            result.append(f"Property '{prev_key}{key}' "
                          f"was added with value: {value}")
        elif key.startswith('- '):
            key = key.replace('- ', '')
            result.append(f"Property '{prev_key}{key}' was removed")
    return result


def to_str(val):
    if isinstance(val, dict):
        val = '[complex value]'
    elif isinstance(val, str):
        return f"'{val}'"
    elif val is True:
        return 'true'
    elif val is False:
        return 'false'
    elif val is None:
        return 'null'
    return val
