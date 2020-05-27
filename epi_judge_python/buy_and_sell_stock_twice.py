from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # Build array selling from one end
    max_profit_left, min_price_so_far = [0] * len(prices), prices[0]
    for i in range(1, len(prices)):
        max_profit_left[i] = max(max_profit_left[i-1], prices[i] - min_price_so_far)
        min_price_so_far = min(min_price_so_far, prices[i])
    
    # Build array selling from other end
    max_profit_right, max_price_so_far = [0] * len(prices), prices[-1]
    for i in reversed(range(len(prices) - 1)):
        max_profit_right[i] = max(max_profit_right[i+1], max_price_so_far - prices[i])
        max_price_so_far = max(max_price_so_far, prices[i])

    # Compare and return max
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, max_profit_left[i - 1] + max_profit_right[i])
    max_profit = max(max(max_profit_left), max_profit)
    return max_profit


if __name__ == '__main__':
    # buy_and_sell_stock_twice([0.1, 0.2])
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
