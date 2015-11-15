def swap_members_inplace(m, p1, p2):
    m[p1[0]][p1[1]] ^= m[p2[0]][p2[1]]
    m[p2[0]][p2[1]] ^= m[p1[0]][p1[1]]
    m[p1[0]][p1[1]] ^= m[p2[0]][p2[1]]

def rotate_point(p, length):
    return (length - 1 - p[1], p[0])

def find_rotation_points(p, length):
    return_points = []
    return_points.append(p)
    for i in range(0, 3):
        return_points.append(rotate_point(return_points[-1], length))

    return return_points

def rotate_matrix(m):
    for x in range(0, len(m)/2):
        for y in range(0, (len(m)+1)/2):
            rpoints = find_rotation_points((x, y), len(m))
            for i in range(0, 3):
                swap_members_inplace(m, rpoints[i], rpoints[i + 1])


tests = [
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
    ],
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [3, 1],
            [4, 2]
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
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
    ]
]

for test in tests:
    rotate_matrix(test[0])
    if test[0] == test[1]:
        print 'Pass'
    else:
        print 'Failure: expected "{}", found "{}"'.format(test[1], test[0])




