#!/usr/bin/python3
""" N queens problem
"""

import sys


def nqueens(queens_pos, col, N):
    """ finds non attacking pos recursively."""
    if queens_pos[0][1] >= N:
        return

    i = len(queens_pos)
    if i >= N:
        print(queens_pos)
        queens_pos = [[0, queens_pos[0][1] + 1]]
        return nqueens(queens_pos, 0, N)

    pos_flag = True
    for j in range(col, N):
        pos_flag = True
        for q in queens_pos:
            if j == q[1] or i - j == q[0] - q[1] or \
               i + j == q[0] + q[1]:
                pos_flag = False
                break
        if pos_flag:
            queens_pos.append([i, j])
            return nqueens(queens_pos, 0, N)

    if not pos_flag:
        while(i > 0):
            i -= 1
            col = queens_pos[i][1] + 1
            if i == 0:
                return nqueens([[0, queens_pos[0][1] + 1]], 0, N)
            else:
                del queens_pos[i]
                if col < N:
                    return nqueens(queens_pos, col, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except TypeError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    nqueens([[0, 0]], 0, N)
