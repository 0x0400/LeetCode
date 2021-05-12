# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rs = s[::-1]
        for i in range(0, len(rs)):
            if self.isPalindrome(rs[i:]):
                return rs[:i] + s
        return rs + s

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
