# https://leetcode.com/problems/implement-trie-prefix-tree/

from typing import List, Optional

class Node:
    def __init__(self, char: Optional[str] = None, isWord: bool = False) -> None:
        self.char: str = char
        self.isWord: bool = isWord
        self.children: List['Node']  = []

    def findNode(self, char: str) -> Optional['Node']:
        for node in self.children:
            if node.char == char:
                return node
        return None

    def addChild(self, node: 'Node') -> None:
        self.children.append(node)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self.root
        for idx, char in enumerate(word) :
            node = curNode.findNode(char)
            if not node:
                node = Node(char)
                curNode.addChild(node)
            if idx == len(word)-1:
                node.isWord = True
            curNode = node



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self.root
        for idx, char in enumerate(word) :
            node = curNode.findNode(char)
            if not node:
                return False
            if idx == len(word)-1:
                return node.isWord
            curNode = node
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curNode = self.root
        for char in prefix:
            node = curNode.findNode(char)
            if not node:
                return False
            curNode = node
        return curNode.char != None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
