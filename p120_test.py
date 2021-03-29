from p120 import Solution

test_cases = [
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
    ([[-10]], -10),
]

def test_minimumTotal():
    s = Solution()
    for case in test_cases:
        assert s.minimumTotal(case[0]) == case[1], case
