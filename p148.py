# https://leetcode.com/problems/sort-list/

from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        middleNode = self.findMiddleNode(head)
        left = head
        right = middleNode.next
        if not right:
            return head
        middleNode.next = None
        return self.mergeList(self.sortList(left), self.sortList(right))

    def mergeList(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not head1:
            return head2
        if not head2:
            return head1

        # if head1.val < head2.val:
        #     head1.next = self.mergeList(head1.next, head2)
        #     return head1

        # head2.next = self.mergeList(head1, head2.next)
        # return head2
        sentinal = ListNode()
        lastNode = sentinal
        while head1 and head2:
            if head1.val < head2.val:
                lastNode.next = head1
                lastNode = head1
                head1 = head1.next
            else:
                lastNode.next = head2
                lastNode = head2
                head2 = head2.next
        lastNode.next = head1 if head1 else head2
        return sentinal.next

    def findMiddleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slowP = head
        fastP = head
        while fastP.next and fastP.next.next:
            slowP = slowP.next
            fastP = fastP.next.next
        return slowP
