# https://leetcode.com/problems/roman-to-integer/#/description

class Solution(object):

    SYMBOL_MAP = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return self.SYMBOL_MAP[s]

        val = 0
        pre_txt, sub_txt = (s[:2], s[2:]) if s[:2] in self.SYMBOL_MAP else (s[:1], s[1:])
        return self.SYMBOL_MAP[pre_txt] + self.romanToInt(sub_txt)
