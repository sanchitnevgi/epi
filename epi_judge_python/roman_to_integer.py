from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i, int_value = 0, 0

    while i < len(s) - 1:
        roman = s[i]
        next_roman, next_value = s[i + 1], roman_to_int[s[i + 1]]
        # Next value is greater
        if roman_to_int[roman] < next_value:
            if (
                (roman == 'I' and next_roman in ['X', 'V']) 
                or (roman == 'X' and next_roman in ['L', 'C']) 
                or (roman == 'C' and next_roman in ['D', 'M']) 
                ):
                int_value += next_value - roman_to_int[roman]
                i += 2
            else:
                return -1
        else:
            int_value += roman_to_int[roman]
            i += 1
    
    if i < len(s):
        int_value += roman_to_int[s[i]]

    return int_value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
