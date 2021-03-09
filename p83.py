# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        curNode = head
        while curNode and curNode.next is not None:
            if curNode.next.val == curNode.val:
                curNode.next = curNode.next.next
                continue
            curNode = curNode.next
        return head
