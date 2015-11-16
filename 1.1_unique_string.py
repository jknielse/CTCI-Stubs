from tester import runtests

# is_unique should return true if there are no duplicate characters in astring

def is_unique(astring):
    # Your code here
    pass

tests = [
    [['this'], True],
    [['abcdefgh'], True],
    [['abcdefgha'], False],
    [['HAha'], True],
    [['blarg'], True],
    [['letters'], False],
    [[''], True],
]

runtests(tests, is_unique)
