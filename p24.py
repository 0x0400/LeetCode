# https://leetcode.com/problems/swap-nodes-in-pairs/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = current = ListNode(0)
        if head is None or head.next is None:
            return head
        current.next = head
        while current.next is not None and current.next.next is not None:
            next_node = current.next.next
            current.next.next = next_node.next
            next_node.next = current.next
            current.next = next_node
            current = next_node.next

        return sentinel.next
