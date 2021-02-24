# https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        if len(nums) == 1:
            return [nums]
        rst = []
        for i, num in enumerate(nums):
            plans = self.permute(nums[0:i] + nums[i+1:])
            for p in plans:
                rst.append([num] + p)
        return rst
