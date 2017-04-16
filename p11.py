# https://leetcode.com/problems/container-with-most-water/#/description

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        min_h = min(height[0], height[-1])
        lidx, ridx = 0, len(height) - 1
        direct = 1 if height[0] < height[-1] else -1
        max_size = min_h * (ridx - lidx)
        while lidx < ridx:
            if direct == 1:
                while height[lidx] <= min_h and lidx < ridx:
                    lidx += 1
            else:
                while height[ridx] <= min_h and lidx < ridx:
                    ridx -= 1
            max_size = max(max_size,
                            min(height[lidx], height[ridx]) * (ridx - lidx))
            direct = 1 if height[lidx] < height[ridx] else -1
            min_h = min(height[lidx], height[ridx])

        return max_size
