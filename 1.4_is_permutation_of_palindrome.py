from tester import runtests
from collections import defaultdict

def str_to_dict(string):
    d = defaultdict(int)
    for char in string:
        d[char] += 1
    return d

def is_permutation_of_plaindrome(string):
    newstring = string.replace(' ', '')
    d = str_to_dict(newstring)
    had_odd = False
    for k in d:
        v = d[k]
        if v % 2 == 1:
            if had_odd:
                return False
            else:
                had_odd = True
    return True

tests = [
    [['tact coa'], True], 
    [['grad drag'], True],
    [['WAAARGARBLL'], False],
    [[''], True],
    [['r'], True],
    [['r '], True],
    [['rb'], False],
]

runtests(tests, is_permutation_of_plaindrome)
