from test_framework import generic_test
import operator

def evaluate(expression: str) -> int:
    tokens = expression.split(",")
    numbers = []
    operators = { "*": operator.mul, "+": operator.add, "-": operator.sub, "/": operator.floordiv }

    for token in tokens:
        if token in operators:
            num2, num1 = numbers.pop(), numbers.pop()
            res = operators[token](num1, num2)
            numbers.append(res)
        else:
            numbers.append(int(token))

    return numbers[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
