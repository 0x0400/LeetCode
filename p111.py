# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from common.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        curNodes = [root]
        curDepth = 1
        while curNodes:
            nextNodes = []
            for node in curNodes:
                if not node.left and not node.right:
                    return curDepth

                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            curNodes = nextNodes
            curDepth += 1
        return curDepth
