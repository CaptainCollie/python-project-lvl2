#!/usr/bin/env python
from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()

    diff_str = generate_diff(args.first_file, args.second_file, args.format)
    print(diff_str)


if __name__ == '__main__':
    main()
