# https://leetcode.com/problems/gray-code/

from typing import List

class Solution:
    # 规律就是 首位加1 其它位用之前结果反向遍历
    def grayCode(self, n: int) -> List[int]:
        rst = [0, 1]
        for i in range(2, n+1):
            addNum = 1 << (i-1)
            rst += [addNum + val for val in reversed(rst)]

        return rst
