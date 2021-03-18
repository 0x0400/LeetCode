# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        rst = []
        if not root:
            return rst

        curLevelNodes = [root]
        isReversed = False
        while curLevelNodes:
            nextLevelNodes = []
            curVals = []
            for node in curLevelNodes:
                curVals.append(node.val)
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)
            if isReversed:
                curVals.reverse()
            rst.append(curVals)
            curLevelNodes = nextLevelNodes
            isReversed = not isReversed
        return rst
