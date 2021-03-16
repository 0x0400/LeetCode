# https://leetcode.com/problems/unique-binary-search-trees/

from typing import Dict

class Solution:
    def numTrees(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        return self.numTreesWithCache(n, cache)

    def numTreesWithCache(self, n: int, cache: Dict[int, int]) -> int:
        if n in cache:
            return cache[n]

        if n == 1:
            return 1

        if n == 2:
            return 2

        rst = 0
        for i in range(1, n+1):
            if i == 1 or i == n:
                rst += self.numTreesWithCache(n-1, cache)
                continue
            rst += self.numTreesWithCache(i-1, cache) * self.numTreesWithCache(n-i, cache)

        cache[n] = rst
        return rst
