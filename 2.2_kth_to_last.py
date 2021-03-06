from linkedlist import linkedlist_from_list
from tester import runtests

# kth_from_last should return the k-th-from-last element in the linked list ll.

def kth_from_last(k, ll):
    # Your code here
    pass

tests = [
    [[5, linkedlist_from_list([1, 2, 3, 3, 4, 5])], 1],
    [[0, linkedlist_from_list([5, 4, 3, 2, 5 ,1])], 1],
    [[1, linkedlist_from_list([1, 1])], 1],
    [[0, linkedlist_from_list([1])], 1],
    [[2, linkedlist_from_list(['always', 'always', 'remove', 'duplicates'])], 'always'],
    [[1, linkedlist_from_list([1, 2, 3, 1, 3, 0])], 3]
]

runtests(tests, kth_from_last)
