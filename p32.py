# https://leetcode.com/problems/longest-valid-parentheses/

class CharElm(object):
    def __init__(self, idx, char):
        self.idx = idx
        self.char = char


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = []
        flagList = [False] * len(s)

        for idx in range(len(s)):
            char = s[idx]
            if char == '(':
                tmp.append(CharElm(idx, char))
                continue
            if not tmp:
                continue
            if tmp[-1].char == '(':
                elm = tmp.pop()
                flagList[idx] = True
                flagList[elm.idx] = True
            else:
                tmp = []
        maxCnt = curCnt = 0
        for flag in flagList:
            if flag:
                curCnt += 1
                maxCnt = max(curCnt, maxCnt)
            else:
                curCnt = 0
        return maxCnt
