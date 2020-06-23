from typing import Iterator, List
import heapq
import itertools

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    result, min_heap = [], []
    for num in itertools.islice(sequence, k):
        heapq.heappush(min_heap, num)

    for num in sequence:
        min_el = heapq.heapreplace(min_heap, num)
        result.append(min_el)    
    
    result.extend(heapq.nsmallest(k, min_heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
