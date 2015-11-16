from tester import runtests

# is_one_away should return true if str1 can be modified to be equal to str2
# using only one insertion, one deletion, or one modification (of one character).

def is_one_away(str1, str2):
    # Your code here
    pass

tests = [
    [['blarg', 'blarg'], True],
    [['blar', 'blarg'], True],
    [['bla', 'blarg'], False],
    [['', 'b'], True],
    [['brarg', 'blarg'], True],
    [['blrarg', 'blarg'], True],
    [['', ''], True],
    [['blarg', 'blargg'], True],
    [['blarg', 'blarggg'], False],
]

runtests(tests, is_one_away)
