from tester import runtests

# rotate_matrix takes a 2-nested list representing a square matrix, and modifies
# the numbers inplace to rotate the matrix by 90 degrees clockwise.

def rotate_matrix(m):
    # Your code here
    pass


tests = [
    [
        [[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]],
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
    ],
    [
        [[
            [1, 2],
            [3, 4]
        ]],
        [
            [3, 1],
            [4, 2]
        ]
    ],
    [
        [[
            [1]
        ]],
        [
            [1]
        ]
    ],
    [
        [[]],
        []
    ],
    [
        [[
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]],
        [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
    ]
]

runtests(tests, rotate_matrix, inplace=True)
