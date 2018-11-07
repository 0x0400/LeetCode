# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        while left+1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
                continue
            if nums[mid] < target:
                left = mid + 1
                continue

            leftMid = (left + mid) // 2
            while nums[left] != target:
                if nums[leftMid] < target:
                    left = leftMid + 1
                    leftMid = (left + mid) // 2
                    continue
                leftMid = (left + leftMid) // 2

            rightMid = (mid + right + 1) // 2
            while nums[right] != target:
                if nums[rightMid] > target:
                    right = rightMid - 1
                    rightMid = (mid + right + 1) // 2
                    continue
                rightMid = (rightMid + right + 1) // 2

            return [left, right]

        rst = [-1, -1]
        if nums[left] == target:
            rst = [left, left]
        if nums[right] == target:
            rst[1] = right
            if rst[0] == -1:
                rst[0] = right
        return rst

