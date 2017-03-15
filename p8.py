# https://leetcode.com/problems/string-to-integer-atoi/#/description

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        sign = 1
        if str[0] == "-":
            sign = -1
            str = str[1:]
        elif str[0] == "+":
            str = str[1:]
        if not str:
            return 0

        rst = 0
        for char in str:
            if not char.isdigit():
                break
            rst = rst * 10 + int(char)
        rst = rst * sign
        if rst > 2147483647:
            rst = 2147483647
        elif rst < -2147483648:
            rst = -2147483648
        return rst
