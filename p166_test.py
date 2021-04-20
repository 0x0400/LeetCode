from p166 import Solution

test_cases = [
    ((1, 2), "0.5"),
    ((2, 1), "2"),
    ((2, 3), "0.(6)"),
    ((4, 333), "0.(012)"),
    ((1, 5), "0.2"),
    ((-50, 8), "-6.25"),
    ((-22, -2), "11"),
]

def test_fractionToDecimal():
    for case in test_cases:
        s = Solution()
        assert s.fractionToDecimal(*case[0]) == case[1], case
