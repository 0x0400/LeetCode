# https://leetcode.com/problems/implement-strstr/description/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len < needle_len:
            return -1

        for idx in range(0, haystack_len - needle_len + 1):
            if haystack[idx:idx+needle_len] == needle:
                return idx
        return -1
