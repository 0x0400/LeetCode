# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

    def findKthLargestQS(self, nums: List[int], k: int) -> int:
        ''' 使用 快排 的方式，查找对应的值
        '''
        targetIdx = len(nums) - k

        start = 0
        end = len(nums) - 1
        while start < end:
            ltIdx = start-1
            for i in range(start, end):
                if nums[i] < nums[end]:
                    ltIdx += 1
                    nums[i], nums[ltIdx] = nums[ltIdx], nums[i]
            sentinalIdx = ltIdx + 1
            nums[end], nums[sentinalIdx] = nums[sentinalIdx], nums[end]
            if sentinalIdx == targetIdx:
                return nums[sentinalIdx]
            if targetIdx < sentinalIdx:
                end = sentinalIdx - 1
                continue
            if targetIdx > sentinalIdx:
                start = sentinalIdx + 1

        return nums[targetIdx]
