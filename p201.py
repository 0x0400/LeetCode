# https://leetcode.com/problems/bitwise-and-of-numbers-range/

import math

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        rst = left
        for i in range(left+1, right+1):
            rst = rst & i
        return rst

    def rangeBitwiseAndV2(self, left: int, right: int) -> int:
        """ left 和 right 的最高位1的位数不一样的话，期间必然包含一个 2的X次方数，前后的数与其 & 操作，结果是 0
            相同的情况，需要看后面的数位数相同情况
        """
        if left == 0:
            return 0

        leftLog = int(math.log2(left))
        rightLog = int(math.log2(right))
        if leftLog != rightLog:
            return 0
        val = 2 ** leftLog
        return val + self.rangeBitwiseAndV2(left-val, right-val)

