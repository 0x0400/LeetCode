from p84_v2 import Solution

test_cases = [
    ([2,1,5,6,2,3], 10),
    ([2,4], 4),
]


def test_largestRectangleArea():
    s = Solution()
    for case in test_cases:
        assert s.largestRectangleArea(case[0]) == case[1], case
