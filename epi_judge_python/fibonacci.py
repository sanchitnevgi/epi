from test_framework import generic_test

cache = {}
def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    nth_fib = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = nth_fib

    return nth_fib


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
