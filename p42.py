# https://leetcode.com/problems/trapping-rain-water/

from typing import Dict, List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        leftIdx = 0
        passedHeights = []
        totalHeight = 0
        # 处理最高点左侧的面积计算
        for idx, h in enumerate(height):
            if idx == leftIdx:
                continue
            if h >= height[leftIdx]:
                totalHeight += len(passedHeights) * height[leftIdx] - sum(passedHeights)
                leftIdx = idx
                passedHeights = []
                continue
            passedHeights.append(h)

        # 逆向排序之后，递归调用计算
        if passedHeights:
            passedHeights.reverse()
            passedHeights.append(height[leftIdx])
            totalHeight += self.trap(passedHeights)
        return totalHeight

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([4,2,0,3,2,5]))
    # print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
