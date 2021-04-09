from p139 import Solution

test_cases = [
    (("applepenapple", ["apple","pen"]), True),
    (("catsandog", ["cats","dog","sand","and","cat"]), False),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False),
]

def test_wordBreak():
    for case in test_cases:
        s = Solution()
        assert s.wordBreak(*case[0]) == case[1], case
