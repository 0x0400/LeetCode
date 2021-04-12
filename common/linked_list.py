

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getLinkedList(nums):
    lastNode = None
    for val in reversed(nums):
        node = ListNode(val, lastNode)
        lastNode = node
    return lastNode

def getListFromLinkedList(head: 'ListNode'):
    rst = []
    curNode = head
    while curNode:
        rst.append(curNode.val)
        curNode = curNode.next
    return rst
