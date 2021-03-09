# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]

        return self.findLargestRectangleArea(heights, 0, len(heights)-1)


    def findLargestRectangleArea(self, heights: List[int], start: int, end: int) -> int:
        if start < 0 or end >= len(heights) or end < start:
            return 0
        if start == end:
            return heights[start]

        minIndexes = []
        minHeight = heights[start]
        for idx in range(start, end+1):
            if heights[idx] == minHeight:
                minIndexes.append(idx)
                continue
            if heights[idx] < minHeight:
                minHeight = heights[idx]
                minIndexes = [idx]
                continue

        # print(start, end, heights[start:end+1])
        # print(minHeight, minIndexes)
        baseArea = (end - start + 1) * minHeight
        maxArea = baseArea
        for i, idx  in enumerate(minIndexes):
            if i == 0:
                tmpArea = self.findLargestRectangleArea(heights, start, idx-1)
                maxArea = max(maxArea, tmpArea)
            if i == len(minIndexes) - 1:
                tmpArea = self.findLargestRectangleArea(heights, idx+1, end)
                maxArea = max(maxArea, tmpArea)
            else:
                tmpArea = self.findLargestRectangleArea(heights, idx+1, minIndexes[i+1]-1)
                maxArea = max(maxArea, tmpArea)
        return maxArea
