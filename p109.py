# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        cnt = 0
        curNode = head
        while curNode:
            cnt += 1
            curNode = curNode.next
        return self.sortedListToBSTWithLen(head, cnt)

    def sortedListToBSTWithLen(self, head: ListNode, listLen: int) -> TreeNode:
        if listLen == 0:
            return None

        if listLen == 1:
            return TreeNode(head.val)

        if listLen == 2:
            return TreeNode(head.next.val, TreeNode(head.val))

        rootIdx = listLen // 2
        curIdx = 0
        curNode = head
        while curIdx < rootIdx:
            curNode = curNode.next
            curIdx += 1
        root = TreeNode(curNode.val)
        root.left = self.sortedListToBSTWithLen(head, rootIdx)
        root.right = self.sortedListToBSTWithLen(curNode.next, listLen - rootIdx - 1)
        return root
