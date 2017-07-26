# https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description

from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_map = {
            "0": ["0"],
            "1": ["1"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []

        digits_map_list = [letter_map[char] for char in digits]

        result = []
        for letters in product(*digits_map_list):
            result.append("".join(letters))
        return result
