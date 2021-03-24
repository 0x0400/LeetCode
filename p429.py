# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        rst = []
        if not root:
            return rst

        curNodes = [root]
        while curNodes:
            nextNodes = []
            curVals = []
            for node in curNodes:
                curVals.append(node.val)
                if node.children:
                    nextNodes += node.children
            rst.append(curVals)
            curNodes = nextNodes
        return rst
