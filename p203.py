# https://leetcode.com/problems/remove-linked-list-elements/


from common.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinal = ListNode(next=head)

        curNode = sentinal
        while curNode.next:
            if curNode.next.val == val:
                curNode.next = curNode.next.next
                continue
            curNode = curNode.next

        return sentinal.next
