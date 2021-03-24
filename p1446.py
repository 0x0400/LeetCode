# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        preChar = ""
        curCnt = 0
        maxCnt = 0
        for char in s:
            if char == preChar:
                curCnt += 1
            else:
                maxCnt = max(maxCnt,curCnt)
                preChar = char
                curCnt = 1
        maxCnt = max(maxCnt, curCnt)
        return maxCnt
