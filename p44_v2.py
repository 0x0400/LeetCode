# https://leetcode.com/problems/wildcard-matching/

from typing import List, Dict

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        chars = [""]
        for char in p:
            if char == "*":
                if chars[-1] != char:
                    chars.append(char)
                continue
            if char == "?":
                chars.append(char)
                continue

            if chars[-1] != "*" and chars[-1] != "?":
                chars[-1] += char
            else:
                chars.append(char)
        if not chars[0]:
            chars.pop(0)
        return self._isMatch(s, chars, 0, 0, {})

    def _isMatch(self, s: str, p: List[str], curSIdx : int, curPIdx : int, cache: Dict[str, int]) -> bool:
        print(s, p, curSIdx, curPIdx, cache)
        if not p:
            return len(s) == curSIdx

        if p[0] == "*":
            if len(p) == 1:
                return True

            newP = p[1:]
            newPIdx = curPIdx + 1
            newSIdx = curSIdx
            while newSIdx <= len(s):
                if newP and newP[0] != "?":
                    newSIdx = max(newSIdx, cache.get(newPIdx, 0))

                if self._isMatch(s, newP, newSIdx, newPIdx, cache):
                    return True
                newSIdx += 1
            return False

        if curSIdx >= len(s):
            return False

        if p[0] == "?":
            return self._isMatch(s, p[1:], curSIdx+1, curPIdx+1, cache)

        if not s[curSIdx:].startswith(p[0]):
            # 如何失败的话，以后递归查询时，可以直接跳到 curSIdx 之后的位置去匹配
            cache[curPIdx] = max(cache.get(curPIdx, 0), curSIdx+1)
            return False
        return self._isMatch(s, p[1:], curSIdx+len(p[0]), curPIdx+1, cache)
