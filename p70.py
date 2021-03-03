# https://leetcode.com/problems/climbing-stairs/

from typing import Dict

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        return self.climbStairsWithCache(n, cache)

    def climbStairsWithCache(self, n: int, cache: Dict[int, int]) -> int:
        if n in cache:
            return cache[n]
        val = self.climbStairsWithCache(n-1, cache) + self.climbStairsWithCache(n-2, cache)
        cache[n] = val
        return val
