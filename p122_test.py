from p122 import Solution

test_cases = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
]

def test_maxProfit():
    s = Solution()
    for case in test_cases:
        assert s.maxProfit(case[0]) == case[1], case
