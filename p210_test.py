from p210 import Solution

test_cases = [
    [[2, [[1,0]]], [0,1]],
    [[4, [[1,0],[2,0],[3,1],[3,2]]], [0,1,2,3]],
    [[1, []], [0]],
    [[2, [[1,0],[0,1]]], []],
]

def test_findOrder():
    s = Solution()
    for case in test_cases:
        assert s.findOrder(*case[0]) == case[1], case
