def write_zeros(m, p):
    for x in range(0, len(m)):
        m[x][p[1]] = 0
    for y in range(0, len(m)):
        m[p[0]][y] = 0


def zero_matrix(m):
    zero_points = []
    for x in range(0, len(m)):
        for y in range(0, len(m)):
            if m[x][y] == 0:
                zero_points.append([x, y])
    for point in zero_points:
        write_zeros(m, point)



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

for test in tests:
    zero_matrix(test[0])
    if test[0] == test[1]:
        print 'Pass'
    else:
        print 'Failure: expected "{}", found "{}"'.format(test[1], test[0])

