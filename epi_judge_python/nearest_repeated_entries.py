from typing import List
import math
from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    last_idx, min_so_far = dict(), float('inf')
    for i, word in enumerate(paragraph):
        last = last_idx.setdefault(word, float('-inf'))
        min_so_far = min(min_so_far, i - last)
        last_idx[word] = i
    return -1 if math.isinf(min_so_far) else min_so_far
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
