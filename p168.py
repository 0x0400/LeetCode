# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        rst = ""
        base = 26
        while columnNumber > 0:
            columnNumber, remainder = (columnNumber-1) // base, (columnNumber-1) % base
            rst = chr(remainder + ord("A")) + rst
        return rst
