# https://leetcode.com/problems/minimum-path-sum/

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rowLen = len(grid)
        colLen = len(grid[0])

        rowIdx = rowLen - 1
        preRows = grid[rowIdx].copy()
        for colIdx in range(colLen-2, -1, -1):
            preRows[colIdx] += preRows[colIdx+1]

        for rowIdx in range(rowLen-2, -1, -1):
            curRows = grid[rowIdx].copy()
            curRows[-1] += preRows[-1]
            for colIdx in range(colLen-2, -1, -1):
                curRows[colIdx] += min(preRows[colIdx], curRows[colIdx+1])
            preRows = curRows
        return preRows[0]
