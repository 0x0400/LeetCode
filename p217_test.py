from p217 import Solution

test_cases = [
    [[1,2,3,1], True],
    [[1,2,3,4], False],
    [[1,1,1,3,3,4,3,2,4,2], True],
]

def test_containsDuplicate():
    s = Solution()
    for case in test_cases:
        assert s.containsDuplicate(case[0]) == case[1], case

