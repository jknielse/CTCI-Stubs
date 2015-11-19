from linkedlist import linkedlist_from_list
from tester import runtests

# The partition function should take a linked list and a value.
# the linked list should be modified inplace such that all values
# less than the value end up in the first half of the list, and the
# values greater than or equal to the passed value end up in the
# second half of the list.

def swap(l1, l2):
    val = l2.val
    l2.val = l1.val
    l1.val = val


def partition_better(ll, val):
    lp = ll
    gp = ll

    while lp:
        # advance gp until it hits a value greater than or equal to val
        while gp and gp.val < val:
            gp = gp.n

        lp = gp
        # advance lp past gp until we hit a value less than val
        while lp and lp.val >= val:
            lp = lp.n

        # if we hit something, swap the values.
        if lp:
            swap(lp, gp)


def partition(ll, val):
    lvals = []
    rvals = []
    head = ll
    
    while ll:
        if ll.val < val:
            lvals.append(ll.val)
        else:
            rvals.append(ll.val)
        ll = ll.n

    ll = head
    while (lvals):
        ll.val = lvals.pop(0)
        ll = ll.n

    while (rvals):
        ll.val = rvals.pop(0)
        ll = ll.n


tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5]), 3], linkedlist_from_list([1, 2, 3, 3, 4, 5])],
    [[linkedlist_from_list([3, 3, 4, 5, 1, 2]), 3], linkedlist_from_list([1, 2, 3, 3, 4, 5])],
    [[linkedlist_from_list([6, 2, 33, 3, 44, 5]), 6], linkedlist_from_list([2, 3, 5, 6, 33, 44])],
    [[linkedlist_from_list([]), 3], linkedlist_from_list([])],
    [[linkedlist_from_list([6]), 3], linkedlist_from_list([6])],
    [[linkedlist_from_list([3, 2]), 3], linkedlist_from_list([2, 3])]
]

runtests(tests, partition, inplace=True)

# Sigh, these tests totally assume a particular implementation. This makes me sad.
second_tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5]), 3], linkedlist_from_list([1, 2, 3, 3, 4, 5])],
    [[linkedlist_from_list([3, 3, 4, 5, 1, 2]), 3], linkedlist_from_list([1, 2, 4, 5, 3, 3])],
    [[linkedlist_from_list([6, 2, 33, 3, 44, 5]), 6], linkedlist_from_list([2, 3, 5, 6, 44, 33])],
    [[linkedlist_from_list([]), 3], linkedlist_from_list([])],
    [[linkedlist_from_list([6]), 3], linkedlist_from_list([6])],
    [[linkedlist_from_list([3, 2]), 3], linkedlist_from_list([2, 3])]
]

runtests(second_tests, partition_better, inplace=True)
