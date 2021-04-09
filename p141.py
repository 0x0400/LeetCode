# https://leetcode.com/problems/linked-list-cycle/

from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = {}
        idx = 0
        curNode = head
        while curNode:
            if curNode in visited:
                return True

            visited[curNode] = idx
            idx += 1
            curNode = curNode.next

        return False
