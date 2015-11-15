from tester import runtests

def is_unique(astring):
    letter_set = set()
    for letter in astring:
        if letter in letter_set:
            return False
        letter_set.add(letter)
    return True

tests = [
    [['this'], True],
    [['abcdefgh'], True],
    [['abcdefgha'], False],
    [['HAha'], True],
    [['blarg'], True],
    [['letters'], False],
]

runtests(tests, is_unique)
