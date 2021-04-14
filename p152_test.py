from p152 import Solution

test_cases = [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
    ([-2], -2),
    ([0, -2, -3], 6),
    ([0], 0),
    ([-4,-3,-2], 12),
    ([3, -1, 4], 4),
]

def test_maxProduct():
    for case in test_cases:
        s = Solution()
        assert s.maxProduct(case[0]) == case[1], case

def test_maxProductV2():
    for case in test_cases:
        s = Solution()
        assert s.maxProductV2(case[0]) == case[1], case
