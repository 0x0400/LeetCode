# https://leetcode.com/problems/permutations-ii/

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        if len(nums) == 1:
            return [nums]
        rst = []
        cache = {}
        for i, num in enumerate(nums):
            if num in cache:
                continue
            plans = self.permuteUnique(nums[0:i] + nums[i+1:])
            for p in plans:
                rst.append([num] + p)
            cache[num] = True
        return rst
