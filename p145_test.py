from p145 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([1,None,2,3], [3,2,1]),
    ([], []),
    ([1], [1]),
    ([1,2], [2,1]),
    ([1,None,2], [2,1]),
]

def test_postorderTraversal():
    for case in test_cases:
        s = Solution()
        assert s.postorderTraversal(buildTreeFromList(case[0])) == case[1], case
