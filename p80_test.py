from p80 import Solution

test_cases = [
    ([1,1,1,2,2,3], 5),
    ([0,0,1,1,1,1,2,3,3], 7),
]


def test_removeDuplicates():
    s = Solution()
    for case in test_cases:
        assert s.removeDuplicates(case[0]) == case[1], case
