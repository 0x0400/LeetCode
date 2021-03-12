from p89 import Solution

test_cases = [
    (2, [0,1,3,2]),
    (1, [0,1]),
    (3, [0, 1, 3, 2, 6, 7, 5, 4])
]


def test_grayCode():
    s = Solution()
    for case in test_cases:
        assert s.grayCode(case[0]) == case[1], case
