from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def generate(num_left_parens_needed, num_right_parens_needed, valid_prefix):
        if num_left_parens_needed > 0:
            generate(num_left_parens_needed - 1, num_right_parens_needed, valid_prefix + "(")
        if num_right_parens_needed > num_left_parens_needed:
            generate(num_left_parens_needed, num_right_parens_needed - 1 ,valid_prefix + ")")

        if num_right_parens_needed == 0:
            result.append(valid_prefix)

    result = []
    generate(num_pairs, num_pairs, "")
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
