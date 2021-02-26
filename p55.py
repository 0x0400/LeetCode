# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        totalLen = len(nums)
        if totalLen == 1:
            return True

        for i, n in enumerate(nums):
            nums[i] = i + n

        curIdx = 0
        maxIdx = nums[curIdx]
        if maxIdx >= totalLen-1:
            return True
        while curIdx < totalLen:
            if curIdx == maxIdx:
                return False
            if maxIdx >= totalLen-1:
                return True
            for i in range(curIdx+1, maxIdx+1):
                if nums[i] >= maxIdx:
                    curIdx = i
                    maxIdx = nums[i]
