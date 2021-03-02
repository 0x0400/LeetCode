# https://leetcode.com/problems/valid-number/

class Solution:

    SIGN_CHARS = ["-", "+"]
    DIGITALS = [str(i) for i in range(0, 10)]

    def isNumber(self, s: str) -> bool:
        eIdx = None
        dotCnt = 0
        totalLen = 0
        signCnt = 0
        for idx, char in enumerate(s):
            totalLen += 1
            if char == '.':
                dotCnt += 1
                if dotCnt > 1:
                    return False
                continue
            if char == 'e' or char == 'E':
                eIdx = idx
                break
            if char in self.SIGN_CHARS:
                signCnt += 1
                if signCnt > 2:
                    return False
                continue
            if char not in self.DIGITALS:
                return False
        if eIdx is None:
            return self.isInteger(s) if dotCnt == 0 else self.isDecimal(s)
        left = self.isInteger(s[:eIdx]) if dotCnt == 0 else self.isDecimal(s[:eIdx])
        right = self.isInteger(s[eIdx+1:])
        return left and right


    def isInteger(self, s: str) -> bool:
        if not s:
            return False

        if s[0] in self.SIGN_CHARS:
            s = s[1:]
        if not s:
            return False
        for char in s:
            if char not in self.DIGITALS:
                return False
        return True

    def isDecimal(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in self.SIGN_CHARS:
            s = s[1:]
        dotCnt = 0
        charCnt = 0
        for char in s:
            if char == ".":
                dotCnt += 1
                if dotCnt > 1:
                    return False
                continue
            if char not in self.DIGITALS:
                return False
            charCnt += 1
        return charCnt > 0
