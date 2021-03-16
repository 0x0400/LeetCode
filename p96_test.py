from p96 import Solution

test_cases = [
    (3, 5),
    (1, 1),
]


def test_numTrees():
    s = Solution()
    for case in test_cases:
        assert s.numTrees(case[0]) == case[1], case
