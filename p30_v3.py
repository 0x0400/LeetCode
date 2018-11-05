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

        rst = []
        for idx in range(word_len):
            start = idx
            last = start
            wordCntTmp = Counter()
            while last < s_len:
                substr = s[last:last+word_len]
                if substr not in wordCnt:
                    start = last +word_len
                    last = start
                    wordCntTmp = Counter()
                    continue
                wordCntTmp[substr] += 1
                if wordCntTmp[substr] > wordCnt[substr]:
                    while start < last:
                        startStr = s[start:start+word_len]
                        wordCntTmp[startStr] -= 1
                        start += word_len
                        if startStr == substr:
                            break
                last += word_len
                if last == start + words_len:
                    rst.append(start)
                    wordCntTmp[s[start:start+word_len]] -= 1
                    start += word_len
        return rst
