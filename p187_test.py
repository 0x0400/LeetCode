from p187 import Solution

test_cases = [
    ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC","CCCCCAAAAA"]),
    ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ("AAAAAAAAAAA", ["AAAAAAAAAA"]),

]

def test_findRepeatedDnaSequences():
    for case in test_cases:
        s = Solution()
        assert s.findRepeatedDnaSequences(case[0]) == case[1], case

