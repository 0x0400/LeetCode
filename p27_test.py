from p27 import Solution


def test_removeElement():
    s = Solution()

    assert s.removeElement([3, 2, 2, 3], 3) == 2
    assert s.removeElement([3, 2, 2, 3], 4) == 4
    assert s.removeElement([3, 3, 3, 3], 3) == 0
