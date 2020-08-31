from typing import List

from test_framework import generic_test

def find_biggest_n_minus_one_product(A: List[int]) -> int:
    left_multiplication = [1] * len(A)
    right_multiplication = [1] * len(A)

    for idx in range(1, len(A)):
        left_multiplication[idx] = A[idx - 1] * left_multiplication[idx - 1]
    
    right_product, max_product = 1, float("-inf")
    for idx in reversed(range(len(A))):
        max_product = max(max_product, left_multiplication[idx] * right_product)
        right_product = right_product * A[idx]

    return max_product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_product_all_but_one.py',
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
