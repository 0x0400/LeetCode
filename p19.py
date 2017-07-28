# https://leetcode.com/problems/remove-nth-node-from-end-of-list/tabs/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = pre_node = head
        for _ in range(0, n):
            tail = tail.next
        if not tail:
            return pre_node.next
        while tail.next:
            tail, pre_node = tail.next, pre_node.next

        pre_node.next = pre_node.next.next
        return head
