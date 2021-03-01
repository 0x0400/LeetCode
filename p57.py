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

            # 后面的元素和 newInterva 没有重合
            if item[0] > newInterval[1]:
                rst.append(newInterval)
                rst += intervals[idx:]
                return rst

            # 存在重合的情况
            rst.append([min(item[0], newInterval[0]), max(item[1], newInterval[1])])
            isMerged = True
            for curIdx in range(idx+1, len(intervals)):
                if intervals[curIdx][1] <= rst[-1][1]:
                    continue

                if intervals[curIdx][0] <= rst[-1][1]:
                    rst[-1] = [rst[-1][0], intervals[curIdx][1]]
                else:
                    rst.append(intervals[curIdx])
                rst += intervals[curIdx+1:]
                return rst
            return rst

        if not isMerged:
            rst.append(newInterval)
        return rst




