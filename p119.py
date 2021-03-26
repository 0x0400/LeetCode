# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        curRowIdx = 0
        while curRowIdx < rowIndex:
            for i in range(len(row)-1, 0, -1):
                row[i] = row[i] + row[i-1]
            row.append(1)
            curRowIdx += 1
        return row
