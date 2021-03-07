from p78 import Solution

test_cases = [
    ([0], [[],[0]]),
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
]


def test_subsets():
    s = Solution()
    for case in test_cases:
        rst = s.subsets(case[0])
        rst.sort()
        case[1].sort()
        assert rst == case[1], case
