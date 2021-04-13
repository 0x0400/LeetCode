# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from common.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        if not root:
            return cnt

        nodes = [(root, root.val)]
        while nodes:
            nextNodes = []
            for (node, maxVal) in nodes:
                if node.val >= maxVal:
                    cnt += 1
                if node.left:
                    nextNodes.append((node.left, max(node.val, maxVal)))
                if node.right:
                    nextNodes.append((node.right, max(node.val, maxVal)))
            nodes = nextNodes
        return cnt
