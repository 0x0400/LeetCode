# https://leetcode.com/problems/jump-game-ii/

from typing import List, Dict

# 递归次数太多会导致程序异常退出

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self._jump(nums, len(nums)-1, {0:0})

    def _jump(self, nums: List[int], curIdx: int, cache: Dict[int, int]):
        idx = curIdx
        steps = None
        plans = []
        while idx > 0:
            idx -= 1
            if nums[idx] >= curIdx - idx:
                plans.append(idx)

        for idx in reversed(plans):
            if idx not in cache:
                cache[idx] = self._jump(nums, idx, cache)
            preSteps = cache[idx]
            if preSteps is None:
                continue

            if nums[idx] >= curIdx - idx:
                steps = preSteps+1 if steps is None else min(steps, preSteps+1)

        if steps is not None:
            for i in range(curIdx, max(len(nums), nums[curIdx]+1)):
                cache[i] = steps+1 if i not in cache else min(cache[i], steps+1)
        return steps
