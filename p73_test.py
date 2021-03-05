from p73 import Solution

test_cases = [
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
]


def test_setZeroes():
    s = Solution()
    for case in test_cases:
        matrix = case[0].copy()
        s.setZeroes(matrix)
        assert matrix == case[1], case
