from p151 import Solution

test_cases = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
    ("Alice does not even like bob", "bob like even not does Alice"),

]

def test_reverseWords():
    for case in test_cases:
        s = Solution()
        assert s.reverseWords(case[0]) == case[1], case
