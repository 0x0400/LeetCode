# https://leetcode.com/problems/decode-ways/

from typing import Dict

class Solution:

    def numDecodings(self, s: str) -> int:
        return self.numDecodingsWithCache(s, {})

    def numDecodingsWithCache(self, s: str, cache: Dict[str, int]) -> int:
        if s in cache:
            return cache[s]

        if not s:
            return 0

        if len(s) == 1:
            cnt = 1 if s != "0" else 0
            cache[s] = cnt
            return cnt


        if s[-1] == '0':
            if s[-2:] not in ["10", "20"]:
                return 0
            if len(s) == 2:
                return 1
            cnt = self.numDecodingsWithCache(s[:-2], cache)
            cache[s] = cnt
            return cnt


        if "1" <= s[-1] <= "6" and s[-2] in ["1", "2"]:
            if len(s) == 2:
                return 2
            cnt = self.numDecodingsWithCache(s[:-1], cache) + self.numDecodingsWithCache(s[:-2], cache)
            cache[s] = cnt
            return cnt

        if "7" <= s[-1] and s[-2]  == "1":
            if len(s) == 2:
                return 2
            cnt = self.numDecodingsWithCache(s[:-1], cache) + self.numDecodingsWithCache(s[:-2], cache)
            cache[s] = cnt
            return cnt

        cnt = self.numDecodingsWithCache(s[:-1], cache)
        cache[s] = cnt
        return cnt
