from p128 import Solution

test_cases = [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([-1,-9,-5,-2,-9,8,-8,1,-9,-3,-3], 3),
    ([-9,-4,9,-7,0,7,3,-1,6,2,-2,8,-2,0,2,-7,-5,-2,6,-5,0,-8,8,1,0,6,8,-8,-1], 6),
]

def test_longestConsecutive():
    s = Solution()
    for case in test_cases:
        assert s.longestConsecutive(case[0]) == case[1], case
