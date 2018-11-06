# https://leetcode.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 2
        while idx >= 0:
            if nums[idx] >= nums[idx+1]:
                idx -= 1
                continue

            minIdx = len(nums) -1
            while minIdx > idx:
                if nums[minIdx] <= nums[idx]:
                    minIdx -= 1
                    continue
                break
            nums[idx], nums[minIdx] = nums[minIdx], nums[idx]
            break
        idx += 1
        lastIdx = len(nums) - 1
        i = 0
        while idx + i < lastIdx - i:
            nums[idx+i], nums[lastIdx-i] = nums[lastIdx-i], nums[idx+i]
            i += 1
