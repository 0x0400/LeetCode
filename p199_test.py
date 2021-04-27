from p199 import Solution

from common.tree import buildTreeFromList

test_cases = [
    ([1,2,3,None,5,None,4], [1,3,4]),
    ([1,None,3], [1,3]),
    ([], []),
    ([1,2,3,4], [1,3,4])
]

def test_rightSideView():
    s = Solution()
    for case in test_cases:
        assert s.rightSideView(buildTreeFromList(case[0])) == case[1], case
