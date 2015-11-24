from tester import runtests
from stack import Stack

# implement a data structure called SetOfStacks.
# SetOfStacks should be composed of several stacks
# and create a new stack once the stack reaches a
# certain capacity. (let's say 4 items)
# push() and pop() should operate just like a single
# stack. 

class SetOfStacks(object):
    def __init__(self):
        # Your code here
        pass

    def push(self, item):
        # Your code here
        pass

    def pop(self):
        # Your code here
        pass

    def number_of_stacks(self):
        # this should return the number of stacks that
        # are being used within this object. (This is used
        # to test that your stack allocation is correct)
        pass


# This expects to be passed a list of integers and 'p's.
# The integers represent numbers to be pushed onto the SetOfStacks
# The 'p's represent a pop() operation.
# After each operation (either pushing or popping) the popped values
# will be saved into a list, and the number of stacks used by SetOfStacks
# will be saved into another list. The two lists will be returned as a
# tuple for the tests to inspect.

def results_from_testcase(testcase):
    test = SetOfStacks()
    ra = []
    rb = []
    for thing in testcase:
        if type(thing) is int:
            test.push(thing)
        else:
            ra.append(test.pop())
        rb.append(test.number_of_stacks())
    return (ra, rb)

(r1a, r1b) = results_from_testcase([1, 2, 'p', 'p'])
(r2a, r2b) = results_from_testcase([1, 2, 3, 4, 5, 'p', 'p', 'p', 'p', 'p', 'p'])
(r3a, r3b) = results_from_testcase([1, 2, 3, 4, 5, 'p', 'p', 'p', 'p', 'p', 'p', 'p'])
(r4a, r4b) = results_from_testcase([2, 5, 'p', 6, 7, 'p', 8, 9, 10, 'p', 'p', 'p', 'p', 'p'])
(r5a, r5b) = results_from_testcase(['p', 1, 2, 3, 4, 5, 'p'])

tests = [
    [[r1a], [2, 1]],
    [[r1b], [1, 1, 1, 0]],
    [[r2a], [5, 4, 3, 2, 1, None]],
    [[r2b], [1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 0]],
    [[r3a], [5, 4, 3, 2, 1, None, None]],
    [[r3b], [1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 0, 0]],
    [[r4a], [5, 7, 10, 9, 8, 6, 2]],
    [[r4b], [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0]],
    [[r5a], [None, 5]],
    [[r5b], [0, 1, 1, 1, 1, 2, 1]],
]

runtests(tests)
