# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        colorLens = [0, 0, 0]
        for idx, num in enumerate(nums):
            if num == 2:
                continue

            if num == 1:
                nums[idx], nums[colorLens[0] + colorLens[1]] = nums[colorLens[0] + colorLens[1]], nums[idx]
                colorLens[1] += 1
                continue

            tmp = nums[colorLens[0]]
            if tmp == 0:
                pass
            elif tmp == 1:
                nums[idx], nums[colorLens[0] + colorLens[1]], nums[colorLens[0]] = nums[colorLens[0] + colorLens[1]], tmp, 0
            else:
                nums[idx], nums[colorLens[0]] = 2, 0
            colorLens[0] += 1
