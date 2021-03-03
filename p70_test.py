from p70 import Solution

test_cases = [
    (1, 1),
    (2, 2),
    (3, 3),
]


def test_climbStairs():
    s = Solution()
    for case in test_cases:
        assert s.climbStairs(case[0]) == case[1], case
