# https://leetcode.com/problems/remove-element/description/


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        array_len = len(nums)
        val_cnt = 0
        idx = 0
        while idx < array_len - val_cnt:
            if nums[idx] == val:
                val_cnt += 1
                nums.pop(idx)
            else:
                idx += 1
        return array_len - val_cnt
