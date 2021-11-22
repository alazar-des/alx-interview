#!/usr/bin/python3
"""
Returns list of Pascal Triangle.
"""


def pascal_triangle(n):
    """ Calculate pascal Triangel elements and return as a list.

    Args:
        n (int): number of rows to calculate.

    Yields:
        list which contains pascal triangle elements.
    """

    arr = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if i == 0 or j == 0:
                ele = 1
            else:
                ele = ele * (i - j) / j
            row.append(int(ele))
        arr.append(row)
    return arr
