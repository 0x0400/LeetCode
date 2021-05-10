# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from typing import Dict, List

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children: Dict[str, 'WordDictionary'] = {}


    def addWord(self, word: str) -> None:
        curNode: WordDictionary = self
        for idx, char in enumerate(word) :
            node = curNode.children.get(char, None)
            if not node:
                node = WordDictionary()
                curNode.children[char] = node
            if idx == len(word)-1:
                node.isWord = True
            curNode = node


    def search(self, word: str) -> bool:
        curNodes: List[WordDictionary] = [self]
        for char in word:
            nodes: List[WordDictionary]= []
            for curNode in curNodes:
                if char == ".":
                    nodes += curNode.children.values()
                    continue

                node = curNode.children.get(char, None)
                if not node:
                    continue
                nodes.append(node)
            if not nodes:
                return False
            curNodes = nodes

        for node in curNodes:
            if node.isWord:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
