from p164 import Solution

test_cases = [
    ([3,6,9,1], 3),
    ([10], 0),
]

def test_maximumGap():
    for case in test_cases:
        s = Solution()
        assert s.maximumGap(case[0]) == case[1], case
