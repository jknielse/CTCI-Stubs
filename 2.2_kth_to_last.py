from linkedlist import linkedlist_from_list
from tester import runtests

def kth_from_last(k, ll):
    length = 0
    list_pointer = ll
    while list_pointer:
        length += 1
        list_pointer = list_pointer.n

    if k >= length:
        return None

    count = length - 1 - k
    list_pointer = ll
    while count:
        list_pointer = list_pointer.n
        count -= 1

    return list_pointer.val

tests = [
    [[5, linkedlist_from_list([1, 2, 3, 3, 4, 5])], 1],
    [[0, linkedlist_from_list([5, 4, 3, 2, 5 ,1])], 1],
    [[1, linkedlist_from_list([1, 1])], 1],
    [[0, linkedlist_from_list([1])], 1],
    [[2, linkedlist_from_list(['always', 'always', 'remove', 'duplicates'])], 'always'],
    [[1, linkedlist_from_list([1, 2, 3, 1, 3, 0])], 3]
]

runtests(tests, kth_from_last)
