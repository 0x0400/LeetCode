from p214 import Solution

test_cases = [
    ("aacecaaa", "aaacecaaa"),
    ("abcd", "dcbabcd"),
]

def test_shortestPalindrome():
    s = Solution()
    for case in test_cases:
        assert s.shortestPalindrome(case[0]) == case[1], case
