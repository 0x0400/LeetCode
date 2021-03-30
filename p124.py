# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from common.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self) -> None:
        self.maxSum = None

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = None
        self.getPathSum(root)
        return self.maxSum

    def getPathSum(self, root: TreeNode) -> int:
        leftSum = 0
        if root.left:
            leftSum = self.getPathSum(root.left)

        rightSum = 0
        if root.right:
            rightSum = self.getPathSum(root.right)

        # nodeSum 表示以当前 root 为根的树 的 maxPathSum
        nodeSum = root.val
        if leftSum > 0:
            nodeSum += leftSum
        if rightSum > 0:
            nodeSum += rightSum

        if self.maxSum is None:
            self.maxSum = nodeSum
        else:
            self.maxSum = max(nodeSum, self.maxSum)

        # 上一层节点如果往该root节点遍历的话，能够增加的 pathSum
        return root.val + max(leftSum, rightSum, 0)
