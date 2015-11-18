from tester import runtests

def urlify(string):
    # string is a bit of a misnomer, it's actually a list, but w/e.
    read_index = len(string) - 1
    while read_index >= 0 and string[read_index] == ' ':
        read_index -= 1

    write_index = len(string) - 1
    while read_index >= 0:
        if string[read_index] == ' ':
            string[write_index] = '0'
            string[write_index - 1] = '2'
            string[write_index - 2] = '%'
            write_index -= 3
        else:
            string[write_index] = string[read_index]
            write_index -= 1
        read_index -= 1


tests = [
    [[list('this is a url string        ')], list('this%20is%20a%20url%20string')],
    [[list('smalltest')], list('smalltest')], 
    [[list('')], list('')], 
    [[list(' b  ')], list('%20b')],
    [[list('blarg arg  ')], list('blarg%20arg')],
]

runtests(tests, urlify, inplace=True)
