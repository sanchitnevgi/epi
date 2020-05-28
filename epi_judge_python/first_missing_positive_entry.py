from typing import List

from test_framework import generic_test


def find_first_missing_positive(A: List[int]) -> int:
    n, i = len(A), 0
    while i < n:
        if 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
        else:
            i += 1
    
    for i in range(n):
        if A[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == '__main__':
    A = [11, 15, 18, 0, -3, 16, 4, 2, 6, 2, 1, 11, 16, 5, 3, 20, 11, -4, 12, 9, 20, 22, 22]
    # missing = find_first_missing_positive(A)
    # 7
    # print(missing)
    exit(
        generic_test.generic_test_main('first_missing_positive_entry.py',
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
