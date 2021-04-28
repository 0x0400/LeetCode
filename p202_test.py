from p202 import Solution

test_cases = [
    (19, True),
    (2, False),
]


def test_isHappy():
    s = Solution()
    for case in test_cases:
        assert s.isHappy(case[0]) == case[1], case
