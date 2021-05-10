from p211 import WordDictionary

def test_WordDictionary():
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    assert wordDictionary.search("pad") == False
    assert wordDictionary.search("bad") == True
    assert wordDictionary.search(".ad") == True
    assert wordDictionary.search("b..") == True
