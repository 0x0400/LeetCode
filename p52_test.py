from p52 import Solution

test_cases = [
    (1, 1),
    (2, 0),
    (4, 2)
]


def test_my ():
    s = Solution()
    for case in test_cases:
        assert s.totalNQueens(case[0]) == case[1], case
