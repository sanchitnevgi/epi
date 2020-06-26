from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # Stack to store open brackets
    open_brackets = []

    matching_pairs = { "(": ")", "{": "}", "[": "]" }

    for token in s:
        # If opening bracket, push in stack
        if token in matching_pairs:
            open_brackets.append(token)
        else:
            # If stack is empty or not matching
            if not open_brackets or matching_pairs[open_brackets[-1]] != token:
                return False
            else:
                open_brackets.pop()

    return not open_brackets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
