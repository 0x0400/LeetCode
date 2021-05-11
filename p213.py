# https://leetcode.com/problems/house-robber-ii/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # cache[0] 表示前一个屋子未被rob 的情况的最大值
        # cache[1] 表示前一个屋子被rob 的情况的最大值

        # 不 rob 第一个屋子
        cache = [0, 0]
        for num in nums[1:]:
            cache[0], cache[1] = max(cache[0], cache[1]), cache[0] + num
        curMax = max(cache)

        # 不 rob 最后一个屋子
        cache = [0, 0]
        for num in nums[:-1]:
            cache[0], cache[1] = max(cache[0], cache[1]), cache[0] + num

        return max(curMax, max(cache))
