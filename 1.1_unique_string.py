
def is_unique(astring):
    letter_set = set()
    for letter in astring:
        if letter in letter_set:
            return False
        letter_set.add(letter)
    return True


for test in ['this', 'abcdefgh', 'abcdefgha', 'HAha', 'blarg', 'letters']:
    print 'Checking "{}"'.format(test)
    print is_unique(test)
