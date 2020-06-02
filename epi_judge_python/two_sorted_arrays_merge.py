from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    a, b, f = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if A[a] >= B[b]:
            A[f] = A[a]
            a -= 1
        else: # B[b] < A[a]
            A[f] = B[b]
            b -= 1

        f -= 1

    if b >= 0:
        A[:b + 1] = B[:b + 1]

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
