from tester import runtests

def string_compress(string):
    """
    replaces runs of characters with the character followed by the number
    of character. If that would be longer than the original string, then
    it returns the original string.
    """
    
    newstring = ''
    i = 0
    
    while i < len(string):
        cur_char = string[i]
        counter = 0
        while i < len(string) and string[i] == cur_char:
            counter += 1
            i += 1
        newstring += '{}{}'.format(cur_char, counter)

    if len(newstring) < len(string):
        return newstring
    return string

tests = [
    [['abcdef'], 'abcdef'], 
    [['aaaaaaa'], 'a7'],
    [['aaabbbb'], 'a3b4'],
    [[''], ''],
    [['aaabbbabcdefg'], 'aaabbbabcdefg'],
    [['aaabbbabcdefgggggggggggggggggggggggg'], 'a3b3a1b1c1d1e1f1g24'],
]

runtests(tests, string_compress)
