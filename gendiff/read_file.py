import os


def read_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return f.read(), os.path.splitext(path_to_file)[-1]
