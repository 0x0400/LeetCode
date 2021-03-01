# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        rst = [intervals[0]]
        for item in intervals:
            if item[0] <= rst[-1][1]:
                rst[-1][0] = min(item[0], rst[-1][0])
                rst[-1][1] = max(item[1], rst[-1][1])
            else:
                rst.append(item.copy())
        return rst
