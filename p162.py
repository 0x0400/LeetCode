# https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                continue
            if i < len(nums)-1 and nums[i] < nums[i+1]:
                continue
            return i
        return len(nums)-1

    def findPeakElementV2(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                i += 1
                continue
            return i
        return len(nums)-1
