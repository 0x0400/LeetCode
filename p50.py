# https://leetcode.com/problems/powx-n/

class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        halfN, isOdd = n//2, n%2
        tmp = self.myPow(x, halfN)
        rst = tmp * tmp
        return rst * x if isOdd else rst
