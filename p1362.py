# https://leetcode.com/problems/closest-divisors/

from typing import List
from math import sqrt

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1 = num + 1
        num2 = num + 2
        minDivUpper = int(sqrt(num2))
        curVal = minDivUpper
        while curVal >= 1:
            if num1 % curVal == 0:
                return [curVal, num1 // curVal]
            if num2 % curVal == 0:
                return [curVal, num2 // curVal]
            curVal -= 1
