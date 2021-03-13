# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rst = self.subsetsWithoutBlank(nums)
        return [[]] + rst

    def subsetsWithoutBlank(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]

        curNum = nums[0]
        duplicateNums = []
        for idx, val in enumerate(nums):
            if curNum != val:
                break
            duplicateNums.append(nums[:idx+1])
        duplicatedLen = len(duplicateNums[-1])
        if duplicatedLen == len(nums):
            return duplicateNums
        subsets = self.subsetsWithoutBlank(nums[duplicatedLen:])
        rst = duplicateNums.copy()
        for duplicatePlan in duplicateNums:
            for plan in subsets:
                rst.append(duplicatePlan + plan)
        rst += subsets
        return rst
