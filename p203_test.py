from p203 import Solution

from common.linked_list import getLinkedList, getListFromLinkedList

test_cases = [
    (([1,2,6,3,4,5,6], 6), [1,2,3,4,5]),
    (([], 1) , []),
    (([7,7,7,7], 7), []),
]


def test_removeElements():
    s = Solution()
    for case in test_cases:
        assert getListFromLinkedList(s.removeElements(getLinkedList(case[0][0]), case[0][1]))  == case[1], case
