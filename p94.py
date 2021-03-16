# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        rst = []
        curNode = root
        while stack or curNode:
            if curNode:
                while curNode:
                    stack.append(curNode)
                    curNode = curNode.left
            else:
                curNode = stack.pop()
                rst.append(curNode.val)
                curNode = curNode.right
        return rst
