from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    last_reachable_idx = len(A) - 1

    for i in reversed(range(len(A) - 1)):
        if A[i] + i >= last_reachable_idx:
            last_reachable_idx = i

    return last_reachable_idx == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
