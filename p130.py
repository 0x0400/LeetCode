# https://leetcode.com/problems/surrounded-regions/

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        oPoints = {}
        unsurrounedPoints = {}

        rowLen = len(board)
        colLen = len(board[0])
        for rowIdx in range(0, rowLen):
            for colIdx in range(0, colLen):
                if board[rowIdx][colIdx] == "O":
                    if rowIdx in [0, rowLen-1] or colIdx in [0, colLen-1]:
                        unsurrounedPoints[(rowIdx, colIdx)] = True
                    else:
                        oPoints[(rowIdx, colIdx)] = True

        while unsurrounedPoints:
            for (rowIdx, colIdx) in list(unsurrounedPoints.keys()):
                if (rowIdx-1, colIdx) in oPoints:
                    oPoints.pop((rowIdx-1, colIdx))
                    unsurrounedPoints[(rowIdx-1, colIdx)] = True
                if (rowIdx+1, colIdx) in oPoints:
                    oPoints.pop((rowIdx+1, colIdx))
                    unsurrounedPoints[(rowIdx+1, colIdx)] = True
                if (rowIdx, colIdx-1) in oPoints:
                    oPoints.pop((rowIdx, colIdx-1))
                    unsurrounedPoints[(rowIdx, colIdx-1)] = True
                if (rowIdx, colIdx+1) in oPoints:
                    oPoints.pop((rowIdx, colIdx+1))
                    unsurrounedPoints[(rowIdx, colIdx+1)] = True
                unsurrounedPoints.pop((rowIdx, colIdx))

        for (rowIdx, colIdx) in oPoints:
            board[rowIdx][colIdx] = 'X'
