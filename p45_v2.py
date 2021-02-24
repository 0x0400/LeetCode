# https://leetcode.com/problems/jump-game-ii/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cache = {0:0}
        curCnt = 0
        curPlan = [0]
        target = len(nums) - 1
        while target not in cache:
            if len(curPlan) == 1:
                curIdx = curPlan[0]
                while nums[curIdx] == 1:
                    if curIdx == target:
                        return curCnt
                    curIdx += 1
                    curCnt += 1
                if curIdx == target:
                    return curCnt
                curPlan = [curIdx]

            nextPlan = []
            for curIdx in curPlan:
                if curIdx + nums[curIdx] >= target:
                    return curCnt + 1
                for nextIdx in range(curIdx+1, curIdx + nums[curIdx]+1):
                    if nextIdx not in cache:
                        cache[nextIdx] = curCnt+1
                        if curIdx + nums[curIdx] < nextIdx + nums[nextIdx]:
                            nextPlan.append(nextIdx)
            curPlan = nextPlan
            curCnt += 1

        return cache[target]

