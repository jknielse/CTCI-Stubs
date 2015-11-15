class linkedlist(object):
    def __init__(self, val, n=None):
        self.val = val
        self.n = n

    def __str__(self):
        return_string = '['
        l = self
        while l:
            return_string += '{}, '.format(l.val)
            l = l.n
        return_string = return_string[:-2]
        return_string += ']'
        return return_string

    def __eq__(self, other):
        return _equal(self, other)


def linkedlist_from_list(l):
    head_of_list = None
    prev_item = None
    for thing in l:
        if not head_of_list:
            head_of_list = linkedlist(thing)
            prev_item = head_of_list
        else:
            new_item = linkedlist(thing)
            prev_item.n = new_item
            prev_item = new_item

    return head_of_list

# Compares linked lists
def _equal(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.n
        l2 = l2.n
    return l1 is l2