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


for test in [['abcdef', 'abcdef'], ['aaaaaaa', 'a7'], ['aaabbbb', 'a3b4'], ['', ''], ['aaabbbabcdefg', 'aaabbbabcdefg']]:
    if test[1] == string_compress(test[0]):
        print 'Pass'
    else:
        print 'Failure: expected "{}", got "{}"'.format(test[1], string_compress(test[0]))
