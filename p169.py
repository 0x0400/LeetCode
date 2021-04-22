# https://leetcode.com/problems/majority-element/

from collections import Counter

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common(1)[0][0]

    def majorityElementV2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)>>1]
