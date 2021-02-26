# https://leetcode.com/problems/jump-game/

from typing import List, Tuple

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        totalLen = len(nums)
        if totalLen == 1:
            return True

        curIdx = 0
        maxIdx = nums[curIdx] + curIdx
        if maxIdx >= totalLen - 1:
            return True

        while curIdx <= maxIdx:
            if nums[curIdx] + curIdx > maxIdx:
                maxIdx = nums[curIdx] + curIdx
                if maxIdx >= totalLen - 1:
                    return True
            curIdx += 1
        return False
