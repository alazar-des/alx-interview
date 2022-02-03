#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """if 1 check its sides and if 0 add 1 to perimeter.
    """
    perimeter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (grid[i][j] == 1):
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                    perimeter += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j + 1 >= len(grid[i]) or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
