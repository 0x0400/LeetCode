# https://leetcode.com/problems/reverse-linked-list/

from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prevNode, curNode = None, head
        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        return prevNode
