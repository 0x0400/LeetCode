from p207 import Solution

test_cases = [
    [[2, [[1,0]]], True],
    [[2, [[1,0],[0,1]]], False],
]

def test_canFinish():
    s = Solution()
    for case in test_cases:
        assert s.canFinish(*case[0]) == case[1], case
