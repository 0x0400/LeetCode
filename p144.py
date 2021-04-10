# https://leetcode.com/problems/binary-tree-preorder-traversal/

from common.tree import TreeNode
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        rst = []
        if not root:
            return rst

        stack = [root]
        while stack:
            curNode = stack.pop()
            rst.append(curNode.val)
            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)
        return rst
