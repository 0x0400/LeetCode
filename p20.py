# https://leetcode.com/problems/valid-parentheses/tabs/description


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        queue = []
        for char in s:
            if char not in bracket_map:
                queue.append(char)
            else:
                if not queue:
                    return False
                pre_bracket = queue.pop()
                if pre_bracket != bracket_map.get(char, ""):
                    return False
        return len(queue) == 0
