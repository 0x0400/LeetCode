from p219 import Solution

test_cases = [
    [[[1,2,3,1], 3], True],
    [[[1,0,1,1], 1], True],
    [[[1,2,3,1,2,3], 2], False],
]

def test_containsNearbyDuplicate():
    s = Solution()
    for case in test_cases:
        assert s.containsNearbyDuplicate(*case[0]) == case[1], case

