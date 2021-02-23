# https://leetcode.com/problems/wildcard-matching/


# 如何优化匹配的速率
# 主要是遇到 * 时，后面的匹配需要一直遍历才行

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        chars = [""]
        for char in p:
            if char == "*" and chars[-1] == char:
                continue
            chars.append(char)
        p = "".join(chars)

        return self._isMatch(s, p)

    def _isMatch(self, s: str, p: str) -> bool:
        if not p:
            return len(s) == 0

        if p[0] == "*":
            if len(p) == 1:
                return True

            newP = p[1:]
            i = 0
            while i <= len(s):
                if self._isMatch(s[i:], newP):
                    return True
                i += 1
            return False

        if not s:
            return False

        if p[0] != "?" and p[0] != s[0]:
            return False
        return self._isMatch(s[1:], p[1:])
