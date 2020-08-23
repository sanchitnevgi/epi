from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    steps_to_reach = [float('inf')] * top + [1]

    # Go over steps in reverse
    for i in reversed(range(top)):
        # Sum over each step size
        steps_to_reach[i] = sum([steps_to_reach[i + step_size] 
                                    for step_size in range(1, maximum_step + 1) 
                                    if i + step_size <= top])
    return steps_to_reach[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
