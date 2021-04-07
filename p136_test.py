from p136 import Solution

test_cases = [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1),
]

def test_singleNumber():
    s = Solution()
    for case in test_cases:
        assert s.singleNumber(case[0]) == case[1], case
