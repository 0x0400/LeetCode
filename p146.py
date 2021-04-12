# https://leetcode.com/problems/lru-cache/
from typing import Dict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []


    def get(self, key: int) -> int:
        if not self.data:
            return -1

        i = 0
        while i < len(self.data):
            if self.data[i][0] == key:
                break
            i += 1
        if i == len(self.data):
            return -1

        item = self.data.pop(i)
        self.data.insert(0, item)
        return self.data[0][1]


    def put(self, key: int, value: int) -> None:
        idx = self.get(key)
        if idx == -1:
            self.data.insert(0, [key, value])
            if len(self.data) > self.capacity:
                self.data.pop()
        else:
            self.data[0][1] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node:
    def __init__(self, key: int, val: int, prev: 'Node' = None, next: 'Node' = None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCacheV2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys : Dict[int, Node] = {}
        self.head: Node = None
        self.last: Node = None

    def _add(self, node: Node):
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

        if self.last is None:
            self.last = node
            self.last.next = None

    def _remove(self, node: Node):
        if self.head == node:
            self.head = node.next
            node.next = None
            return

        if self.last == node:
            self.last = node.prev
            if self.last:
                self.last.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys.get(key)
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return

        node = Node(key, value)
        self.keys[key] = node
        self._add(node)

        if len(self.keys) > self.capacity:
            del self.keys[self.last.key]
            self._remove(self.last)
