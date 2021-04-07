# https://leetcode.com/problems/single-number-ii/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
            if cache[num] == 3:
                cache.pop(num)
        return list(cache.keys())[0]
