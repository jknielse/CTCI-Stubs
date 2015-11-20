from linkedlist import linkedlist_from_list
from tester import runtests

# palindrome should return True if ll represents a palindrome.

def palindrome(ll):
    saved_values = []
    cursor = ll
    while cursor:
        saved_values.append(cursor.val)
        cursor = cursor.n

    cursor = ll
    while cursor:
        if cursor.val != saved_values.pop():
            return False
        cursor = cursor.n

    return True

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
