from p189 import Solution

test_cases = [
    [[[1,2,3,4,5,6,7], 3], [5,6,7,1,2,3,4]],
    [[[-1,-100,3,99], 2], [3,99,-1,-100]],

]

def test_rotate():
    s = Solution()
    for case in test_cases:
        s.rotate(case[0][0], case[0][1])
        assert case[0][0] == case[1]

