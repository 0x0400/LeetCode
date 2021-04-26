# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache[0] 表示前一个屋子未被rob 的情况的最大值
        # cache[1] 表示前一个屋子被rob 的情况的最大值
        cache = [0, 0]
        for num in nums:
            cache[0], cache[1] = max(cache[0], cache[1]), cache[0] + num
        return max(cache)
