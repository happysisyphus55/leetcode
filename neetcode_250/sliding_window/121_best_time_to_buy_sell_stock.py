from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            # only add to max_profilt if the the right is bigger than left
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                l = r  # shift the left pointer all the way to right
            r += 1
        return max_profit
