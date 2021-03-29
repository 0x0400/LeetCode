# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profiles = []
        curMinPrice = curMaxPrice = prices[0]
        i = 1
        while i < len(prices):
            while i < len(prices) and prices[i] >= prices[i-1]:
                curMaxPrice = prices[i]
                i += 1

            if curMaxPrice > curMinPrice:
                profiles.append(curMaxPrice-curMinPrice)

            while i < len(prices) and  prices[i] < prices[i-1]:
                curMinPrice = prices[i]
                i += 1

        return sum(profiles)
