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

    def majorityElementV3(self, nums: List[int]) -> int:
        major, cnt = nums[0], 0
        for num in nums:
            if cnt == 0:
                major, cnt = num, 1
                continue
            if num == major:
                cnt += 1
            else:
                cnt -= 1
        return major
