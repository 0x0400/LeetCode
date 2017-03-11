# https://leetcode.com/problems/median-of-two-sorted-arrays/?tab=Description

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if not nums1 and not nums2:
            return 0

        median_idx, remain = divmod(len(nums1) + len(nums2) + 1, 2)
        two = remain
        median = 0
        tmp = []
        total = 0

        while True:
            if not nums1:
                tmp.append(nums2.pop(0))
            elif not nums2:
                tmp.append(nums1.pop(0))
            else:
                if nums1[0] < nums2[0]:
                    tmp.append(nums1.pop(0))
                else:
                    tmp.append(nums2.pop(0))
            total += 1
            if total == median_idx:
                median += tmp[-1]
                if remain == 1:
                    median_idx += 1
                    remain = 0
                else:
                    break

        if two:
            return median / 2.0
        return median
