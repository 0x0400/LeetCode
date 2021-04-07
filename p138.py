# https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        cache = {}
        dstHead = Node(head.val, None, head.random)
        cache = {head: dstHead}
        srcNode = head
        dstNode = dstHead
        while srcNode.next:
            newNode = Node(srcNode.next.val, None, srcNode.next.random)
            dstNode.next = newNode
            cache[srcNode.next] = newNode
            srcNode = srcNode.next
            dstNode = newNode

        curNode = dstHead
        while curNode:
            if curNode.random:
                curNode.random = cache.get(curNode.random, None)
            curNode = curNode.next
        return dstHead
