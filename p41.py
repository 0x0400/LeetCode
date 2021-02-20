# https://leetcode.com/problems/first-missing-positive/

from typing import Dict, List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cache = {num : True for num in nums}
        curNum = 1
        while True:
            if curNum not in cache:
                return curNum
            curNum += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1,2,0]))
    print(sol.firstMissingPositive([3,4,-1,1]))
    print(sol.firstMissingPositive([7,8,9,11,12]))
