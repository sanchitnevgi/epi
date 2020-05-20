from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    base_10 = 0
    letters = { 'A', 'B', 'C', 'D', 'E', 'F' }
    is_negative = False

    if num_as_string.startswith('-'):
        num_as_string, is_negative = num_as_string[1:], True

    # Get the number in base 10
    for char in num_as_string:
        if char in letters:
            digit = ord(char) - ord('A') + 10    
        else:
            digit = ord(char) - ord('0')
        base_10 = base_10 * b1 + digit

    # Find the MSB
    most_significant = 1
    while most_significant * b2 <= base_10:
        most_significant *= b2
    
    b2_num = []

    while base_10:
        digit = base_10 // most_significant

        if digit > 9:
            digit = chr(ord('A') + digit - 10)
        else:
            digit = chr(digit + ord('0'))

        b2_num.append(digit)
        base_10 = base_10 % most_significant
        most_significant //= b2

    # Append the last with zeros
    while most_significant > 0:
        b2_num.append('0')
        most_significant //= b2

    return  ('-' if is_negative else '') + ''.join(b2_num)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
