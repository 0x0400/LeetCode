# https://leetcode.com/problems/add-two-numbers/?tab=Description

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNode = prevNode = ListNode(0)
        prevCarry = 0
        while (l1 is not None) or (l2 is not None):
            currentValue = prevCarry
            if l1 is not None:
                currentValue += l1.val
                l1 = l1.next
            if l2 is not None:
                currentValue += l2.val
                l2 = l2.next

            prevCarry, currentValue = divmod(currentValue, 10)
            prevNode.next = ListNode(currentValue)
            prevNode = prevNode.next

        if prevCarry == 1:
            prevNode.next = ListNode(prevCarry)

        return firstNode.next
