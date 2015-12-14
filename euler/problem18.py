small_triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

big_triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


def move(row, column, direction='1'):
    """
    direction == '0' means left
    direction == '1' means right

    >>> move(0, 0, '0')
    (1, 0)
    >>> move(0, 0, '1')
    (1, 1)
    >>> move(1, 0, '1')
    (2, 1)
    >>> move(2, 1, '1')
    (3, 2)
    """
    row += 1
    if direction == '1':
        column += 1
    return (row, column)


def value_at(row, column, triangle):
    return triangle[row][column]


def path_sum(path, triangle):
    """
    >>> path_sum('011', small_triangle)
    23
    >>> path_sum('000', small_triangle)
    20
    """
    result = triangle[0][0]
    row, column = 0, 0
    for p in path:
        row, column = move(row, column, p)
        result += value_at(row, column, triangle)

    return result


def problem18(triangle=big_triangle):
    """
    >>> problem18(small_triangle)
    23
    >>> from helper import md5
    >>> md5(problem18())
    '708f3cf8100d5e71834b1db77dfa15d6'
    """
    path_length = len(triangle) - 1
    maximum_path_sum = 0
    for i in range(2 ** path_length):
        # bin(0) == '0b0'
        # bin(0)[2:] == '0'
        # bin(0)[2:].zfill(3) == '000'
        path = bin(i)[2:].zfill(path_length)
        maximum_path_sum = max(
            maximum_path_sum,
            path_sum(path, triangle))
    return maximum_path_sum
