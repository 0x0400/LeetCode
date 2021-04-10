from p143 import Solution
from common.linked_list import getLinkedList, getListFromLinkedList

test_cases = [
    ([1,2,3,4], [1,4,2,3]),
    ([1,2,3,4,5], [1,5,2,4,3]),
]

def test_reorderList():
    for case in test_cases:
        s = Solution()
        assert getListFromLinkedList(s.reorderList(getLinkedList(case[0]))) == case[1], case
