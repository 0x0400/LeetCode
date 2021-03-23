# https://leetcode.com/problems/path-sum/

from common.tree import TreeNode

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum:
            if not root.left and not root.right:
                return True
            # 子树的值为 0 也是正确的
            # return False

        if root.left:
            isHas = self.hasPathSum(root.left, targetSum-root.val)
            if isHas:
                return True
        if root.right:
            isHas = self.hasPathSum(root.right, targetSum-root.val)
            return isHas
        return False
