from p154 import Solution

test_cases = [
    ([1,3,5], 1),
    ([2,2,2,0,1], 0),
]

def test_findMin():
    for case in test_cases:
        s = Solution()
        assert s.findMin(case[0]) == case[1], case
