from p88 import Solution

test_cases = [
    ([[1,2,3,0,0,0], 3,  [2,5,6], 3], [1,2,2,3,5,6]),
    ([[1], 1, [], 0], [1]),
]


def test_merge():
    s = Solution()
    for case in test_cases:
        s.merge(*case[0])
        assert case[0][0] == case[1], case
