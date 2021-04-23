from p173 import BSTIterator
from common.tree import buildTreeFromList

test_cases = [
    (["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"], [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]), [None, 3, 7, True, 9, True, 15, True, 20, False]
]

def test_BSTIterator():
    rst = []
    obj = None
    for name, args in zip(test_cases[0][0], test_cases[0][1]):
        if name == "BSTIterator":
            obj = BSTIterator(buildTreeFromList(*args))
            rst.append(None)
            continue
        rst.append(getattr(obj, name)())
    assert rst == test_cases[1]
