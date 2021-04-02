from p134 import Solution

test_cases = [
    (([1,2,3,4,5], [3,4,5,1,2]), 3),
    (([2,3,4], [3,4,3]), -1),
]

def test_canCompleteCircuit():
    s = Solution()
    for case in test_cases:
        assert s.canCompleteCircuit(*case[0]) == case[1], case
