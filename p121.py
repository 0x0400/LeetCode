# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMaxProfit = 0
        minPrice = prices[0]
        for price in prices:
            curMaxProfit = max(curMaxProfit, price - minPrice)
            minPrice = min(price, minPrice)
        return curMaxProfit
