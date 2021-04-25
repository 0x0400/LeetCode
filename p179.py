# https://leetcode.com/problems/largest-number/

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strs = [str(num) for num in nums]
        num_strs.sort()

        rst = []
        while num_strs:
            curNum = num_strs.pop()
            for idx, num in enumerate(num_strs):
                # 需要考虑 有数值是 最大值的前缀 情况
                if curNum.startswith(num) and curNum != num:
                    if num + curNum >= curNum + num:
                        num_strs.pop(idx)
                        num_strs.append(curNum)
                        curNum = num
                        break
            rst.append(curNum)
        return "".join(rst).lstrip("0") or "0"

    def largestNumberV2(self, nums: List[int]) -> str:

        def cmp_func(x: str, y: str):
            if x+y == y+x:
                return 0
            if x+y > y+x:
                return 1
            return -1

        num_strs = [str(num) for num in nums]
        num_strs.sort(key=cmp_to_key(cmp_func), reverse=True)
        return "".join(num_strs).lstrip("0") or "0"
