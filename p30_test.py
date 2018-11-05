from p30 import Solution as Solution

test_cases = [
    ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
    ("wordgoodstudentgoodword", ["word","student"], [])
]


def test_findSubstring():
    s = Solution()
    for case in test_cases:
        assert s.findSubstring(case[0], case[1]) == case[2]
