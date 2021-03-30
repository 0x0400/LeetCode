from p124 import Solution
from common.tree import buildTreeFromList
from common.linked_list import getLinkedList

test_cases = [
    ([1,2,3], 6),
    ([-10,9,20,None,None,15,7], 42),
]

def test_maxPathSum():
    s = Solution()
    for case in test_cases:
        assert s.maxPathSum(buildTreeFromList(case[0])) == case[1], case
