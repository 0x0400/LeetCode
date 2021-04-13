from p1448 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([3,1,4,3,None,1,5], 4),
    ([3,3,None,4,2], 3),
    ([1], 1),
]

def test_goodNodes():
    s = Solution()
    for case in test_cases:
        assert s.goodNodes(buildTreeFromList(case[0])) == case[1], case
