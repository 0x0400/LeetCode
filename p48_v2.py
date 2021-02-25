# https://leetcode.com/problems/rotate-image/

# 按边处理；从外圈到内圈
# 选定4个顶点，其他点通过距离这些顶点的距离来计算翻转后的坐标

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        totalLen = len(matrix)
        # 上下翻转
        for rowIdx in range(totalLen):
            reversedRowIdx = totalLen - rowIdx -1
            if rowIdx >= reversedRowIdx:
                break
            for colIdx in range(totalLen):
                matrix[rowIdx][colIdx], matrix[reversedRowIdx][colIdx] = matrix[reversedRowIdx][colIdx], matrix[rowIdx][colIdx]

        # 沿着对角线翻转
        for rowIdx in range(totalLen):
            for colIdx in range(totalLen):
                if colIdx <= rowIdx:
                    continue
                matrix[rowIdx][colIdx], matrix[colIdx][rowIdx] = matrix[colIdx][rowIdx], matrix[rowIdx][colIdx]
