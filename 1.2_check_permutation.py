from tester import runtests
from collections import defaultdict

def str_to_dict(string):
    d = defaultdict(int)
    for char in string:
        d[char] += 1
    return d

def check_permutation(str1, str2):
    return str_to_dict(str1) == str_to_dict(str2)


tests = [
    [['thing', 'thang'], False],
    [['thing', 'ting'], False],
    [['thing', 'thing'], True],
    [['thing', 'gnith'], True],
    [['', ''], True],
    [['', 'blarg'], False],
    [['blarggg', 'blarg'], False],
]

runtests(tests, check_permutation)
