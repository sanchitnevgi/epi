from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    n = len(partial_assignment)

    def check(nums):
        seen = set()
        for num in nums:
            if num != 0 and num in seen:
                return False
            else:
                seen.add(num)
        return True

    # Check rows and columns
    for i in range(n):
        # Row
        if not check(partial_assignment[i]):
            return False
        
        # Col
        col = [row[i] for row in partial_assignment]
        if not check(col):
            return False

    # Blocks
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            block = [partial_assignment[i + k][j + l] for k in range(3) for l in range(3)]
            if not check(block):
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
