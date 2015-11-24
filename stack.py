from tester import runtests

class Stack(object):
    def __init__(self):
        self._l = []

    def push(self, item):
        self._l.append(item)

    def pop(self):
        if self._l:
            return self._l.pop(-1)
        return None


test = Stack()
for thing in [1, 2]:
    test.push(thing)

r1 = []

for thing in range(0, 2):
    r1.append(test.pop())

test = Stack()
for thing in [1, 2, 3, 4, 5]:
    test.push(thing)

r2 = []

for thing in range(0, 5):
    r2.append(test.pop())

test = Stack()
for thing in [1, 2, 3, 4, 5]:
    test.push(thing)

r3 = []

for thing in range(0, 7):
    r3.append(test.pop())

test = Stack()
r4 = []
test.push(2)
test.push(5)
r4.append(test.pop())
test.push(6)
test.push(7)
r4.append(test.pop())
test.push(8)
test.push(9)
test.push(10)
r4.append(test.pop())
r4.append(test.pop())
r4.append(test.pop())
r4.append(test.pop())
r4.append(test.pop())
r4.append(test.pop())

tests = [
    [[r1], [2, 1]],
    [[r2], [5, 4, 3, 2, 1]],
    [[r3], [5, 4, 3, 2, 1, None, None]],
    [[r4], [5, 7, 10, 9, 8, 6, 2, None]],
]

if not runtests(tests, quiet=True):
    raise Exception('Oes Noes! the Stack class doesn\'t even work properly! Abandon all hope!')
