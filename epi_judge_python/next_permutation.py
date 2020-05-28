from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # Find peak from right
    peak = len(perm) - 1
    while peak > 0 and perm[peak] <= perm[peak - 1]:
        peak -= 1

    if peak == 0:
        return []
    
    peak_left = peak - 1

    # Find the least number larger than peak_left
    while peak < len(perm) and perm[peak] > perm[peak_left]:
        peak += 1
    peak -= 1

    perm[peak], perm[peak_left] = perm[peak_left], perm[peak]

    perm[peak_left + 1:] = sorted(perm[peak_left + 1:])

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
