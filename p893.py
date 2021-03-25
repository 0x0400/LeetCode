# https://leetcode.com/problems/groups-of-special-equivalent-strings/

from typing import List, Tuple

class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        cache = {}
        for s in A:
            # cache[self.getStrKey(s)] = True
            cache[self.getStrKeyV2(s)] = True
        return len(cache)

    def getStrKey(self, s: str) -> Tuple[str, str]:
        odd = []
        even = []
        for idx, char in enumerate(s):
            if idx % 2 == 0:
                even.append(char)
            else:
                odd.append(char)
        odd.sort()
        even.sort()
        return ("".join(odd), "".join(even))

    def getStrKeyV2(self, s: str):
        asn = [0] * 52
        for idx, char in enumerate(s):
            asn[ord(char) - ord('a') + 26 * (idx %2)] += 1
        return tuple(asn)
