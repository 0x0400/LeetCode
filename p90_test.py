from p90 import Solution

test_cases = [
    ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
    ([0], [[],[0]]),
    ([4,4,4,1,4], [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]),
]


# if __name__ == '__main__':
def test_subsetsWithDup():
    s = Solution()
    for case in test_cases:
        assert s.subsetsWithDup(case[0]) == case[1], case
