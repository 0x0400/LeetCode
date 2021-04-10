from p144 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([1,None,2,3], [1,2,3]),
    ([], []),
    ([1], [1]),
    ([1,2], [1,2]),
    ([1,None,2], [1,2]),
]

def test_preorderTraversal():
    for case in test_cases:
        s = Solution()
        assert s.preorderTraversal(buildTreeFromList(case[0])) == case[1], case
