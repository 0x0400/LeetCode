# https://leetcode.com/problems/repeated-dna-sequences/

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cache = {}
        for idx in range(10, len(s)+1):
            subStr = s[idx-10:idx]
            cache[subStr] = cache.get(subStr, 0) + 1
        return [subStr for subStr, cnt in cache.items() if cnt > 1]
