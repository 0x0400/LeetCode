# https://leetcode.com/problems/reverse-nodes-in-k-group/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        sentinel = current = ListNode(0)
        current.next = head
        next_node = head
        idx = 0
        while idx < k and next_node is not None:
            current, next_node, next_node.next = next_node, next_node.next, current
            idx += 1
        

        current.next = self.reverseKGroup(current.next, k)
        while True:
            head, tail, swapped = self.swapNodes(current.next, k)
            if not swapped:
                break
            current.next = head
            current = tail
        return sentinel.next

    def reverse(self, head, tail):
        pre_node, current = head, head.next
        while current != tail:
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node
        head.next = None
