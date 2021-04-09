# https://leetcode.com/problems/word-break/

from typing import List

class Solution:

    def __init__(self) -> None:
        self.cache = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        通过 cache 来缓存之前计算的结果（False），后面遇到同样的字符串重复计算
        """
        if s in self.cache:
            return self.cache[s]

        for word in wordDict:
            if s == word:
                self.cache[s] = True
                return True
            if s.startswith(word):
                isOk = self.wordBreak(s[len(word):], wordDict)
                self.cache[s] = isOk
                if isOk:
                    return True
        self.cache[s] = False
        return False
