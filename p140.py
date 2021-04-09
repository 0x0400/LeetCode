# https://leetcode.com/problems/word-break-ii/

from typing import List

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s in self.cache:
            return self.cache[s]

        rst = []
        for word in wordDict:
            if s == word:
                rst.append(s)
                continue

            if s.startswith(word):
                subWords = self.wordBreak(s[len(word):], wordDict)
                for words in subWords:
                    rst.append(word + " " + words)
        self.cache[s] = rst
        return self.cache[s]
