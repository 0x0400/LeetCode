# https://leetcode.com/problems/largest-number/

from typing import List

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
