from p893 import Solution

test_cases = [
    (["abcd","cdab","cbad","xyzz","zzxy","zzyx"], 3),
    (["abc","acb","bac","bca","cab","cba"], 3),
]

def test_numSpecialEquivGroups():
    s = Solution()
    for case in test_cases:
        assert s.numSpecialEquivGroups(case[0]) == case[1], case
