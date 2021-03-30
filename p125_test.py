from p125 import Solution

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("0P", False),
]

def test_isPalindrome():
    s = Solution()
    for case in test_cases:
        assert s.isPalindrome(case[0]) == case[1], case
