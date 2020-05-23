from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    is_primes = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if is_primes[i]:
            primes.append(i)
            # Sieve
            for j in range(i ** 2, n + 1, i):
                is_primes[j] = False

    return primes

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
