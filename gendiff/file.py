import os.path


def read(path):
    with open(path, 'r') as f:
        return f.read()


def get_file_extension(path):
    return os.path.splitext(path)[-1].replace('.', '')
