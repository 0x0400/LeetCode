# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

class Solution:

    def __init__(self) -> None:
        self.cache = {}

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        if s in self.cache:
            return self.cache[s]

        if len(s) == 1:
            return [[s]]

        rst = set()
        for idx in range(1, len(s)):
            left = self.partition(s[:idx])
            right = self.partition(s[idx:])
            for part1 in left:
                for part2 in right:
                    rst.add(tuple(part1 + part2))

        if self.isPalindrome(s):
            rst.add((s,))

        self.cache[s] = [list(plan) for plan in rst]
        return self.cache[s]

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
