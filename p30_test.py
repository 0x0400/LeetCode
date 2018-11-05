from p30 import Solution as Solution
from p30_v2 import Solution as Solution2


test_cases = [
    ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
    ("wordgoodstudentgoodword", ["word","student"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6, 9, 12])
]


def test_findSubstring():
    s = Solution()
    for case in test_cases:
        assert s.findSubstring(case[0], case[1]) == case[2]

def test_findSubstring_v2():
    s = Solution2()
    for case in test_cases:
        assert s.findSubstring(case[0], case[1]) == case[2]
