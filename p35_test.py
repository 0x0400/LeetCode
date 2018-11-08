from p35 import Solution as Solution


test_cases = [
    (([1,3,5,6], 5), 2),
    (([1,3,5,6], 2), 1),
    (([1,3,5,6], 7), 4),
    (([1,3,5,6], 0), 0),
]


def test_searchInsert():
    s = Solution()
    for case in test_cases:
        assert s.searchInsert(*case[0]) == case[1]
