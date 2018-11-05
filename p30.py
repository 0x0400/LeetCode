# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        word_len = len(words[0])
        if word_len <= 0:
            return []
        words_len = word_len * len(words)
        s_len = len(s)
        if s_len < words_len:
            return []

        rst = []
        i = 0
        while i <= s_len - words_len:
            left_words = words[:]
            j = i
            while left_words:
                substr = s[j:j+word_len]
                if substr in left_words:
                    left_words.remove(substr)
                    j += word_len
                else:
                    break
            if not left_words:
                rst.append(i)
            i += 1
        return rst
