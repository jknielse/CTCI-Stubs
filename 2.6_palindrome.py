from linkedlist import linkedlist_from_list
from tester import runtests

# palindrome should return True if ll represents a palindrome.

def palindrome(ll):
    # Your code here
    pass

tests = [
    [[linkedlist_from_list([1, 2, 3, 2, 1])], True],
    [[linkedlist_from_list([1, 2, 3, 3, 2, 1])], True],
    [[linkedlist_from_list([1, 2, 3, 4, 2, 1])], False],
    [[linkedlist_from_list([1, 2, 3, 3, 2, 2])], False],
    [[linkedlist_from_list([1, 2])], False],
    [[linkedlist_from_list([1])], True],
    [[linkedlist_from_list([])], True]
]

runtests(tests, palindrome)
