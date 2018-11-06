# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        leftIdx = 0
        rightIdx = len(nums) - 1

        while leftIdx + 1 < rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            if nums[midIdx] == target:
                return midIdx

            if nums[midIdx] > nums[leftIdx]:
                if nums[leftIdx] <= target < nums[midIdx]:
                    rightIdx = midIdx - 1
                else:
                    leftIdx = midIdx + 1
                continue

            if nums[midIdx] < target <= nums[rightIdx]:
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx - 1

        if nums[leftIdx] == target:
            return leftIdx
        if nums[rightIdx] == target:
            return rightIdx

        return -1
