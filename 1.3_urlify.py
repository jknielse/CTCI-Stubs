from tester import runtests

# urlify should take in a list of characters, and replace spaces with '%20'.
# it must do this inplace, but is guaranteed that there will be trailing
# whitespace to accomodate the extra characters that will need to be written.

def urlify(lstring):
    # Your code here
    pass

tests = [
    [[list('this is a url string        ')], list('this%20is%20a%20url%20string')],
    [[list('smalltest')], list('smalltest')], 
    [[list('')], list('')], 
    [[list(' b  ')], list('%20b')],
    [[list('blarg arg  ')], list('blarg%20arg')],
]

runtests(tests, urlify, inplace=True)
