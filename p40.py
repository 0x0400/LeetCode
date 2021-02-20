# https://leetcode.com/problems/combination-sum-ii/

from typing import Dict, List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rst = self.findCombinationSum2(candidates, target, 0, [])
        return rst


    def findCombinationSum2(self, candidates: List[int], target: int, startIndex: int, curPlan:  List[int]) -> List[List[int]]:
        rst : List[List[int]] = []

        for idx, curVal in enumerate(candidates):
            if idx < startIndex:
                continue

            # 如果前一个值和当前值一致，可能的组合已经由之前的值算好了
            if idx > startIndex and candidates[idx - 1] == curVal:
                continue

            if target < curVal:
                return rst

            if target == curVal:
                rst.append(curPlan.copy() + [curVal])
                return rst

            if target > curVal:
                tmpPlan = curPlan.copy() + [curVal]
                plans = self.findCombinationSum2(candidates, target - curVal, idx+1, tmpPlan)
                rst += plans
        return rst

if __name__ == "__main__":
    sol = Solution()
    # print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
    # print(sol.combinationSum2([2,5,2,1,2], 5))
    print(sol.combinationSum2([2,3,5], 7))

