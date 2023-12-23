#!/usr/bin/python3
"""The module contains one function island_perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described
        in grid
    Args:
      grid (list): list of list of integers
        0 represents a water zone
        1 represenrs a land zone
      Returns:
        - int: Perimeter of the island.
      
      Constraints:
        - One cell is a square with side length 1
        - Grid cells are connected horizontally/vertically not
        diagonally
        - Grid is rectangular, width and height don't exceed 100
        - Grid is completely surrounded by water, and there is
        one island (or nothing).
            - The island doesn’t have “lakes” (water inside that
        isn’t connected to the water around the island).
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    
    return perimeter    
