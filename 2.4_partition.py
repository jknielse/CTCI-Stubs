from linkedlist import linkedlist_from_list
from tester import runtests

# The partition function should take a linked list and a value.
# the linked list should be modified inplace such that all values
# less than the value end up in the first half of the list, and the
# values greater than or equal to the passed value end up in the
# second half of the list.

def partition(ll, val):
    # Your code here
    pass

tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5]), 3], linkedlist_from_list([1, 2, 3, 3, 4, 5])],
    [[linkedlist_from_list([3, 3, 4, 5, 1, 2]), 3], linkedlist_from_list([1, 2, 3, 3, 4, 5])],
    [[linkedlist_from_list([6, 2, 33, 3, 44, 5]), 6], linkedlist_from_list([2, 3, 5, 6, 33, 44])],
    [[linkedlist_from_list([]), 3], linkedlist_from_list([])],
    [[linkedlist_from_list([6]), 3], linkedlist_from_list([6])],
    [[linkedlist_from_list([3, 2]), 3], linkedlist_from_list([2, 3])]
]

runtests(tests, partition, inplace=True)
