from p234 import Solution
from common.tree import buildTreeFromList, TreeNode

test_cases = [
    (([6,2,8,0,4,7,9,None,None,3,5], 2, 4), 2),
    (([2,1], 2, 1), 2)
]

def test_lowestCommonAncestor():
    s = Solution()
    for case in test_cases:
        assert s.lowestCommonAncestor(buildTreeFromList(case[0][0]), TreeNode(case[0][1]), TreeNode(case[0][2])).val == case[1], case
