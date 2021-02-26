from p53 import Solution

test_cases = [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([0], 0),
    ([-1], -1),
    ([-100000], -100000),
]


def test_my ():
    s = Solution()
    for case in test_cases:
        assert s.maxSubArray(case[0]) == case[1], case
