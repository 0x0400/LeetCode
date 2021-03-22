# https://leetcode.com/problems/recover-binary-search-tree/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "<TreeNode:{}>".format(self.val)

class Solution:
    """
    通过 inorder 遍历树结构生成数组;
    对数据排序；
    对比排序前后的数组可以比对出差异的节点
    """

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = self.inorderTravelTree(root)
        unorder = self.findUnorderNodes(nodes)
        if len(unorder) == 2:
            unorder[0].val, unorder[1].val = unorder[1].val, unorder[0].val
        return root

    def inorderTravelTree(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        inorderNodes = []
        nodes = []
        curNode = root
        while curNode or nodes:
            if curNode:
                nodes.append(curNode)
                curNode = curNode.left
            else:
                curNode = nodes.pop()
                inorderNodes.append(curNode)
                curNode = curNode.right
        return inorderNodes

    def findUnorderNodes(self, nodes: List[TreeNode]) -> List[TreeNode]:
        orig = nodes.copy()
        nodes = sorted(nodes, key=lambda node: node.val)
        unorder = []
        for idx in range(0, len(orig)):
            if orig[idx].val != nodes[idx].val:
                unorder.append(orig[idx])
        return unorder
