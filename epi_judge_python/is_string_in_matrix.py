from typing import List
from itertools import product
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    prev_max_length = [ [0] * len(grid[0]) for _ in range(len(grid)) ]
    n, m = len(grid), len(grid[0])

    for idx, dig in enumerate(pattern):
        pattern_len = idx + 1
        max_length_found = [ [0] * len(grid[0]) for _ in range(len(grid)) ]
        for i, j in product(range(n), range(m)):
            if pattern_len == 1:
                max_length_found[i][j] = pattern_len if grid[i][j] == dig else 0
            else:
                # 2 or longer, find cells with value == pattern_len - 1 and check its neighbours
                
                if prev_max_length[i][j] == pattern_len - 1:
                    # Check neighbours
                    for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        # Not a valid neighbour
                        if not (0 <= nx < n and 0 <= ny < m):
                            continue

                        # If neighbour is the next in pattern, mark it
                        if grid[nx][ny] == dig:
                            max_length_found[nx][ny] = pattern_len
            prev_max_length = max_length_found

    # Check if full pattern length exits
    return any([ len(pattern) == max_length_found[i][j] for i in range(n) for j in range(m) ])
                     
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
