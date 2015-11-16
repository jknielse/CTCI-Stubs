from tester import _assert_equal
from linkedlist import linkedlist_from_list

# delete_middle_node deletes a node, given that the node has
# both a parent, and a child.

def delete_middle_node(node):
    # Your code here
    pass

tests = [
    [[1, 2, 3, 4, 5], 2, [1, 2, 4, 5]],
    [[1, 3, 5], 1, [1, 5]],
    [[1, 2, 3, 4, 5], 3, [1, 2, 3, 5]],
]

for test in tests:
    first_ll = linkedlist_from_list(test[0])
    pointer = first_ll
    for i in range(0, test[1] - 1):
        pointer = pointer.n
    _assert_equal(linkedlist_from_list(test[2]), first_ll)
