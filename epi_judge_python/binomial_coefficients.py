from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    def compute(_n, _k):
        if (_n, _k) in cache:
            return cache[_n, _k]
        if _k == 0 or _n == _k:
            return 1
        ways = compute(_n - 1, _k) + compute(_n - 1, _k - 1)
        cache[_n, _k] = ways
        return ways
    
    cache = {}

    return compute(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
