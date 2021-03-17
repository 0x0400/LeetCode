# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTInrange(root, None, None)

    def isValidBSTInrange(self, root: TreeNode, minVal: int, maxVal: int) -> bool:
        if not root:
            return True

        if minVal is not None and root.val <= minVal:
            return False
        if maxVal is not None and root.val >= maxVal:
            return False

        if root.left:
            if root.val <= root.left.val:
                return False
            isValid = self.isValidBSTInrange(root.left, minVal, root.val)
            if not isValid:
                return False
        if root.right:
            if root.val >= root.right.val:
                return False
            isValid = self.isValidBSTInrange(root.right, root.val, maxVal)
            if not isValid:
                return False

        return True
