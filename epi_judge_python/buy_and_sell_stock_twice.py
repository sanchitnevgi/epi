from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_l, min_price_so_far = [0.0] * len(prices), prices[0]
    
    # max_l[i] has the maximum profit obtained by buying & selling upto and including day i
    for idx in range(1, len(prices)):
        price = prices[idx]

        max_l[idx] = max(max_l[idx - 1], price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)
    
    max_r, max_price_so_far = [0.0] * len(prices), prices[-1]


    # max_r[i] has the maximum profit obtained by buying from day i upto the end
    for idx in reversed(range(len(prices) - 1)):
        price = prices[idx]

        max_r[idx] = max(max_r[idx + 1], max_price_so_far - price)
        max_price_so_far = max(max_price_so_far, price)

    maximum_selling_2 = max(l + r for l, r in zip(max_l[:-1], max_r[1:]))
    maximum = max(maximum_selling_2, max(max_l))
    return maximum


if __name__ == '__main__':
    # buy_and_sell_stock_twice([0.2, 0.7, 0.9, 0.4, 0.1, 0.1, 0.5, 0.4, 0.9])
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
