# https://leetcode.com/problems/binary-tree-postorder-traversal/

from common.tree import TreeNode
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        rst = []
        if not root:
            return rst

        stack: List[TreeNode] = []
        curNode = root
        lastVisitedNode = None
        while curNode or stack:
            if curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                peekNode = stack[-1]
                if peekNode.right and peekNode.right != lastVisitedNode:
                    curNode = peekNode.right
                else:
                    lastVisitedNode = stack.pop()
                    rst.append(lastVisitedNode.val)
        return rst
