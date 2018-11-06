# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):

    def ascendingSearch(self, nums, target, leftIdx, rightIdx):
        if rightIdx < leftIdx:
            return -1
        if leftIdx == rightIdx:
            return leftIdx if nums[leftIdx] == target else -1

        midIdx = (leftIdx + rightIdx) // 2
        if nums[midIdx] == target:
            return midIdx

        if nums[midIdx] > target:
            return self.ascendingSearch(nums, target, leftIdx, midIdx-1)
        if nums[midIdx] < target:
            return self.ascendingSearch(nums, target, midIdx+1, rightIdx)

    def rotatedSearch(self, nums, target, leftIdx, rightIdx):
        if rightIdx < leftIdx:
            return -1
        if leftIdx == rightIdx:
            return leftIdx if nums[leftIdx] == target else -1

        midIdx = (leftIdx + rightIdx) // 2
        if nums[midIdx] == target:
            return midIdx

        if midIdx == leftIdx:
            return rightIdx if nums[rightIdx] == target else -1

        if nums[midIdx] > nums[leftIdx]:
            if nums[midIdx] > target >= nums[leftIdx]:
                return self.ascendingSearch(nums, target, leftIdx, midIdx-1)
            return self.rotatedSearch(nums, target, midIdx+1, rightIdx)

        if nums[midIdx] < target <= nums[rightIdx]:
            return self.ascendingSearch(nums, target, midIdx+1, rightIdx)
        return self.rotatedSearch(nums, target, leftIdx, midIdx-1)


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.rotatedSearch(nums, target, 0, len(nums)-1)
