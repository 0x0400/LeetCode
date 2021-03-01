from p56 import Solution

test_cases = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[1,4],[0,0]], [[0,0],[1,4]])
]


def test_merge():
    s = Solution()
    for case in test_cases:
        assert s.merge(case[0]) == case[1], case
