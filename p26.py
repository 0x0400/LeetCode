# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_len = len(nums)
        dup_cnt = 0
        idx = 0
        while idx < array_len - dup_cnt - 1:
            if nums[idx] == nums[idx+1]:
                dup_cnt += 1
                nums.pop(idx+1)
            else:
                idx += 1
        return array_len - dup_cnt
