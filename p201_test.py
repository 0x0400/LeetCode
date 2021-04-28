from p201 import Solution

test_cases = [
    ((5, 7), 4),
    ((0, 0), 0),
    ((1, 2147483647), 0),
]


def test_rangeBitwiseAnd():
    s = Solution()
    for case in test_cases:
        # assert s.rangeBitwiseAnd(*case[0]) == case[1], case
        assert s.rangeBitwiseAndV2(*case[0]) == case[1], case
