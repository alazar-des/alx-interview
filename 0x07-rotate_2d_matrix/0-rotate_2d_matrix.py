#!/usr/bin/python3
"""Rotate Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate matrix 90 degree clockwise
    """
    N = len(matrix)
    for i in range(N - 1):
        for j in range(i, N - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp
