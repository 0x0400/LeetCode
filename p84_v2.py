# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]

        maxArea = 0
        skipIdx = {}
        for i in range(0, len(heights)):
            if i in skipIdx:
                continue
            tmpArea = heights[i]
            for j in range(i+1, len(heights)):
                if heights[j] < heights[i]:
                    break
                if heights[j] == heights[i]:
                    skipIdx[j] = True
                tmpArea += heights[i]
            for j in range(i-1, -1, -1):
                if heights[j] >= heights[i]:
                    tmpArea += heights[i]
                    continue
                break
            maxArea = max(maxArea, tmpArea)

        return maxArea
