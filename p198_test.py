from p198 import Solution

test_cases = [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
]

def test_rob():
    s = Solution()
    for case in test_cases:
        assert s.rob(case[0]) == case[1], case
