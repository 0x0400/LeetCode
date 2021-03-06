from p1528 import Solution

test_cases = [
    (("codeleet", [4,5,6,7,0,2,1,3]), "leetcode"),
    (("abc", [0,1,2]), "abc"),
    (("aiohn", [3,1,4,2,0]), "nihao"),
    (("aaiougrt", [4,0,2,6,7,3,1,5]), "arigatou"),
    (("art", [1,0,2]), "rat"),
]

def test_restoreString():
    s = Solution()
    for case in test_cases:
        assert s.restoreString(*case[0]) == case[1], case
