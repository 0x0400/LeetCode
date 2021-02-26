# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        curNum = None
        for n in nums:
            if curNum is None:
                maxNum = max(n, maxNum)
                if n > 0:
                    curNum = n
                continue
            curNum += n
            maxNum = max(curNum, maxNum)
            if curNum <= 0:
                curNum = None
        return maxNum
