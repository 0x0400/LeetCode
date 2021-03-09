from p81 import Solution

test_cases = [
    (([2,5,6,0,0,1,2], 0), True),
    (([2,5,6,0,0,1,2], 3), False),
    (([0,1,1,1,2,2], 0), True)
]


def test_search():
    s = Solution()
    for case in test_cases:
        assert s.search(*case[0]) == case[1], case
