# https://leetcode.com/problems/integer-to-roman/#/description

from collections import OrderedDict

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        NOTATION = OrderedDict([(1000, "M"),
                              (900, "CM"),
                              (500, "D"),
                              (400, "CD"),
                              (100, "C"),
                              (90, "XC"),
                              (50, "L"),
                              (40, "XL"),
                              (10, "X"),
                              (9, "IX"),
                              (5, "V"),
                              (4, "IV"),
                              (1, "I"), ])
        rst = ""
        for val, symbol in NOTATION.items():
            while val <= num:
                rst += symbol
                num -= val
        return rst
