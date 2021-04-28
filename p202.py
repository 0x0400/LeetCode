# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        while n != 1:
            if n in cache:
                return False
            cache[n] = False

            m = 0
            while n != 0:
                m += (n % 10) ** 2
                n = n // 10
            n = m
        return True
