from p71 import Solution

test_cases = [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c"),
]


def test_simplifyPath():
    s = Solution()
    for case in test_cases:
        assert s.simplifyPath(case[0]) == case[1], case
