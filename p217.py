# https://leetcode.com/problems/contains-duplicate/

from typing import Dict, List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache: Dict[int, int] = {}
        for num in nums:
            if num in cache:
                return True
            cache[num] = num
        return False
