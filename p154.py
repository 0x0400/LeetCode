# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        val = nums[0]
        for curVal in nums:
            if curVal < val:
                return curVal
        return val
