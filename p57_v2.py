# https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rst = []
        if not intervals:
            rst.append(newInterval)
            return rst


        isMerged = False
        for idx, item in enumerate(intervals):
            if item[1] < newInterval[0]:
                rst.append(item)
                continue

            # 后面的元素和 newInterval 没有重合
            if item[0] > newInterval[1]:
                rst.append(newInterval)
                rst += intervals[idx:]
                return rst

            # 存在重合的情况
            newInterval = [min(item[0], newInterval[0]), max(item[1], newInterval[1])]
            isMerged = False

        if not isMerged:
            rst.append(newInterval)
        return rst




