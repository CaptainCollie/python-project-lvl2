from gendiff.difference import diff
from gendiff.parser import parser
from gendiff.format import format
from gendiff.read_file import read_file


def generate_diff(first_source, second_source, formatter='stylish'):
    """Generates diff"""
    raw_data = (read_file(first_source), read_file(second_source))
    dicts = map(lambda x: parser(*x), raw_data)
    diff_d = diff(*dicts)
    return format(diff_d, formatter)
