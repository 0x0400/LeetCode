from p85 import Solution

test_cases = [
    ([], 0),
    ([["0"]], 0),
    ([["1"]], 1),
    ([["0","0"]], 0),
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 6),
    ([["0","1"],["0","1"]], 2),
    ([["1","0"],["1","0"]], 2),
]


def test_maximalRectangle():
    s = Solution()
    for case in test_cases:
        assert s.maximalRectangle(case[0]) == case[1], case
