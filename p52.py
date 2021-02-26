# https://leetcode.com/problems/n-queens-ii/

from typing import List, Tuple, Dict

class Solution:
    def totalNQueens(self, n: int) -> int:
        rst = self._solveNQueens(0, n, {}, list(range(n)))
        return len(rst)

    def _solveNQueens(self, rowIdx: int, n: int, curPlan: Dict[Tuple[int, int], bool], cols: List[int]):
        if rowIdx >= n:
            return []
        rst = []
        for idx, col in enumerate(cols):
            point = (rowIdx, col)
            rowStr = self._getRowStr(n, col)
            isOk = self._isOk(point, n, curPlan)
            if not isOk:
                continue
            if rowIdx == n-1:
                rst.append([rowStr])
                continue

            newCols = cols.copy()
            newCols.pop(idx)
            newPlan = curPlan.copy()
            newPlan[point] = True

            subRst = self._solveNQueens(rowIdx+1, n, newPlan, newCols)
            for item in subRst:
                if len(item) == len(newCols):
                    rst.append([rowStr] + item)
        return rst

    def _getRowStr(self, n: int, col: int) -> str:
        rst = ""
        for i in range(n):
            rst += "Q" if i == col else "."
        return rst

    def _isOk(self, point: Tuple[int, int], n:int, curPlan: Dict[Tuple[int, int], bool]) -> bool:
        (2, 0)

        for colIdx in range(0, n):
            step = abs(point[1] - colIdx)
            if step == 0:
                continue
            for rowIdx in (point[0] - step, point[0] + step):
                if 0 <= rowIdx < n:
                    if (rowIdx, colIdx) in curPlan:
                        return False
        return True
