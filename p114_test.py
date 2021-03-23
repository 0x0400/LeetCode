from p114 import Solution
from common.tree import buildTreeFromList, getListFromTreeV2

test_cases = [
    ([1,2,5,3,4,None,6], [1,None,2,None,3,None,4,None,5,None,6]),
    ([], []),
    ([0], [0]),
]

def test_flatten():
    s = Solution()
    for case in test_cases:
        tree = buildTreeFromList(case[0])
        s.flatten(tree)
        assert getListFromTreeV2(tree) == case[1], case
