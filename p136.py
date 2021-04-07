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


    def singleNumberV2(self, nums: List[int]) -> int:
        ''' 同一数字与自身 异或运算之后是 0
            所以将所有数值进行异或之后，得到的结果就是只出现一次的数值
        '''
        single = nums[0]
        for num in nums[1:]:
            single = single ^ num
        return single
