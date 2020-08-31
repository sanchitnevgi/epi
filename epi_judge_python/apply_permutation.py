from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    idx = 0
    while idx < len(A):
        # Check if element in correct place
        if perm[idx] == idx:
            idx += 1
            continue
        permute_to = perm[idx]
        A[idx], A[permute_to] = A[permute_to], A[idx]
        perm[idx], perm[permute_to] = perm[permute_to], perm[idx]

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
