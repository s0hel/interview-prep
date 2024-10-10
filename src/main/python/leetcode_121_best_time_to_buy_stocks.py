# 121. Best Time to Buy and Sell Stock
# Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        max_profit = 0

        # initialize min prices cache
        i = len(prices) - 1
        max_prices = [0] * (len(prices))
        max_prices[i] = prices[i]
        i -= 1

        while i >= 0:
            max_prices[i] = max(max_prices[i + 1], prices[i])
            i -= 1

        for i in range(len(prices)):
            buy_price = prices[i]
            if i + 1 < len(prices):
                min_sell_price = max_prices[i + 1]
                max_profit = max(max_profit, min_sell_price - buy_price)

        return max_profit

    def maxProfit_better(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices[1:]:
            buy_price = min(buy_price, price)
            profit = max(profit, price - buy_price)

        return profit


s = Solution()
result = s.maxProfit_better([7, 1, 5, 3, 6, 4])
print(result)
assert result == 5

result = s.maxProfit_better([7, 6, 4, 3, 1])
print(result)
assert result == 0

# consider caching min values for each index
