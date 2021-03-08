from p79 import Solution

test_cases = [
    (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True),
    (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True),
    (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), False),
]


def test_exist():
    s = Solution()
    for case in test_cases:
        assert s.exist(*case[0]) == case[1], case
