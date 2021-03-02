from p67 import Solution

test_cases = [
    (("11", "1"), "100"),
    (("1010", "1011"), "10101"),
]


def test_addBinary():
    s = Solution()
    for case in test_cases:
        assert s.addBinary(*case[0]) == case[1], case
