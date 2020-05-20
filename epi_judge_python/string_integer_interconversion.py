from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    is_neg = False
    if x < 0:
        x, is_neg = -x, True
    
    digits = []

    while x:
        dig = x % 10
        digits.append(chr(dig + ord('0')))
        x //= 10

    string = ''.join(reversed(digits))

    if is_neg:
        string = '-' + string

    return string


def string_to_int(s: str) -> int:
    number = 0
    is_neg = False
    
    if s.startswith('-'):
        is_neg = True
        s = s[1:]
    if s.startswith('+'):
        s = s[1:]

    for char in s:
        dig = ord(char) - ord('0')
        number = number * 10 + dig
    if is_neg:
        number = -number

    return number


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
