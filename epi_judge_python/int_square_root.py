from test_framework import generic_test

def square_root(k: int) -> int:    
    lo, hi = 0, k
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_sq = mid ** 2
        if mid_sq > k:
            hi = mid - 1
        else: #mid_sq <= k
            lo = mid + 1
    return lo - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
