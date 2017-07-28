from p20 import Solution


def test_isValid():
    s = Solution()
    assert s.isValid("()")
    assert s.isValid("()[]{}")
    assert not s.isValid("(]")
    assert not s.isValid("([)]")
