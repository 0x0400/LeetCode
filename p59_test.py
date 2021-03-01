from p59 import Solution

test_cases = [
    (3, [[1,2,3],[8,9,4],[7,6,5]]),
    (1, [[1]]),
]


def test_my ():
    s = Solution()
    for case in test_cases:
        assert s.generateMatrix(case[0]) == case[1], case
