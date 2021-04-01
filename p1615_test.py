from p1615 import Solution

test_cases = [
    ((4, [[0,1],[0,3],[1,2],[1,3]]), 4),
    ((5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]), 5),
    ((8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]), 5),
]

def test_maximalNetworkRank():
    s = Solution()
    for case in test_cases:
        assert s.maximalNetworkRank(*case[0]) == case[1], case
