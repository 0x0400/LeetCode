# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from common.tree import TreeNode

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)

        curNode = root
        while True:
            if  minVal <= curNode.val <= maxVal:
                return curNode

            if curNode.val > maxVal:
                curNode = curNode.left
                continue

            if curNode.val < minVal:
                curNode = curNode.right
