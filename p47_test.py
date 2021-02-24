from p47 import Solution


test_cases = [
    ([1,1,2], [[1,1,2], [1,2,1], [2,1,1]]),
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
]


def test_jump():
    s = Solution()
    for case in test_cases:
         assert s.permuteUnique(case[0]) == case[1], case
