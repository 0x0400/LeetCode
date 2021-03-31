# https://leetcode.com/problems/shuffle-string/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        chars = [''] * len(indices)
        for origIdx, targetIdx in enumerate(indices):
            chars[targetIdx] = s[origIdx]
        return ''.join(chars)
