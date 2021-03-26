# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 与 p116 一样的解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        curLevelNodes = [root]
        while curLevelNodes:
            nextLevelNodes = []
            for idx, n in enumerate(curLevelNodes):
                if idx < len(curLevelNodes)-1:
                    n.next = curLevelNodes[idx+1]
                if n.left:
                    nextLevelNodes.append(n.left)
                if n.right:
                    nextLevelNodes.append(n.right)
            curLevelNodes = nextLevelNodes
        return root
