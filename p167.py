# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1

        while leftIdx < rightIdx:
            if numbers[leftIdx] + numbers[rightIdx] == target:
                return [leftIdx+1, rightIdx+1]
            if numbers[leftIdx] + numbers[rightIdx] < target:
                leftIdx += 1
                continue
            rightIdx -= 1

        return []
