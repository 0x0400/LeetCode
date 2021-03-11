# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # 使用 双链表
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        ltHead = None
        ltLastNode = None
        gteHead = None
        gteLastNode = None

        curNode = head
        while curNode:
            if curNode.val >= x:
                if not gteHead:
                    gteHead = curNode
                if gteLastNode:
                    gteLastNode.next = curNode
                gteLastNode = curNode
                curNode = curNode.next
                continue

            if not ltHead:
                ltHead = curNode
            if ltLastNode:
                ltLastNode.next = curNode
            ltLastNode = curNode
            curNode = curNode.next

        # gteLastNode 和 ltLastNode 的 next 需要正确设置，否则会出现死循环
        if gteLastNode:
            gteLastNode.next = None
        if ltHead:
            ltLastNode.next = gteHead
            return ltHead
        return gteHead


    def partitionV2(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        ltArray = []
        gteArray = []
        curNode = head
        while curNode:
            if curNode.val >= x:
                gteArray.append(curNode)
            else:
                ltArray.append(curNode)
            curNode = curNode.next

        nodes = ltArray + gteArray
        for idx, node in enumerate(nodes):
            if idx == len(nodes) - 1:
                node.next = None
            else:
                node.next = nodes[idx+1]
        return nodes[0]
