# https://leetcode.com/problems/scramble-string/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 == s2

        charCnt1 = [0] * (ord('z') - ord('a') + 1)
        charCnt2 = charCnt1.copy()
        revertCharCnt2 = charCnt1.copy()
        aInt = ord('a')
        for i in range(0, len(s1)-1):
            charCnt1[ord(s1[i]) - aInt] += 1
            charCnt2[ord(s2[i]) - aInt] += 1
            revertCharCnt2[ord(s2[-1-i]) - aInt] += 1
            if charCnt1 == charCnt2:
                leftIsOk = self.isScramble(s1[:i+1], s2[:i+1])
                if leftIsOk:
                    rightIsOk = self.isScramble(s1[i+1:], s2[i+1:])
                    if rightIsOk:
                        return True
            if charCnt1 == revertCharCnt2:
                leftIsOk = self.isScramble(s1[:i+1], s2[-1-i:])
                if leftIsOk:
                    rightIsOk = self.isScramble(s1[i+1:], s2[:-1-i])
                    if rightIsOk:
                        return True

        return s1 == s2
