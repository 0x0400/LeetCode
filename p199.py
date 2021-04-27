# https://leetcode.com/problems/binary-tree-right-side-view/

from common.tree import TreeNode

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rst: List[int] = []
        if not root:
            return rst

        nodes: List[TreeNode] = [root]
        while nodes:
            rst.append(nodes[-1].val)

            tmp: List[TreeNode] = []
            for n in nodes:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            nodes = tmp
        return rst
