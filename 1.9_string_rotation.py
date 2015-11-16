from tester import runtests

# A rotated string is a string that has been scrolled in a direction with
# wrap-around. (see below for examples.)
# Implement is_rotation such that it uses the is_substring function exactly
# once to determine whether s1 is a rotation of s2.

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

    # Your code here


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