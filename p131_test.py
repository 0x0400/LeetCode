from p131 import Solution

test_cases = [
   ("aab", [["a","a","b"],["aa","b"]]),
   ("a", [["a"]]),
   ("fff", [["f", "f", "f"], ["f", "ff"], ["ff", "f"], ["fff"]]),
]

def test_solve():
    for case in test_cases:
        s = Solution()
        assert sorted(s.partition(case[0])) == sorted(case[1]), case
