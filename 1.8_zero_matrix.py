from tester import runtests

# zero_matrix takes a matrix m (similar to the previous question), and modifies
# it inplace to zero-out any rows and columns that had a zero on them.

def zero_matrix(m):
    # Your code here
    pass

tests = [
    [
        [
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ],
        [
            [1, 0, 3],
            [0, 0, 0],
            [7, 0, 9]
        ]
    ],
    [
        [
            [1, 2],
            [0, 4]
        ],
        [
            [0, 2],
            [0, 0]
        ]
    ],
    [
        [
            [1]
        ],
        [
            [1]
        ]
    ],
    [
        [],
        []
    ],
    [
        [
            [0, 0, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 7, 8],
            [0, 0, 11, 12],
            [0, 0, 15, 16]
        ]
    ],
    [
        [
            [0, 2, 3, 4],
            [5, 0, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 11, 12],
            [0, 0, 15, 16]
        ]
    ]
]

runtests(tests, zero_matrix, inplace=True)
