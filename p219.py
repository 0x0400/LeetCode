# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}
        for idx, num in enumerate(nums):
            if num not in cache:
                cache[num] = idx
                continue
            if idx - cache[num] <= k:
                return True
            cache[num] = idx
        return False
