# https://leetcode.com/problems/lru-cache/
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
