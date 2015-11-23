from linkedlist import linkedlist_from_list
from tester import runtests

# is_loop should return True if there is a loop in the linked list.
# That is, if any node in the linked list points to a node earlier in the list (or itself).

def is_loop(ll):
    p1 = ll
    p2 = ll
    while p1 and p1.n:
        p1 = p1.n.n
        p2 = p2.n
        if p1 is p2:
            return True
    return False

test1 = linkedlist_from_list([1])
test1.n = test1

test2 = linkedlist_from_list([1, 2, 3, 4, 5])
test2.n.n.n.n = test2

test3 = linkedlist_from_list([1, 2, 3, 4])
test3.n.n.n = test3

test4 = linkedlist_from_list([1, 2, 3, 4])
test4.n.n.n = test4.n.n

tests = [
    [[test1], True],
    [[test2], True],
    [[test3], True],
    [[test4], True],
    [[linkedlist_from_list([1, 2, 3, 3, 4, 5])], False],
    [[linkedlist_from_list([1])], False],
    [[linkedlist_from_list([])], False],
]

runtests(tests, is_loop)
