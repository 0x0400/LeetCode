from p99 import Solution
from common.tree import buildTreeFromList, getListFromTree

test_cases = [
    ([1,3,None,None,2], [3,1,None,None,2]),
    ([3,1,4,None,None,2], [2,1,4,None,None,3]),
]

def test_recoverTree():
    s = Solution()
    for case in test_cases:
        assert getListFromTree(s.recoverTree(buildTreeFromList(case[0]))) == case[1], case
