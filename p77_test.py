from p77 import Solution

test_cases = [
    # ((1, 1), [[1]]),
    ((4, 2), [
        [1,2],
        [1,3],
        [1,4],
        [2,3],
        [2,4],
        [3,4],
    ]),
]


def test_combine():
    s = Solution()
    for case in test_cases:
        assert s.combine(*case[0]) == case[1], case
