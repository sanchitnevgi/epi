from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    if not s:
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left, right = left + 1, right - 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
