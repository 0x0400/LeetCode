# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinInRange(nums, 0, len(nums)-1)

    def findMinInRange(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return nums[start]
        if start == end - 1:
            return min(nums[start], nums[end])

        middle = (start + end) // 2
        if nums[middle] > nums[end]:
            return self.findMinInRange(nums, middle, end)
        if nums[middle] < nums[start]:
            return self.findMinInRange(nums, start, middle)
        return nums[start]
