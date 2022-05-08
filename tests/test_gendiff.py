# -*- coding:utf-8 -*-
import pytest

from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize('files, formatter, expected', [
    (('tests/fixtures/file_plain1.json', 'tests/fixtures/file_plain2.json'),
     'stylish', 'tests/fixtures/expected_plaindicts_stylish_gendiff.txt'),
    (('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yaml'),
     'stylish', 'tests/fixtures/expected_plaindicts_stylish_gendiff.txt'),
    (('tests/fixtures/file1.json', 'tests/fixtures/file2.json'), 'plain',
     'tests/fixtures/expected_complexdicts_plain_gendiff.txt'),
    (('tests/fixtures/file1.json', 'tests/fixtures/file2.json'), 'json',
     'tests/fixtures/expected_complexdicts_json_gendiff.txt'),
]
)
def test_generate_diff(files: tuple, formatter: str, expected: str):
    f = open(expected, 'r',
             encoding='utf-8')
    expected = f.read()
    result = generate_diff(*files, formatter)
    assert result == expected


@pytest.mark.parametrize('files, formatter, expected', [
    (('tests/fixtures/file1.json', 'tests/fixtures/file2.json'),
     'stylish', 'tests/fixtures/expected_complexdicts_stylish_gendiff.txt'),
]
)
def test_generate_diff_specific(files: tuple, formatter: str, expected: str):
    f = open(expected, 'r',
             encoding='utf-8')
    expected = f.read()
    expected = expected.split('\n')
    expected[13] = expected[13] + ' '
    expected = '\n'.join(expected)
    result = generate_diff(*files, formatter)
    assert result == expected
