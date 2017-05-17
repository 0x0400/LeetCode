# -*- coding: utf-8 -*-

from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = []

        nums_cnt = Counter(nums)
        uniq_nums = nums_cnt.keys()
        uniq_nums.sort()

        if nums_cnt[0] >= 3:
            rst.append([0, 0, 0])
            nums_cnt[0] = 1

        for first_idx, first_num in enumerate(uniq_nums):
            if first_num >= 0:
                break
            # 前两个值相同
            if nums_cnt[first_num] >= 2:
                third_num = 0 - first_num - first_num
                if third_num > first_num and third_num in nums_cnt:
                    rst.append([first_num, first_num, third_num])
            # 第一个值与后面不同
            for second_num in uniq_nums[first_idx+1:]:
                third_num = 0 - first_num - second_num
                if third_num < second_num:
                    break
                if third_num == second_num:
                    if nums_cnt[second_num] >= 2:
                        rst.append([first_num, second_num, third_num])
                    break
                if third_num in nums_cnt:
                    rst.append([first_num, second_num, third_num])
        return rst
