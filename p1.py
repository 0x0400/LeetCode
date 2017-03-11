# https://leetcode.com/problems/two-sum/?tab=Description

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for idx_1 in range(0, nums_len):
            for idx_2 in range(idx_1 + 1, nums_len):
                if nums[idx_1] + nums[idx_2] == target:
                    return [idx_1, idx_2]
        return []
