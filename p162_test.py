from p162 import Solution

test_cases = [
    ([1,2,3,1], 2),
    ([1,2,1,3,5,6,4], 1),
]

def test_findPeakElement():
    for case in test_cases:
        s = Solution()
        assert s.findPeakElement(case[0]) == case[1], case

def test_findPeakElementV2():
    for case in test_cases:
        s = Solution()
        assert s.findPeakElementV2(case[0]) == case[1], case
