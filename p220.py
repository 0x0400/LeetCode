# https://leetcode.com/problems/contains-duplicate-iii/

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ''' Time Limit Exceeded
        '''
        if not nums:
            return False
        numsLen = len(nums)
        for i in range(numsLen):
            for j in range(i+1, min(numsLen, i+k+1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicateV2(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        cache = {}
        for idx, num in enumerate(nums):
            quotient = num // t if t else num
            for quotientIdx in [quotient, quotient+1, quotient-1]:
                if quotientIdx in cache:
                    prevIdx, prevNum = cache[quotientIdx]
                    if abs(prevNum - num) <= t and abs(idx - prevIdx) <= k:
                        return True
            cache[quotient] = (idx, num)
        return False
