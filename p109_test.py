from p109 import Solution
from common.tree import getListFromTree
from common.linked_list import getLinkedList

test_cases = [
    ([-10,-3,0,5,9], [0,-3,9,-10,None,5]),
    ([], []),
    ([0], [0]),
    ([1,3], [3, 1]),
]

def test_sortedListToBST():
    s = Solution()
    for case in test_cases:
        assert getListFromTree(s.sortedListToBST(getLinkedList(case[0]))) == case[1], case
