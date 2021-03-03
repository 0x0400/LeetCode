from p69 import Solution

test_cases = [
    (4, 2),
    (8, 2),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 1),

]


def test_mySqrt():
    s = Solution()
    for case in test_cases:
        assert s.mySqrt(case[0]) == case[1], case
