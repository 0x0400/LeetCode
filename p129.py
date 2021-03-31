# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import List
from common.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return sum(int(num) for num in self.getTreeNumbers(root))

    def getTreeNumbers(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        rst = []
        if root.left:
            rst += [str(root.val) + num for num in self.getTreeNumbers(root.left)]
        if root.right:
            rst += [str(root.val) + num for num in self.getTreeNumbers(root.right)]
        return rst
