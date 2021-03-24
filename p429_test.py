from p429 import Solution
from common.tree import buildNAryTreeFromList

test_cases = [
    ([1,None,3,2,4,None,5,6], [[1],[3,2,4],[5,6]]),
    ([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14], [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
),
]

def test_levelOrder():
    s = Solution()
    for case in test_cases:
        assert s.levelOrder(buildNAryTreeFromList(case[0])) == case[1], case
