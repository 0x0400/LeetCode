from p165 import Solution

test_cases = [
    (("1.01", "1.001"), 0),
    (("1.0", "1.0.0"), 0),
    (("0.1", "1.1"), -1),
    (("1.0.1", "1"), 1),
    (("7.5.2.4", "7.5.3"), -1),
]

def test_compareVersion():
    for case in test_cases:
        s = Solution()
        assert s.compareVersion(*case[0]) == case[1], case
