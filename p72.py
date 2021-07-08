# https://leetcode.com/problems/edit-distance/

# refer to https://en.wikipedia.org/wiki/Levenshtein_distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        if len(word1) > len(word2):
            word1, word2 = word2, word1

        distance = list(range(0, len(word1)+1))
        for idx2, char2 in enumerate(word2):
            _distance = [idx2+1] * (len(word1)+1)
            for idx1, char1 in enumerate(word1):
                if char1 == char2:
                    _distance[idx1+1] = distance[idx1]
                else:
                    _distance[idx1+1] = min(_distance[idx1], distance[idx1+1], distance[idx1]) + 1
            distance = _distance
        return distance[-1]
