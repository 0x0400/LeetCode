# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        totalLen = 1
        curNode = head
        while curNode.next is not None:
            curNode = curNode.next
            totalLen += 1

        lastNode = curNode
        k = k % totalLen
        if k == 0:
            return head

        idx = totalLen - k - 1
        curNode = head
        while idx > 0:
            curNode = curNode.next
            idx -= 1
        nextNode = curNode.next
        curNode.next = None
        lastNode.next = head
        return nextNode
