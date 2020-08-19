from test_framework import generic_test
import math

def number_of_ways(n: int, m: int) -> int:
    # Tracks how many ways from the previous row
    row_ways = [1] * m
    
    for row in range(1, n):
        for col in range(m):
            if col == 0:
                prev_col = 0
            row_ways[col] = row_ways[col] + prev_col
            prev_col = row_ways[col]

    return row_ways[-1]

def number_of_ways_const(n: int, m: int) -> int:
    return math.factorial(m - 1 + n - 1) // (math.factorial(m - 1) * math.factorial(n - 1))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
