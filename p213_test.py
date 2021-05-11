from p213 import Solution

test_cases = [
    [[2,3,2], 3],
    [[1,2,3,1], 4],
    [[0], 0],
]

def test_rob():
    s = Solution()
    for case in test_cases:
        assert s.rob(case[0]) == case[1], case
