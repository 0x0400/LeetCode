from p209 import Solution

test_cases = [
    ((7, [2,3,1,2,4,3]), 2),
    ((4, [1,4,4]), 1),
    ((11, [1,1,1,1,1,1,1,1]), 0),
]

def test_minSubArrayLen():
    s = Solution()
    for case in test_cases:
        assert s.minSubArrayLen(*case[0]) == case[1], case
