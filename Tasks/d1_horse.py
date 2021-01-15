import numpy as np
# def calculate_paths(shape: (int, int), point: (int, int)) -> int:
#     """
#     Given field with size rows*cols count available paths from (0, 0) to point
#
#     :param shape: tuple of rows and cols (each from 1 to rows/cols)
#     :param point: desired point for horse
#     :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
#     """
#
#
#     f = [[0] * (shape[1]) for i in range(shape[0])]
#     f[shape[0] - 1][0] = 1
#     print(f)
#
#
#     for i in range(shape[0] - 1, 0, -1):
#         for j in range(shape[1]):
#             if f[i][j] != 0:
#                 if i - 2 >= 0 and j - 1 >= 0:
#                     f[i - 2][j - 1] += 2 * f[i][j]
#                 if i - 2 >= 0 and j + 1 < shape[1]:
#                     f[i - 2][j + 1] += 2 * f[i][j]
#                 if i - 1 >= 0 and j + 2 < shape[1]:
#                     f[i - 1][j + 2] += 2 * f[i][j]
#                 if i - 1 >= 0 and j - 2 >= 0:
#                     f[i - 1][j - 2] += 2 * f[i][j]
#
#     for i in range(0, shape[0]):
#         for j in range(0, shape[1]):
#             print(f[i][j], end=" ")
#         print()
#
#
#     return f[shape[0]-point[0]-1][point[1]]
# n = (8, 8)
# p = (7, 7)
# print(calculate_paths(n, p))

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    a = np.full(shape, 0)
    a[0][0] = 1
    print(a)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            if a[i][j] == 0:
                if i - 2 >= 0 and j - 1 >= 0:
                    a[i][j] += 2 * a[i - 2][j - 1]
                if i - 1 >= 0 and j - 2 >= 0:
                    a[i][j] += 2 * a[i - 1][j - 2]
                if i + 1 < shape[0] and j + 2 < shape[1]:
                    a[i][j] += 2 * a[i - 1][j + 2]
                if i + 2 < shape[0] and j + 1 < shape[1]:
                    a[i][j] += 2 * a[i + 2][j + 1]
    return a[point[0]][point[1]]

print(calculate_paths((9, 9), (8, 8)))
