from p91 import Solution

test_cases = [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("06", 0),
    ("10", 1),
    ("27", 1),
    ("2611055971756562", 4),
    ("111111111111111111111111111111111111111111111", 1836311903)
]


# if __name__ == '__main__':
def test_numDecodings():
    s = Solution()
    for case in test_cases:
        assert s.numDecodings(case[0]) == case[1], case
