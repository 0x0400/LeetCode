# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricTrees(root.left, root.right)

    def isSymmetricTrees(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True

        if not root1 and root2:
            return False

        if root1 and not root2:
            return False

        if root1.val != root2.val:
            return False

        isSymmetric = self.isSymmetricTrees(root1.left, root2.right)
        if not isSymmetric:
            return False

        return self.isSymmetricTrees(root1.right, root2.left)
