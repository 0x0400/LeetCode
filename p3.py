# https://leetcode.com/problems/longest-substring-without-repeating-characters/?tab=Descriptions

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = []
        maxLen = 0

        for char in s:
            if char  in letters:
                index = letters.index(char)
                letters = letters[index+1:]
            letters.append(char)
            maxLen = max(maxLen, len(letters))
        return maxLen
