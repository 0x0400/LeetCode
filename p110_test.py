from p110 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([3,9,20,None,None,15,7], True),
    ([1,2,2,3,3,None,None,4,4], False),
    ([], True),
]

def test_isBalanced():
    s = Solution()
    for case in test_cases:
        assert s.isBalanced(buildTreeFromList(case[0])) == case[1], case
