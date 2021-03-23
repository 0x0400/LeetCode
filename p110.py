# https://leetcode.com/problems/balanced-binary-tree/

from common.tree import TreeNode
from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        rst = self.getIsBalanceAndDepth(root)
        return rst[0]

    def getIsBalanceAndDepth(self, root: TreeNode) -> Tuple[bool, int]:
        if not root:
            return (True, 0)
        left = self.getIsBalanceAndDepth(root.left)
        right = self.getIsBalanceAndDepth(root.right)
        return (left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1], right[1])+1)
