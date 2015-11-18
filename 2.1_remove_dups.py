from linkedlist import linkedlist_from_list
from tester import runtests

def remove_dups(ll):
    repeat_values = set()
    while ll:
        repeat_values.add(ll.val)
        if ll.n and ll.n.val in repeat_values:
            ll.n = ll.n.n
        else:
            ll = ll.n

tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5])], linkedlist_from_list([1, 2, 3, 4, 5])],
    [[linkedlist_from_list([5, 4, 3, 2, 5 ,1])], linkedlist_from_list([5, 4, 3, 2, 1])],
    [[linkedlist_from_list([1, 1])], linkedlist_from_list([1])],
    [[linkedlist_from_list([1])], linkedlist_from_list([1])],
    [[linkedlist_from_list(['always', 'always', 'remove', 'duplicates'])], linkedlist_from_list(['always', 'remove', 'duplicates'])],
    [[linkedlist_from_list([])], linkedlist_from_list([])],
    [[linkedlist_from_list([1, 2, 3, 1, 3, 0])], linkedlist_from_list([1, 2, 3, 0])]
]

runtests(tests, remove_dups, inplace=True)
