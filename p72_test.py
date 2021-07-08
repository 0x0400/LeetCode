from p72 import Solution

test_cases = [
    (("horse", "ros"), 3),
    (("intention", "execution"), 5),
]


def test_minDistance():
    s = Solution()
    for case in test_cases:
        assert s.minDistance(*case[0]) == case[1], case
