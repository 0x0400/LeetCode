# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        curLevelNodes = [root]
        levels = 0
        while curLevelNodes:
            levels += 1
            nextLevelNodes = []
            for node in curLevelNodes:
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)
            curLevelNodes = nextLevelNodes
        return levels
