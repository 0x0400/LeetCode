# https://leetcode.com/problems/minimum-window-substring/

# 如果字符不会重复出现的情况

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = {char: False for char in t}

        if len(s) < len(chars):
            return ""

        if len(chars) == 1:
            return t[0] if t[0] in s else ""

        rst = ""
        charQueue = []
        charDict = {}
        for curIdx, curChar in enumerate(s):
            if curChar not in chars:
                continue
            if curChar in charDict:
                charQueue.remove(curChar)
                charQueue.append(curChar)
                charDict[curChar] = curIdx
                continue

            charQueue.append(curChar)
            charDict[curChar] = curIdx
            if len(charQueue) == len(chars):
                curStr = s[charDict[charQueue[0]]:curIdx+1]
                if not rst or len(rst) > len(curStr):
                    rst = curStr
                charDict.pop(charQueue[0])
                charQueue.pop(0)
        return rst
