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



for test in [['this is a url string        ', 'this%20is%20a%20url%20string'], ['smalltest', 'smalltest'], ['', ''], ['blarg arg  ', 'blarg%20arg']]:
    var = list(test[0])
    urlify(var)
    if test[1] == ''.join(var):
        print 'Pass'
    else:
        print 'Failure: expected "{}", got "{}"'.format(test[1], ''.join(var))
