# https://leetcode.com/problems/reverse-integer/#/description

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = -1 if x < 0 else 1
        x = abs(x)
        rst = 0
        while True:
            x, remainder = divmod(x, 10)
            rst = rst * 10 + remainder
            if x == 0:
                break
        if rst >= 2**31:
            return 0
        return rst * negative
