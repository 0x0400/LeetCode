# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        return self.mySqrtInRange(x, 0, x)

    def mySqrtInRange(self, x: int, start: int, end : int) -> int:
        curVal =  (start + end) // 2

        curSquare = curVal * curVal
        if curSquare == x:
            return curVal
        if curSquare > x:
            return self.mySqrtInRange(x, start, curVal)
        nextValSquare =  curSquare + 2 * curVal + 1
        if nextValSquare > x:
            return curVal
        if nextValSquare == x:
            return curVal + 1
        return self.mySqrtInRange(x, curVal+1, end)
