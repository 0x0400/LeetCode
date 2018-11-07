from p34 import Solution as Solution


test_cases = [
    ([5,7,7,8,8,10], 8, [3, 4]),
    ([5,7,7,8,8,10], 6, [-1, -1]),
    ([], 1, [-1, -1]),
    ([1], 1, [0, 0]),
]


def test_searchRange():
    s = Solution()
    for case in test_cases:
        assert s.searchRange(case[0], case[1]) == case[2]
