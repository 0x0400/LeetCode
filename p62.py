# https://leetcode.com/problems/unique-paths/

from typing import Dict, Tuple

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsWithCache(m, n, {})

    def uniquePathsWithCache(self, m: int, n: int, cache: Dict[Tuple[int, int], int]) -> int:
        if (m, n) in cache:
            return cache[(m, n)]
        if (n, m) in cache:
            return cache[(n, m)]
        if m < 0 or n < 0:
            cache[(m, n)] = 0
            return 0
        if m == 1 or n == 1:
            cache[(m, n)] = 1
            return 1
        cnt = self.uniquePathsWithCache(m-1, n, cache) + self.uniquePathsWithCache(m, n-1, cache)
        cache[(m, n)] = cnt
        return cnt

    # 不实用之前计算结果的话，会超时
    def uniquePathsV1(self, m: int, n: int) -> int:
        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
