from p64 import Solution

test_cases = [
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6]], 12),
]


def test_minPathSum():
    s = Solution()
    for case in test_cases:
        assert s.minPathSumV2(case[0]) == case[1], case
