from p93 import Solution

test_cases = [
    ("25525511135", ["255.255.11.135","255.255.111.35"]),
    ("0000", ["0.0.0.0"]),
    ("1111", ["1.1.1.1"]),
    ("010010", ["0.10.0.10","0.100.1.0"]),
    ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),
]


def test_restoreIpAddresses():
    s = Solution()
    for case in test_cases:
        assert s.restoreIpAddresses(case[0]) == case[1], case
