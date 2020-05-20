from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n == 1:
        return '1'
    
    last_output, current_output = ['1'], []
    for i in range(1, n):
        group_char, group_len = -1, 0
        
        for char in last_output:
            if char != group_char:
                # Either new group or first group
                if group_char != -1:
                    current_output.extend([str(group_len), group_char])
                group_char, group_len = char, 1
            else:
                group_len += 1
        current_output.extend([str(group_len), group_char])

        if i == n - 2:
            return ''.join(current_output)

        last_output, current_output = current_output, []

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
