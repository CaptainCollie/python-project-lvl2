import itertools


def do_format(current_value, depth=0, replacer=' ', spaces_count=4):
    if not isinstance(current_value, dict):
        current_value = to_str(current_value)
        return str(current_value)

    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    current_indent = replacer * depth
    lines = []
    for key, val in current_value.items():
        deep_indent, key = move_sign_from_key_to_indent(deep_indent, key)
        lines.append(f'{deep_indent}{key.strip()}: '
                     f'{do_format(val, deep_indent_size)}')
        deep_indent = replacer * deep_indent_size

    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def to_str(val):
    if val is True:
        return 'true'
    if val is False:
        return 'false'
    if val is None:
        return 'null'
    return val


def move_sign_from_key_to_indent(indent, key):
    sign = ''
    if '-' in key:
        sign = '-'
    if '+' in key:
        sign = '+'
    if sign:
        indent = indent[:-2] + sign + indent[-1:]
        key = key.replace(sign, '')
    return indent, key
