from p205 import Solution

test_cases = [
    (("egg", "add"), True),
    (("foo", "bar"), False),
    (("paper", "title"), True),
    (("badc", "baba"), False),
]

def test_isIsomorphic():
    s = Solution()
    for case in test_cases:
        assert s.isIsomorphic(*case[0]) == case[1], case
