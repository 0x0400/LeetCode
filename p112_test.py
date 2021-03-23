from p112 import Solution
from common.tree import buildTreeFromList

test_cases = [
    (([5,4,8,11,None,13,4,7,2,None,None,None,1], 22), True),
    (([1,2,3], 5), False),
    (([1,2], 0), False),
    (([], 0), False),
    (([1,-2,-3,1,3,-2,None,-1], -1), True),
]

def test_hasPathSum():
    s = Solution()
    for case in test_cases:
        assert s.hasPathSum(buildTreeFromList(case[0][0]), case[0][1]) == case[1], case
