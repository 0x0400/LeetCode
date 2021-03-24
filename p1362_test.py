from p1362 import Solution

test_cases = [
    (8, [3,3]),
    (123, [5,25]),
    (999, [25,40]),
]

def test_closestDivisors():
    s = Solution()
    for case in test_cases:
        assert s.closestDivisors(case[0]) == case[1], case
