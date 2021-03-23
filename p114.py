# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from common.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if root.right:
            self.flatten(root.right)

        if root.left:
            self.flatten(root.left)
            curNode = root.left
            while curNode.right:
                curNode = curNode.right
            curNode.right = root.right
            root.right = root.left
            root.left = None





