from p174 import Solution

test_cases = [
    ([[-2,-3,3],[-5,-10,1],[10,30,-5]], 7),
    ([[0]], 1),
    ([[100]], 1),
]

def test_calculateMinimumHP():
    for case in test_cases:
        s = Solution()
        assert s.calculateMinimumHP(case[0]) == case[1], case

def test_calculateMinimumHPV2():
    for case in test_cases:
        s = Solution()
        assert s.calculateMinimumHPV2(case[0]) == case[1], case
