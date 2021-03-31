# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        需要考虑 num 会重复出现情况
        """
        cache = {}

        for num in nums:
            # cache[num] = cache.pop(num+1, cache.pop(num, num))
            cache[num] = num

        maxCnt = 0
        for startNum in list(cache.keys()):
            if startNum not in cache:
                continue

            nextNum = cache[startNum]
            while nextNum in cache or nextNum+1 in cache:
                if nextNum in cache:
                    nextNum = cache.pop(nextNum)
                else:
                    nextNum = cache.pop(nextNum+1)

            cache[startNum] = nextNum
            maxCnt = max(maxCnt, nextNum-startNum+1)

        return maxCnt
