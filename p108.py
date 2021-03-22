# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from common.tree import TreeNode

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        if len(nums) == 2:
            return TreeNode(nums[1], TreeNode(nums[0]))

        rootIdx = len(nums) // 2
        return TreeNode(nums[rootIdx], self.sortedArrayToBST(nums[:rootIdx]), self.sortedArrayToBST(nums[rootIdx+1:]))
