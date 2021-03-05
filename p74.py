# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])

        for rowIdx in range(0, rowLen):
            if matrix[rowIdx][colLen-1] < target:
                continue
            if matrix[rowIdx][colLen-1] == target:
                return True
            for colIdx in range(0, colLen):
                if matrix[rowIdx][colIdx] == target:
                    return True
                if matrix[rowIdx][colIdx] > target:
                    return False
        return False
