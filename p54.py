# https://leetcode.com/problems/spiral-matrix/

from typing import Collection, List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rowLen = len(matrix)
        colLen = len(matrix[0])
        curRowIdx = 0
        curColIdx = -1
        rst = []
        while True:
            for acIdx, ac in enumerate(actions):
                curLen = {0: colLen, 1: rowLen-1, 2: colLen-1, 3: rowLen-2}.get(acIdx)
                if curLen <= 0:
                    return rst
                for i in range(0, curLen):
                    curRowIdx +=  ac[0]
                    curColIdx +=  ac[1]
                    rst.append(matrix[curRowIdx][curColIdx])
            rowLen -= 2
            colLen -= 2
