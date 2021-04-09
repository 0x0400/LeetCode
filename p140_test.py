from p140 import Solution

test_cases = [
    (("catsanddog", ["cat","cats","and","sand","dog"]), ["cats and dog","cat sand dog"]),
    (("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
    (("catsandog", ["cats","dog","sand","and","cat"]), []),
]

def test_wordBreak():
    for case in test_cases:
        s = Solution()
        assert sorted(s.wordBreak(*case[0])) == sorted(case[1]), case
