from p167 import Solution

test_cases = [
    (([2,7,11,15], 9), [1, 2]),
    (([2,3,4], 6), [1, 3]),
    (([-1,0], -1), [1, 2]),
]

def test_twoSum():
    for case in test_cases:
        s = Solution()
        assert s.twoSum(*case[0]) == case[1], case
