from typing import List
import heapq
from collections import namedtuple

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    Candidate = namedtuple('Candidate', ['val', 'idx'])

    largest_heap, result = [Candidate(-A[0], 0)], []

    while len(result) < k:
        candidate = heapq.heappop(largest_heap)
        
        # Add to result
        result.append(-candidate.val)

        # Add the left and right child to heap
        left, right = 2 * candidate.idx + 1, 2 * candidate.idx + 2

        if left < len(A):
            heapq.heappush(largest_heap, Candidate(-A[left], left))
        
        if right < len(A):
            heapq.heappush(largest_heap, Candidate(-A[right], right))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
