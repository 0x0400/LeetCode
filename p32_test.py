from p32 import Solution as Solution
from p32_v2 import Solution as Solution2


test_cases = [
    ("(()", 2),
    (")()())", 4),
    ("()(()", 2),
    ("()(())", 6)
]


def test_longestValidParentheses():
    s = Solution()
    for case in test_cases:
        assert s.longestValidParentheses(case[0]) == case[1]

def test_longestValidParentheses_v2():
    s = Solution2()
    for case in test_cases:
        assert s.longestValidParentheses(case[0]) == case[1]
