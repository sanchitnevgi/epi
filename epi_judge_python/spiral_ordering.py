from typing import List

from test_framework import generic_test

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    def layer(offset):
        square_matrix

def matrix_in_spiral_order_(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)
    total = n ** 2
    directions, cur_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
    row, col = 0, 0
    output = []
    
    for _ in range(total):
        output.append(square_matrix[row][col])
        square_matrix[row][col] = -1

        next_row, next_col = row + directions[cur_dir][0], col + directions[cur_dir][1]
        
        if (next_row < 0 or next_row >= n or next_col < 0 or next_col >= n 
            or square_matrix[next_row][next_col] == -1):
            cur_dir = (cur_dir + 1) % 4
            next_row, next_col = row + directions[cur_dir][0], col + directions[cur_dir][1]

        row, col = next_row, next_col

    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
