from tester import runtests
from collections import defaultdict

# is_permutation_of_plaindrome should return true if string can be permuted
# into a palindrome
# (A palindrome is a sentence/word that reads the same backwards and forwards)
# (for example, taco cat)
# Whitespace can be ignored.

def is_permutation_of_palindrome(string):
    # Your code here
    pass

tests = [
    [['tact coa'], True], 
    [['grad drag'], True],
    [['WAAARGARBLL'], False],
    [[''], True],
    [['r'], True],
    [['r '], True],
    [['rb'], False],
]

runtests(tests, is_permutation_of_palindrome)
