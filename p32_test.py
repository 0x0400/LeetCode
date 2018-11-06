from p32 import Solution as Solution

test_cases = [
    ("(()", 2),
    (")()())", 4),
    ("()(()", 2),
]


def test_longestValidParentheses():
    s = Solution()
    for case in test_cases:
        assert s.longestValidParentheses(case[0]) == case[1]
