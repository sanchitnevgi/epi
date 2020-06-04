from typing import List
import random
from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    
    def partiion_around_pivot(left, right, pivot_idx):
        pivot = A[pivot_idx]
        new_pivot_idx = left

        # Move pivot out of the way
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        
        for i in range(left, right):
            if A[i] > pivot:
                A[new_pivot_idx], A[i] = A[i], A[new_pivot_idx]
                new_pivot_idx += 1
        
        # Move the pivot to correct place
        A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]

        return new_pivot_idx

    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)

        new_pivot_idx = partiion_around_pivot(left, right, pivot_idx)

        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx < k - 1:
            left = new_pivot_idx + 1
        else: #new_pivot_idx > k - 1
            right = new_pivot_idx - 1

# Variant 1: Median of unsorted array

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
