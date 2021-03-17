# https://leetcode.com/problems/interleaving-string/

# 使用 动态规划 算法解决

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3

        # 因为中间状态可能重复，所以需要使用 set 而不能是 list
        plans = set()
        if s1[0] == s3[0]:
            plans.add((1, 0))
        if s2[0] == s3[0]:
            plans.add((0, 1))
        idx3 = 1
        while idx3 < len(s3) and plans:
            curPlans = set()
            for (idx1, idx2) in plans:
                if idx1 == len(s1):
                    if s2[idx2:] == s3[idx3:]:
                        return True
                else:
                    if s1[idx1] == s3[idx3]:
                        curPlans.add((idx1+1, idx2))
                if idx2 == len(s2):
                    if s1[idx1:] == s3[idx3:]:
                        return True
                else:
                    if s2[idx2] == s3[idx3]:
                        curPlans.add((idx1, idx2+1))
            plans = curPlans
            idx3 += 1
        return (idx3 == len(s3)) and plans
