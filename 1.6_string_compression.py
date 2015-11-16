from tester import runtests

# string_compress should return a string that has had any runs of letters
# condensed into just that letter, followed by the number of that letter.
# for example, 'aaaaaaa' -> 'a7', 'aaabbbb' -> 'a3b4'
# If the "compressed" string is larger than the original string,
# the function should instead return the original string.

def string_compress(string):
    # Your code here
    pass

tests = [
    [['abcdef'], 'abcdef'], 
    [['aaaaaaa'], 'a7'],
    [['aaabbbb'], 'a3b4'],
    [[''], ''],
    [['aaabbbabcdefg'], 'aaabbbabcdefg'],
    [['aaabbbabcdefgggggggggggggggggggggggg'], 'a3b3a1b1c1d1e1f1g24'],
]

runtests(tests, string_compress)
