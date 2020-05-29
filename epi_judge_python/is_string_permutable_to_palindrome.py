from test_framework import generic_test
from collections import Counter

def can_form_palindrome(s: str) -> bool:
    count = Counter(s)
    ones = sum([value for key, value in count.items() if value == 1])

    return ones <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
