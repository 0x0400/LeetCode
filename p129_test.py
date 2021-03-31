from p129 import Solution
from common.tree import buildTreeFromList

test_cases = [
    ([1,2,3], 25),
    ([4,9,0,5,1], 1026),
]

def test_sumNumbers():
    s = Solution()
    for case in test_cases:
        assert s.sumNumbers(buildTreeFromList(case[0])) == case[1], case
