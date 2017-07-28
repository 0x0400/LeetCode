# https://leetcode.com/problems/4sum/#/description

from collections import defaultdict


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        nums.sort()
        nums_len = len(nums)
        cache = defaultdict(list)
        for index1 in range(0, nums_len - 1):
            for index2 in range(index1 + 1, nums_len):
                cache[nums[index1] + nums[index2]].append([index1, index2])

        for index1 in range(0, nums_len - 3):
            if index1 > 0 and nums[index1] == nums[index1 - 1]:
                continue
            for index2 in range(index1 + 1, nums_len - 2):
                if index2 > index1 + 1 and nums[index2] == nums[index2 - 1]:
                    continue
                left = target - nums[index1] - nums[index2]
                if left in cache:
                    for (index3, index4) in cache[left]:
                        if index3 > index2:
                            item = [nums[index1], nums[index2], nums[index3],
                                    nums[index4]]
                            if item not in result:
                                result.append(item)

        return result
