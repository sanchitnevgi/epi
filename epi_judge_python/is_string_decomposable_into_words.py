import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    last_length = [-1] * len(domain)

    # For each prefix
    for i in range(len(domain)):
        # If prefix is a dictionary word:
        if domain[:i+1] in dictionary:
            # Set the word-length
            last_length[i] = i + 1
            continue
            
        # Not a dictionary word, check if prefix of prefix has valid decomposition and the other is a dictionary word
        for j in range(i):
            if last_length[j] != -1 and domain[j + 1: i + 1] in dictionary:
                last_length[i] = i - j
                break
        
    # No valid decomposition of full string
    if last_length[-1] == -1:
        return []
    
    # Get the decomposition
    decomposition = []
    i = len(domain) - 1
    while i >= 0:
        word_len = last_length[i]
        decomposition.append(domain[i + 1 - word_len:i + 1])
        i -= word_len

    return decomposition[::-1]



@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')

# print(decompose_into_dictionary_words("bedbathandbeyond", {"bed", "bath", "and", "beyond"}))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
