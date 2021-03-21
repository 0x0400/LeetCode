# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        rst = []
        if not root:
            return rst

        curLevelNodes = [root]
        while curLevelNodes:
            nextLevelNodes = []
            curVals = []
            for node in curLevelNodes:
                curVals.append(node.val)
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)
            rst.insert(0, curVals)
            curLevelNodes = nextLevelNodes
        return rst
