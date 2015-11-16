from tester import runtests

# check_permutation should return true if str1 is a permutation of str2
# a permutation means that the letters are all the same, but may be rearanged.

def check_permutation(str1, str2):
    # Your code here
    pass

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
