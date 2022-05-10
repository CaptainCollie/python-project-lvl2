from gendiff.dicts_difference import generate_dicts_diff
from gendiff.file import read, get_file_extension
from gendiff.format import format
from gendiff.parser import parser


def generate_diff(first_source, second_source, formatter='stylish'):
    """Generates diff"""
    data = map(read, (first_source, second_source))
    data_types = map(get_file_extension, (first_source, second_source))
    dicts = map(lambda x: parser(*x), zip(data, data_types))
    diff_dict = generate_dicts_diff(*dicts)
    return format(diff_dict, formatter)
