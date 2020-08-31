import collections
from typing import List

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A: List[int]) -> Subarray:
    start = 0
    max_subarray_len, max_subarray = 1, Subarray(0, 0)
    for end in  range(1, len(A)):
        # Non-Increasing 
        if A[end] <= A[end - 1]:
            start = end
            continue
        if end - start + 1 > max_subarray_len:
            max_subarray_len = end - start + 1
            max_subarray = Subarray(start, end)

    return max_subarray


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_increasing_subarray.py',
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
