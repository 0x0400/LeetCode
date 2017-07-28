# https://leetcode.com/problems/4sum/#/description


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        nums.sort()
        for index1, num1 in enumerate(nums[:-3]):
            for index2, num2 in enumerate(nums[index1 + 1:-2]):
                for index3, num3 in enumerate(nums[index1 + index2 + 2:-1]):
                    left = target - num1 - num2 - num3
                    if left < num3:
                        break
                    try:
                        _ = nums.index(left, index1 + index2 + index3 + 3)
                        result.append((num1, num2, num3, left))
                    except ValueError:
                        pass
        return list(set(result))
