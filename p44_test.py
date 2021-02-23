from p44 import Solution as Solution
from p44_v2 import Solution as SolutionV2


test_cases = [
    (["aa", "a"], False),
    (["aa", "*"], True),
    (["cb", "?a"], False),
    (["adceb", "*a*b"], True),
    (["acdcb", "a*c?b"], False),
    (["", "******"], True),
    (["babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"], False),
    (["aab", "c*a*b"], False),
]


def test_isMatch():
    s = Solution()
    for case in test_cases:
         assert s.isMatch(*case[0]) == case[1]


def test_isMatchV2():
    s = SolutionV2()
    for case in test_cases:
        assert s.isMatch(*case[0]) == case[1]
