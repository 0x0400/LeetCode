# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        rowLen = len(grid)
        colLen = len(grid[0])
        for rowIdx in range(0, rowLen):
            for colIdx in range(0, colLen):
                if grid[rowIdx][colIdx] != "1":
                    continue
                cnt += 1
                self.markNodeX(rowIdx, colIdx, grid)
        return cnt

    def markNodeX(self, rowIdx: int, colIdx: int, grid: List[List[str]]):
        """ 将与 (rowIdx, colIdx) 相关联的所有值为 1 的节点都标记成 X
        """
        nodes = [(rowIdx, colIdx)]
        rowLen = len(grid)
        colLen = len(grid[0])
        while nodes:
            curRowIdx, curColIdx = nodes.pop()
            grid[curRowIdx][curColIdx] = "X"
            if curColIdx-1 >= 0 and grid[curRowIdx][curColIdx-1] == "1":
                nodes.append((curRowIdx, curColIdx-1))
            if curColIdx+1 < colLen and grid[curRowIdx][curColIdx+1] == "1":
                nodes.append((curRowIdx, curColIdx+1))
            if curRowIdx-1 >= 0 and grid[curRowIdx-1][curColIdx] == "1":
                nodes.append((curRowIdx-1, curColIdx))
            if curRowIdx+1 < rowLen and grid[curRowIdx+1][curColIdx] == "1":
                nodes.append((curRowIdx+1, curColIdx))
