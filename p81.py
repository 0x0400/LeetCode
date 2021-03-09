# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 3:
            return target in nums

        pivot = len(nums) // 2
        if target == nums[pivot]:
            return True

        left = self.binarySearch(nums, 0, pivot, target) if nums[0] < nums[pivot] else self.search(nums[:pivot], target)
        right = self.binarySearch(nums, pivot, len(nums)-1, target) if nums[pivot] < nums[-1] else self.search(nums[pivot:], target)
        return left or right


    def binarySearch(self, nums: List[int], start: int, end: int, target: int) -> bool:
        if start == end:
            return nums[start] == target

        if start < 0 or start > end or end >= len(nums):
            return False

        pivot = (start + end) // 2
        if nums[pivot] == target:
            return True
        if nums[pivot] < target:
            return self.binarySearch(nums, pivot+1, end, target)
        return self.binarySearch(nums, start, pivot-1, target)
