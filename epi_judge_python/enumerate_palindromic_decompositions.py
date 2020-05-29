from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    palindromes = set()
    
    def get_palindromes(lo, hi):
        if lo > hi:
            return

        mid = (lo + hi) // 2

        # Add the single character
        palindromes.add(text[mid])

        # Get palindromes from the left half
        palindromes_left = get_palindromes(lo, mid - 1)

        # Get palindromes from the right half
        palindromes_right = get_palindromes(mid + 1, hi)

        # Get palindromes starting from the center
        

    return []


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
