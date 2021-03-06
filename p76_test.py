from p76 import Solution

test_cases = [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"), "a"),
    (("a", "aa"), ""),
]


def test_minWindow():
    s = Solution()
    for case in test_cases:
        assert s.minWindow(*case[0]) == case[1], case
