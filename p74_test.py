from p74 import Solution

test_cases = [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False),
]


def test_searchMatrix():
    s = Solution()
    for case in test_cases:
        assert s.searchMatrix(*case[0]) == case[1], case
