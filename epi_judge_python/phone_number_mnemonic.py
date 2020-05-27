from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    if not phone_number:
        return []
    mapping = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")

    digit, suffix = int(phone_number[0]), phone_number[1:]
    def traverse(pnemonics, suffix):
        if not suffix:
            return pnemonics
        
        digit = int(suffix[0])
        values = []
        for pnemonic in pnemonics:
            for char in mapping[digit]:
                values.append(pnemonic + char)

        return traverse(values, suffix[1:])

    return traverse(list(mapping[digit]), suffix)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
