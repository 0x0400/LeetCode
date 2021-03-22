from p108 import Solution
from common.tree import getListFromTree

test_cases = [
    ([-10,-3,0,5,9], [0,-3,9,-10,None,5]),
    ([1,3], [3, 1]),
]

def test_recoverTree():
    s = Solution()
    for case in test_cases:
        assert getListFromTree(s.sortedArrayToBST(case[0])) == case[1], case
