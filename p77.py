# https://leetcode.com/problems/combinations

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combineWithRange(1, n, k)

    def combineWithRange(self, start: int, end: int, k: int) ->List[List[int]]:
        if k == 1:
            return [[i] for i in range(start, end+1)]

        delta = end - start + 1 - k
        if delta < 0:
            return []
        if delta == 0:
            return [list(range(start, end+1))]

        rst = []
        for curStart in range(start, start+delta+1):
            for plan in self.combineWithRange(curStart+1, end, k-1):
                rst.append([curStart] + plan)
        return rst
