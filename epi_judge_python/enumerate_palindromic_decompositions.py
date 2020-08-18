from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    def decomposition(offset, partial):
        if offset == len(text):
            result.append(partial.copy())
            return
        # Find all palindromes starting from offset and recurse
        for i in range(offset + 1, len(text) + 1):
            # Palindrome check
            prefix = text[offset:i]
            if prefix == prefix[::-1]:
                decomposition(i, partial + [prefix])
    
    result = []
    decomposition(0, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
