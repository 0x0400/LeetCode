# https://leetcode.com/problems/word-search-ii/

from typing import Dict, List, Set, Tuple

from collections import defaultdict, Counter

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        cache = defaultdict(list)
        charCounter = Counter()
        rowLen = len(board)
        colLen = len(board[0])
        for rowIdx in range(rowLen):
            for colIdx in range(colLen):
                cache[board[rowIdx][colIdx]].append((rowIdx, colIdx))
                charCounter[board[rowIdx][colIdx]] += 1

        rst = []
        for word in words:
            wordCounter = Counter(word)
            for char, cnt in wordCounter.items():
                if cnt > charCounter.get(char, 0):
                    break
            else:
                # 为了规避 board 都是单字母的情况下，可能会出现超时的情况
                if len(wordCounter) == 1:
                    rst.append(word)
                    continue
                if self.isWordInBoard(word, cache):
                # if self.isWordInBoardDFS(word, [], cache):
                    rst.append(word)
        return rst

    def isWordInBoard(self, word: str, cache: Dict[str, List[Tuple[int, int]]]) -> bool:
        if word[0] not in cache:
            return False

        neighborDeltas = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        plans = [[cell] for cell in cache[word[0]]]
        for char in word[1:]:
            if char not in cache:
                return False
            newPlans = []
            choices = cache[char]
            for plan in plans:
                lastCell = plan[-1]
                for delta in neighborDeltas:
                    newCell = (lastCell[0]+delta[0], lastCell[1]+delta[1])
                    if newCell in plan:
                        continue
                    if newCell not in choices:
                        continue
                    newPlans.append(plan + [newCell])
            if not newPlans:
                return False
            plans = newPlans
        return True

    def isWordInBoardDFS(self, word: str, traveledCells: List[Tuple[int, int]], cache: Dict[str, List[Tuple[int, int]]]) -> bool:
        if not word:
            return True

        if word[0] not in cache:
            return False

        neighborDeltas = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        choices = cache[word[0]]
        for cell in choices:
            if cell in traveledCells:
                continue
            for delta in neighborDeltas:
                neighborCell = (cell[0]+delta[0], cell[1]+delta[1])
                if traveledCells and neighborCell != traveledCells[-1]:
                    continue
                if self.isWordInBoardDFS(word[1:], traveledCells + [cell], cache):
                    return True
        return False
