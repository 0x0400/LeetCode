# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List

# 可以参考 p54 的代码
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rst = []
        for i in range(n):
            rst.append([0] * n)

        actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rowLen = n
        colLen = n
        curRowIdx = 0
        curColIdx = -1
        curNum = 0
        while True:
            for acIdx, ac in enumerate(actions):
                curLen = {0: colLen, 1: rowLen-1, 2: colLen-1, 3: rowLen-2}.get(acIdx)
                if curLen <= 0:
                    return rst
                for i in range(0, curLen):
                    curNum += 1
                    curRowIdx += ac[0]
                    curColIdx += ac[1]
                    rst[curRowIdx][curColIdx] = curNum
            rowLen -= 2
            colLen -= 2
