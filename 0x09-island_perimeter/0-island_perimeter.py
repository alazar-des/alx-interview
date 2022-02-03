#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """if 1 check its sides and if 0 add 1 to perimeter.
    """
    perimeter = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if (grid[i][j] == 1):
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
