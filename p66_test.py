from p66 import Solution

test_cases = [
    ([1,2,3], [1, 2, 4]),
    ([4,3,2,1], [4, 3, 2, 2]),
    ([0], [1]),
    ([9], [1, 0]),
]


def test_isNumber():
    s = Solution()
    for case in test_cases:
        assert s.plusOneV2(case[0]) == case[1], case
