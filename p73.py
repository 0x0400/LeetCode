# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])
        zeroCols = {}
        for rowIdx in range(0, rowLen):
            for colIdx in range(0, colLen):
                if matrix[rowIdx][colIdx] != 0:
                    continue
                zeroCols[colIdx] = True
                for j in range(0, colIdx):
                    matrix[rowIdx][j] = 0
                for j in range(colIdx+1, colLen):
                    if matrix[rowIdx][j] == 0:
                        zeroCols[j] = True
                    else:
                         matrix[rowIdx][j] = 0
                break
        for colIdx in zeroCols:
            for rowIdx in range(0, rowLen):
                matrix[rowIdx][colIdx] = 0
