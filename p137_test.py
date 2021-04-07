from p137 import Solution

test_cases = [
    ([2,2,3,2], 3),
    ([0,1,0,1,0,1,99], 99),
]

def test_singleNumber():
    s = Solution()
    for case in test_cases:
        assert s.singleNumber(case[0]) == case[1], case
