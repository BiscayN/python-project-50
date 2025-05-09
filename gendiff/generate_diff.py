from gendiff.formatters import formatting_diff
from gendiff.get_diff import get_diff
from gendiff.read import reader


def generate_diff(path1, path2, format='stylish'):
    file1 = reader(path1)
    file2 = reader(path2)
    diff = get_diff(file1, file2)
    return formatting_diff(diff, format)
