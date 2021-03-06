# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        if len(t) == 1:
            return t if t in s else ""

        charCnt = {}
        for char in t:
            charCnt[char] = charCnt.get(char, 0) + 1

        rst = ""
        charQueue = []
        charDict = {}
        for curIdx, curChar in enumerate(s):
            if curChar not in charCnt:
                continue
            if curChar in charDict:
                charDict[curChar].append(curIdx)
                charQueue.append(curChar)
                # 超过该字符的个数，需要删除该字符出现的第一个位置
                if len(charDict[curChar]) > charCnt[curChar]:
                    charQueue.remove(curChar)
                    charDict[curChar].pop(0)
            else:
                charQueue.append(curChar)
                charDict[curChar] = [curIdx]

            if len(charQueue) == len(t):
                curStr = s[charDict[charQueue[0]][0]:curIdx+1]
                if not rst or len(rst) > len(curStr):
                    rst = curStr
                # 删除该窗口的第一个字符，并重新查找
                firstChar = charQueue[0]
                charQueue.pop(0)
                charDict[firstChar].pop(0)
                if not charDict[firstChar]:
                    charDict.pop(firstChar)
        return rst
