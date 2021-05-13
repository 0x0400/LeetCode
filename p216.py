# https://leetcode.com/problems/combination-sum-iii/

from typing import List, NamedTuple

class Plan(NamedTuple):
    nums: List[int]

    @property
    def sum(self) -> int:
        return sum(self.nums)

    def __len__(self) -> int:
        return len(self.nums)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n == 0:
            return []

        rst = []
        allPlans = [Plan([])]
        for i in range(1, 10):
            plans = []
            for p in allPlans:
                np = Plan(p.nums + [i])
                if len(np) > k:
                    continue
                if np.sum > n:
                    continue
                if np.sum == n:
                    if len(np) == k:
                        rst.append(np.nums)
                    continue
                plans.append(np)
            allPlans += plans
        return rst
