# https://leetcode.com/problems/maximum-gap/

from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxGrap = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            maxGrap = max(maxGrap, nums[i] - nums[i-1])
        return maxGrap
