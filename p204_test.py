from p204 import Solution

test_cases = [
    (10, 4),
    (0, 0),
    (1, 0),
]


def test_countPrimes():
    s = Solution()
    for case in test_cases:
        assert s.countPrimes(case[0]) == case[1], case
