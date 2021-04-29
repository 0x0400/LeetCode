# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cache = {}
        for (sChar, tChar) in zip(s, t):
            if sChar not in cache:
                cache[sChar] = tChar
                reversedChar = " " + tChar
                if reversedChar in cache:
                    return False
                cache[reversedChar] = sChar
                continue
            if cache[sChar] != tChar:
                return False
        return True
