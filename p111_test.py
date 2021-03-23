from p111 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([3,9,20,None,None,15,7], 2),
    ([2,None,3,None,4,None,5,None,6], 5),
    ([], 0),
]

def test_minDepth():
    s = Solution()
    for case in test_cases:
        assert s.minDepth(buildTreeFromList(case[0])) == case[1], case
