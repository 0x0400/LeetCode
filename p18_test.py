from p18_v2 import Solution


def test_fourSum():
    s = Solution()
    assert len(s.fourSum([1, 0, -1, 0, -2, 2], 0)) == 3
    assert len(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)) == 8
