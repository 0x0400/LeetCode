# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMaxProduct = nums[0]

        plans = []
        for idx, num in enumerate(nums):
            curMaxProduct = max(curMaxProduct, num)
            if not plans and num != 0:
                plans.append(num)
                continue

            if num == 0:
                for p in plans:
                    curMaxProduct = max(curMaxProduct, p)
                plans = []
                continue

            if num < 0:
                for p in plans:
                    curMaxProduct = max(curMaxProduct, p)

            for pIdx, p in enumerate(plans):
                plans[pIdx] = p * num
            if idx > 0 and nums[idx-1] < 0:
                plans.append(num)
        for p in plans:
            curMaxProduct = max(curMaxProduct, p)
        return curMaxProduct
