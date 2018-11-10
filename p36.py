# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if len(board) != 9:
            return False

        # row
        for row in board:
            if len(row) != 9:
                return False
            nums = {}
            for num in row:
                if num in nums:
                    return False
                if num != ".":
                    nums[num] = True

        # column
        for colIdx in range(0, 9):
            nums = {}
            for rowIdx in range(0, 9):
                num = board[rowIdx][colIdx]
                if num in nums:
                    return False
                if num != ".":
                    nums[num] = True

        # sub-box
        for subRowIdx in range(0, 9, 3):
            for subColIdx in range(0, 9, 3):
                nums = {}
                for rowIdx in range(subRowIdx, subRowIdx + 3):
                    for colIdx in range(subColIdx, subColIdx + 3):
                        num = board[rowIdx][colIdx]
                        if num in nums:
                            return False
                        if num != ".":
                            nums[num] = True

        return True
