from tester import runtests

def prune_same(str1, str2):
    i = 0
    end = min(len(str1), len(str2))
    while (i < end and str1[i] == str2[i]):
        i += 1

    return (str1[i:], str2[i:])


def is_one_away(str1, str2):
    (newstr1, newstr2) = prune_same(list(str1), list(str2))
    newstr1.reverse()
    newstr2.reverse()
    (newstr1, newstr2) = prune_same(''.join(newstr1), ''.join(newstr2))
    return abs(len(newstr2) - len(newstr1)) <= 1

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
