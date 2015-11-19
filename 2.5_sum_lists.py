from linkedlist import linkedlist_from_list
from tester import runtests

# sum_lists should take two linked lists, treat them as if they were decimal numbers,
# and return a list that represents the sum of those numbers. (see tests for examples)

def sum_lists(l1, l2):
    # Your code here
    pass

tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4]), linkedlist_from_list([1, 2, 3, 3, 4])], linkedlist_from_list([2, 4, 6, 6, 8])],
    [[linkedlist_from_list([1, 5, 0]), linkedlist_from_list([1, 5, 0])], linkedlist_from_list([3, 0, 0])],
    [[linkedlist_from_list([9, 9]), linkedlist_from_list([1])], linkedlist_from_list([1, 0, 0])],
    [[linkedlist_from_list([9]), linkedlist_from_list([9])], linkedlist_from_list([1, 8])],
    [[linkedlist_from_list([]), linkedlist_from_list([])], linkedlist_from_list([])],
    [[linkedlist_from_list([9, 9, 9, 9, 9]), linkedlist_from_list([2])], linkedlist_from_list([1, 0, 0, 0, 0, 1])],
    [[linkedlist_from_list([1, 0, 0, 0, 0]), linkedlist_from_list([2])], linkedlist_from_list([1, 0, 0, 0, 0, 2])],
]

runtests(tests, sum_lists)
