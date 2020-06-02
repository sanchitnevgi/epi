from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    intersection = []
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            if a == 0 or A[a] != A[a - 1]:
                intersection.append(A[a])
            a, b = a + 1, b + 1
        elif A[a] < B[b]:
            a += 1
        else: # B[b] < A[a]
            b += 1
    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
