# https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rst = [[1]]
        rowIdx = 2
        while rowIdx <= numRows:
            row = []
            for i in range(rowIdx):
                if i == 0 or i == rowIdx-1:
                    row.append(1)
                else:
                    row.append(rst[-1][i-1]+rst[-1][i])
            rst.append(row)
            rowIdx += 1
        return rst
