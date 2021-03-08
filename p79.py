# https://leetcode.com/problems/word-search/

from typing import List, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        for rowIdx in range(0, rowLen):
            for colIdx in range(0, colLen):
                isExist = self.findWord(board, word, (rowIdx, colIdx), 0, [])
                if isExist:
                    return True
        return False

    def getAdjacentNodes(self, node: Tuple[int, int], rowLen: int, colLen: int) -> List[Tuple[int, int]]:
        nodes = []
        if node[1] + 1 < colLen:
            nodes.append((node[0], node[1]+1))
        if node[0] + 1 < rowLen:
            nodes.append((node[0]+1, node[1]))
        if node[1] - 1 >= 0:
            nodes.append((node[0], node[1]-1))
        if node[0] - 1 >= 0:
            nodes.append((node[0]-1, node[1]))
        return nodes

    def findWord(self, board: List[List[str]], word: str, curNode: Tuple[int, int], curWordIdx: int, nodes: List[Tuple[int, int]]) -> bool:
        if board[curNode[0]][curNode[1]] != word[curWordIdx]:
            return False
        nodes.append(curNode)
        if curWordIdx == len(word)-1:
            return True

        aNodes = self.getAdjacentNodes(curNode, len(board), len(board[0]))
        for node in aNodes:
            if node in nodes:
                continue
            isExist = self.findWord(board, word, node, curWordIdx+1, nodes)
            if isExist:
                return True
        nodes.pop()
        return False
