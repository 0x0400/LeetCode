# https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = [0]
        maxCnt = 0
        for char in s:
            if char == '(':
                tmp.append(char)
                continue
            if tmp[-1] == '(':
                tmp[-1] = 2
            elif len(tmp) >= 2 and tmp[-2] == '(':
                tmp[-2] = 2
            else:
                tmp = [0]
                continue

            curCnt = 0
            while tmp:
                if tmp[-1] == '(':
                    break
                curCnt += tmp.pop()
            maxCnt = max(curCnt, maxCnt)
            tmp.append(curCnt)
        return maxCnt
