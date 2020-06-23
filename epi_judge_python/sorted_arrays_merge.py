from typing import List
import heapq
from collections import namedtuple
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # Pthonic solution
    # return list(heapq.merge(*sorted_arrays))

    Item = namedtuple('Item', ['value', 'list_idx', 'idx'])
    result = []

    # Initialize heap, assume at least 1 item in a list
    candidate_heap = [ Item(arr[0], list_idx, 0) for list_idx, arr in enumerate(sorted_arrays) ]
    heapq.heapify(candidate_heap)
    
    while candidate_heap:
        # Get the minium value from heap and add to result
        min_item = heapq.heappop(candidate_heap)
        result.append(min_item.value)

        # Check if list is exhausted
        if min_item.idx == len(sorted_arrays[min_item.list_idx]) - 1:
            continue
        
        # Else add the next value from list to result
        next_item = Item(sorted_arrays[min_item.list_idx][min_item.idx + 1], min_item.list_idx, min_item.idx + 1)
        heapq.heappush(candidate_heap, next_item)

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
