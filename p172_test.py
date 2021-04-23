from p172 import Solution

test_cases = [
    (3, 0),
    (5, 1),
    (0, 0),
    (9, 1),
    (30, 7),
    (50, 12),
]

def test_trailingZeroes():
    for case in test_cases:
        s = Solution()
        assert s.trailingZeroes(case[0]) == case[1], case
