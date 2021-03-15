# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        beforeNode = None
        firstNode = None

        curIdx = 1
        curNode = head
        while curIdx < left:
            if curIdx == left - 1:
                beforeNode = curNode
            curNode = curNode.next
            curIdx += 1

        firstNode = curNode
        prevNode = curNode
        curNode = curNode.next
        curIdx += 1
        lastNode = None

        while curIdx <= right:
            if curIdx == right:
                lastNode = curNode
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            curIdx += 1

        firstNode.next = nextNode
        if beforeNode:
            beforeNode.next = lastNode
            return head

        return lastNode
