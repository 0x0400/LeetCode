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

    def minPathSumV2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rowLen = len(grid)
        colLen = len(grid[0])

        preRow = grid[0].copy()
        for colIdx in range(1, colLen):
            preRow[colIdx] += preRow[colIdx-1]

        for rowIdx in range(1, rowLen):
            curRow = grid[rowIdx].copy()
            curRow[0] += preRow[0]
            for colIdx in range(1, colLen):
                curRow[colIdx] += min(preRow[colIdx], curRow[colIdx-1])
            preRow = curRow
        return preRow[-1]
