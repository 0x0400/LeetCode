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
        while True:
            head, tail, swapped = self.swapNodes(current.next, k)
            if not swapped:
                break
            current.next = head
            current = tail
        return sentinel.next

    def swapNodes(self, head, k):
        swapped = False
        current, idx = head, 1
        while idx < k and current:
            current = current.next
            idx += 1
        if idx < k or current is None:
            return (head, None, swapped)

        next_head = current.next
        swapped = True
        pre_node, current, idx = ListNode(0), head, 1
        while idx <= k:
            next_node = current.next
            current.next = pre_node
            pre_node, current = current, next_node
            idx += 1

        head.next = next_head
        return (pre_node, head, swapped)
