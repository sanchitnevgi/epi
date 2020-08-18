from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    mapping = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")

    def recurse(i):
        if i == len(phone_number):
            result.append("".join(partial))
            return
        for char in mapping[int(phone_number[i])]:
            partial[i] = char
            recurse(i + 1)
    
    result = []
    partial = [0] * len(phone_number)

    recurse(0)

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
