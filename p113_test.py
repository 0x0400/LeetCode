from p113 import Solution
from common.tree import buildTreeFromList

test_cases = [
    (([5,4,8,11,None,13,4,7,2,None,None,5,1], 22), [[5,4,11,2],[5,8,4,5]]),
    (([1,2,3], 5), []),
    (([1,2], 0), []),
    (([], 0), []),
    (([1,-2,-3,1,3,-2,None,-1], -1), [[1, -2, 1, -1]]),
]

def test_pathSum():
    s = Solution()
    for case in test_cases:
        assert s.pathSum(buildTreeFromList(case[0][0]), case[0][1]) == case[1], case
