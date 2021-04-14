from p153 import Solution

test_cases = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11),

]

def test_findMin():
    for case in test_cases:
        s = Solution()
        assert s.findMin(case[0]) == case[1], case

