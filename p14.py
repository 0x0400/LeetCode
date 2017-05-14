# https://leetcode.com/problems/longest-common-prefix/#/description

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_len = min(len(string) for string in strs)
        max_prefix = 0
        while max_prefix < min_len:
            char = strs[0][max_prefix]
            for string in strs[1:]:
                if char != string[max_prefix]:
                    return string[:max_prefix]
            max_prefix += 1
        return strs[0][:max_prefix]
