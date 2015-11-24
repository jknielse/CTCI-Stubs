from linkedlist import linkedlist_from_list
from tester import runtests

# palindromically_reorder should modify the passed linked list inplace such that
# the i'th node of the list will be followed by the N-1-i'th node.
# Sounds confusing. Is a little. Have a look at the test cases.

def reverse(ll):
    if not ll:
        return None

    prev = None
    while ll.n:
        n = ll.n
        ll.n = prev
        prev = ll
        ll = n
    ll.n = prev

    return ll


def ith_node(ll, i):
    while i > 0:
        i -= 1
        ll = ll.n

    return ll


def length(ll):
    counter = 0
    while ll:
        ll = ll.n
        counter += 1

    return counter

def zipll(ll1, ll2):
    while ll1:
        next_node = ll1.n
        if ll2:
            ll1.n = ll2
            ll2 = ll2.n
            ll1.n.n = next_node
        ll1 = next_node

def palindromically_reorder(ll):
    l = length(ll)
    mid_node = ith_node(ll, l/2)
    if not mid_node:
        return None
    second_half = mid_node.n
    mid_node.n = None
    rev_second_half = reverse(second_half)
    zipll(ll, rev_second_half)

tests = [
    [[linkedlist_from_list([1, 2, 3, 4, 5])], linkedlist_from_list([1, 5, 2, 4, 3])],
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5])], linkedlist_from_list([1, 5, 2, 4, 3, 3])],
    [[linkedlist_from_list([])], linkedlist_from_list([])],
    [[linkedlist_from_list([1])], linkedlist_from_list([1])],
    [[linkedlist_from_list([1, 2])], linkedlist_from_list([1, 2])],
    [[linkedlist_from_list([1, 2, 3])], linkedlist_from_list([1, 3, 2])],
]

runtests(tests, palindromically_reorder, inplace=True)
