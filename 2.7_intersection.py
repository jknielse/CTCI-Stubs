from linkedlist import linkedlist_from_list
from tester import runtests

# intersection should return true if the two passed linked lists
# have a shared node.

def intersection(ll1, ll2):
    # Your code here
    pass


test_list = linkedlist_from_list([5])
intersecting_list = linkedlist_from_list([1, 2, 3])
test_list.n = intersecting_list


tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5]), linkedlist_from_list([1, 2, 3, 3, 4, 5])], False],
    [[linkedlist_from_list([]), linkedlist_from_list([3, 4, 5])], False],
    [[linkedlist_from_list([]), linkedlist_from_list([])], False],
    [[intersecting_list, intersecting_list], True],
    [[test_list, intersecting_list], True],
]

runtests(tests, intersection)
