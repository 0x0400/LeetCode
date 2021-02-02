# https://leetcode.com/problems/sudoku-solver

from typing import List, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Node:
    row: int
    column: int
    value: str = "."
    availables: List[str] = None

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return False
        return o.row == self.row and o.column == self.column


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        values = set([str(i) for i in range(1, 10)])
        sureValues = defaultdict(set)
        unsureNodes: List[Node] = []
        for rowIdx in range(0, 9):
            for colIdx in range(0, 9):
                val = board[rowIdx][colIdx]
                if val != ".":
                    sureValues[(rowIdx, None)].add(val)
                    sureValues[(None, colIdx)].add(val)
                    sureValues[(rowIdx // 3, colIdx // 3)].add(val)
                else:
                    unsureNodes.append(Node(rowIdx, colIdx))

        # 通过 行、列、小矩阵 的约束，来确定节点值
        hasNewNode = True
        while hasNewNode:
            hasNewNode = False
            for node in unsureNodes[:]:
                node.availables = (
                    values
                    - sureValues[(node.row, None)]
                    - sureValues[(None, node.column)]
                    - sureValues[(node.row // 3, node.column // 3)]
                )
                # 该节点只有一个可选值
                if len(node.availables) == 1:
                    node.value = node.availables.pop()
                    sureValues[(node.row, None)].add(node.value)
                    sureValues[(None, node.column)].add(node.value)
                    sureValues[(node.row // 3, node.column // 3)].add(node.value)
                    board[node.row][node.column] = node.value
                    hasNewNode = True
                    unsureNodes.remove(node)

        if not unsureNodes:
            return

        # 通过 递归 来暴力破解
        isOk = self.recurseGuess(0, unsureNodes, sureValues)
        if isOk:
            for node in unsureNodes:
                board[node.row][node.column] = node.value


    def recurseGuess(self, idx: int, unsureNodes: List[Node], sureValues: list):
        node = unsureNodes[idx]
        for val in sorted(unsureNodes[idx].availables):
            if (
                val not in sureValues[(node.row, None)]
                and val not in sureValues[(None, node.column)]
                and val not in sureValues[(node.row // 3, node.column // 3)]
            ):
                sureValues[(node.row, None)].add(val)
                sureValues[(None, node.column)].add(val)
                sureValues[(node.row // 3, node.column // 3)].add(val)
                node.value = val

                # 如果是最后一个节点，则成功
                if idx == len(unsureNodes) - 1:
                    return True

                # 递归调用
                isOk = self.recurseGuess(idx + 1, unsureNodes, sureValues)
                if isOk:
                    return True

                # 恢复状态
                sureValues[(node.row, None)].discard(val)
                sureValues[(None, node.column)].discard(val)
                sureValues[(node.row // 3, node.column // 3)].discard(val)
                node.value = "."
        return False


if __name__ == "__main__":
    # board = [
    #     ["5","3",".",".","7",".",".",".","."],
    #     ["6",".",".","1","9","5",".",".","."],
    #     [".","9","8",".",".",".",".","6","."],
    #     ["8",".",".",".","6",".",".",".","3"],
    #     ["4",".",".","8",".","3",".",".","1"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".","6",".",".",".",".","2","8","."],
    #     [".",".",".","4","1","9",".",".","5"],
    #     [".",".",".",".","8",".",".","7","9"]
    # ]
    board = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ]

    sol = Solution()
    sol.solveSudoku(board)
    print(board)
