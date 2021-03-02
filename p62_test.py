
from p62 import Solution

test_cases = [
    ((3, 2), 3),
    ((7, 3), 28),
    ((3, 3), 6),
    ((23, 12), 193536720)
]


def test_uniquePaths():
    s = Solution()
    for case in test_cases:
        assert s.uniquePaths(*case[0]) == case[1], case
