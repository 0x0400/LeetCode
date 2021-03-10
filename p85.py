# https://leetcode.com/problems/maximal-rectangle/

from typing import List, Tuple

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rowLen = len(matrix)
        colLen = len(matrix[0])

        maxArea = 0
        for rowIdx in range(0, rowLen):
            for colIdx in range(0, colLen):
                if matrix[rowIdx][colIdx] == "1":
                    maxArea = max(maxArea, self.findMaximalRectangel(matrix, (rowIdx, colIdx)))
        return maxArea


    def findMaximalRectangel(self, matrix: List[List[str]], point: Tuple[int, int]) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])

        maxArea = 1
        maxColIdx = colLen
        for rowIdx in range(point[0], rowLen):
            if matrix[rowIdx][point[1]] != "1":
                break

            oldMaxColIdx = maxColIdx
            for colIdx in range(point[1], maxColIdx):
                if matrix[rowIdx][colIdx] != "1":
                    maxColIdx = colIdx
                    maxArea = max(maxArea, (maxColIdx - point[1]) * (rowIdx - point[0] + 1))
                    break
            if maxColIdx == oldMaxColIdx:
                maxArea = max(maxArea, (maxColIdx - point[1]) * (rowIdx - point[0] + 1))

        return maxArea

