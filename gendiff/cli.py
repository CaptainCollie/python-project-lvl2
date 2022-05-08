import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(metavar='first_file', type=str, dest='first_file')
    parser.add_argument(metavar='second_file', type=str, dest='second_file')
    parser.add_argument('-f', '--format', dest='format', type=str,
                        metavar='FORMAT',
                        help='set format of output', default='stylish')
    args = parser.parse_args()
    return args
