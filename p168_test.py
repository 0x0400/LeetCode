from p168 import Solution

test_cases = [
    (1, "A"),
    (28, "AB"),
    (701, "ZY"),
    (2147483647, "FXSHRXW"),
]

def test_convertToTitle():
    for case in test_cases:
        s = Solution()
        assert s.convertToTitle(case[0]) == case[1], case
