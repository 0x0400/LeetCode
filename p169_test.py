from p169 import Solution

test_cases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
]

def test_majorityElement():
    for case in test_cases:
        s = Solution()
        assert s.majorityElement(case[0]) == case[1], case

def test_majorityElementV2():
    for case in test_cases:
        s = Solution()
        assert s.majorityElementV2(case[0]) == case[1], case

def test_majorityElementV3():
    for case in test_cases:
        s = Solution()
        assert s.majorityElementV3(case[0]) == case[1], case
