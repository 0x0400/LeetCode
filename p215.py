# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
