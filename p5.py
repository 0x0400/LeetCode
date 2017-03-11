
# https://leetcode.com/problems/longest-palindromic-substring/?tab=Description

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = defaultdict(list)
        for idx, char in enumerate(s):
            chars[char].append(idx)
        longest = ""
        for start_idx, char in enumerate(s):
            cur_char_idxs = chars[char]
            for end_idx in reversed(cur_char_idxs):
                if end_idx - start_idx + 1 <= len(longest):
                    break
                i, j = start_idx + 1, end_idx - 1
                while i < j:
                    if s[i] != s[j]:
                        break
                    i += 1
                    j -= 1
                if i >= j:
                    if end_idx - start_idx + 1 > len(longest):
                        longest = s[start_idx:end_idx+1]
                        break
        return longest
