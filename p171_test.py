from p171 import Solution

test_cases = [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
    ("FXSHRXW", 2147483647),
]

def test_titleToNumber():
    for case in test_cases:
        s = Solution()
        assert s.titleToNumber(case[0]) == case[1], case
