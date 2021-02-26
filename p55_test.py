from p55 import Solution
from p55_v2 import Solution as SolutionV2

test_cases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
]


def test_canJumpV2():
    s = SolutionV2()
    for case in test_cases:
        assert s.canJump(case[0]) == case[1], case

def test_canJump():
    s = Solution()
    for case in test_cases:
        assert s.canJump(case[0]) == case[1], case
