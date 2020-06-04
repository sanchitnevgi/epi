from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    lo, hi, result = 0, len(A) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] < k:
            lo = mid + 1
        elif A[mid] > k:
            hi = mid - 1
        else:
            result = mid
            hi = mid - 1
    return result

# Variant #1 Bisect right
def bisect_right(A: List[int], k) -> int:
    lo, hi, result = 0, len(A) - 1, len(A)

    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] <= k:
            lo = mid + 1
        elif A[mid] > k:
            hi = mid - 1
            result = mid

    return result

# Vairant #2 Find local minimum
def local_min(A: List[int]) -> int:
    for i in range(1, len(A) - 1):
        if A[i] <= A[i + 1]:
            return i
    return -1

# Variant #4 Test if p is a prefix of a string in a list of sorted strings 

if __name__ == '__main__':
    # print(local_min([6, 5, 4, 3, 1, 2]))
    print(bisect_right([1, 2, 2, 3], 0))
    print(bisect_right([1, 2, 2, 3], 2))
    print(bisect_right([1, 2, 2, 3], 4))
    print(bisect_right([1, 2, 2, 3], 3))
    # exit(
    #     generic_test.generic_test_main('search_first_key.py',
    #                                    'search_first_key.tsv',
    #                                    search_first_of_k))
