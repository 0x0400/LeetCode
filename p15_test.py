
from p15 import Solution

def test_threeSum():
    s = Solution()
    assert len(s.threeSum([-1, 0, 1, 2, -1, -4])) == 2
    assert len(s.threeSum([0, 0, 0])) == 1
    assert len(s.threeSum([-1,0,1,0])) == 1
