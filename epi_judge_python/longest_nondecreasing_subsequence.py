from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    longest_nondecreasing = [1] * len(A)
    
    # For each item, the longest nondecreasing ending at it 
    # is the max of non_decreasing of smaller elements to its left
    for i in range(1, len(A)):
        longest_nondecreasing[i] = max([longest_nondecreasing[j] for j in range(i) if A[j] <= A[i]], default=0) + 1

    return max(longest_nondecreasing)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
