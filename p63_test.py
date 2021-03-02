
from p63 import Solution

test_cases = [
    ([[0,0,0],[0,1,0],[0,0,0]], 2),
    ([[0,1],[0,0]], 1),
    ([[0,0],[0,1]], 0),
]


def test_uniquePathsWithObstacles():
    s = Solution()
    for case in test_cases:
        assert s.uniquePathsWithObstacles(case[0]) == case[1], case
