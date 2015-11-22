from linkedlist import linkedlist_from_list
from tester import runtests

# intersection should return true if the two passed linked lists
# have a shared node.

def last(ll):
    if not ll:
        return None
    while (ll.n):
        ll = ll.n

    return ll

def intersection(ll1, ll2):
    if not ll1:
        return False
    return last(ll1) is last(ll2)


test_list = linkedlist_from_list([5])
intersecting_list = linkedlist_from_list([1, 2, 3])
test_list.n = intersecting_list


tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5]), linkedlist_from_list([1, 2, 3, 3, 4, 5])], False],
    [[linkedlist_from_list([]), linkedlist_from_list([3, 4, 5])], False],
    [[linkedlist_from_list([3, 4, 5]), linkedlist_from_list([])], False],
    [[linkedlist_from_list([]), linkedlist_from_list([])], False],
    [[intersecting_list, intersecting_list], True],
    [[test_list, intersecting_list], True],
]

runtests(tests, intersection)
