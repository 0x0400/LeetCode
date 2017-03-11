# https://leetcode.com/problems/zigzag-conversion/?tab=Description

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows <= 1:
            return s
        sLen = len(s)
        tmp = []
        row = 0
        totalStep = numRows * 2 - 2
        while row < numRows:
            step = (numRows - row) * 2 - 2
            if step == 0:
                step = totalStep
            idx = row
            while idx < sLen:
                tmp.append(s[idx])
                idx += step
                step = totalStep - step
                if step == 0:
                    step = totalStep
            row += 1
        return "".join(tmp)
