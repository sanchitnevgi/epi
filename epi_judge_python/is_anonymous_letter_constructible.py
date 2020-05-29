from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    return not Counter(letter_text) - Counter(magazine_text)
    
    # letter_count, magazine_count = Counter(letter_text), Counter(magazine_text)
    # 
    # for letter, count in letter_count.items():
    #     if count > magazine_count[letter]:
    #         return False
    # return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
