# https://leetcode.com/problems/merge-k-sorted-lists/description/

from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sentinel = current = ListNode(0)

        queue = PriorityQueue()
        for node in lists:
            if node:
                queue.put((node.val, node))

        while not queue.empty():
            _, node = queue.get()
            current.next = node
            current = node
            if node.next:
                queue.put((node.next.val, node.next))

        return sentinel.next
