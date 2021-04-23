# https://leetcode.com/problems/binary-search-tree-iterator/

from common.tree import TreeNode
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack: List[TreeNode] = []
        self._push(root)

    def _push(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            if node.right:
                self._push(node.right)
            return node.val
        return None

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
