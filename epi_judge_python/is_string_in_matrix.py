from typing import List
from itertools import product
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    rows, cols = len(grid), len(grid[0])

    # Error condition
    if not pattern:
        return True

    if not rows or not cols:
        return False

    # Set flags for 1st char in pattern
    len_n_pattern = [[grid[r][c] == pattern[0] for c  in range(cols) ] for r in range(rows)]

    # Go over rest of the pattern and modify
    for char in pattern[1:]:
        # Keep the current pattern
        next_len = [[False] * cols for _ in range(rows)]

        # Check neighbours of each cell in grid
        for row, col in product(range(rows), range(cols)):
            # If cell is not char, continue
            if grid[row][col] is not char:
                continue

            for nx, ny in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                # Check if valid neighbour
                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue

                # The pattern upto length exists
                if len_n_pattern[nx][ny]:
                    next_len[row][col] = True
                    # No need to check more neighbours
                    break
        
        # Update the len_n_pattern
        len_n_pattern = next_len

    return any(len_n_pattern[r][c] for r in range(rows) for c in range(cols))
                     
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
