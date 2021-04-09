# https://leetcode.com/problems/linked-list-cycle-ii/

from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = {}
        idx = 0
        curNode = head
        while curNode:
            if curNode in visited:
                return curNode

            visited[curNode] = idx
            idx += 1
            curNode = curNode.next

        return None
