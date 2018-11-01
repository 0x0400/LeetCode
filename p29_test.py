from p29 import Solution as Solution

test_cases = [
    (10, 1, 10),
    (0, 1, 0),
    (10, 3, 3),
    (7, -3, -2),
    (1, -1, -1),
    (2, 2, 1),
    (-2147483648, -1, 2147483647)
]


def test_divide():
    s = Solution()
    for case in test_cases:
        assert s.divide(case[0], case[1]) == case[2]
