from p148 import Solution
from common.linked_list import getLinkedList, getListFromLinkedList

test_cases = [
    ([4,2,1,3], [1,2,3,4]),
    ([-1,5,3,4,0], [-1,0,3,4,5]),
]

def test_sortList():
    for case in test_cases:
        s = Solution()
        assert getListFromLinkedList(s.sortList(getLinkedList(case[0]))) == case[1], case
