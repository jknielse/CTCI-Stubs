from linkedlist import linkedlist_from_list
from tester import runtests

# remove_dups should modify ll inplace to remove any nodes of the linked list
# with duplicate values.

def remove_dups(ll):
    # Your code here
    pass

tests = [
    [linkedlist_from_list([1, 2, 3, 3, 4, 5]), linkedlist_from_list([1, 2, 3, 4, 5])],
    [linkedlist_from_list([5, 4, 3, 2, 5 ,1]), linkedlist_from_list([5, 4, 3, 2, 1])],
    [linkedlist_from_list([1, 1]), linkedlist_from_list([1])],
    [linkedlist_from_list([1]), linkedlist_from_list([1])],
    [linkedlist_from_list(['always', 'always', 'remove', 'duplicates']), linkedlist_from_list(['always', 'remove', 'duplicates'])],
    [linkedlist_from_list([]), linkedlist_from_list([])],
    [linkedlist_from_list([1, 2, 3, 1, 3, 0]), linkedlist_from_list([1, 2, 3, 0])]
]

runtests(tests, remove_dups, inplace=True)
