from p87 import Solution

test_cases = [
    (("great", "rgeat"), True),
    (("abcde", "caebd"), False),
    (("a", "a"), True),
]


def test_isScramble():
    s = Solution()
    for case in test_cases:
        assert s.isScramble(*case[0]) == case[1], case
