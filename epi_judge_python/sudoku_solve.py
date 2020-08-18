import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def get_next_cell(row, col):
        next_col = (col + 1) % 9        
        next_row = row + 1 if next_col == 0 else row

        return next_row, next_col

    def can_solve(row, col):
        # Filled all squares, solvable
        if row == len(partial_assignment):
            return True
        
        # If already filled,  continue with next assignment
        if partial_assignment[row][col] != 0:
            return can_solve(*get_next_cell(row, col))

        # Find all valid positions
        possible = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

        # Remove all elements from the current row
        possible.difference_update(partial_assignment[row])

        # Remove all elements from the current column
        possible.difference_update([row[col] for row in partial_assignment])

        # Remove all elements from the grid
        grid_x, grid_y = row // 3, col // 3
        grid_values = [partial_assignment[x][y] for x in range(grid_x * 3, grid_x * 3 + 3) for y in range(grid_y * 3, grid_y * 3 + 3) ]
        possible.difference_update(grid_values)
        
        for assignment in possible:
            partial_assignment[row][col] = assignment
            
            if can_solve(*get_next_cell(row, col)):
                return True

            partial_assignment[row][col] = 0

        return False

    return can_solve(0, 0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
