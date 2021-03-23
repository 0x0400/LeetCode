# https://leetcode.com/problems/path-sum-ii/

from common.tree import TreeNode

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        if root.val == targetSum:
            if not root.left and not root.right:
                return [[root.val]]

        paths = []
        if root.left:
            subPaths = self.pathSum(root.left, targetSum-root.val)
            if subPaths:
                for p in subPaths:
                    paths.append([root.val] + p)
        if root.right:
            subPaths = self.pathSum(root.right, targetSum-root.val)
            if subPaths:
                for p in subPaths:
                    paths.append([root.val] + p)
        return paths
