# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        curSum = 0
        curStart = 0
        minLen = len(nums) + 1

        for idx, num in enumerate(nums):
            if num > target:
                return 1
            curSum += num
            if curSum < target:
                continue

            while curSum >= target:
                curSum -= nums[curStart]
                curStart += 1
            minLen = min(minLen, idx-curStart+2)

        return 0 if minLen > len(nums) else minLen
