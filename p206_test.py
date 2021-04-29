from p206 import Solution

from common.linked_list import getLinkedList, getListFromLinkedList

test_cases = [
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2], [2,1]),
    ([], []),
]


def test_reverseList():
    s = Solution()
    for case in test_cases:
        assert getListFromLinkedList(s.reverseList(getLinkedList(case[0]))) == case[1], case
