# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(0, 32):
            cnt += n & 1
            n = n >> 1
        return cnt
