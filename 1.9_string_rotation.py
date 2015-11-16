from tester import runtests

def is_rotation(s1, s2):
    # This is gross. What is the correct way to do this?
    global used_once
    used_once = False

    def is_substring(s1, s2):
        global used_once
        if not used_once:
            used_once = True
            return s1 in s2
        raise Exception('Cheater cheater pumkin eater')

    return len(s1) == len(s2) and is_substring(s2, s1 + s1)


tests = [
    [['is this a rotation?', 'rotation?is this a '], True],
    [['is this a rotation?', 'rotation?is this a  '], False],
    [['\'Twas then that the hurdy gurdy man came singing songs of love\'Twas then that the hurdy gurdy man came singing songs of love', '\'Twas then that the hurdy gurdy man came singing songs of love'], False],
    [['shakira', 'shakirashakira'], False],
    [['blargg', 'gblarg'], True],
    [['',''], True],
    [['Oh baby when you talk like that', ''], False]
]

runtests(tests, is_rotation)