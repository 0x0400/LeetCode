# https://leetcode.com/problems/unique-paths-ii/

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[-1][-1] == 1:
            return 0

        cache = {}
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])

        cache[(rowLen-1, colLen-1)] = 1
        rowIdx = rowLen - 1
        for colIdx in range(colLen-2, -1, -1):
            if obstacleGrid[rowIdx][colIdx] == 1:
                cache[(rowIdx, colIdx)] = 0
            else:
                cache[(rowIdx, colIdx)] = cache[(rowIdx, colIdx+1)]

        colIdx = colLen - 1
        for rowIdx in range(rowLen-2, -1, -1):
            if obstacleGrid[rowIdx][colIdx] == 1:
                cache[(rowIdx, colIdx)] = 0
            else:
                cache[(rowIdx, colIdx)] = cache[(rowIdx+1, colIdx)]

        for rowIdx in range(rowLen-2, -1, -1):
            for colIdx in range(colLen-2, -1, -1):
                if obstacleGrid[rowIdx][colIdx] == 1:
                    cache[(rowIdx, colIdx)] = 0
                else:
                    cache[(rowIdx, colIdx)] = cache[(rowIdx+1, colIdx)] + cache[(rowIdx, colIdx+1)]
        return cache[(0, 0)]
