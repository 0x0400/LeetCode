# https://leetcode.com/problems/unique-binary-search-trees-ii/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTreeFormList(list(range(1, n+1)))

    def generateTreeFormList(self, vals: List[int]) -> List[TreeNode]:

        if not vals:
            return []

        if len(vals) == 1:
            return [TreeNode(vals[0])]

        rst = []
        for idx, val in enumerate(vals):
            leftPlans = self.generateTreeFormList(vals[:idx])
            rightPlans = self.generateTreeFormList(vals[idx+1:])

            if idx == 0:
                for plan in rightPlans:
                    rst.append(TreeNode(val, right=plan))
                continue

            if idx == len(vals) - 1:
                for plan in leftPlans:
                    rst.append(TreeNode(val, left=plan))
                continue

            for left in leftPlans:
                for right in rightPlans:
                    rst.append(TreeNode(val, left=left, right=right))
        return rst
