from p46 import Solution


test_cases = [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
]


def test_jump():
    s = Solution()
    for case in test_cases:
         assert s.permute(case[0]) == case[1], case
