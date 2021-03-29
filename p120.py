# https://leetcode.com/problems/triangle/

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curTotals = triangle[0]
        for curRowIdx in range(1, len(triangle)):
            nextTotals = [None] * (len(curTotals) + 1)
            for curIdx, total in enumerate(curTotals):
                if nextTotals[curIdx] is None:
                    nextTotals[curIdx] = total + triangle[curRowIdx][curIdx]
                else:
                    nextTotals[curIdx] = min(total + triangle[curRowIdx][curIdx], nextTotals[curIdx])
                nextTotals[curIdx+1] = total + triangle[curRowIdx][curIdx+1]
            curTotals = nextTotals
        return min(curTotals)
