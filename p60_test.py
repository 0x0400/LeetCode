from p60 import Solution

test_cases = [
    ((3, 3), "213"),
    ((4, 9), "2314"),
    ((3, 1), "123"),
    ((3, 2), "132")
]


def test_my ():
    s = Solution()
    for case in test_cases:
        assert s.getPermutation(*case[0]) == case[1], case
