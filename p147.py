# https://leetcode.com/problems/insertion-sort-list/

from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        curNode = head.next
        head.next = None
        sentinal = ListNode(0, head)
        while curNode:
            nextNode = curNode.next
            insertNode = sentinal
            while insertNode.next and insertNode.next.val <= curNode.val:
                insertNode = insertNode.next
            if insertNode.next == None:
                insertNode.next = curNode
                curNode.next = None
            else:
                curNode.next = insertNode.next
                insertNode.next = curNode
            curNode = nextNode
        return sentinal.next
