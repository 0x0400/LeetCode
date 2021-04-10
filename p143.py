# https://leetcode.com/problems/reorder-list/

from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        curNode = head
        while curNode:
            nodes.append(curNode)
            curNode = curNode.next

        if len(nodes) <= 2:
            return head

        startIdx, endIdx = 0, len(nodes)-1
        while startIdx < endIdx:
            nodes[startIdx].next = nodes[endIdx]
            nodes[endIdx].next = nodes[startIdx+1]
            startIdx += 1
            endIdx -= 1

        if startIdx == endIdx:
            nodes[startIdx].next = None
        else:
            nodes[endIdx+1].next = None

        return head
