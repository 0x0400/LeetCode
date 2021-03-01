from p58 import Solution

test_cases = [
    ("Hello World", 5),
    (" ", 0),
]


def test_insert():
    s = Solution()
    for case in test_cases:
        assert s.lengthOfLastWord(case[0]) == case[1], case
