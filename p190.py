# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        target = 0
        for i in range(0, 32):
            target = (target << 1) | (n & 1)
            n = n >> 1
        return target
