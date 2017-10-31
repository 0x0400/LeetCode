from p26 import Solution


def test_removeDuplicates():
    s = Solution()

    assert s.removeDuplicates([]) == 0
    assert s.removeDuplicates([1, 1, 2]) == 2
    assert s.removeDuplicates([1, 2, 3]) == 3
