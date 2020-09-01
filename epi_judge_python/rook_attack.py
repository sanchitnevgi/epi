import copy
from typing import List
import itertools

from test_framework import generic_test

def rook_attack(A: List[List[int]]) -> None:
    m, n = len(A), len(A[0])
    
    first_row_has_zero = 0 in A[0]
    first_col_has_zero = any(not A[r][0] for r in range(n))

    for row, col in itertools.product(range(1, m), range(1, n)):
        if not A[row][col]:
            A[row][0] = A[0][col] = 0

    # Go over 1st col
    for row in range(1, m):
        # Set the entire row to 0
        if A[row][0] == 0:
            for col in range(n):
                A[row][col] = 0
    
    # Go over 1st row
    for col in range(1, n):
        # Set the entire row to 0
        if A[0][col] == 0:
            for row in range(m):
                A[row][col] = 0

    # If first row has zero
    if first_row_has_zero:
        for col in range(col):
            A[0][col] = 0
    # If first col has zero
    if first_col_has_zero:
        for row in range(m):
            A[row][0]= 0


def rook_attack(A: List[List[int]]) -> None:
    """In-place, using a flag"""
    rows, cols = len(A), len(A[0])

    for row, col in itertools.product(range(rows), range(cols)):
        if A[row][col] == 0:
            # Make the row and col in B equal to 0
            for r in range(rows):
                A[r][col] = "_" if A[r][col] != 0 else 0
            for c in range(cols):
                A[row][c] = "_" if A[row][c] != 0 else 0
    
    # Make all -1 into 0
    for row, col in itertools.product(range(rows), range(cols)):
        if A[row][col] == "_":
            A[row][col] = 0


def rook_attack_1(A: List[List[int]]) -> None:
    """Using Additional Space"""
    rows, cols = len(A), len(A[0])
    B = copy.deepcopy(A)
    
    for row, col in itertools.product(range(rows), range(cols)):
        if A[row][col] == 0:
            # Make the row and col in B equal to 0
            for r in range(rows):
                B[r][col] = 0
            for c in range(cols):
                B[row][c] = 0
    
    # Copy B to A
    for row, col in itertools.product(range(rows), range(cols)):
        A[row][col] = B[row][col]


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rook_attack.py', 'rook_attack.tsv',
                                       rook_attack_wrapper))
