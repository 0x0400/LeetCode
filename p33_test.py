from p33 import Solution as Solution


test_cases = [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([3, 1], 1, 1)
]


def test_search():
    s = Solution()
    for case in test_cases:
        assert s.search(case[0], case[1]) == case[2]


