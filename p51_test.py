from p51 import Solution

test_cases = [
    (1, [['Q']]),
    (2, []),
    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
]


def test_my ():
    s = Solution()
    for case in test_cases:
        assert s.solveNQueens(case[0]) == case[1], case
