# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import List
from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        nodesA = self.getNodeList(headA)
        nodesB = self.getNodeList(headB)

        interactionNode = None
        maxLen = min(len(nodesA), len(nodesB))
        for i in range(-1, -maxLen-1, -1):
            if nodesA[i] != nodesB[i]:
                break
            interactionNode = nodesA[i]
        return interactionNode

    def getNodeList(self, head: ListNode) -> List[ListNode]:
        rst = []
        while head:
            rst.append(head)
            head = head.next
        return rst


    def getIntersectionNodeV2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        lenA = self.getNodeLen(headA)
        lenB = self.getNodeLen(headB)

        if lenA > lenB:
            headA = self.skipNNode(headA, lenA - lenB)
        elif lenB > lenA:
            headB = self.skipNNode(headB, lenB - lenA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getNodeLen(self, head: ListNode) -> int:
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def skipNNode(self, head: ListNode, n: int) -> ListNode:

        while n > 0:
            n -= 1
            head = head.next
        return head
