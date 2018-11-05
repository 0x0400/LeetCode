# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter

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

        wordCnt = Counter()
        for word in words:
            wordCnt[word] += 1

        flagList = [True] * s_len

        rst = []
        i = 0
        s_end = s_len - words_len
        while i <= s_end:
            wordCntTmp = wordCnt.copy()
            j = i
            while j < s_len:
                if not flagList[j]:
                    break
                substr = s[j:j+word_len]
                if substr not in wordCntTmp:
                    idx = i
                    while idx <= j - word_len:
                        flagList[idx] = False
                        idx += word_len
                if wordCntTmp[substr]:
                    wordCntTmp[substr] -= 1
                    j += word_len
                else:
                    break
            for val in wordCntTmp.values():
                if val > 0:
                    break
            else:
                rst.append(i)
            i += 1
        return rst
