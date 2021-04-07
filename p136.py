# https://leetcode.com/problems/single-number/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = num
            else:
                cache.pop(num)
        return list(cache.keys())[0]
