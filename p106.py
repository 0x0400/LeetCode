# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0], None, None)

        root = TreeNode(postorder[-1])
        leftLen = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:leftLen], postorder[:leftLen])
        root.right = self.buildTree(inorder[leftLen+1:], postorder[leftLen:-1])

        return root
