# https://leetcode.com/problems/implement-trie-prefix-tree/

from typing import Dict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children: Dict[str, 'Trie'] = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode: Trie = self
        for idx, char in enumerate(word) :
            node = curNode.children.get(char, None)
            if not node:
                node = Trie()
                curNode.children[char] = node
            if idx == len(word)-1:
                node.isWord = True
            curNode = node


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode: Trie = self
        for idx, char in enumerate(word) :
            node = curNode.children.get(char, None)
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
        if not prefix:
            return True
        if not self.children:
            return False

        curNode: Trie = self
        for char in prefix:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        return True

    def __repr__(self) -> str:
        return "Trie<isWord={}, children={}>".format(self.isWord, self.children)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
