from p130 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
    ([["X"]], [["X"]]),
]

def test_solve():
    s = Solution()
    for case in test_cases:
        s.solve(case[0])
        assert case[0] == case[1], case
