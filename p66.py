# https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rst = []
        plus = 1
        for num in reversed(digits):
            plus, remain = (num + plus) // 10, (num+plus) % 10
            rst.append(remain)
        if plus:
            rst.append(plus)
        rst.reverse()
        return rst

    def plusOneV2(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                plus = 0
                break
            digits[i] = 0
        if plus:
            digits.insert(0, plus)
        return digits
