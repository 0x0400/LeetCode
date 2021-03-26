from p119 import Solution

test_cases = [
    (3, [1,3,3,1]),
    (0, [1]),
    (1, [1, 1]),
    (4, [1,4,6,4,1]),
]

def test_getRow():
    s = Solution()
    for case in test_cases:
        assert s.getRow(case[0]) == case[1], case
