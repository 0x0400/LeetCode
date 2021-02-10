# https://leetcode.com/problems/combination-sum/

from typing import Dict, List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache : Dict[int, List[List[int]]] = {}
        candidates.sort()
        rst = self.combinationWithCache(candidates, target, cache)
        # print(cache)
        return rst


    def combinationWithCache(self, candidates: List[int], target: int, cache:Dict[int, List[List[int]]]) -> List[List[int]]:
        rst = []
        for curVal in candidates:
            remainder = target - curVal
            if remainder < 0:
                break
            if remainder == 0:
                rst.append([curVal])
                break

            plans : List[List[int]] = []
            if remainder not in cache:
                plans = self.combinationWithCache(candidates, remainder, cache)
            else:
                plans = cache.get(remainder, [])

            if curVal <= remainder:
                for plan in plans:
                    # remainder = curVal 的情况，不重复添加
                    if plan[0] >= curVal:
                        tmp = plan.copy() + [curVal]
                        tmp.sort()
                        rst.append(tmp)
        cache[target] = rst
        return rst

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    print(sol.combinationSum([2,3,5], 8))
    print(sol.combinationSum([2], 1))
    print(sol.combinationSum([1], 1))
    print(sol.combinationSum([1], 2))
    print(sol.combinationSum([1, 2], 4))
