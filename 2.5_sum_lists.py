from linkedlist import linkedlist_from_list, linkedlist
from tester import runtests

# sum_lists should take two linked lists, treat them as if they were decimal numbers,
# and return a list that represents the sum of those numbers. (see tests for examples)

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


def sum_lists(l1, l2):
    # This is pretty destructive and gross, but it works :/
    # I should really put them back in order at the end.
    # Side-effects are gross.
    l1 = reverse(l1)
    l2 = reverse(l2)
    new_sum_l = None
    sum_l = None
    carry = 0

    while l1 or l2:
        l1_val = 0 if not l1 else l1.val
        l2_val = 0 if not l2 else l2.val
        total = l1_val + l2_val + carry
        carry = total / 10
        new_sum_l = linkedlist(total % 10, sum_l)
        sum_l = new_sum_l
        if l1:
            l1 = l1.n
        if l2:
            l2 = l2.n

    if carry:
        new_sum_l = linkedlist(carry, sum_l)

    return new_sum_l

tests = [
    [[linkedlist_from_list([1, 2, 3, 3, 4]), linkedlist_from_list([1, 2, 3, 3, 4])], linkedlist_from_list([2, 4, 6, 6, 8])],
    [[linkedlist_from_list([1, 5, 0]), linkedlist_from_list([1, 5, 0])], linkedlist_from_list([3, 0, 0])],
    [[linkedlist_from_list([9, 9]), linkedlist_from_list([1])], linkedlist_from_list([1, 0, 0])],
    [[linkedlist_from_list([9]), linkedlist_from_list([9])], linkedlist_from_list([1, 8])],
    [[linkedlist_from_list([]), linkedlist_from_list([])], linkedlist_from_list([])],
    [[linkedlist_from_list([9, 9, 9, 9, 9]), linkedlist_from_list([2])], linkedlist_from_list([1, 0, 0, 0, 0, 1])],
    [[linkedlist_from_list([1, 0, 0, 0, 0]), linkedlist_from_list([2])], linkedlist_from_list([1, 0, 0, 0, 2])],
]

runtests(tests, sum_lists)
