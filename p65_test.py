from p65 import Solution

test_cases = [
    # ("2", True),
    # ("0089", True),
    ("-0.1", True),
    ("+3.14", True),
    ("4.", True),
    ("-.9", True),
    ("2e10", True),
    ("-90E3", True),
    ("3e+7", True),
    ("+6e-1", True),
    ("53.5e93", True),
    ("-123.456e789", True),
    ("abc", False),
    ("1a", False),
    ("1e", False),
    ("e3", False),
    ("99e2.5", False),
    ("--6", False),
    ("-+3", False),
    ("95a54e53", False),
    ("4e+", False),
]


def test_isNumber():
    s = Solution()
    for case in test_cases:
        assert s.isNumber(case[0]) == case[1], case
