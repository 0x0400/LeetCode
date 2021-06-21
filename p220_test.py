from p220 import Solution

test_cases = [
    [[[1,2,3,1], 3, 0], True],
    [[[1,0,1,1], 1, 2], True],
    [[[1,5,9,1,5,9], 2, 3], False],
]

def test_containsNearbyAlmostDuplicate():
    s = Solution()
    for case in test_cases:
        assert s.containsNearbyAlmostDuplicate(*case[0]) == case[1], case

def test_containsNearbyAlmostDuplicateV2():
    s = Solution()
    for case in test_cases:
        assert s.containsNearbyAlmostDuplicateV2(*case[0]) == case[1], case
