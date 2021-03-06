from p75 import Solution

test_cases = [
    ([2,0,2,1,1,0], [0,0,1,1,2,2]),
    ([2,0,1], [0,1,2]),
    ([0], [0])
]


def test_sortColors():
    s = Solution()
    for case in test_cases:
        nums = case[0].copy()
        s.sortColors(nums)
        assert nums == case[1], case
