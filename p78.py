# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst = self.subsetsWithoutBlank(nums)
        return [[]] + rst

    def subsetsWithoutBlank(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        rst = [[nums[0]]]
        subsets = self.subsetsWithoutBlank(nums[1:])
        rst += subsets
        for plan in subsets:
            rst.append([nums[0]] + plan)
        return rst
