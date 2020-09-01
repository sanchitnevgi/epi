from typing import List

from test_framework import generic_test


def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
    # Edge cases
    if k == 0:
        return 0.0
    # k >= n/2, optimum strategy is to by at valley and sell at peak
    elif 2 * k >= len(prices):
        # Find the 
        return sum(max(0, b - a) for a, b in zip(prices[:-1], prices[1:]))

    max_profit = [ [0] * len(prices) for _ in range(k + 1) ]

    for num_transactions in range(1, k + 1):
        for day in range(1, len(prices)):
            # The maximum profit for given day and num_transactions is
            # Not doing any transaction on the day
            no_transaction = max_profit[num_transactions][day - 1]
        
            # Selling on that day and buying it at day m (m in 0, day - 1) 
            # and the max_profit by doing one less transaction ending on day m
            # NOTE: max_profit[num_transactions - 1][buy_day] is max profit for 1 less trasaction that ends on buy_day
            selling_on_day = max( (prices[day] - prices[buy_day]) + max_profit[num_transactions - 1][buy_day] for buy_day in range(day) )

            max_profit[num_transactions][day] = max(no_transaction, selling_on_day)

    return max_profit[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_k_times.py',
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
