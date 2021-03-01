# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lens = 0
        totalLen = len(s)
        curIdx = totalLen - 1
        while curIdx >= 0 and s[curIdx] == " ":
            curIdx -= 1

        if curIdx < 0:
            return 0

        lens = 0
        while curIdx >= 0 and s[curIdx] != " ":
            lens += 1
            curIdx -= 1

        return lens
