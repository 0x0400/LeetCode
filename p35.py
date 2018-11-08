# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
                continue
            right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[left] > target:
            return left
        if nums[right] > target:
            return right
        return right + 1

