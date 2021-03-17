from p97 import Solution

test_cases = [
    (("aabcc", "dbbca", "aadbbcbcac"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (("", "", ""), True),
    (("a", "", "a"), True),
    (("", "a", "a"), True),
    (("", "a", "b"), False),
    (("a", "b", "ab"), True),
    (("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc", "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb","abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"), True)
]


def test_isInterleave():
    s = Solution()
    for case in test_cases:
        assert s.isInterleave(*case[0]) == case[1], case
