# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastDuplicateNum = None
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] == nums[idx+1]:
                if lastDuplicateNum != nums[idx]:
                    lastDuplicateNum = nums[idx]
                    continue
                nums.pop(idx)

        return len(nums)
