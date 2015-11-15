from collections import defaultdict

def str_to_dict(string):
    d = defaultdict(int)
    for char in string:
        d[char] += 1
    return d

def check_permutation(str1, str2):
    return str_to_dict(str1) == str_to_dict(str2)


for test in [['thing', 'thang'], ['thing', 'ting'], ['thing', 'thing'], ['thing', 'gnith']]:
    print '{} {}'.format(*test)
    print check_permutation(*test)
