
def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)
    return 0

    f = [[0] * (shape[1]) for i in range(shape[0])]
    f[shape[0] - 1][0] = 1

    for i in range(shape[0] - 1, 0, -1):
        for j in range(shape[1]):
            if f[i][j] != 0:
                if i - 2 >= 0 and j - 1 >= 0:
                    f[i - 2][j - 1] += 2 * f[i][j]
                if i - 2 >= 0 and j + 1 < shape[1]:
                    f[i - 2][j + 1] += 2 * f[i][j]
                if i - 1 >= 0 and j + 2 < shape[1]:
                    f[i - 1][j + 2] += 2 * f[i][j]
                if i - 1 >= 0 and j - 2 >= 0:
                    f[i - 1][j - 2] += 2 * f[i][j]

    return f[shape[0]-point[0]-1][point[1]]
n = (8, 8)
p = (7, 7)
print(calculate_paths(n, p))

def horse(shape: (int, int), point: (int, int)) -> int:
    a = np.full(shape, 0)
    a[0][0] = 1
    a[2][3] = 5
    print(a)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            print(a[i][j])
horse((4, 6), 6)
    # print(shape, point)
    # return 0
