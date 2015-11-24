from linkedlist import linkedlist_from_list
from tester import runtests

# palindromically_reorder should modify the passed linked list inplace such that
# the i'th node of the list will be followed by the N-1-i'th node.
# Sounds confusing. Is a little. Have a look at the test cases.

def palindromically_reorder(ll):
    # Your code here
    pass


tests = [
    [[linkedlist_from_list([1, 2, 3, 4, 5])], linkedlist_from_list([1, 5, 2, 4, 3])],
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5])], linkedlist_from_list([1, 5, 2, 4, 3, 3])],
    [[linkedlist_from_list([])], linkedlist_from_list([])],
    [[linkedlist_from_list([1])], linkedlist_from_list([1])],
    [[linkedlist_from_list([1, 2])], linkedlist_from_list([1, 2])],
    [[linkedlist_from_list([1, 2, 3])], linkedlist_from_list([1, 3, 2])],
]

runtests(tests, palindromically_reorder, inplace=True)
