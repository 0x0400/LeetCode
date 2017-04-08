# https://leetcode.com/problems/palindrome-number/#/description

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y, z = abs(x), 0
        while y != 0:
            z = z * 10 + y % 10
            y = y / 10
        return z == abs(x)
