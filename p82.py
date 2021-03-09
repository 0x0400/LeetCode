# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        sentinal = ListNode(None, head)
        preNode = sentinal
        curNode = sentinal.next
        duplicatedVal = None
        while curNode and curNode.next != None:
            while curNode.next != None:
                if curNode.next.val == curNode.val:
                    duplicatedVal = curNode.val
                    curNode = curNode.next
                    continue
                break
            if duplicatedVal != None:
                preNode.next = curNode.next
                curNode = preNode.next
                duplicatedVal = None
            else:
                preNode = preNode.next
                curNode = curNode.next
        return sentinal.next
